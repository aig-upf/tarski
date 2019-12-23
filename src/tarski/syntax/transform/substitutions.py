
import copy
import itertools
from typing import List

from ..symrefs import symref
from ..formulas import CompoundFormula, QuantifiedFormula, Atom, Formula
from ..terms import Term, CompoundTerm, Variable, Constant
from .errors import SubstitutionError


class TermSubstitution:
    """ Apply the given substitution to a formula, term or action effect. """
    def __init__(self, subst):
        self.subst = subst

    def visit(self, phi):
        from ... import fstrips as fs
        if isinstance(phi, CompoundFormula):
            _ = [self.visit(f) for f in phi.subformulas]

        elif isinstance(phi, QuantifiedFormula):
            if any(symref(x) in self.subst for x in phi.variables):
                raise SubstitutionError(phi, self.subst, 'Attempted to substitute variable bound by quantifier')
            self.visit(phi.formula)

        elif isinstance(phi, (Atom, CompoundTerm)):
            new_subterms = list(phi.subterms)
            for k, t in enumerate(new_subterms):
                if isinstance(t, Variable):
                    v = symref(t)
                    if v in self.subst:
                        new_subterms[k] = self.subst[v]
                else:
                    self.visit(t)
            phi.subterms = tuple(new_subterms)

        elif isinstance(phi, fs.BaseEffect):
            self.visit(phi.condition)
            if isinstance(phi, (fs.AddEffect, fs.DelEffect)):
                self.visit(phi.atom)

            elif isinstance(phi, fs.LiteralEffect):
                self.visit(phi.lit)

            elif isinstance(phi, fs.FunctionalEffect):
                self.visit(phi.lhs)

                if isinstance(phi.rhs, Variable):
                    v = symref(phi.rhs)
                    if v in self.subst:
                        phi.rhs = self.subst.get(v)
                else:
                    self.visit(phi.rhs)


def term_substitution(phi, substitution, inplace=False):
    """ Return the result of applying the given substitution to the given formula or term of the language.
    If `inplace` is true, the given formula is the one modified.
    """
    from ... import fstrips as fs
    assert isinstance(phi, (Formula, Term, fs.BaseEffect))
    phi = phi if inplace else copy.deepcopy(phi)
    op = TermSubstitution(substitution)
    op.visit(phi)
    return phi


def create_substitution(symbols, values):
    return {symref(symbols[k]): v for k, v in enumerate(values)}


def enumerate_substitutions(variables: List[Variable]):
    """ Enumerates all possible substitutions for the given variables. """
    assert all(isinstance(var, Variable) for var in variables)
    domains = [var.sort.domain() for var in variables]
    for values in itertools.product(*domains):
        yield create_substitution(variables, values)
