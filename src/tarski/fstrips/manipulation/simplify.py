import copy

from multipledispatch import dispatch

from ..fstrips import AddEffect, DelEffect, UniversalEffect, FunctionalEffect
from ..ops import collect_all_symbols, compute_number_potential_groundings
from ...evaluators.simple import evaluate
from ...grounding.ops import approximate_symbol_fluency
from ...syntax.terms import Constant, Variable, CompoundTerm
from ...syntax.formulas import CompoundFormula, QuantifiedFormula, Atom, Pass, Tautology, Contradiction, Connective, is_neg, \
    Quantifier, unwrap_conjunction_or_atom, is_eq_atom, land, exists
from ...syntax.transform.substitutions import substitute_expression
from ...syntax.util import get_symbols
from ...syntax.walker import FOLWalker
from ...syntax.ops import flatten
from ...syntax import symref


def bool_to_expr(val, lang):
    if not isinstance(val, bool):
        return val
    return Tautology(lang) if val else Contradiction(lang)


class Simplify:
    """ A class to simplify FSTRIPS/STRIPS problems, actions and logical expressions.

    The simplifications being made try to symbolically evaluate static atoms and terms and propagate the result
    up the expression AST. Thus, an expression $x < c$ will be simplified to $x < 6$ if $c$ happens to be a static
    symbol (i.e. a symbol such that no action affects its denotation) whose value on the initial state is 6.
    If additionally $x$ was also a static symbol with value 3, then $x < c$ would be simplified to True.

    This class only implements very simple simplification strategies. For further sophistication we should probably
    move into using sympy or some similar symbolic maths library. These are some of the strategies we
    currently implement:
    * Remove double negations
    * Simplify conjunctions and disjunctions where one conjunct / disjunct evaluates to True or False.
    * Evaluate static terms and atoms into their constant or truth value.
    """
    def __init__(self, problem=None, model=None):
        self.problem = problem
        self.model = model
        self.static_symbols = None
        if problem is not None:
            _, self.static_symbols = approximate_symbol_fluency(problem)

    def simplify(self, inplace=False, remove_unused_symbols=False):
        """ Simplify the whole problem """
        if remove_unused_symbols and not inplace:
            # ATM there are problems generating a full clone of the language+problem,
            # since language.deepcopy is disabled
            raise RuntimeError(f'Full problem simplification with remove_unused_symbols=True '
                               f'can at the moment only be performed in place (set inplace=True)')

        problem = self.problem if inplace else copy.deepcopy(self.problem)

        # Simplify the goal
        problem.goal = self.simplify_expression(problem.goal, inplace=True)

        # Simplify the actions
        for aname, a in list(problem.actions.items()):
            if compute_number_potential_groundings(a.sort()) == 0:
                del problem.actions[aname]
                continue

            problem.actions[aname] = self.simplify_action(a, inplace=True)
            if problem.actions[aname] is None:
                del problem.actions[aname]

        # Check what symbols are still used after the simplifications
        used = collect_all_symbols(problem)

        # Remove unused symbols from language and initial state
        unused = [s for s in get_symbols(problem.language, type_='all', include_builtin=False) if s not in used]
        for s in unused:
            problem.language.remove_symbol(s)

            if problem.init is not None:
                problem.init.remove_symbol(s)

        return problem

    def simplify_action(self, action, inplace=False):
        simple = action if inplace else copy.deepcopy(action)
        simple.precondition = self.simplify_expression(simple.precondition, inplace=True)
        if simple.precondition is False or isinstance(simple.precondition, Contradiction):
            return None

        # Filter out those effects that are None, e.g. because they are not applicable:
        simple.effects = list(filter(None.__ne__, (self.simplify_effect(eff, inplace=True) for eff in simple.effects)))

        if not simple.effects:  # If not effects remain, the action is useless
            return None

        return simple

    def simplify_expression(self, node, inplace=True):
        node = node if inplace else copy.deepcopy(node)

        # Nothing to be simplified about these:
        if isinstance(node, (Variable, Constant)):
            return node

        if isinstance(node, Contradiction):
            return False

        if isinstance(node, Tautology):
            return True

        if isinstance(node, Pass):
            return True

        if isinstance(node, (CompoundTerm, Atom)):
            node.subterms = [self.simplify_expression(st) for st in node.subterms]
            if not self.node_can_be_statically_evaluated(node):
                return node
            return evaluate(node, self.model)  # Will return the constant to which this expression evaluates

        elif is_neg(node):
            sub = self.simplify_expression(node.subformulas[0])
            if is_neg(sub):
                return sub.subformulas[0]
            if isinstance(sub, bool):
                return not sub
            node.subformulas = [sub]
            return node

        if isinstance(node, CompoundFormula):
            assert node.connective in (Connective.And, Connective.Or)
            isand = (node.connective == Connective.And)
            newsubformulas = []
            # Let's do a partial evaluation of the connective
            for st in node.subformulas:
                simp = self.simplify_expression(st)
                if not isinstance(simp, bool):
                    newsubformulas.append(simp)
                    continue
                if isand and simp is False:
                    return False  # x and false = false
                if not isand and simp is True:
                    return True  # x or True = true

            if len(newsubformulas) == 0:
                return isand  # A conjunction with 0 conjuncts is true, a disjunction of 0 disjuncts is false
            if len(newsubformulas) == 1:
                return newsubformulas[0]

            node.subformulas = newsubformulas
            return node

        if isinstance(node, QuantifiedFormula):
            node.formula = self.simplify_expression(node.formula)
            if isinstance(node.formula, bool):
                return node.formula
            return node

        raise RuntimeError(f'Unexpected type "{type(node)}" for expression "{node}"')

    def simplify_effect(self, effect, inplace=True):
        effect = effect if inplace else copy.deepcopy(effect)

        if isinstance(effect, (AddEffect, DelEffect)):
            effect.condition = bool_to_expr(self.simplify_expression(effect.condition), self.problem.language)
            if isinstance(effect.condition, Contradiction):
                return None
            effect.atom = self.simplify_expression(effect.atom)
            return effect

        if isinstance(effect, FunctionalEffect):
            effect.condition = bool_to_expr(self.simplify_expression(effect.condition), self.problem.language)
            if isinstance(effect.condition, Contradiction):
                return None
            effect.lhs = self.simplify_expression(effect.lhs)
            effect.rhs = self.simplify_expression(effect.rhs)
            return effect

        if isinstance(effect, UniversalEffect):
            # Go recursively to the universally quantified effects, filter those that are inapplicable
            effect.effects = list(filter(None.__ne__, (self.simplify_effect(eff, inplace=True) for eff in effect.effects)))
            return effect

        raise RuntimeError(f'Effect "{effect}" of type "{type(effect)}" cannot be analysed')

    def symbol_can_be_statically_evaluated(self, symbol):
        return symbol.builtin or (self.static_symbols is not None and symbol in self.static_symbols)

    def node_can_be_statically_evaluated(self, node):
        """ Return true if the given atom or compound term can be statically evaluated. """
        return self.model is not None and self.symbol_can_be_statically_evaluated(node.symbol) and \
            all(isinstance(st, Constant) for st in node.subterms)


def simplify_existential_quantification(node, inplace=True):
    """ Replaces a formula of the form ∃x.φ[x] ∧ x = t by the formula φ[x/t]. """
    walker = ExistentialQuantificationSimplifier()
    return walker.run(node, inplace=inplace)


class ExistentialQuantificationSimplifier(FOLWalker):
    """ Replaces a formula of the form ∃x.φ[x] ∧ x = t by the formula φ[x/t]. """
    @dispatch(object)
    def visit(self, node):  # pylint: disable-msg=E0102
        return self.default_handler(node)

    @dispatch(QuantifiedFormula)
    def visit(self, node: QuantifiedFormula):  # pylint: disable-msg=E0102
        if node.quantifier == Quantifier.Forall:
            return node

        exvars = {symref(v) for v in node.variables}
        conjuncts = unwrap_conjunction_or_atom(flatten(node.formula))

        go_on = True
        while go_on:
            go_on, conjuncts = _attempt_single_ex_var_substitution(exvars, conjuncts)

        substituted = land(*(c for i, c in enumerate(conjuncts)), flat=True)
        
        if exvars:
            return exists(*(v.expr for v in exvars), substituted)
        return substituted


def _attempt_single_ex_var_substitution(exvars, conjuncts):
    replaced, substitution = None, None
    toremove = set()
    for i, c in enumerate(conjuncts):
        if is_eq_atom(c):
            t1, t2 = c.subterms
            t1_quantified = symref(t1) in exvars
            t2_quantified = symref(t2) in exvars
            if not t1_quantified and not t2_quantified:
                continue

            if symref(t1) == symref(t2):
                # A corner case, we have an atom z=z, for z a variable. We don't want to do any replacement here,
                # just remove the atom
                toremove.add(i)
                continue

            if t1_quantified and t2_quantified:
                # Also a bit of a corner case: we have a formula ∃x,y.φ[x,y] ∧ x = y, still equivalent to ∃x.φ[y/x]
                substitution = (symref(t2), t1)
            elif t1_quantified:
                substitution = (symref(t1), t2)
            elif t2_quantified:
                substitution = (symref(t2), t1)

            replaced = i
            break

    # Let's remove the spureous z=z atoms first of all
    conjuncts = [c for i, c in enumerate(conjuncts) if i not in toremove]

    if replaced is None:  # No more replaceable conjuncts
        return False, conjuncts

    exvars.remove(substitution[0])
    substitution = dict([substitution])
    conjuncts = [substitute_expression(c, substitution, inplace=True) for i, c in enumerate(conjuncts) if i != replaced]
    return True, conjuncts
