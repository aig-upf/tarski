# -*- coding: utf-8 -*-
"""
    Visitors implementing diverse aspects of FSTRIPS problems translation,
    analysis and compilation.
"""
from ..syntax.temporal import ltl
from ..syntax.formulas import CompoundFormula, Atom, QuantifiedFormula
from ..syntax.visitors import SymbolReference
from ..syntax.terms import CompoundTerm


class FluentHeuristic:
    action_effects = 1
    precondition = 2
    constraint = 3


class FluentSymbolCollector:
    """
        This visitor collects CompoundTerms which are candidates to become
        state variables.
    """

    def __init__(self, lang, fluents, statics, mode: FluentHeuristic):
        self.mode = mode
        self.lang = lang
        self.fluents = fluents
        self.statics = statics
        self.under_next = False
        self.visited = set()

    def reset(self):
        self.visited = set()

    def _visit_action_effect_formula(self, phi):

        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            # print("Atom: {}".format(str(phi)))
            if not phi.predicate.builtin:
                self.fluents.add(SymbolReference(phi))
            else:
                for t in phi.subterms:
                    t.accept(self)
        elif isinstance(phi, CompoundTerm):
            # print("Compound Term: {}, {}, {}".format(str(phi), phi.symbol, phi.symbol.builtin))
            if not phi.symbol.builtin:
                self.fluents.add(SymbolReference(phi))
            else:
                for t in phi.subterms:
                    t.accept(self)

    def _visit_constraint_formula(self, phi):
        if isinstance(phi, ltl.TemporalCompoundFormula) and phi.connective == ltl.TemporalConnective.X:
            old_value = self.under_next
            self.under_next = True
            for f in phi.subformulas:
                f.accept(self)
            self.under_next = old_value
        elif isinstance(phi, CompoundFormula):
            old_visited = self.visited.copy()
            for f in phi.subformulas:
                f.accept(self)
            delta = self.visited - old_visited
            # print('Fluents: {}'.format([str(x) for x in self.fluents]))
            # print('Delta: {}'.format([str(x) for x in delta]))
            if any(f in self.fluents for f in delta):
                # print("Fluency propagates")
                for f in delta:
                    self.fluents.add(f)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            if not phi.predicate.builtin:
                self.visited.add(SymbolReference(phi))
            if self.under_next:
                if not phi.predicate.builtin:
                    self.fluents.add(SymbolReference(phi))
            else:
                self.statics.add(SymbolReference(phi))
            for t in phi.subterms:
                t.accept(self)

        elif isinstance(phi, CompoundTerm):
            if not phi.symbol.builtin:
                self.visited.add(SymbolReference(phi))
            if self.under_next:
                if not phi.symbol.builtin:
                    self.fluents.add(SymbolReference(phi))
            else:
                self.statics.add(SymbolReference(phi))
            for t in phi.subterms:
                t.accept(self)

    def _visit_precondition_formula(self, phi):
        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            self.statics.add(SymbolReference(phi))
        elif isinstance(phi, CompoundTerm):
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
        if self.mode == FluentHeuristic.action_effects:
            self._visit_action_effect_formula(phi)
        elif self.mode == FluentHeuristic.constraint:
            self._visit_constraint_formula(phi)
        else:
            assert self.mode == FluentHeuristic.precondition
            self._visit_precondition_formula(phi)
