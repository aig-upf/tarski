"""
    NNF Rewriter
"""
import copy

from ..formulas import neg, QuantifiedFormula, Quantifier, CompoundFormula, Connective


class NNFTransformation:
    """
        This class rewrites the input formula phi into an equivalent formula
        in NNF
    """

    def __init__(self, phi, do_copy=True):
        self.blueprint = None
        if do_copy:
            self.blueprint = copy.deepcopy(phi)
        else:
            self.blueprint = phi
        self.nnf = None

    def _convert(self, phi):
        if isinstance(phi, CompoundFormula):
            if phi.connective == Connective.Not:
                p = phi.subformulas[0]
                if isinstance(p, QuantifiedFormula):
                    if p.quantifier == Quantifier.Exists:
                        p.quantifier = Quantifier.Forall
                    else:
                        assert p.quantifier == Quantifier.Forall
                        p.quantifier = Quantifier.Exists
                    p.formula = self._convert(neg(p.formula))
                    return p
                elif isinstance(p, CompoundFormula):  # De Morgan
                    if p.connective == Connective.Not:
                        return p.subformulas[0]  # eliminate \neg \neg
                    elif p.connective == Connective.And:
                        p.connective = Connective.Or
                    else:
                        assert p.connective == Connective.Or
                        p.connective = Connective.And

                    new_sub = [self._convert(neg(p.subformulas[0])),
                               self._convert(neg(p.subformulas[1]))]
                    p.subformulas = tuple(new_sub)
                    return p
                else:
                    return phi  # nothing to do
            else:
                assert phi.connective == Connective.And or phi.connective == Connective.Or
                new_sub = [self._convert(phi.subformulas[0]),
                           self._convert(phi.subformulas[1])]
                phi.subformulas = tuple(new_sub)
                return phi
        elif isinstance(phi, QuantifiedFormula):
            phi.formula = self._convert(phi.formula)
            return phi
        else:
            return phi

    def convert(self):
        self.nnf = self._convert(self.blueprint)

    @staticmethod
    def rewrite(phi, do_copy=True):
        trans = NNFTransformation(phi, do_copy)
        trans.convert()
        return trans
