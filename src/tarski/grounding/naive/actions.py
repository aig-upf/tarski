# -*- coding: utf-8 -*-
import itertools
import copy

from ... import fstrips as fs
from ...syntax.transform import TermSubstitution
from ...syntax.visitors import CollectVariables
from ...util import IndexDictionary
from . import instantiation


class ActionGrounder:

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_actions = IndexDictionary()
        self.schemas = list(self.problem.actions.values())
        self.actions_generated = 0

    def __str__(self):
        return 'Actions generated: {}'.format(self.actions_generated)

    def calculate_actions(self):

        for act_schema in self.schemas:
            k, syms, substs = instantiation.enumerate_groundings(self.L, act_schema.parameters)
            for values in itertools.product(*substs):
                subst = {syms[k]: v for k, v in enumerate(values)}
                g_prec = copy.deepcopy(act_schema.precondition)
                op = TermSubstitution(self.L, subst)
                g_prec.accept(op)
                var_collector = CollectVariables(self.L)
                g_prec.accept(var_collector)
                assert len(var_collector.variables) == 0
                g_effs = []
                for eff in act_schema.effects:
                    g_eff = copy.deepcopy(eff)
                    g_eff.condition.accept(op)
                    if isinstance(g_eff, fs.AddEffect):
                        g_eff.atom.accept(op)
                    elif isinstance(g_eff, fs.DelEffect):
                        g_eff.atom.accept(op)
                    elif isinstance(g_eff, fs.FunctionalEffect):
                        g_eff.lhs.accept(op)
                        g_eff.rhs.accept(op)
                    elif isinstance(g_eff, fs.LogicalEffect):
                        g_eff.formula.accept(op)

                    # MRJ: invariant
                    var_collector = CollectVariables(self.L)
                    g_eff.condition.accept(var_collector)
                    if isinstance(g_eff, fs.AddEffect):
                        g_eff.atom.accept(var_collector)
                    elif isinstance(g_eff, fs.DelEffect):
                        g_eff.atom.accept(var_collector)
                    elif isinstance(g_eff, fs.FunctionalEffect):
                        g_eff.lhs.accept(var_collector)
                        g_eff.rhs.accept(var_collector)
                    elif isinstance(g_eff, fs.LogicalEffect):
                        g_eff.formula.accept(var_collector)
                    assert len(var_collector.variables) == 0

                    g_effs.append(g_eff)
                self.problem.ground_actions.add(fs.Action(self.L, act_schema.name, [], g_prec, g_effs))
            self.actions_generated += k
