# -*- coding: utf-8 -*-
import itertools, copy

from . import instantiation
from tarski import fstrips as fs
from tarski.syntax.transform import TermSubstitution
from tarski.util import IndexDictionary
from tarski.syntax import *

class ConstraintGrounder(object):

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_constraints = IndexDictionary()
        self.schemas = list(self.problem.constraints)
        self.constraints_generated = 0

    def __str__(self):
        return 'Constraints Generated: {}'.format(self.constraints_generated)

    def calculate_constraints(self):

        for const_schema in self.schemas:
            # 1. Collect set of free variables in the constraint
            raise NotImplementedError()

            #K, syms, substs = instantiation.enumerate(self.L, const_schema.parameters )
            #for values in itertools.product(*substs):
            #    subst = { syms[k] : v for k,v in enumerate(values) }
            #    g_prec = copy.deepcopy(act_schema.precondition)
            #    op = TermSubstitution(self.L,subst)
            #    g_prec.accept(op)
            #    var_collector = CollectVariables(self.L)
            #    g_prec.accept(var_collector)
            #    assert len(var_collector.variables) == 0
            #    g_effs = []
            #    for eff in act_schema.effects:
            #        g_eff = copy.deepcopy(eff)
            #        g_eff.accept(op)
            #        var_collector = CollectVariables(self.L)
            #        g_eff.accept(var_collector)
            #        assert len(var_collector.variables) == 0
            #        g_effs.append(g_eff)
            #    self.problem.ground_actions.add(fs.Action(self.L, act_schema.name, [], g_prec, g_effs))
            #self.actions_generated += K
