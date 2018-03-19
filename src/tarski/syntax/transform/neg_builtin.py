# -*- coding: utf-8 -*-

"""
    Negation Builtin Rewriter
"""
import copy

from tarski.syntax.temporal import ltl
from tarski.syntax.formulas import *
from tarski.syntax.builtins import BuiltinPredicate, create_atom
from . errors import TransformationError


class NegatedBuiltinAbsorption(object):
    """
        This class rewrites the input formula phi into an equivalent formula
        absorbing the negation if the negated formula is a built-in
    """

    def __init__(self,phi, do_copy = True):
        self.blueprint = None
        if do_copy :
            self.blueprint = copy.deepcopy(phi)
        else :
            self.blueprint = phi
        self.formula = None


    def _convert(self, phi):
        if isinstance(phi, CompoundFormula):
            if phi.connective == Connective.Not :
                P = phi.subformulas[0]
                if isinstance(P,Atom):
                    if P.predicate.builtin:
                        try:
                            c = BuiltinPredicate.complement(P.predicate.symbol)
                            return create_atom(c, P.subterms[0],P.subterms[1])
                        except KeyError:
                            pass
                return phi

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
        self.formula = self._convert(self.blueprint)

    @staticmethod
    def rewrite( phi, do_copy = True):
        trans =  NegatedBuiltinAbsorption(phi, do_copy)
        trans.convert()
        return trans
