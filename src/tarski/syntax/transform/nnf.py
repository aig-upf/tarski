# -*- coding: utf-8 -*-

"""
    NNF Rewriter
"""
import copy

from tarski.syntax.temporal import ltl
from tarski.syntax.formulas import *

from . errors import TransformationError


class NNFTransformation(object):
    """
        This class rewrites the input formula phi into an equivalent formula
        in NNF (referenced by the )
    """

    def __init__(self,phi, do_copy = True):
        self.blueprint = None
        if do_copy :
            self.blueprint = copy.deepcopy(phi)
        else :
            self.blueprint = phi
        self.nnf = None


    def _convert(self, phi):
        if isinstance(phi, CompoundFormula):
            if phi.connective == Connective.Not :
                P = phi.subformulas[0]
                if isinstance(P,QuantifiedFormula):
                    if P.quantifier == Quantifier.Exists:
                        P.quantifier = Quantifier.Forall
                    else:
                        assert P.quantifier == Quantifier.Forall
                        P.quantifier = Quantifier.Exists
                    P.formula = self._convert(neg(P.formula))
                    return P
                elif isinstance(P,CompoundFormula): # De Morgan
                    if P.connective == Connective.Not:
                        return P.subformulas[0] # eliminate \neg \neg
                    elif P.connective == Connective.And:
                        P.connective = Connective.Or
                    else:
                        assert P.connective == Connective.Or
                        P.connective = Connective.And

                    new_sub = [self._convert(neg(P.subformulas[0])),\
                                 self._convert(neg(P.subformulas[1]))]
                    P.subformulas = tuple(new_sub)
                    return P
                else :
                    return phi # nothing to do
            else :
                assert phi.connective == Connective.And or phi.connective == Connective.Or
                new_sub = [self._convert(phi.subformulas[0]),\
                            self._convert(phi.subformulas[1])]
                phi.subformulas = tuple(new_sub)
                return phi
        elif isinstance(phi,QuantifiedFormula):
            phi.formula = self._convert(phi.formula)
            return phi
        else:
            return phi

    def convert(self):
        self.nnf = self._convert(self.blueprint)

    @staticmethod
    def rewrite( phi, do_copy = True):
        trans =  NNFTransformation(phi, do_copy)
        trans.convert()
        return trans
