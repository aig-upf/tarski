# -*- coding: utf-8 -*-
import itertools
import copy

import tarski.fstrips as fs
import tarski.fstrips.hybrid as hybrid
from tarski.syntax.transform import TermSubstitution
from tarski.syntax.visitors import CollectVariables
from tarski.util import IndexDictionary

from . import instantiation


class ReactionGrounder(object):

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_reactions = IndexDictionary()
        self.schemas = list(self.problem.reactions.values())
        self.reactions_generated = 0

    def __str__(self):
        return 'Reactions generated: {}'.format(self.reactions_generated)

    def calculate_reactions(self):

        for react_schema in self.schemas:
            k, syms, substs = instantiation.enumerate_groundings(self.L, react_schema.parameters)
            for values in itertools.product(*substs):
                subst = {syms[k]: v for k, v in enumerate(values)}

                g_cond = copy.deepcopy(react_schema.condition)
                op = TermSubstitution(self.L, subst)
                g_cond.accept(op)
                var_collector = CollectVariables(self.L)
                g_cond.accept(var_collector)
                assert len(var_collector.variables) == 0

                g_eff = copy.deepcopy(react_schema.effect)
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

                self.problem.ground_reactions.add(hybrid.Reaction(self.L, \
                react_schema.name, [], g_cond, g_eff))
            self.reactions_generated += k
