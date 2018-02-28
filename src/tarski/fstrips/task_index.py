# -*- coding: utf-8 -*-

"""
    Creates a TaskIndex for a  planning task as given by Tarski's AST.
"""
from collections import OrderedDict
import itertools

from tarski import util
from .visitors import FluentSymbolCollector

class TaskIndex(object):
    def __init__(self, domain_name, instance_name):
        self.domain_name = domain_name
        self.instance_name = instance_name
        self.all_symbols = util.UninitializedAttribute('all_symbols')
        self.static_symbols = util.UninitializedAttribute('static_symbols')
        self.fluent_symbols = util.UninitializedAttribute('fluent_symbols')
        self.initial_fluent_atoms = util.UninitializedAttribute('initial_fluent_atoms')
        self.initial_static_data = util.UninitializedAttribute('initial_static_data')
        self.state_variables = util.UninitializedAttribute('state_variables')

    def process_symbols(self, P):

        self.fluent_symbols = set()
        self.static_symbols = set()

        visitor = FluentSymbolCollector(P.language,self.fluent_symbols,self.static_symbols)

        oF = len(self.fluent_symbols)
        oS = len(self.static_symbols)
        while True :
            for _, act in P.actions.items() :
                for eff in act.effects :
                    visitor.reset()
                    eff.accept(visitor)
            for const in P.constraints :
                visitor.reset()
                const.accept(visitor)

            visitor.post_process()
            if len(self.fluent_symbols) == oF and\
                 len(self.static_symbols) == oS:
                 break
            oF = len(self.fluent_symbols)
            oS = len(self.static_symbols)

        self.all_symbols = self.fluent_symbols | self.static_symbols


    def is_fluent(self, symbol):
        return symbol_name in self.fluent_symbols

    def process_initial_state(self, I):
        raise NotImplementedError()

    def process_state_variables(self):
        raise NotImplementedError()
