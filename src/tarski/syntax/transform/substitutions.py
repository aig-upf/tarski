
import copy
import itertools
from typing import List

from ..symrefs import symref
from ..formulas import CompoundFormula, QuantifiedFormula, Atom, Formula, Tautology, Contradiction, Connective
from ..terms import Term, CompoundTerm, Variable, Constant, IfThenElse
from .errors import SubstitutionError


class TermSubstitution:
    """ Apply the given substitution to a formula, term or action effect. """
    def __init__(self, subst):
        self.subst = subst

    def visit(self, phi):
        from ... import fstrips as fs

        if isinstance(phi, (Tautology, Contradiction, Constant)):
            pass

        elif isinstance(phi, CompoundFormula):
            _ = [self.visit(f) for f in phi.subformulas]

        elif isinstance(phi, QuantifiedFormula):
            if any(symref(x) in self.subst for x in phi.variables):
                raise SubstitutionError(phi, self.subst, 'Attempted to substitute variable bound by quantifier')
            self.visit(phi.formula)

        elif isinstance(phi, (Atom, CompoundTerm)):
            phi.subterms = self.substitute_termlist(phi.subterms)

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
        elif isinstance(phi, IfThenElse):
            self.visit(phi.condition)
            phi.subterms = self.substitute_termlist(phi.subterms)

        else:
            raise TypeError(f'Unexpected element {phi} of type {type(phi)} when performing term substitution')

    def substitute_termlist(self, termlist):
        new_subterms = list(termlist)
        for k, t in enumerate(new_subterms):
            if isinstance(t, Variable):
                v = symref(t)
                if v in self.subst:
                    new_subterms[k] = self.subst[v]
            else:
                self.visit(t)

        return tuple(new_subterms)


def substitute_subformula(phi, subst):
    if isinstance(phi, (Tautology, Contradiction, Constant)):
        return phi
    elif isinstance(phi, CompoundFormula):
        if phi.connective == Connective.Not:
            try:
                return subst[symref(phi)]
            except KeyError:
                return phi

        new_subf = []
        for gamma in phi.subformulas:
            new_subf += [substitute_subformula(gamma, subst)]
        phi.subformulas = new_subf
        return phi
    elif isinstance(phi, QuantifiedFormula):
        raise SubstitutionError(phi, subst, "substitute_subformula(): operation unsafe for quantified formulas")
    elif isinstance(phi, Atom):
        try:
            return subst[symref(phi)]
        except KeyError:
            return phi
    elif isinstance(phi, CompoundTerm):
        return phi
    elif isinstance(phi, IfThenElse):
        phi.condition = substitute_subformula(phi.condition, subst)
        return phi
    else:
        raise TypeError(f'Unexpected element {phi} of type {type(phi)} when performing subformula substitution')


def term_substitution(element, substitution, inplace=False):
    """ Apply the given substitution to the given element of a problem or language.
    :param element: A formula, term, or FSTRIPS action effect.
    :param substitution: A dictionary from TermReferences that are expected to be Variables to other terms.
    :param inplace: If true, the given element is modified in place; otherwise a different object is returned.
    :return: The result of applying the substituion to the element.
    """
    from ... import fstrips as fs
    assert isinstance(element, (Formula, Term, fs.BaseEffect, fs.Action))
    phi = element if inplace else copy.deepcopy(element)
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
