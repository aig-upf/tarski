"""
    Tranformation of formulas into Negation Normal Form (NNF)
"""
import copy

from ... import errors as err
from ..formulas import neg, Formula, QuantifiedFormula, CompoundFormula, Connective, negate_quantifier, Tautology, \
    Contradiction, Atom


class NNFTransformation:
    """ Rewrite the input formula into an equivalent formula in NNF """

    def __init__(self, phi, do_copy=True):
        self.blueprint = copy.deepcopy(phi) if do_copy else phi
        self.nnf = None

    def _convert(self, phi: Formula):
        if isinstance(phi, (Tautology, Contradiction, Atom)):  # All of them are already in NNF
            return phi

        if isinstance(phi, QuantifiedFormula):  # Convert quantified formulas recursively
            phi.formula = self._convert(phi.formula)
            return phi

        if isinstance(phi, CompoundFormula) and phi.connective in (Connective.And, Connective.Or):
            # Convert conjunct / disjunct formulas recursively
            phi.subformulas = tuple(self._convert(sub) for sub in phi.subformulas)
            return phi

        if isinstance(phi, CompoundFormula) and phi.connective == Connective.Not:
            return self._push_negation(phi)

        raise err.UnexpectedElementType(phi)

    def _push_negation(self, phi):
        assert len(phi.subformulas) == 1
        p = phi.subformulas[0]

        if isinstance(p, Tautology):
            return Contradiction

        if isinstance(p, Contradiction):
            return Tautology

        if isinstance(p, Atom):
            return phi  # A negated literal is already in NNF

        if isinstance(p, QuantifiedFormula):
            p.quantifier = negate_quantifier(p.quantifier)
            p.formula = self._convert(neg(p.formula))
            return p

        if isinstance(p, CompoundFormula):  # Apply De Morgan
            if p.connective == Connective.Not:
                return p.subformulas[0]  # eliminate \neg \neg
            elif p.connective == Connective.And:
                p.connective = Connective.Or
            else:
                assert p.connective == Connective.Or
                p.connective = Connective.And

            p.subformulas = tuple(self._convert(neg(sub)) for sub in p.subformulas)
            return p

        raise err.UnexpectedElementType(p)

    def convert(self):
        self.nnf = self._convert(self.blueprint)

    @staticmethod
    def rewrite(phi, do_copy=True):
        trans = NNFTransformation(phi, do_copy)
        trans.convert()
        return trans
