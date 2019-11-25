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

    def _convert(self, phi: Formula, negated=False):
        if isinstance(phi, Tautology):
            return Contradiction if negated else phi

        if isinstance(phi, Contradiction):
            return Tautology if negated else phi

        if isinstance(phi, Atom):
            return neg(phi) if negated else phi

        if isinstance(phi, QuantifiedFormula):  # Convert quantified formulas recursively
            phi.formula = self._convert(phi.formula, negated)
            phi.quantifier = negate_quantifier(phi.quantifier) if negated else phi.quantifier
            return phi

        if isinstance(phi, CompoundFormula) and phi.connective in (Connective.And, Connective.Or):
            # Convert conjunct / disjunct formulas recursively, applying De Morgan if negated=True
            phi.subformulas = tuple(self._convert(sub, negated) for sub in phi.subformulas)
            phi.connective = negate_connective(phi.connective) if negated else phi.connective
            return phi

        if isinstance(phi, CompoundFormula) and phi.connective == Connective.Not:
            assert len(phi.subformulas) == 1
            return self._convert(phi.subformulas[0], not negated)

        raise err.UnexpectedElementType(phi)

    def convert(self):
        self.nnf = self._convert(self.blueprint)
        return self.nnf

    @staticmethod
    def rewrite(phi, do_copy=True):
        trans = NNFTransformation(phi, do_copy)
        trans.convert()
        return trans


def negate_connective(connective):
    return {Connective.Or: Connective.And, Connective.And: Connective.Or}[connective]


def to_negation_normal_form(phi, do_copy=True):
    trans = NNFTransformation(phi, do_copy)
    return trans.convert()
