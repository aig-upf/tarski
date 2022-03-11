import itertools

from ...syntax import (QuantifiedFormula, Quantifier, create_substitution,
                       substitute_expression)
from ...syntax.ops import all_variables
from ...syntax.transform import (CNFTransformation, NegatedBuiltinAbsorption,
                                 QuantifierEliminationMode, remove_quantifiers)
from ...util import SymbolIndex
from . import instantiation


class ConstraintGrounder:

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_constraints = SymbolIndex()
        self.schemas = list(self.problem.constraints)
        self.constraints_generated = 0

    def __str__(self):
        return f'Constraints Generated: {self.constraints_generated}'

    def calculate_constraints(self):

        for const_schema in self.schemas:
            # 1. Collect set of free variables in the constraint
            const_schema = remove_quantifiers(self.L, const_schema, QuantifierEliminationMode.Forall)
            K, syms, substs = instantiation.enumerate_groundings(all_variables(const_schema))
            for values in itertools.product(*substs):
                subst = create_substitution(syms, values)
                g_const = substitute_expression(const_schema, subst)
                # Simplification steps
                s0 = NegatedBuiltinAbsorption.rewrite(self.L, g_const)
                # CNF
                if isinstance(s0.formula, QuantifiedFormula):
                    assert s0.formula.quantifier == Quantifier.Exists
                    # s0 is of the form \exists x1, ..., xn phi, phi is quantifier free
                    s0.formula.formula = CNFTransformation.rewrite(self.L, s0.formula.formula).cnf
                    self.problem.ground_constraints.add(s0.formula)
                else:
                    s1 = CNFTransformation.rewrite(self.L, s0.formula)
                    self.problem.ground_constraints.add(s1.cnf)
            self.constraints_generated += K
