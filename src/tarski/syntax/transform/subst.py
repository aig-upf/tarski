
import copy

from ..symrefs import symref
from ..formulas import CompoundFormula, QuantifiedFormula, Atom, Formula
from ..terms import Term, CompoundTerm
from .errors import SubstitutionError


class TermSubstitution:
    """ This Visitor applies a substitution operation on a given formula, replacing terms in the dictionary
        'subst' by the associated term. """

    def __init__(self, lang, subst):
        self.lang = lang
        self.subst = subst

    def visit(self, phi):
        if isinstance(phi, CompoundFormula):
            _ = [self.visit(f) for f in phi.subformulas]

        elif isinstance(phi, QuantifiedFormula):
            if any(symref(x) in self.subst for x in phi.variables):
                raise SubstitutionError(phi, self.subst, 'Attempted to substitute variable bound by quantifier')
            self.visit(phi.formula)

        elif isinstance(phi, (Atom, CompoundTerm)):
            new_subterms = list(phi.subterms)
            for k, t in enumerate(new_subterms):
                rep = self.subst.get(symref(t), None)
                if rep is None:
                    self.visit(t)
                else:
                    new_subterms[k] = rep
            phi.subterms = tuple(new_subterms)


def term_substitution(language, phi, substitution, inplace=False):
    """ Return the result of applying the given substitution to the given formula or term of the language.
    If `inplace` is true, the given formula is the one modified.
    """
    assert isinstance(phi, (Formula, Term))
    phi = phi if inplace else copy.deepcopy(phi)
    op = TermSubstitution(language, substitution)
    op.visit(phi)
    return phi


def create_substitution(symbols, values):
    return {symref(symbols[k]): v for k, v in enumerate(values)}
