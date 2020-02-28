"""
    Temporal NDL

    For reference see

    Temporal Planning with Clock-Based SMT Encodings
    Jussi Rintanen
    Proceedings of the 26th Int'l Joint Conference on Artificial Intelligence (IJCAI)
    2017
"""
from ..syntax import Atom, CompoundTerm, CompoundFormula, Constant, symref, Connective
from ..model import Model


class NDLSyntaxError(Exception):
    pass


class UnsupportedFeature(Exception):
    pass


class SemanticError(Exception):
    pass


class ResourceLock:

    def __init__(self, **kwargs):
        self.ts = kwargs['ts']
        self.td = kwargs['td']
        self.r = kwargs['r']
        if not isinstance(self.r, CompoundTerm):
            raise NDLSyntaxError("NDL Syntactic Error: resource lock needs to be a term (given: {})".format(self.r))


class ResourceLevel:

    def __init__(self, **kwargs):
        self.ts = kwargs['ts']
        self.td = kwargs['td']
        self.r = kwargs['r']
        if not isinstance(self.r, CompoundTerm):
            raise NDLSyntaxError("NDL Syntactic Error: resource lock must refer to term (given: {})".format(self.r))
        self.n = kwargs['n']
        if not isinstance(self.n, Constant):
            raise NDLSyntaxError("NDL Syntactic Error: resource level must be a constant (given: {}".format(self.n))
        if self.n.sort != self.r.sort:
            raise NDLSyntaxError(
                "NDL Type Mismatch: resource and level have different sorts (resource is: {}, level is: {}".format(
                    self.r.sort, self.n.sort))


def is_literal(l):
    if not isinstance(l, Atom):
        if isinstance(l, CompoundFormula):
            return l.connective == Connective.Not and isinstance(l.subformulas[0], Atom)
        return False
    return True


class Action:
    """
        An action with resources is made of:

        - precondition: a propositional formula over some first-order language
        - a set of resource requirements:
          - [locks] (ts, td, r) subseteq Q x Q x R where Q is the rationals and R is a set of terms mapping
          to the naturals
          - [levels] (ts, td, r, n) subset Q x Q R x N where Q is the rationals and R is a term mapping to
          the naturals, required
          to have a specific value
        such that td >= 0
        - an effect: a set of pairs (t,l) where t in Q, t >=0, l is a literal
    """

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        # precondition
        prec = kwargs['precondition']
        if not isinstance(prec, CompoundFormula) and not isinstance(prec, Atom):
            raise NDLSyntaxError(
                "NDL Syntactic Error: precondition of action must be a compound formula (given: {})".format(prec))
        self.precondition = prec
        # resource requirements
        self.locks = []
        self.levels = []
        for req in kwargs['requirements']:
            if isinstance(req, ResourceLock):
                self.locks += [req]
            elif isinstance(req, ResourceLevel):
                self.levels += [req]
            else:
                raise NDLSyntaxError("NDL syntax error: '{}' is not a resource lock or level request".format(req))
        # effects
        self.effects = []
        for t, l in kwargs['effects']:
            if not isinstance(t, float):
                raise NDLSyntaxError("NDL Syntax error: timepoint '{}' must be rational".format(t))
            if not is_literal(l):
                raise NDLSyntaxError("NDL Syntax error: effect '{}' must be a literal".format(l))
            self.effects += [(t, l)]


class Instance:

    def __init__(self, **kwargs):
        self.language = kwargs['L']
        self.X = []
        for x in kwargs['X']:
            if not isinstance(x, Atom):
                raise NDLSyntaxError("NDL Syntax Error: State variables must be boolean terms, found: {}".format(x))
            self.X += [x]
        init = kwargs['I']
        if not isinstance(init, Model):
            raise UnsupportedFeature("NDL Unsupported feature: initial state must be instance of tarski.Model")
        if init.evaluator is None:
            raise SemanticError("NDL Semantic Error: initial state evaluator was not specified")
        self.I = init
        goal = kwargs['G']
        if not isinstance(goal, CompoundFormula) and not isinstance(goal, Atom):
            raise NDLSyntaxError("NDL Syntax Error: Goal needs to be a compound formula or an atom")
        self.G = goal
        self.A = []
        self.R = set()
        for act in kwargs['A']:
            if isinstance(act, Action):
                self.A += [act]
                # collect resources
                for lock in act.locks:
                    self.R.add(symref(lock.r))
                for level in act.levels:
                    self.R.add(symref(level.r))
