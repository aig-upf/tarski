
import itertools

from ...fstrips import hybrid
from ...syntax import create_substitution, substitute_expression
from ...util import SymbolIndex
from . import instantiation


class DifferentialConstraintGrounder:

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_differential_constraints = SymbolIndex()
        self.schemas = list(self.problem.differential_constraints.values())
        self.differential_constraints_generated = 0

    def __str__(self):
        return 'Reactions generated: {}'.format(self.differential_constraints_generated)

    def calculate_constraints(self):

        for ode_schema in self.schemas:
            k, syms, substs = instantiation.enumerate_groundings(ode_schema.parameters)
            for values in itertools.product(*substs):
                subst = create_substitution(syms, values)
                g_cond = substitute_expression(ode_schema.condition, subst)
                g_variate = substitute_expression(ode_schema.variate, subst)
                g_ode = substitute_expression(ode_schema.ode, subst)

                self.problem.ground_differential_constraints.add(
                    hybrid.DifferentialConstraint(self.L, ode_schema.name, [], g_cond, g_variate, g_ode))
            self.differential_constraints_generated += k
