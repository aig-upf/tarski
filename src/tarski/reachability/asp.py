"""
    A module to create reachability-related logic programs from PDDL tasks
"""
import itertools

from ..syntax import Formula, Atom, CompoundFormula, Connective
from ..syntax.sorts import parent
from ..fstrips import Problem

SOLVABLE = "solvable"
SUBFORMULA = "_sf"


def create_reachability_lp(problem: Problem):
    lp = LogicProgram()
    return ReachabilityLPCompiler(problem, lp).create()


class ReachabilityLPCompiler:
    def __init__(self, problem: Problem, lp):
        self.problem = problem
        self.lp = lp
        self.node_cache = dict()

    def create(self):
        problem, lang, lp = self.problem, self.problem.language, self.lp
        tr = Translator()

        # Declare the PDDL objects with their types, e.g. with a fact "block(b1)".
        constants = lang.constants()
        _ = [lp.rule(_atom(tr.normalize(c.sort.name), tr.normalize(c.symbol))) for c in constants]

        # Declare the type hierarchy, e.g. with a rule "object(X) :- block(X)."
        for s in lang.sorts:
            if not s.builtin:  # TODO Decide what to do with builtins
                p = parent(s)
                if p is not None:
                    lp.rule(_atom(tr.normalize(p.name), _var()),
                            _atom(tr.normalize(s.name), _var()))

        # Process goal: e.g. "solvable :- on(a,b), on(b,c)." (note that the goal is always ground)
        body = self.process_formula(problem.goal)
        lp.rule(LPAtom(SOLVABLE), body)

        with open("/tmp/test_asp_model.lp", "w") as fd:
            _ = [print(str(r), file=fd) for r in lp.rules]

        assert 0



    def process_formula(self, f: Formula):
        # TODO Cache recurring formulas
        # TODO Deal with non-conjunctive formulas

        if isinstance(f, Atom):
            body = [f]
        elif isinstance(f, CompoundFormula):
            if f.connective == Connective.And:
                body = list(itertools.chain.from_iterable(self.process_formula(sub) for sub in f.subformulas))
            else:
                raise RuntimeError('Unexpected connective "{}" within CompoundFormula "{}"'.format(f.connective, f))
        else:
            raise RuntimeError('Unexpected formula "{}" with type "{}"'.format(f, type(f)))

        return body


class LPAtom:
    def __init__(self, symbol: str, args=None):
        self.symbol = symbol
        self.args = args or []

    def __str__(self):
        """ Return a string of the form 'symbol(arg1, ..., argn)', or 'symbol()', if args is empty """
        arglist = ", ".join(str(arg) for arg in _ensure_list(self.args))
        return "{}({})".format(self.symbol, arglist)


def _atom(symbol, args=None):
    """ Return a string of the form 'symbol(arg1, ..., argn)', or 'symbol()', if args is empty """
    args = args or []
    arglist = ", ".join(str(arg) for arg in _ensure_list(args))
    return "{}({})".format(symbol, arglist)


def _ensure_list(elem):
    return elem if isinstance(elem, list) else [elem]


class Translator:
    def __init__(self):
        self.d = dict()
        self.inv = dict()

    def normalize(self, name: str):
        """ Translate a given name and keep the translation """
        try:
            return self.d[name]
        except KeyError:
            sanitized = sanitize(name)
            if name in self.inv or sanitized in self.inv:
                raise RuntimeError('Sanitization of STRIPS name for ASP purposes would create a name clash for key '
                                   '"{}"'.format(name))

            return self._insert(name, sanitized)

    def _insert(self, k, v):
        self.d[k] = v
        self.inv[v] = k
        return v


class LogicProgram:
    def __init__(self):
        self.rules = []

    def rule(self, head, body=None):
        self.rules.append(_print_rule(head, body))


class InFileLogicProgram:
    def __init__(self, fd):
        self.fd = fd

    def rule(self, head, body=None):
        self.fd.write(_print_rule(head, body) + "\n")


def _print_rule(head, body):
    return "{}.".format(head) if body is None else "{} :- {}.".format(head, _print_body(body))


def _print_body(body):
    return ", ".join(str(x) for x in body)


def sanitize(name: str):
    """ Normalize the given string by removing chars that are potentially problematic for the LP solver """
    return name.replace("-", "__").lower()


def _var(i=0, lowercase=False):
    """ Return a distinct variable name for each given value of i """
    alphabet = "XYZABCDEFGHIJKLMNOPQRSTUFW"
    res = alphabet[i] if i < len(alphabet) else "X{}".format(i)
    return res.lower() if lowercase else res
