# -*- coding: utf-8 -*-
import itertools
import copy

import tarski.fstrips as fs
import tarski.fstrips.hybrid as hybrid
from tarski.syntax.transform import TermSubstitution
from tarski.syntax.visitors import CollectVariables
from tarski.util import IndexDictionary
from . import instantiation


class DifferentialConstraintGrounder(object):

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_differential_constraints = IndexDictionary()
        self.schemas = list(self.problem.differential_constraints.values())
        self.differential_constraints_generated = 0

    def __str__(self):
        return 'Reactions generated: {}'.format(self.differential_constraints_generated)

    def calculate_constraints(self):

        for ode_schema in self.schemas:
            k, syms, substs = instantiation.enumerate_groundings(self.L, ode_schema.parameters)
            for values in itertools.product(*substs):
                subst = {syms[k]: v for k, v in enumerate(values)}
                g_cond = copy.deepcopy(ode_schema.condition)
                op = TermSubstitution(self.L, subst)
                g_cond.accept(op)
                var_collector = CollectVariables(self.L)
                g_cond.accept(var_collector)
                assert len(var_collector.variables) == 0

                g_variate = copy.deepcopy(ode_schema.variate)
                op = TermSubstitution(self.L, subst)
                g_variate.accept(op)
                var_collector = CollectVariables(self.L)
                g_variate.accept(var_collector)
                assert len(var_collector.variables) == 0

                g_ode = copy.deepcopy(ode_schema.ode)
                op = TermSubstitution(self.L, subst)
                g_ode.accept(op)
                var_collector = CollectVariables(self.L)
                g_ode.accept(var_collector)
                assert len(var_collector.variables) == 0

                self.problem.ground_differential_constraints.add(\
                    hybrid.DifferentialConstraint( self.L, ode_schema.name, [], \
                    g_cond, g_variate, g_ode))
            self.differential_constraints_generated += k
