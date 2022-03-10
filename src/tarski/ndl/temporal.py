"""
    Temporal NDL

    For reference see

    Temporal Planning with Clock-Based SMT Encodings
    Jussi Rintanen
    Proceedings of the 26th Int'l Joint Conference on Artificial Intelligence (IJCAI)
    2017
"""
from ..syntax import Atom, CompoundTerm, CompoundFormula, Constant, symref, Connective, Tautology


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

    def __str__(self):
        return "LOCK {} AFTER {} FOR {}".format(self.r, self.ts, self.td)


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

    def __str__(self):
        return "LOCK {} AFTER {} FOR {}".format(self.r, self.ts, self.td)


class SetLiteralEffect:
    """
    Set literal truth value
    """

    def __init__(self, lit, value):
        self.lit = lit
        self.value = value

    def __str__(self):
        return "SET({}, {})".format(self.lit, self.value)


class AssignValueEffect:
    """
    Sets equality constraint
    """

    def __init__(self, atom, value):
        self.atom = atom
        self.value = value

    def __str__(self):
        return "ASSIGN({}, {})".format(self.atom, self.value)


class UniversalEffect:
    """
    Forall effect
    """

    def __init__(self, variable, effect):
        self.var = variable
        self.eff = effect

    def __str__(self):
        return "FORALL({}, {})".format(self.var, self.effect)


class ConditionalEffect:
    """
    If Then Else effect
    """

    def __init__(self, cond, then_eff, else_eff):
        self.condition = cond
        self.then_eff = then_eff
        self.else_eff = else_eff

    def __str__(self):
        return "IF ({}) \nTHEN {}\n ELSE {}".format(self.condition, self.then_eff, self.else_eff)


class TimedEffect:
    """
    (t, eff) time-delayed effect
    """

    def __init__(self, delay, eff):
        self.delay = delay
        self.eff = eff

    def __str__(self):
        return "AFTER {} APPLY {}".format(self.delay, self.eff)


class UnionExpression:
    """
    A union set expression
    """

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


def is_literal(lit):
    if not isinstance(lit, Atom):
        if isinstance(lit, CompoundFormula):
            return lit.connective == Connective.Not and isinstance(lit.subformulas[0], Atom)
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
        self.parameters = kwargs['parameters']
        self.max_eff_time = 0.0
        self.duration = kwargs.get('duration', None)
        self.grounding_constraints = kwargs.get('grounding_constraints', [])
        self.effect_times = {}
        # precondition
        prec = kwargs['precondition']
        if not isinstance(prec, CompoundFormula) \
                and not isinstance(prec, Atom)\
                and not isinstance(prec, Tautology):
            raise NDLSyntaxError("NDL Syntactic Error: precondition of action must be a compound formula,"
                                 " atom or tautology (given: {})".format(prec))
        self.precondition = prec
        # post-condition
        post = kwargs.get('postcondition', None)
        if post is not None:
            if not isinstance(post, CompoundFormula) \
                    and not isinstance(post, Atom)\
                    and not isinstance(post, Tautology):
                raise NDLSyntaxError("NDL Syntactic Error: post-condition of action must be a compound formula,"
                                     " atom or tautology (given: {})".format(prec))
        self.postcondition = post
        # resource requirements
        self.locks = []
        self.levels = []
        for req in kwargs['requirements']:
            if isinstance(req.eff, ResourceLock):
                self.locks += [req]
                self.max_eff_time = max(self.max_eff_time, req.eff.td)
            elif isinstance(req.eff, ResourceLevel):
                self.levels += [req]
                self.max_eff_time = max(self.max_eff_time, req.eff.td)
            else:
                raise NDLSyntaxError("NDL syntax error: '{}' is not a resource lock or level request".format(req))
        # effects
        self.untimed_effects = []
        self.timed_effects = []
        for eff in kwargs['timed_effects']:
            if not isinstance(eff, TimedEffect):
                raise NDLSyntaxError("NDL Syntax error: eff '{}' must be timed".format(eff))
            self.timed_effects += [eff]
            self.max_eff_time = max(self.max_eff_time, eff.delay)
            wrapped_effect = eff.eff
            if isinstance(wrapped_effect, AssignValueEffect):
                self.effect_times[symref(wrapped_effect.atom == eff.eff.value)] = eff.delay
            elif isinstance(wrapped_effect, SetLiteralEffect):
                self.effect_times[(symref(wrapped_effect.lit), wrapped_effect.value)] = eff.delay
            else:
                raise NotImplementedError("Effects of type {} cannot be handled yet".format(type(wrapped_effect)))
        for elem in kwargs['untimed_effects']:
            self.untimed_effects += [(0, elem)]

    def get_effect_time(self, elem):
        return self.effect_times[elem]


# class Instance:
#
#     def __init__(self, **kwargs):
#         self.language = kwargs['L']
#         self.X = []
#         for x in kwargs['X']:
#             if not isinstance(x, Atom):
#                 raise NDLSyntaxError("NDL Syntax Error: State variables must be boolean terms, found: {}".format(x))
#             self.X += [x]
#         init = kwargs['I']
#         if not isinstance(init, Model):
#             raise UnsupportedFeature("NDL Unsupported feature: initial state must be instance of tarski.Model")
#         if init.evaluator is None:
#             raise SemanticError("NDL Semantic Error: initial state evaluator was not specified")
#         self.I = init
#         goal = kwargs['G']
#         if not isinstance(goal, CompoundFormula) and not isinstance(goal, Atom):
#             raise NDLSyntaxError("NDL Syntax Error: Goal needs to be a compound formula or an atom")
#         self.G = goal
#         self.A = []
#         self.R = set()
#         for act in kwargs['A']:
#             if isinstance(act, Action):
#                 self.A += [act]
#                 # collect resources
#                 for lock in act.locks:
#                     self.R.add(symref(lock.r))
#                 for level in act.levels:
#                     self.R.add(symref(level.r))
