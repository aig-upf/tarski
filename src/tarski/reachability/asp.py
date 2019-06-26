"""
    A module to create reachability-related logic programs from PDDL tasks
"""
import itertools

from ..syntax.builtins import symbol_complements
from ..syntax.ops import free_variables
from ..syntax import Formula, Atom, CompoundFormula, Connective, Term, Variable, Constant, Tautology, \
    BuiltinPredicateSymbol, QuantifiedFormula, symref, Quantifier
from ..syntax.sorts import parent
from ..fstrips import Problem, SingleEffect, UniversalEffect, AddEffect, DelEffect

SOLVABLE = "solvable"


def create_reachability_lp(problem: Problem):
    """ Return a reachability logic program, along with the symbol translation dictionary used to create it """
    lp = LogicProgram()
    compiler = ReachabilityLPCompiler(problem, lp)
    compiler.create()
    return lp, compiler.tr


class ReachabilityLPCompiler:
    def __init__(self, problem: Problem, lp):
        self.problem = problem
        self.lp = lp
        self.node_cache = dict()  # A cache of auxiliary subformulas
        self.aux_atom_count = 0
        self.tr = Translator()

    def gen_aux_atom(self, args=None):
        """ Return a new auxiliary atom with the given arguments """
        self.aux_atom_count += 1
        return self.lp_atom("__f{}".format(self.aux_atom_count), args)

    def create(self):
        problem, lang, lp = self.problem, self.problem.language, self.lp

        # Declare the PDDL objects with their types, e.g. with a fact "block(b1)".
        constants = lang.constants()
        _ = [lp.rule(self.lp_type_atom_from_term(c)) for c in constants]

        # Declare the type hierarchy, e.g. with a rule "object(X) :- block(X)."
        for s in lang.sorts:
            if not s.builtin:  # TODO Decide what to do with builtins
                p = parent(s)
                if p is not None:
                    lp.rule(self.lp_atom(p.name, [_var()]), [self.lp_atom(s.name, [_var()])])

        # Process all atoms in the initial state, e.g. "on(b1, b2)."
        for atom in problem.init.as_atoms():
            assert isinstance(atom, Atom)
            lp.rule(self.tarski_atom_to_lp_atom(atom))

        # Process all actions
        for _, action in problem.actions.items():
            # Construct the head and part of the body of the action atom, e.g. "move(X, Y) :- object(X), object(Y)"
            # Note that we need to capitalize the parameters of the action schema, as they are LP variables.
            action_atom = self.lp_atom(action.name, [make_variable_name(v.symbol) for v in action.parameters])
            body = [self.lp_type_atom_from_term(v) for v in action.parameters]

            # Add precondition atoms to the body
            body += self.process_formula(action.precondition)
            lp.rule(action_atom, body)

            # Now process the effects
            for eff in action.effects:
                head, body = self.process_effect(eff)
                if head is not None:
                    lp.rule(head, [action_atom] + body)

        # Process all derived predicates
        # TODO To be implemented yet
        assert not problem.derived_predicates

        # Process goal, e.g. "solvable :- on(a,b), on(b,c)." (note that the goal is always ground)
        body = self.process_formula(problem.goal)
        lp.rule(self.lp_atom(SOLVABLE), body)

    def process_formula(self, f: Formula):
        """ Process a given formula and return the corresponding LP rule body, along with declaring in the given LP
        any number of extra rules necessary to ensure equivalence of the body with the truth value of the formula.
        """
        ref = symref(f)
        res = self.node_cache.get(ref, None)
        # If the formula has been processed before and an auxiliary LP atom for it created, return that
        if res is not None:
            return res

        if isinstance(f, Tautology):
            return []

        elif isinstance(f, Atom):
            return [self.tarski_atom_to_lp_atom(f)]

        elif isinstance(f, CompoundFormula):
            if f.connective == Connective.And:
                return list(itertools.chain.from_iterable(self.process_formula(sub) for sub in f.subformulas))

            elif f.connective == Connective.Or:
                variables = free_variables(f)
                aux = self.gen_aux_atom([self.process_term(v) for v in variables])
                sub = [self.process_formula(s) for s in f.subformulas]
                for body in sub:
                    self.lp.rule(aux, body)
                return [aux]

            elif f.connective == Connective.Not:
                assert len(f.subformulas) == 1
                subf = f.subformulas[0]
                if not isinstance(subf, Atom):
                    raise RuntimeError("Negation of compound formulas not yet implemented")
                processed, = self.process_formula(subf)  # Unpack the length-1 list
                return [negate_lp_atom(processed)]

            else:
                raise RuntimeError('Unexpected connective "{}" within CompoundFormula "{}"'.format(f.connective, f))

        elif isinstance(f, QuantifiedFormula):
            if f.quantifier == Quantifier.Exists:
                aux = self.gen_aux_atom()  # Simply don't use any variable in the new atom
                self.lp.rule(aux, self.process_formula(f.formula))
                return [aux]

            else:
                assert f.quantifier == Quantifier.Forall
                raise RuntimeError('TODO')

        raise RuntimeError('Unexpected formula "{}" with type "{}"'.format(f, type(f)))

    def process_term(self, t: Term):
        """ Return the name of the LP constant corresponding to the given term. For instance, the variable "from" of
        type "place" will get transformed into a name "From" (capitalized), whereas the constant "b1" of type block will
        get transformed into a name "b1". We assume that the type information is used elsewhere. """
        if isinstance(t, Variable):
            return make_variable_name(t.symbol)  # lp_atom_from_term(t)
        elif isinstance(t, Constant):
            return t.symbol

        raise RuntimeError('Unexpected term "{}" with type "{}"'.format(t, type(t)))

    def process_effect(self, eff):
        """ Process a given effect and return the corresponding LP rule (a pair with head and body). For instance a
        conditional effect "p -> q(X)" will be transformed into a head q(X) and a body p.
        Additionally, declare in the given LP any number of extra rules necessary to ensure equivalence of the body
        with the truth value of the effect conditions (i.e. this will be mostly necessary for conditional effects).
        """
        assert isinstance(eff, (SingleEffect, UniversalEffect))
        if isinstance(eff, AddEffect):
            head = self.tarski_atom_to_lp_atom(eff.atom)
            return head, self.process_formula(eff.condition)
        elif isinstance(eff, DelEffect):
            return None, []  # Simply ignore the delete effects

        raise RuntimeError('Unexpected effect "{}" with type "{}"'.format(eff, type(eff)))

    def tarski_atom_to_lp_atom(self, atom: Atom):
        return self.lp_atom(atom.predicate.symbol, [self.process_term(sub) for sub in atom.subterms])

    def lp_type_atom_from_term(self, t: Term):
        """ Return a LP atom with type information from a given term, e.g. of the form block(b) for a constant,
        or block(X) for a variable. """
        if not isinstance(t, (Constant, Variable)):
            raise RuntimeError("Rechability logic program not ready for functional terms")
        name = make_variable_name(t.symbol) if isinstance(t, Variable) else _uncapitalize(t.symbol)
        return self.lp_atom(t.sort.name, [name])

    def lp_atom(self, symbol, args=None):
        args = args or []
        infix = False
        if isinstance(symbol, BuiltinPredicateSymbol):  # Special treatment for built-ins as =, !=, <, etc.
            symbol = symbol.value
            infix = True
        return LPAtom(self.tr.normalize(symbol), [self.tr.normalize(a) for a in args], infix=infix)


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
    if negated is None:
        # We must have a non-builtin predicate symbol, hence we use the classical ASP negation symbol "-"
        assert not atom.infix
        negated = "-{}".format(negated)
    else:
        assert atom.infix
    return LPAtom(negated, atom.args, atom.infix)


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

    def normalize(self, name: str):
        """ Translate a given name and keep the translation """
        translated = self.d.get(name, None)
        if translated is None:
            translated = sanitize(name)
            if name in self.inv or translated in self.inv:
                raise RuntimeError('Sanitization of STRIPS name for ASP purposes would create a name clash for key '
                                   '"{}"'.format(name))

            if translated != name:
                translated = self._insert(name, translated)
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
    alphabet = "XYZABCDEFGHIJKLMNOPQRSTUFW"
    res = alphabet[i] if i < len(alphabet) else "X{}".format(i)
    return res.lower() if lowercase else res
