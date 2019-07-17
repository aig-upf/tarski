
import itertools
import copy

from ...fstrips import hybrid
from ...syntax import create_substitution, TermSubstitution
from ...util import IndexDictionary
from . import instantiation
from .elements import process_expression, process_effect


class ReactionGrounder:

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
            if len(react_schema.parameters) == 0:
                self.problem.ground_reactions.add(hybrid.Reaction(self.L,
                                                                  react_schema.name, [], react_schema.condition,
                                                                  react_schema.effect))
                self.reactions_generated += 1
                continue

            k, syms, substs = instantiation.enumerate_groundings(self.L, react_schema.parameters)
            for values in itertools.product(*substs):
                subst = create_substitution(syms, values)

                op = TermSubstitution(self.L, subst)

                g_cond = process_expression(self.L, react_schema.condition, op)

                g_eff = copy.deepcopy(react_schema.effect)
                g_eff.condition = process_expression(self.L, g_eff.condition, op, False)
                g_eff = process_effect(self.L, g_eff, op)

                self.problem.ground_reactions.add(hybrid.Reaction(self.L, react_schema.name, [], g_cond, g_eff))
            self.reactions_generated += k
