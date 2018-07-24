# -*- coding: utf-8 -*-

"""
    Substitution Operator
"""
from ..formulas import CompoundFormula, QuantifiedFormula, Variable, Atom
from ..terms import CompoundTerm
from .errors import SubstitutionError


class TermSubstitution:
    """
        This Visitor applies a substitution operation on
        a given formula, replacing terms in the dictionary
        ```subst``` by the associated term.
    """

    def __init__(self, lang, subst):
        self.L = lang
        self.subst = subst

    def visit(self, phi):

        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            if any(x in self.subst for x in phi.variables):
                raise SubstitutionError(phi, self.subst, 'Attempted to substitute variable bound by quantifier')
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            new_subterms = list(phi.subterms)
            for k, t in enumerate(new_subterms):
                rep = self.subst.get(t, None)
                if rep is None:
                    t.accept(self)
                else:
                    if isinstance(rep, Variable):
                        new_subterms[k] = rep
                    else:
                        new_subterms[k] = rep
            phi.subterms = tuple(new_subterms)
        elif isinstance(phi, CompoundTerm):
            new_subterms = list(phi.subterms)
            for k, t in enumerate(new_subterms):
                rep = self.subst.get(t, None)
                if rep is None:
                    t.accept(self)
                else:
                    if isinstance(rep, Variable):
                        new_subterms[k] = rep
                    else:
                        new_subterms[k] = rep
            phi.subterms = tuple(new_subterms)
