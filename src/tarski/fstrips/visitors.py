# -*- coding: utf-8 -*-

"""
    Visitors implementing diverse aspects of FSTRIPS problems translation,
    analysis and compilation.
"""
from tarski.syntax.temporal import ltl
from tarski.syntax.formulas import *

class SymbolReference(object):

    def __init__(self, component):
        self.expr = component

    def __hash__(self):
        # MRJ: Note that here we want to have a *guaranteed* hash collision
        # for terms and atoms with the same symbol
        try :
            return hash(self.expr.symbol.symbol)
        except AttributeError:
            return hash(self.expr.predicate.symbol)

    def __eq__(self, other):
        i_am_atom = isinstance(self.expr,Atom)
        other_is_atom = isinstance(other.expr,Atom)
        if i_am_atom and other_is_atom:
            return self.expr == other.expr
        if not i_am_atom and not other_is_atom:
            return self.expr.emvr(other.expr)
        return False

    __cmp__ = __eq__

    def __str__(self):
        return str(self.expr)

class FluentSymbolCollector(object):
    """
        This visitor collects CompoundTerms which are candidates to become
        state variables.
    """

    def __init__(self, L, fluents, statics):
        self.lang = L
        self.fluents = fluents
        self.statics = statics
        self.under_next = False
        self.visited = set()

    def reset(self):
        self.visited = set()

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
            for t in phi.subterms:
                t.accept(self)
        elif isinstance(phi,self.lang.CompoundTerm):
            if not phi.symbol.builtin:
                self.visited.add(SymbolReference(phi))
            if self.under_next:
                if not phi.symbol.builtin :
                    self.fluents.add(SymbolReference(phi))
            for t in phi.subterms :
                t.accept(self)

    def post_process(self):
        """
            Sorts fluent and static sets, so that the only
            static expressions are those which haven't found
            under the scope of a X operator at least once.
        """
        self.statics = self.statics - self.fluents
