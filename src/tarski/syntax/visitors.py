# -*- coding: utf-8 -*-
from ..syntax import symref, CompoundFormula, QuantifiedFormula, Atom, CompoundTerm, Variable


class MatchExpression:
    """
        This Visitor traverses a formula/expression stopping when
        finding an exact syntactic match for the target
    """

    def __init__(self, target):
        self.psi = target
        self.target = symref(target)
        self.hits = 0

    def visit(self, phi):
        if isinstance(phi, CompoundFormula):
            if symref(phi) == self.target:
                self.hits += 1
                return
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            if symref(phi) == self.target:
                self.hits += 1
                return
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            if symref(phi) == self.target:
                self.hits += 1
                return
            for t in phi.subterms:
                t.accept(self)
        elif isinstance(phi, CompoundTerm):
            if symref(phi) == self.target:
                self.hits += 1
                return
            for t in phi.subterms:
                t.accept(self)


class CollectVariables:
    """ Collect all variables in a given formula or term """

    def __init__(self):
        self.variables = set()

    def visit(self, phi):

        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    self.variables.add(t)
                else:
                    t.accept(self)
        elif isinstance(phi, CompoundTerm):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    self.variables.add(t)
                else:
                    t.accept(self)


class CollectFreeVariables:
    """ Collect all free variables in a given formula or term """
    def __init__(self):
        self.quantified_vars = set()
        self._free_variables = set()

    @property
    def free_variables(self):
        for ref in self._free_variables:
            yield ref.expr

    def visit(self, phi):
        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            for x in phi.variables:
                x_ref = symref(x)
                self.quantified_vars.add(x_ref)
            phi.formula.accept(self)
            for x in phi.variables:
                x_ref = symref(x)
                self.quantified_vars.remove(x_ref)

        elif isinstance(phi, Atom):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    t_ref = symref(t)
                    if t_ref not in self.quantified_vars:
                        self._free_variables.add(t_ref)
                else:
                    t.accept(self)
        elif isinstance(phi, CompoundTerm):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    t_ref = symref(t)
                    if t_ref not in self.quantified_vars:
                        self._free_variables.add(t_ref)
                else:
                    t.accept(self)
