# -*- coding: utf-8 -*-
from tarski.syntax.temporal import ltl
from tarski.syntax.formulas import *

class CollectVariables(object):
    """
        This Visitor collects all Variables in a given formula
    """

    def __init__(self, L):
        self.L = L
        self.variables = set()

    def visit(self, phi):

        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas: f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            for k,t in enumerate(phi.subterms):
                if isinstance(t, self.L.Variable):
                    self.variables.add(t)
                else :
                    t.accept(self)
        elif isinstance(phi, self.L.CompoundTerm):
            for k,t in enumerate(phi.subterms):
                if isinstance(t, self.L.Variable):
                    self.variables.add(t)
                else :
                    t.accept(self)
