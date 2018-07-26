# -*- coding: utf-8 -*-
"""
    Creates a TaskIndex for a  planning task as given by Tarski's AST.
"""
from .. import util
from ..fstrips import AddEffect, DelEffect, FunctionalEffect, LogicalEffect
from .visitors import FluentSymbolCollector, FluentHeuristic


class TaskIndex:
    def __init__(self, domain_name, instance_name):
        self.domain_name = domain_name
        self.instance_name = instance_name
        self.all_symbols = util.UninitializedAttribute('all_symbols')
        self.static_symbols = util.UninitializedAttribute('static_symbols')
        self.fluent_symbols = util.UninitializedAttribute('fluent_symbols')
        self.initial_fluent_atoms = util.UninitializedAttribute('initial_fluent_atoms')
        self.initial_static_data = util.UninitializedAttribute('initial_static_data')
        self.state_variables = util.UninitializedAttribute('state_variables')

    def _check_static_not_fluents(self):
        """
            Sorts fluent and static sets, so that the only
            static expressions are those which haven't been flagged
            as fluent by at least one of our heuristics.
        """
        # print('Fluents (before filtering): {}'.format(','.join([str(var) for var in self.fluent_symbols])))
        # print('Statics (before filtering): {}'.format(','.join([str(var) for var in self.static_symbols])))
        self.static_symbols = {x for x in self.static_symbols if x not in self.fluent_symbols}
        assert all([x not in self.static_symbols for x in self.fluent_symbols])
        # print('Fluents (after filtering): {}'.format(','.join([str(var) for var in self.fluent_symbols])))
        # print('Statics (after filtering): {}'.format(','.join([str(var) for var in self.static_symbols])))

    def process_symbols(self, problem):

        self.fluent_symbols = set()
        self.static_symbols = set()

        prec_visitor = FluentSymbolCollector(problem.language, self.fluent_symbols, self.static_symbols,
                                             FluentHeuristic.precondition)
        eff_visitor = FluentSymbolCollector(problem.language, self.fluent_symbols, self.static_symbols,
                                            FluentHeuristic.action_effects)
        constraint_visitor = FluentSymbolCollector(problem.language, self.fluent_symbols, self.static_symbols,
                                                   FluentHeuristic.constraint)

        o_f = len(self.fluent_symbols)
        o_s = len(self.static_symbols)
        while True:
            for _, act in problem.actions.items():
                act.precondition.accept(prec_visitor)
                for eff in act.effects:
                    if isinstance(eff, AddEffect):
                        eff.atom.accept(eff_visitor)
                    elif isinstance(eff, DelEffect):
                        eff.atom.accept(eff_visitor)
                    elif isinstance(eff, FunctionalEffect):
                        eff.lhs.accept(eff_visitor)
                    elif isinstance(eff, LogicalEffect):
                        eff.formula.accept(eff_visitor)
                    else:
                        raise RuntimeError("Effect type '{}' cannot be analysed".format(type(eff)))

            for const in problem.constraints:
                constraint_visitor.reset()
                const.accept(constraint_visitor)
            # print('Fluents: {}'.format(','.join([str(x) for x in self.fluent_symbols])))
            # print('Statics: {}'.format(','.join([str(x) for x in self.static_symbols])))
            self._check_static_not_fluents()
            if len(self.fluent_symbols) == o_f and \
                    len(self.static_symbols) == o_s:
                break
            o_f = len(self.fluent_symbols)
            o_s = len(self.static_symbols)

        self.all_symbols = self.fluent_symbols | self.static_symbols

    def is_fluent(self, symbol):
        return symbol in self.fluent_symbols

    def process_initial_state(self, init):
        raise NotImplementedError()
