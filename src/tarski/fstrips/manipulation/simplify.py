import copy

from ..fstrips import AddEffect, DelEffect, UniversalEffect, FunctionalEffect
from ...evaluators.simple import evaluate
from ...grounding.ops import approximate_symbol_fluency
from ...syntax.terms import Constant, Variable, CompoundTerm
from ...syntax.formulas import CompoundFormula, QuantifiedFormula, Atom, Tautology, Contradiction, Connective, is_neg


def bool_to_expr(val):
    if not isinstance(val, bool):
        return val
    return Tautology() if val else Contradiction()


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
    def __init__(self, problem, model):
        self.problem = problem
        self.model = model
        _, self.static_symbols = approximate_symbol_fluency(problem)

    def simplify(self, inplace=False):
        """ Simplify the whole problem """
        problem = self.problem if inplace else copy.deepcopy(self.problem)
        problem.goal = self.simplify_expression(problem.goal, inplace=True)

        for aname, a in list(problem.actions.items()):
            res = self.simplify_action(a, inplace=True)
            if res is None:
                del problem.actions[aname]

        return problem

    def simplify_action(self, action, inplace=False):
        simple = action if inplace else copy.deepcopy(action)
        simple.precondition = self.simplify_expression(simple.precondition, inplace=True)
        if simple.precondition in (False, Contradiction):
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
            effect.condition = bool_to_expr(self.simplify_expression(effect.condition))
            if isinstance(effect.condition, Contradiction):
                return None
            effect.atom = self.simplify_expression(effect.atom)
            return effect

        if isinstance(effect, FunctionalEffect):
            effect.condition = bool_to_expr(self.simplify_expression(effect.condition))
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
        return symbol.builtin or symbol in self.static_symbols

    def node_can_be_statically_evaluated(self, node):
        """ Return true if the given atom or compound term can be statically evaluated. """
        return self.symbol_can_be_statically_evaluated(node.symbol) and \
            all(isinstance(st, Constant) for st in node.subterms)
