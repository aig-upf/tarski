# -*- coding: utf-8 -*-

"""
    Visitors implementing diverse aspects of FSTRIPS problems translation,
    analysis and compilation.
"""
from tarski.syntax.temporal import ltl
from tarski.syntax.formulas import *
from tarski.syntax.sorts import inclusion_closure

def emvr(self, other):
    """
        Checks if two terms or atoms are equivalent modulo variable renaming
    """

    # @TODO: the variable renaming should be maintained across the
    # whole sub-expression
    if self.head.symbol != other.head.symbol: return False

    for lhs, rhs in zip(self.subterms,other.subterms):
        if isinstance(lhs,self.language.Variable) and\
            isinstance(rhs,self.language.Variable):
            if lhs.sort.name != rhs.sort.name :
                if not rhs.sort in inclusion_closure(lhs.sort):
                    return False
        elif isinstance(lhs,self.language.Constant) and\
            isinstance(rhs,self.language.Constant):
            if lhs.symbol != rhs.symbol: return False
        elif isinstance(lhs,self.language.CompoundTerm) and\
            isinstance(rhs,self.language.CompoundTerm):
            if not emvr(SymbolReference(lhs),SymbolReference(rhs)): return False
        else:
            return False
    return True

class SymbolReference(object):

    def __init__(self, component):
        self.expr = component
        try:
            self.head = self.expr.predicate
            self.is_atom = True
        except AttributeError:
            self.head = self.expr
            self.is_atom = False
    @property
    def language(self):
        return self.head.language

    @property
    def subterms(self):
        return self.expr.subterms

    def __hash__(self):
        return hash(self.head.symbol)

    def __eq__(self, other):
        if self.is_atom and other.is_atom:
            return emvr(self, other)
        if not self.is_atom and not other.is_atom:
            return emvr(self, other)
        return False

    __cmp__ = __eq__

    def __str__(self):
        return str(self.expr)

class FluentHeuristic(object):
    action_effects = 1
    precondition = 2
    constraint = 3

class FluentSymbolCollector(object):
    """
        This visitor collects CompoundTerms which are candidates to become
        state variables.
    """

    def __init__(self, L, fluents, statics, mode : FluentHeuristic ):
        self.mode = mode
        self.lang = L
        self.fluents = fluents
        self.statics = statics
        self.under_next = False
        self.visited = set()

    def reset(self):
        self.visited = set()

    def _visit_action_effect_formula(self, phi):

        if isinstance(phi, ltl.TemporalCompoundFormula)\
            and phi.connective == ltl.TemporalConnective.X:
            old_value = self.under_next
            self.under_next = True
            for f in phi.subformulas: f.accept(self)
            self.under_next = old_value
        elif isinstance(phi, CompoundFormula):
            for f in phi.subformulas : f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            if self.under_next:
                if not phi.predicate.builtin:
                    self.fluents.add(SymbolReference(phi))
                else:
                    for t in phi.subterms:
                        t.accept(self)
            else :
                if not phi.predicate.builtin:
                    self.statics.add(SymbolReference(phi))
        elif isinstance(phi,self.lang.CompoundTerm):
            if self.under_next:
                if not phi.symbol.builtin :
                    self.fluents.add(SymbolReference(phi))
                else :
                    for t in phi.subterms :
                        t.accept(self)
            else :
                self.statics.add(SymbolReference(phi))

    def _visit_constraint_formula(self, phi):
        if isinstance(phi, ltl.TemporalCompoundFormula)\
            and phi.connective == ltl.TemporalConnective.X:
            old_value = self.under_next
            self.under_next = True
            for f in phi.subformulas: f.accept(self)
            self.under_next = old_value
        elif isinstance(phi, CompoundFormula):
            old_visited = self.visited.copy()
            for f in phi.subformulas : f.accept(self)
            delta = self.visited - old_visited
            if any( f in self.fluents for f in delta) :
                for f in delta : self.fluents.add(f)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            if not phi.predicate.builtin:
                self.visited.add(SymbolReference(phi))
            if self.under_next:
                if not phi.predicate.builtin:
                    self.fluents.add(SymbolReference(phi))
            else :
                self.statics.add(SymbolReference(phi))
            for t in phi.subterms:
                t.accept(self)

        elif isinstance(phi,self.lang.CompoundTerm):
            if not phi.symbol.builtin:
                self.visited.add(SymbolReference(phi))
            if self.under_next:
                if not phi.symbol.builtin :
                    self.fluents.add(SymbolReference(phi))
            else :
                self.statics.add(SymbolReference(phi))
            for t in phi.subterms:
                t.accept(self)

    def _visit_precondition_formula(self,phi):
        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas : f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            self.statics.add(SymbolReference(phi))
        elif isinstance(phi,self.lang.CompoundTerm):
            self.statics.add(SymbolReference(phi))

    def visit(self, phi):
        """
            Visitor method to sort atoms and terms into the
            "fluent" and "static" categories. Note that a given
            symbol can be in both sets, this means that it gets
            "votes" as static and fluent... the post_process() method
            is meant to settle the issue (and potentially allow for
            more ellaborate/clever heuristics).

            NB: at the moment we're trawling all (possibly lifted)
            sub-expressions, this is intentional.
        """
        if self.mode == FluentHeuristic.action_effects :
            self._visit_action_effect_formula(phi)
        elif self.mode == FluentHeuristic.constraint :
            self._visit_constraint_formula(phi)
        else :
            assert self.mode == FluentHeuristic.precondition
            self._visit_precondition_formula(phi)
