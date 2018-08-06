# -*- coding: utf-8 -*-
"""
    Universal Quantification Elimination
"""
import itertools
import copy
from ..formulas import land, Quantifier, QuantifiedFormula
from ..transform.prenex import PrenexTransformation
from ..transform.subst import TermSubstitution

from .errors import TransformationError


class UniversalQuantifierElimination:
    """
        This class rewrites the input formula phi into an equivalent formula
        in Prenex NNF (referenced by the )

    """

    def __init__(self, lang, phi, do_copy=True):
        self.L = lang
        self.blueprint = PrenexTransformation.rewrite(self.L, phi, do_copy).prenex
        # print(str(self.blueprint))
        self.universal_free = None

    def _convert(self, phi):

        if isinstance(phi, QuantifiedFormula):
            if phi.quantifier == Quantifier.Forall:
                card, syms, substs = _enumerate_instantations(phi)
                if card == 0:
                    raise TransformationError("universal elimination", phi, "No constants were defined!")
                conjuncts = []
                for values in itertools.product(*substs):
                    subst = {syms[k]: v for k, v in enumerate(values)}
                    g_const = copy.deepcopy(phi.formula)
                    op = TermSubstitution(self.L, subst)
                    g_const.accept(op)
                    conjuncts.append(g_const)
                # print(len(conjuncts))
                return land(*conjuncts)

            else:
                phi.formula = self._convert(phi.formula)
                return phi

        return phi

    def convert(self):
        self.universal_free = self._convert(self.blueprint)

    @staticmethod
    def rewrite(lang, phi, do_copy=True):
        trans = UniversalQuantifierElimination(lang, phi, do_copy)
        trans.convert()
        return trans


def _enumerate_instantations(phi):
    assert isinstance(phi, QuantifiedFormula)
    syms = []
    instantiations = []
    cardinality = 1
    for st in phi.variables:
        if st.sort.builtin:
            raise TransformationError("universal elimination", phi,
                                      "Variable found of built-in sort '{}', domain is too large!".format(
                                          st.sort.name))
        syms.append(st)
        instantiations.append(list(st.sort.domain()))
        cardinality *= len(instantiations[-1])

    return cardinality, syms, instantiations
