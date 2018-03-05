# -*- coding: utf-8 -*-

"""
    Prenex Rewriter
"""
import copy

from tarski.syntax.temporal import ltl
from tarski.syntax.formulas import *
from tarski.syntax.transform.nnf import NNFRewriter

from . errors import TransformationError

class PrenexRewriter(object):
    """
        This class rewrites the input formula phi into an equivalent formula
        in Prenex NNF (referenced by the )

    """

    def __init__(self):
        self.blueprint = None
        self.prenex = None


    def _convert(self, phi) :
        if isinstance(phi,CompoundFormula):
            if phi.connective == Connective.Not:
                if isinstance(phi.subformulas[0],QuantifiedFormula):
                    raise TransformationError('prenex', phi, 'Subformula is not in NNF!')
                elif isinstance(phi.subformulas[0],CompoundFormula):
                    raise TransformationError('prenex', phi, 'Subformula is not in NNF!')
                else :
                    return phi
            else:
                # and/or
                subformulas[0] = self._convert(subformulas[0])
                subformulas[1] = self._convert(subformulas[1])
                lhs = subformulas[0]
                rhs = subformulas[1]
                is_quant_lhs = isinstance(lhs,QuantifiedFormula)
                is_quant_rhs = isinstance(rhs,QuantifiedFormula)
                if not is_quant_lhs and not is_quant_rhs:
                    return phi
                elif is_quant_lhs and is_quant_rhs:
                    raise TransformationError('prenex',phi,'Not Implemented Yet!')
                    pass
                elif is_quant_rhs:
                    raise TransformationError('prenex',phi,'Not Implemented Yet!')
                    pass
                else: # is_quant_lhs
                    assert is_quant_lhs
                    raise TransformationError('prenex',phi,'Not Implemented Yet!')
                    pass

        elif isinstance(phi,QuantifiedFormula):
            phi.formula = self._convert(phi.formula)
            if isintance(phi.formula, QuantifiedFormula):
                if phi.formula.quantifier == phi.quantifier: #absorb
                    for x in phi.variables:
                        phi.formula.variables.append(x)
                    return phi.formula
                if phi.formula.quantifier == Quantifier.Forall: # push up universal
                    phi.quantifier, phi.formula.quantifier = phi.formula.quantifier, phi.quantifier
                    phi.variables, phi.formula.variables = phi.formula.variables, phi.variables
                return phi
            else:
                return phi
        else :
            return phi

    def rewrite(self, phi, do_copy = True):
        to_nnf = NNFRewriter()
        self.blueprint = to_nnf.rewrite(phi,do_copy)
        self.prenex = self._convert(self.blueprint)
