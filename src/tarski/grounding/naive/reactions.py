
import itertools

from ...fstrips import hybrid
from ...fstrips.representation import substitute_expression
from ...syntax import create_substitution
from ...util import SymbolIndex
from . import instantiation


class ReactionGrounder:

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_reactions = SymbolIndex()
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

            k, syms, substs = instantiation.enumerate_groundings(react_schema.parameters)
            for values in itertools.product(*substs):
                subst = create_substitution(syms, values)

                g_cond = substitute_expression(react_schema.condition, subst)
                g_eff = substitute_expression(react_schema.effect, subst)

                self.problem.ground_reactions.add(hybrid.Reaction(self.L, react_schema.name, [], g_cond, g_eff))
            self.reactions_generated += k
