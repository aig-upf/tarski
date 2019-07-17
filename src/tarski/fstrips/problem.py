
from collections import OrderedDict

from .. import model
from .action import Action
from .derived import Derived
from . import fstrips as fs
from . import errors as err


class Problem:
    """ A Functional STRIPS problem """

    def __init__(self, problem_name=None, domain_name=None):
        self.name = problem_name
        self.domain_name = domain_name
        self.language = None
        self.init = None
        self.goal = None
        self.constraints = []
        self.actions = OrderedDict()
        self.derived_ = OrderedDict()
        self.metric_ = None

    @property
    def derived_predicates(self):
        return self.derived_

    @property
    def plan_metric(self):
        return self.metric_

    def action(self, name, parameters, precondition, effects):
        if name in self.actions:
            raise err.DuplicateActionDefinition(name, self.actions[name])

        self.actions[name] = Action(self.language, name, parameters, precondition, effects)
        return self.actions[name]

    def derived(self, name, parameters, formula):
        if name in self.derived_:
            raise err.DuplicateDerivedDefinition(name, self.derived_[name])

        self.derived_[name] = Derived(self.language, name, parameters, formula)
        return self.derived_[name]

    def has_action(self, name):
        return name in self.actions

    def get_action(self, name):
        if not self.has_action(name):
            raise err.UndefinedAction(name)
        return self.actions[name]

    def get_symbols(self, pv, ev, cv):
        """
            Applies visitors to syntactic elements matching the definitions for
            preconditions, effects and constraints.

            parameters:
                - pv: FluentSymbolCollector tuned for preconditions
                - ev: FluentSymbolCollector tuned for effects
                - cv: FluentSymbolCollector tuned for constraints
        """
        for _, act in self.actions.items():
            pv.visit(act.precondition)
            for eff in act.effects:
                pv.visit(eff.condition)
                if isinstance(eff, (fs.AddEffect, fs.DelEffect)):
                    ev.visit(eff.atom)
                elif isinstance(eff, fs.LiteralEffect):
                    ev.visit(eff.lit)
                elif isinstance(eff, fs.FunctionalEffect):
                    ev.visit(eff.lhs)
                elif isinstance(eff, fs.ChoiceEffect):
                    ev.visit(eff.obj)
                    _ = [ev.visit(x) for x in eff.variables]
                else:
                    raise RuntimeError("Effect type '{}' cannot be analysed".format(type(eff)))

        for const in self.constraints:
            cv.reset()
            cv.visit(const)

    def metric(self, opt_expression, opt_type):
        self.metric_ = fs.OptimizationMetric(opt_expression, opt_type)

    def __str__(self):
        return 'FSTRIPS Problem "{}", domain "{}"'.format(self.name, self.domain_name)

    __repr__ = __str__


def create_fstrips_problem(language, problem_name=None, domain_name=None):
    """ Creates an FSTRIPS problem with empty initial state and with no assigned goal """
    problem_name = problem_name or "Unnamed FSTRIPS problem"
    domain_name = domain_name or "Unnamed FSTRIPS domain"
    problem = Problem(problem_name=problem_name, domain_name=domain_name)
    problem.language = language
    problem.init = model.create(language)
    return problem
