"""
    A module to create reachability-related logic programs from PDDL tasks
"""
import itertools

from ..syntax.transform import remove_quantifiers, QuantifierEliminationMode, expand_universal_effect
from ..syntax.builtins import symbol_complements
from ..syntax.ops import free_variables
from ..syntax import Formula, Atom, CompoundFormula, Connective, Term, Variable, Constant, Tautology, \
    BuiltinPredicateSymbol, QuantifiedFormula, Quantifier, CompoundTerm
from ..syntax.sorts import parent
from ..fstrips import Problem, SingleEffect, AddEffect, DelEffect, FunctionalEffect
from ..fstrips.representation import identify_cost_related_functions

SOLVABLE = "_solvable_"


def create_reachability_lp(problem: Problem, ground_actions=True):
    """ Return a reachability logic program, along with the symbol translation dictionary used to create it """
    lp = LogicProgram()
    compiler_class = ReachabilityLPCompiler if ground_actions else VariableOnlyReachabilityLPCompiler
    compiler = compiler_class(problem, lp)
    compiler.create()
    return lp, compiler.tr


class ReachabilityLPCompiler:
    """ A class that handles the compilation of planning problem into suitable logic programs to perform reachability
    analysis. The compilation follows roughly the relaxed reachability analysis outlined in Section 6 of

        Helmert, M. (2009). Concise finite-domain representations for PDDL planning tasks.
        Artificial Intelligence, 173(5-6), 503-535.

    albeit there are some differences which so far we haven't properly described and analyzed.
    """
    def __init__(self, problem: Problem, lp):
        self.problem = problem
        self.lp = lp
        # self.node_cache = dict()  # A cache of auxiliary subformulas
        self.aux_atom_count = 0
        self.tr = Translator()

    def gen_aux_atom(self, args=None):
        """ Return a new auxiliary atom with the given arguments """
        self.aux_atom_count += 1
        return self.lp_atom("__f{}".format(self.aux_atom_count), args)

    def create(self):
        problem, lang, lp = self.problem, self.problem.language, self.lp

        # Preprocess the domain functions to identify those that appear only in
        # cost-related effects, which we can then ignore safely
        cost_related_functions = identify_cost_related_functions(problem)

        # Declare the PDDL objects with their types, e.g. with a fact "block(b1)".
        constants = lang.constants()
        _ = [lp.rule(self.lp_type_atom_from_term(c)) for c in constants]

        # Declare the type hierarchy, e.g. with a rule "object(X) :- block(X)."
        for s in lang.sorts:
            if not s.builtin:  # TODO Decide what to do with builtins
                p = parent(s)
                if p is not None and len(list(s.domain())) > 0:
                    # Don't output the type hierarchy rule if the type has no element
                    lp.rule(self.lp_atom(p.name, [_var()], prefix='type'),
                            [self.lp_atom(s.name, [_var()], prefix='type')])

        # Process all atoms in the initial state, e.g. "on(b1, b2)."
        for atom in problem.init.as_atoms():
            if isinstance(atom, tuple) and isinstance(atom[0], CompoundTerm) and atom[0].symbol.symbol == 'total-cost':
                continue  # Ignore total-cost effects
            if not isinstance(atom, Atom):
                assert isinstance(atom, tuple) and len(atom) == 2 and isinstance(atom[0], CompoundTerm)
                t, v = atom
                if t.symbol.name in cost_related_functions:
                    continue
                raise RuntimeError(
                    f'ReachabilityLPCompiler cannot handle functional atom "{t} := {v}" in the initial state')
            lp.rule(self.tarski_atom_to_lp_atom(atom))

        # Process all actions
        for _, action in problem.actions.items():
            if all(len(list(v.sort.domain())) > 0 for v in action.parameters):
                # We process only those actions such that all their parameter types have at least one object
                self.process_action(action, lang, lp)

        # Process all derived predicates
        # TODO To be implemented yet
        assert not problem.derived_predicates

        # Process goal, e.g. "solvable :- on(a,b), on(b,c)." (note that the goal is always ground)
        phi = remove_quantifiers(lang, problem.goal, QuantifierEliminationMode.Forall)
        body = self.process_formula(phi)
        lp.rule(self.lp_atom(SOLVABLE), body)

    def process_action(self, action, lang, lp):
        # Construct the head and part of the body of the action atom, e.g. "move(X, Y) :- object(X), object(Y)"
        # Note that we need to capitalize the parameters of the action schema, as they are LP variables.
        action_atom = self.lp_atom(action.name, [make_variable_name(v.symbol) for v in action.parameters],
                                   prefix='action')
        body = [self.lp_type_atom_from_term(v) for v in action.parameters]
        # Remove universal quantifiers and add precondition atoms to the body
        phi = remove_quantifiers(lang, action.precondition, QuantifierEliminationMode.Forall)
        body += self.process_formula(phi)
        lp.rule(action_atom, body)
        # Now process the effects
        for eff in action.effects:
            for expanded in expand_universal_effect(eff):
                head, body = self.process_effect(lang, expanded, action.name)
                if head is not None:
                    lp.rule(head, [action_atom] + body)

    def process_formula(self, f: Formula):
        """ Process a given formula and return the corresponding LP rule body, along with declaring in the given LP
        any number of extra rules necessary to ensure equivalence of the body with the truth value of the formula.
        """
        # ref = symref(f)  # At the moment not caching
        # res = self.node_cache.get(ref, None)
        # If the formula has been processed before and an auxiliary LP atom for it created, return that
        # if res is not None:
        #     return res

        if isinstance(f, Tautology):
            return []

        elif isinstance(f, Atom):
            return [self.tarski_atom_to_lp_atom(f)]

        elif isinstance(f, CompoundFormula):
            if f.connective == Connective.And:
                return list(itertools.chain.from_iterable(self.process_formula(sub) for sub in f.subformulas))

            elif f.connective == Connective.Or:
                # Generate an auxiliary term __fi(X) that is reachable whenever any of the disjuncts is reachable, e.g.
                # for a disjunction "p or q(y)", we'll generate an auxiliary term f(y) with ASP rules:
                # f(Y) :- p, object(Y).
                # f(Y) :- q(Y), object(Y).
                variables = free_variables(f)
                aux = self.gen_aux_atom([self.process_term(v) for v in variables])
                varbinding = [self.lp_type_atom_from_term(v) for v in variables]
                sub = [self.process_formula(s) for s in f.subformulas]
                for body in sub:
                    self.lp.rule(aux, body + varbinding)
                return [aux]

            elif f.connective == Connective.Not:
                assert len(f.subformulas) == 1
                subf = f.subformulas[0]
                if not isinstance(subf, Atom):
                    raise RuntimeError("Negation of arbitrary formulas not yet implemented")
                processed, = self.process_formula(subf)  # Watch out the comma that unpacks the length-1 list
                return [negate_lp_atom(processed)]

            else:
                raise RuntimeError('Unexpected connective "{}" within CompoundFormula "{}"'.format(f.connective, f))

        elif isinstance(f, QuantifiedFormula):
            if f.quantifier == Quantifier.Exists:
                # We project away the existential variable by not using it in the LP rule head. e.g. for a formula
                # "Exists x p(x)", we generate the LP rule
                # __f1 :- p(x), object(x).
                # Note that the type atom "object(x)" is needed for degenerate cases such as "Exist x True"
                aux = self.gen_aux_atom()
                varbinding = [self.lp_type_atom_from_term(v) for v in f.variables]
                self.lp.rule(aux, self.process_formula(f.formula) + varbinding)
                return [aux]

            else:
                assert f.quantifier == Quantifier.Forall
                raise RuntimeError('Formula should be forall-free, revise source code')

        raise RuntimeError('Unexpected formula "{}" with type "{}"'.format(f, type(f)))

    @staticmethod
    def process_term(t: Term):
        """ Return the name of the LP constant corresponding to the given term. For instance, the variable "from" of
        type "place" will get transformed into a name "From" (capitalized), whereas the constant "b1" of type block will
        get transformed into a name "b1". We assume that the type information is used elsewhere. """
        if isinstance(t, Variable):
            return make_variable_name(t.symbol)  # lp_atom_from_term(t)
        elif isinstance(t, Constant):
            return t.symbol

        raise RuntimeError('Unexpected term "{}" with type "{}"'.format(t, type(t)))

    def process_effect(self, lang, eff, action_name):
        """ Process a given effect and return the corresponding LP rule (a pair with head and body). For instance a
        conditional effect "p -> q(X)" will be transformed into a head q(X) and a body p.
        Additionally, declare in the given LP any number of extra rules necessary to ensure equivalence of the body
        with the truth value of the effect conditions (i.e. this will be mostly necessary for conditional effects).
        """
        assert isinstance(eff, SingleEffect)
        if isinstance(eff, AddEffect):
            head = self.tarski_atom_to_lp_atom(eff.atom)
            condition = remove_quantifiers(lang, eff.condition, QuantifierEliminationMode.Forall)
            return head, self.process_formula(condition)

        if isinstance(eff, DelEffect):
            return None, []  # Simply ignore the delete effects

        if isinstance(eff, FunctionalEffect):
            if eff.lhs.symbol.name == 'total-cost':
                return None, []  # We ignore total-cost effects
            raise RuntimeError(
                f'ReachabilityLPCompiler cannot handle functional effect "{eff}" in action "{action_name}"')
        raise RuntimeError(f'Unexpected effect "{eff}" with type "{type(eff)}"')

    def tarski_atom_to_lp_atom(self, atom: Atom, prefix=''):
        return self.lp_atom(atom.predicate.symbol, [self.process_term(sub) for sub in atom.subterms], prefix='atom')

    def lp_type_atom_from_term(self, t: Term):
        """ Return a LP atom with type information from a given term, e.g. of the form block(b) for a constant,
        or block(X) for a variable. """
        if not isinstance(t, (Constant, Variable)):
            raise RuntimeError(f'ReachabilityLPCompiler cannot handle functional terms such as "{t}"')
        name = make_variable_name(t.symbol) if isinstance(t, Variable) else _uncapitalize(t.symbol)
        return self.lp_atom(t.sort.name, [name], prefix='type')

    def lp_atom(self, symbol, args=None, prefix=''):
        args = args or []
        infix = False
        if isinstance(symbol, BuiltinPredicateSymbol):  # Special treatment for built-ins as =, !=, <, etc.
            symbol = symbol.value
            infix = True
            prefix = ''
        return LPAtom(self.tr.normalize(symbol, prefix=prefix), [self.tr.normalize(a) for a in args], infix=infix)


class VariableOnlyReachabilityLPCompiler(ReachabilityLPCompiler):
    """ A variation of the standard LP compiler that cares only about state variable, but not action, groundings. """
    def process_action(self, action, lang, lp):
        # See & contrast with method in parent class
        # Construct the part of the body corresponding to the parameter types, e.g. "object(X), block(Y)"
        prec_body = [self.lp_type_atom_from_term(v) for v in action.parameters]
        # Remove universal quantifiers and add precondition atoms to the body
        phi = remove_quantifiers(lang, action.precondition, QuantifierEliminationMode.Forall)
        prec_body += self.process_formula(phi)
        # Now process the effects
        for eff in action.effects:
            head, condeff_body = self.process_effect(lang, eff, action.name)
            if head is not None:
                lp.rule(head, prec_body + condeff_body)


class LPAtom:
    def __init__(self, symbol: str, args=None, infix=False):
        self.symbol = symbol
        self.args = args or []
        self.infix = infix
        assert not infix or len(args) == 2

    def __str__(self):
        """ Return a string of the form 'symbol(arg1, ..., argn)', or 'symbol()', if args is empty """
        if self.infix:
            return "{} {} {}".format(self.args[0], self.symbol, self.args[1])
        arglist = ", ".join(str(arg) for arg in _ensure_list(self.args))
        return "{}({})".format(self.symbol, arglist)

    __repr__ = __str__


def negate_lp_atom(atom: LPAtom):
    negated = symbol_complements.get(atom.symbol, None)
    if negated is not None:  # We have the negation of a builtin comparison symbol, e.g. p != q
        assert atom.infix
        return LPAtom(negated, atom.args, atom.infix)

    # Else, we must have the negation of a non-builtin predicate symbol, in which case we assume it is true, following
    # Helmert, Concise finite-domain representations for PDDL planning tasks, Section 6.1.3
    assert not atom.infix
    return lp_tautology()
    # return LPAtom("-{}".format(atom.symbol), atom.args, atom.infix)


def lp_tautology():
    return LPAtom("=", [1, 1], infix=True)


def make_variable_name(name: str):
    if not name[0].isalpha():  # ASP variable names must start with a capital letter
        name = name[1:]
    return _capitalize(name)


def _capitalize(name: str):
    """ Capitalize the first letter of the name, e.g. for use as an ASP variable """
    return name.capitalize()


def _uncapitalize(name: str):
    """ Uncapitalize the first letter of the name, e.g. for use as an ASP constant """
    return name[0].lower() + name[1:]


def _ensure_list(elem):
    return elem if isinstance(elem, list) else [elem]


class Translator:
    def __init__(self):
        self.d = dict()
        self.inv = dict()

    def normalize(self, name: str, prefix=''):
        """ Translate a given name and store the translation """
        prefix = prefix + '_' if prefix else ''
        prefixed = prefix + name

        translated = self.d.get(prefixed, None)
        if translated is None:
            translated = prefix + sanitize(name)
            if prefixed in self.inv or translated in self.inv:
                raise RuntimeError(f'Sanitization of STRIPS name "{name}" for ASP purposes would create a name clash')

            if translated != prefixed:
                translated = self._insert(prefixed, translated)
        return translated

    def _insert(self, k, v):
        self.d[k] = v
        self.inv[v] = k
        return v

    def back(self, name):
        """ Return the  unnormalized version of the given string, assuming it has been normalized on this translator """
        return self.inv.get(name, name)


class LogicProgram:
    def __init__(self):
        self.rules = []

    def rule(self, head, body=None):
        self.rules.append(_print_rule(head, body))

    def nrules(self):
        return len(self.rules)


class InFileLogicProgram:
    def __init__(self, fd):
        self.fd = fd

    def rule(self, head, body=None):
        self.fd.write(_print_rule(head, body) + "\n")


def _print_rule(head, body):
    assert body is None or isinstance(body, (list, tuple))
    return "{}.".format(head) if body is None else "{} :- {}.".format(head, _print_body(body))


def _print_body(body):
    return ", ".join(str(x) for x in body)


def sanitize(name: str):
    """ Normalize the given string by removing chars that are potentially problematic for the LP solver """
    return name.replace("-", "__")


def _var(i=0, lowercase=False):
    """ Return a distinct variable name for each given value of i """
    alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVW"
    res = alphabet[i] if i < len(alphabet) else "X{}".format(i)
    return res.lower() if lowercase else res
