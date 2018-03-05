# -*- coding: utf-8 -*-

"""
    Prenex Rewriter
"""
import copy

from tarski.syntax.temporal import ltl
from tarski.syntax.formulas import *
from tarski.syntax.transform.nnf import NNFTransformation
from tarski.syntax.transform.subst import TermSubstitution

from . errors import TransformationError

class PrenexTransformation(object):
    """
        This class rewrites the input formula phi into an equivalent formula
        in Prenex NNF (referenced by the )

    """

    def __init__(self, L, phi, do_copy = True):
        self.L = L
        self.blueprint = NNFTransformation.rewrite(phi,do_copy).nnf
        self.prenex = None

    def _merge_quantified_subformulas(self, lhs, rhs ):
        new_variables = { (x.symbol,x.sort.name) : x for x in lhs.variables}
        subst = {}
        for y in rhs.variables :
            key_y = (y.symbol,y.sort.name)
            if not key_y in new_variables:
                new_variables[key_y] = y
            else :
                subst[y] = self.L.variable( "{}'".format(y.symbol), y.sort)
        if len(subst) > 0 :
            substitution = TermSubstitution(self.L, subst)
            rhs.formula.accept(substitution)
        new_phi = QuantifiedFormula(lhs.quantifier, \
            list(new_variables.values()), lor( lhs.formula, rhs.formula ))
        return new_phi

    def _merge_mixed_subformulas(self, q_phi, conn, varphi ):
        new_phi = QuantifiedFormula(q_phi.quantifier, \
            q_phi.variables, CompoundFormula(conn, tuple([q_phi.formula, varphi])))
        return new_phi

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
                lhs, rhs = self._convert(phi.subformulas[0]),\
                           self._convert(phi.subformulas[1])
                is_quant_lhs = isinstance(lhs,QuantifiedFormula)
                is_quant_rhs = isinstance(rhs,QuantifiedFormula)
                if not is_quant_lhs and not is_quant_rhs:
                    return phi
                elif is_quant_lhs and is_quant_rhs:
                    # both parts of the formula are quantified
                    if lhs.quantifier == rhs.quantifier:
                        if lhs.quantifier == Quantifier.Exist:
                            if phi.connective == Connective.And :
                                raise TransformationError('prenex', phi, \
                                'Cannot distribute existential quantifier over conjunction, please consider reformulating')
                            assert phi.connective == Connective.Or
                            return self._merge_quantified_subformulas(lhs,rhs)
                        assert lhs.quantifier == Quantifier.Forall
                        if phi.connective == Connective.Or:
                            raise TransformationError('prenex', phi, \
                            'Cannot distribute universal quantifier over disjunction, please consider reformulating')
                        return self._merge_quantified_subformulas(lhs,rhs)
                    # we have different quantifiers, we apply the null quantifier
                    # equivalence

                    if rhs.quantifier == Quantifier.Exists \
                        and lhs.quantifier == Quantifier.Forall:
                        return self._merge_quantified_subformulas(rhs,lhs)
                    return self._merge_quantified_subformulas(lhs,rhs)
                # \forall ( P \lor Q(x)) \equiv P \lor \forall x Q(x)
                # \exists (P \land Q(x)) \equiv P \land \exists x Q(x)
                elif is_quant_rhs:
                    return self._merge_mixed_subformulas(rhs, phi.connective, lhs)
                else: # is_quant_lhs
                    assert is_quant_lhs
                    return self._merge_mixed_subformulas(lhs, phi.connective, rhs)

        elif isinstance(phi,QuantifiedFormula):
            phi.formula = self._convert(phi.formula)
            if isinstance(phi.formula, QuantifiedFormula):
                if phi.formula.quantifier == phi.quantifier: #absorb
                    for x in phi.variables:
                        phi.formula.variables.append(x)
                    return phi.formula
                if phi.formula.quantifier == Quantifier.Exists: # push up existential
                    phi.quantifier, phi.formula.quantifier = phi.formula.quantifier, phi.quantifier
                    phi.variables, phi.formula.variables = phi.formula.variables, phi.variables
                return phi
            else:
                return phi
        else :
            return phi

    def convert(self):
        self.prenex = self._convert(self.blueprint)

    @staticmethod
    def rewrite(L, phi, do_copy = True):
        trans = PrenexTransformation(L, phi, do_copy)
        trans.convert()
        return trans
