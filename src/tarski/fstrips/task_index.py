# -*- coding: utf-8 -*-
"""
    Creates a TaskIndex for a  planning task as given by Tarski's AST.
"""
from .visitors import FluentSymbolCollector, FluentHeuristic


class TaskIndex:
    def __init__(self, domain_name, instance_name):
        self.domain_name = domain_name
        self.instance_name = instance_name
        self.all_symbols = None
        self.static_terms = None
        self.fluent_terms = None
        self.initial_fluent_atoms = None
        self.initial_static_data = None
        self.state_variables = None

    def _check_static_not_fluents(self):
        """
            Sorts fluent and static sets, so that the only
            static expressions are those which haven't been flagged
            as fluent by at least one of our heuristics.
        """
        # print('Fluents (before filtering): {}'.format(','.join([str(var) for var in self.fluent_terms])))
        # print('Statics (before filtering): {}'.format(','.join([str(var) for var in self.static_terms])))
        self.static_terms = {x for x in self.static_terms if x not in self.fluent_terms}
        assert all([x not in self.static_terms for x in self.fluent_terms])
        # print('Fluents (after filtering): {}'.format(','.join([str(var) for var in self.fluent_terms])))
        # print('Statics (after filtering): {}'.format(','.join([str(var) for var in self.static_terms])))

    def process_symbols(self, problem):
        lang = problem.language
        self.fluent_terms = set()
        self.static_terms = set()

        prec_visitor = FluentSymbolCollector(lang, self.fluent_terms, self.static_terms, FluentHeuristic.precondition)
        eff_visitor = FluentSymbolCollector(lang, self.fluent_terms, self.static_terms, FluentHeuristic.action_effects)
        constr_visitor = FluentSymbolCollector(lang, self.fluent_terms, self.static_terms, FluentHeuristic.constraint)

        o_f = len(self.fluent_terms)
        o_s = len(self.static_terms)
        while True:
            problem.get_symbols(prec_visitor, eff_visitor, constr_visitor)

            # print('Fluents: {}'.format(','.join([str(x) for x in self.fluent_terms])))
            # print('Statics: {}'.format(','.join([str(x) for x in self.static_terms])))
            self._check_static_not_fluents()
            if len(self.fluent_terms) == o_f and len(self.static_terms) == o_s:
                break
            o_f = len(self.fluent_terms)
            o_s = len(self.static_terms)

        self.all_symbols = self.fluent_terms | self.static_terms

    def compute_fluent_and_statics(self):
        """ Return sets with fluent and static predicate / function symbols """
        fluents = set(ref.expr.predicate for ref in self.fluent_terms)
        statics = set(ref.expr.predicate for ref in self.static_terms)
        statics = set(x for x in statics if x not in fluents and not x.builtin)
        return fluents, statics

    def is_fluent(self, symbol):
        return symbol in self.fluent_terms

    def process_initial_state(self, init):
        raise NotImplementedError()
