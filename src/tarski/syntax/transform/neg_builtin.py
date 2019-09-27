"""
    Negation Builtin Rewriter
"""
import copy

from ..formulas import Connective, Atom, QuantifiedFormula, CompoundFormula
from ..builtins import negate_builtin_atom


class NegatedBuiltinAbsorption:
    """
        This class rewrites the input formula phi into an equivalent formula
        absorbing the negation if the negated formula is a built-in
    """

    def __init__(self, lang, phi, do_copy=True):
        self.lang = lang
        self.blueprint = copy.deepcopy(phi) if do_copy else phi
        self.formula = None

    def _convert(self, phi):
        if isinstance(phi, CompoundFormula):
            if phi.connective == Connective.Not:
                p = phi.subformulas[0]
                if isinstance(p, Atom) and p.predicate.builtin:
                    try:
                        return negate_builtin_atom(p)
                    except (AttributeError, KeyError):
                        pass
                return phi

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
        self.formula = self._convert(self.blueprint)

    @staticmethod
    def rewrite(lang, phi, do_copy=True):
        trans = NegatedBuiltinAbsorption(lang, phi, do_copy)
        trans.convert()
        return trans
