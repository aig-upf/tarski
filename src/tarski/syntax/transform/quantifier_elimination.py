"""
    Elimination of first-order universal and existential quantifiers.
"""
import copy
import itertools
from enum import Enum

from ... import errors as err
from .substitutions import create_substitution
from ..formulas import land, lor, Quantifier, QuantifiedFormula, Atom, Tautology, Contradiction, CompoundFormula
from ..transform import term_substitution, to_prenex_negation_normal_form
from .errors import TransformationError


class QuantifierEliminationMode(Enum):
    """" The requested mode for the quantifier elimination algorithm: eliminate only exists, only forall,
    or all quantifiers """
    Exists, Forall, All = range(3)


class QuantifierElimination:
    """ Rewrite the input formula into an equivalent formula where universal and/or existential quantifiers have been
    compiled away by expanding them the finite universe of discourse. Hence, a formula "Forall x p(x)" will be
    transformed into "AND_i p(c_i)", where c_1, ..., c_n are all the (type-consistent) objects in the universe.
    """

    def __init__(self, lang, phi, mode, do_copy=True):
        self.lang = lang
        self.mode = mode
        # self.blueprint = to_prenex_normal_form(lang, phi, do_copy)  # Compile to prenex normal form at preprocessing
        self.blueprint = copy.deepcopy(phi) if do_copy else phi
        self.result = None

    def _eliminate_forall(self):
        return self.mode in (QuantifierEliminationMode.All, QuantifierEliminationMode.Forall)

    def _eliminate_exists(self):
        return self.mode in (QuantifierEliminationMode.All, QuantifierEliminationMode.Exists)

    def _convert(self, phi):
        if isinstance(phi, (Atom, Tautology, Contradiction)):
            return phi  # Already quantifier-free

        if isinstance(phi, CompoundFormula):
            phi.subformulas = tuple(self._convert(sub) for sub in phi.subformulas)
            return phi

        if isinstance(phi, QuantifiedFormula):
            if phi.quantifier == Quantifier.Forall:
                return self._convert(self._expand(phi, land)) if self._eliminate_forall() else self._recurse(phi)

            if phi.quantifier == Quantifier.Exists:
                return self._convert(self._expand(phi, lor)) if self._eliminate_exists() else self._recurse(phi)

        raise err.UnexpectedElementType(phi)

    def _recurse(self, phi):
        phi.formula = self._convert(phi.formula)
        return phi

    def _expand(self, phi: QuantifiedFormula, creator):
        from ...grounding.naive import instantiation
        card, syms, substs = instantiation.enumerate_groundings(phi.variables)
        if card == 0:
            raise TransformationError("quantifier elimination", phi, "No constants were defined!")
        conjuncts = []
        for values in itertools.product(*substs):
            subst = create_substitution(syms, values)
            conjuncts.append(term_substitution(phi.formula, subst))
        return creator(*conjuncts)

    def convert(self):
        self.result = self._convert(self.blueprint)
        return self.result

    @staticmethod
    def rewrite(lang, phi, mode, do_copy=True):
        trans = QuantifierElimination(lang, phi, mode, do_copy)
        trans.convert()
        return trans


def remove_quantifiers(lang, phi, mode, do_copy=True):
    trans = QuantifierElimination(lang, phi, mode, do_copy)
    return trans.convert()
