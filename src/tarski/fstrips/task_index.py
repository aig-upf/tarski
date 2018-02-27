# -*- coding: utf-8 -*-

"""
    Creates a TaskIndex for a  planning task as given by Tarski's AST.
"""
from collections import OrderedDict
import itertools

from . import util
from .state_variables import create_all_possible_state_variables, create_all_possible_state_variables_from_groundings



from .visitors import FluentSymbolCollector

class TaskIndex(object):
    def __init__(self, domain_name, instance_name):
        self.domain_name = domain_name
        self.instance_name = instance_name

        # self.types = util.UninitializedAttribute('types')
        # self.type_map = util.UninitializedAttribute('type_map')
        # self.supertypes = util.UninitializedAttribute('supertypes')
        # self.objects = util.UninitializedAttribute('objects')
        # self.object_types = util.UninitializedAttribute('object_types')
        # self.symbols = util.UninitializedAttribute('symbols')
        # self.symbol_types = util.UninitializedAttribute('symbol_types')
        # self.action_cost_symbols = util.UninitializedAttribute('action_cost_symbols')
        # self.symbol_index = util.UninitializedAttribute('symbol_index')
        self.all_symbols = util.UninitializedAttribute('all_symbols')
        self.static_symbols = util.UninitializedAttribute('static_symbols')
        self.fluent_symbols = util.UninitializedAttribute('fluent_symbols')
        # self.initial_fluent_atoms = util.UninitializedAttribute('initial_fluent_atoms')
        # self.initial_static_data = util.UninitializedAttribute('initial_static_data')
        # self.state_variables = util.UninitializedAttribute('state_variables')
        # self.goal = util.UninitializedAttribute('goal')
        # self.state_constraints = util.UninitializedAttribute('state_constraints')
        # self.action_schemas = util.UninitializedAttribute('action_schemas')
        # self.event_schemas = util.UninitializedAttribute('event_schemas')
        # self.process_schemas = util.UninitializedAttribute('process_schemas')
        # self.constraint_schemas = util.UninitializedAttribute('constraint_schemas')
        # self.metric = util.UninitializedAttribute('metric')
        # self.groundings = None

#    def process_types(self, types, type_map, supertypes):
        # Each typename points to its (unique) 1-based index (index 0 is reserved for bools)
#        self.types = {t: i for i, t in enumerate(types, 1)}
#        self.type_map = type_map
#        self.supertypes = supertypes

#    def process_objects(self, objects):
        # Each object name points to it unique 0-based index / ID
#        self.objects, self.object_types = self._index_objects(objects)

    def process_symbols(self, P):

        self.fluent_symbols = set()
        self.static_symbols = set()

        visitor = FluentSymbolCollector(P.language,self.fluent_symbols,self.static_symbols)

        for _, act in P.actions.items() :
            for eff in act.effects :
                eff.accept(visitor)

        for const in P.constraints :
            const.accept(visitor)

        visitor.post_process()
        self.all_symbols = self.fluent_symbols | self.static_symbols
        #
        # self.symbols, self.symbol_types, self.action_cost_symbols = self._index_symbols(predicates, functions)
        # self.symbol_index = {name: i for i, name in enumerate(self.symbols.keys())}
        #
        # self.all_symbols = list(self.symbol_types.keys())
        #
        # if no_static_symbols :
        #     self.fluent_symbols = self.all_symbols
        #     self.static_symbols = set("=") # only equality
        #     return
        #
        # # All symbols appearing on some action, process or event effect are fluent
        # self.fluent_symbols = set(pddl_helper.get_effect_symbol(eff) for action in actions for eff in action.effects)
        # self.fluent_symbols |= set(pddl_helper.get_effect_symbol(eff) for proc in processes for eff in proc.effects)
        # self.fluent_symbols |= set(pddl_helper.get_effect_symbol(eff) for evt in events for eff in evt.effects)
        #
        # # MRJ: very unsatisfying fix
        # for sym in self.all_symbols:
        #     if util.is_external(sym):  # symbol is procedurally defined
        #         self.fluent_symbols.add(sym)
        #
        # # The rest are static, including, by definition, the equality predicate
        # self.static_symbols = set(s for s in self.all_symbols if s not in self.fluent_symbols) | set("=")


    def is_fluent(self, symbol):
        return symbol_name in self.fluent_symbols

    # @staticmethod
    # def _index_objects(objects):
    #     o_types = {}
    #     idx = IndexDictionary()
    #     idx.add(util.bool_string(False))  # 0
    #     idx.add(util.bool_string(True))  # 1
    #     # idx.add('undefined')  # Do we need an undefined object?
    #     for o in objects:
    #         idx.add(o.name)
    #         o_types[o.name] = o.type
    #     return idx, o_types

    @staticmethod
    def _index_symbols(predicates, functions):
        """
         This method takes care of analyzing any given task to determine which of the task symbols
         are fluent and which static.
        """
        symbols, symbol_types, action_cost_symbols = OrderedDict(), {}, set()

        for s in predicates:
            argtypes = [t.type for t in s.arguments]
            symbols[s.name] = fs.Predicate(s.name, argtypes)
            symbol_types[s.name] = 'bool'

        for s in functions:
            if s.name == 'total-cost':  # Ignore action costs
                action_cost_symbols.add(s.name)
            else:
                argtypes = [t.type for t in s.arguments]
                symbols[s.name] = fs.Function(s.name, argtypes, s.type)
                symbol_types[s.name] = s.type

        return symbols, symbol_types, action_cost_symbols

    def process_initial_state(self, fd_initial_state):
        fd_initial_atoms = self._extract_initial_atom_names_and_arguments(fd_initial_state)

        # Distinguish fluent from static atoms, since we'll treat them differently
        fd_initial_fluent_atoms = [elem for elem in fd_initial_atoms if self.is_fluent(elem[0])]
        fd_initial_static_atoms = [elem for elem in fd_initial_atoms if not self.is_fluent(elem[0])]

        self.initial_fluent_atoms = _process_fluent_atoms(fd_initial_fluent_atoms)
        self.initial_static_data = self._process_static_atoms(fd_initial_static_atoms)

    def _process_static_atoms(self, fd_initial_static_atoms):
        initial_static_data = {}
        for name, args, value in fd_initial_static_atoms:
            # In case the extension for this particular symbol has not yet been initialized
            if name not in initial_static_data:
                initial_static_data[name] = static.instantiate_extension(self.symbols[name])
            initial_static_data[name].add(args, value)

        return initial_static_data

    def _extract_initial_atom_names_and_arguments(self, fd_initial_state):
        names = []
        for atom in fd_initial_state:
            if isinstance(atom, pddl.Assign):
                name = atom.fluent.symbol
                if _check_symbol_in_initial_state(name, self.symbols):
                    args = tuple(int(a) if python.utils.is_int(a) else a for a in atom.fluent.args)
                    value = self.parse_value(atom.expression)
                    names.append((name, args, value))

            elif isinstance(atom, pddl.Atom):
                if atom.negated:
                    raise RuntimeError("No negations allowed in the initialization of atoms")

                name = atom.predicate
                if _check_symbol_in_initial_state(name, self.symbols):
                    names.append((name, atom.args, None))

            else:
                raise RuntimeError("Unrecognized type of atom '{}'".format(atom))

        return names

    def process_state_variables(self):

        self.state_variables =create_all_possible_state_variables(self.fluent_symbols)

    # def process_actions(self, actions):
    #     self.action_schemas = [FSActionSchema(self, action, "control") for action in actions]
    #
    # def process_processes(self, processes):
    #     self.process_schemas = [FSActionSchema(self, proc, "natural") for proc in processes]
    #
    # def process_events(self, events):
    #     self.event_schemas = [FSActionSchema(self, evt, "exogenous") for evt in events]
    #
    # def process_metric(self, metric):
    #     if metric is None:
    #         self.metric = FSMetric(self, None, None)
    #         return
    #     self.metric = FSMetric(self, metric.optimization, metric.expr)
    #
    #
    # def process_goal(self, goal):
    #     self.goal = FSFormula(self, goal)
