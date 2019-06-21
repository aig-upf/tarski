# -*- coding: utf-8 -*-
from collections import OrderedDict

from ..problem import Problem
from .reaction import Reaction
from .differential_constraints import DifferentialConstraint
from . import errors as err
from .. import fstrips as fs


class HybridProblem(Problem):
    """ A Functional STRIPS Hybrid problem """

    def __init__(self):
        super().__init__()
        self.reactions = OrderedDict()
        self.differential_constraints = OrderedDict()

    def reaction(self, name, parameters, condition, effect):
        if name in self.reactions:
            raise err.DuplicateReactionDefinition(name, self.reactions[name])
        self.reactions[name] = Reaction(self.language, name, parameters, condition, effect)
        return self.reactions[name]

    def has_reaction(self, name):
        return name in self.reactions

    def get_reaction(self, name):
        if not self.has_reaction(name):
            raise err.UndefinedReaction(name)
        return self.reactions[name]

    def differential_constraint(self, name, parameters, condition, variate, ode):
        if name in self.reactions:
            raise err.DuplicateDifferentialConstraintDefinition(name, self.reactions[name])
        self.differential_constraints[name] = DifferentialConstraint(self.language, name, parameters, condition,
                                                                     variate, ode)
        return self.differential_constraints[name]

    def has_differential_constraint(self, name):
        return name in self.differential_constraints

    def get_differential_constraint(self, name):
        if not self.has_differential_constraint(name):
            raise err.UndefinedDifferentialConstraint(name)
        return self.differential_constraints[name]

    def get_symbols(self, pv, ev, cv):
        super().get_symbols(pv, ev, cv)
        for _, react in self.reactions.items():
            react.condition.accept(pv)
            eff = react.effect
            if isinstance(eff, (fs.AddEffect, fs.DelEffect)):
                eff.atom.accept(ev)
            elif isinstance(eff, (fs.FunctionalEffect, fs.ChoiceEffect)):
                eff.lhs.accept(ev)
            elif isinstance(eff, fs.BlackBoxEffect):
                for yk in eff.lhs[:, 0]:
                    yk.accept(ev)
            else:
                raise RuntimeError("Effect type '{}' cannot be analysed".format(type(eff)))
        for _, dc in self.differential_constraints.items():
            dc.condition.accept(pv)
            dc.variate.accept(ev)

    def __str__(self):
        return 'FSTRIPS Hybrid Problem "{}", domain "{}"'.format(self.name, self.domain_name)

    __repr__ = __str__
