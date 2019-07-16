
import itertools
import copy

from ...syntax import create_substitution, TermSubstitution
from ... import fstrips as fs
from ...util import IndexDictionary
from . import instantiation
from .elements import process_expression, process_effect


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
                subst = create_substitution(syms, values)
                op = TermSubstitution(self.L, subst)
                g_prec = process_expression(self.L, act_schema.precondition, op)
                g_effs = []
                for eff in act_schema.effects:
                    g_eff = copy.deepcopy(eff)
                    g_eff.condition = process_expression(self.L, g_eff.condition, op, False)
                    g_eff = process_effect(self.L, g_eff, op)

                    g_effs.append(g_eff)
                self.problem.ground_actions.add(fs.Action(self.L, act_schema.name, values, g_prec, g_effs))
            self.actions_generated += k
