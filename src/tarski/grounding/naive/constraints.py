# -*- coding: utf-8 -*-
import itertools, copy

from . import instantiation
from tarski import fstrips as fs
from tarski.syntax.transform import TermSubstitution
from tarski.syntax.transform import UniversalQuantifierElimination
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
            const_schema = UniversalQuantifierElimination.rewrite(self.L, const_schema).universal_free
            var_collector = CollectVariables(self.L)
            const_schema.accept(var_collector)
            K, syms, substs = instantiation.enumerate(self.L, list(var_collector.variables) )
            for values in itertools.product(*substs):
                subst = { syms[k] : v for k,v in enumerate(values) }
                g_const = copy.deepcopy(const_schema)
                op = TermSubstitution(self.L,subst)
                g_const.accept(op)
                op2 = CollectVariables(self.L)
                g_const.accept(op2)
                assert len(op2.variables) == 0
                self.problem.ground_constraints.add(g_const)
            self.constraints_generated += K
