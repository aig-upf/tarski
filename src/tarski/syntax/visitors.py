# -*- coding: utf-8 -*-
from tarski.syntax import *

class MatchSymbol(object):
    """
        This Visitor traverses a formula/expression stopping when
        finding an exact syntactic match for the target
    """

    def __init__(self, target):
        self.psi = target
        self.target = symref(target)
        self.hits = 0

    def visit(self,phi):
        if isinstance(phi, CompoundFormula) and isinstance(self.psi, CompoundFormula):
            if symref(phi) == self.target:
                self.hits += 1
                return
            for f in phi.subformulas: f.accept(self)
        elif isinstance(phi, QuantifiedFormula) and isinstance(self.psi, QuantifiedFormula):
            if symref(phi) == self.target:
                self.hits += 1
                return
            phi.formula.accept(self)
        elif isinstance(phi, Atom) and isinstance(self.psi, Atom):
            if symref(phi) == self.target:
                self.hits += 1
                return
            for k, t in enumerate(phi.subterms):
                t.accept(self)
        elif isinstance(phi, CompoundTerm) and isinstance(self.psi, CompoundTerm):
            if symref(phi) == self.target:
                self.hits += 1
                return
            for k,t in enumerate(phi.subterms):
                t.accept(self)

class CollectVariables:
    """
        This Visitor collects all Variables in a given formula
    """

    def __init__(self, lang):
        self.L = lang
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
    def __init__(self, lang):
        self.L = lang
        self.quantified_vars = set()
        self._free_variables = set()

    @property
    def free_variables(self):
        for ref in self._free_variables:
            yield ref.term

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
