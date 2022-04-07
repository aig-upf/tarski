# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez (miquel.ramirez@pm.me)
# ----------------------------------------------------------------------------------------------------------------------
# io/pddl/instance.py
#
# PDDL parser
# ----------------------------------------------------------------------------------------------------------------------

from collections import namedtuple, OrderedDict
from typing import Tuple
from enum import Enum

import tarski as tsk
from tarski.io.pddl.errors import UnsupportedFeature
from tarski.theories import Theory
from tarski.syntax import Variable, Sort
from tarski.syntax.sorts import Interval, int_encode_fn
from tarski.syntax import symref


AssignmentEffectData = namedtuple('AssignmentEffectData', ['lhs', 'rhs'])
EventData = namedtuple('EventData', ['pre', 'post'])
ActionData = namedtuple('ActionData', ['name', 'parameters', 'pre', 'post'])
DurativeActionData = namedtuple('DurativeActionData', ['name', 'parameters', 'at_start', 'at_end', 'overall', 'duration'])
DerivedPredicateData = namedtuple('DerivedPredicateData', ['head', 'parameters', 'body'])
ObjectiveData = namedtuple('ObjectiveData', ['mode', 'type', 'expr'])


class ObjectiveMode(Enum):
    """
    Enumeration with mode of optimization
    """
    MINIMIZE = 0
    MAXIMIZE = 1


class ObjectiveType(Enum):
    """
    Enumeration of all possible types of objectives
    """
    UNSPECIFIED = 0
    TOTAL_COST = 1
    TOTAL_TIME = 2
    FLUENT_EXPR = 3
    VIOLATED_PREFS = 4


class InstanceModel:
    """
    Instance objects represent the structural components of a planning problem instance as defined in a PDDL program.
    The instance class is meant to be generic by not committing to specific further post-processing (such as
    grounding).
    """
    def __init__(self, **kwargs):
        self.debug = kwargs.get('debug', False)
        self.L = None
        self.bool_t = None
        self.int_t = None
        self.real_t = None
        self.default_numeric_type = None

        self._types = OrderedDict()
        self._constants = OrderedDict()
        self._predicates = OrderedDict()
        self._functions = OrderedDict()

        self._actions = []
        self._durative = []
        self._derived = []

        self.init = None
        self.goal = None
        self._objective = ObjectiveData(mode=ObjectiveMode.MINIMIZE, type=ObjectiveType.UNSPECIFIED, expr=None)

        self.L = tsk.language('pddl-theory', theories=[Theory.EQUALITY, Theory.ARITHMETIC])

        self.bool_t = Interval('Bool', self.L, int_encode_fn, 0, 1, builtin=True)
        self.int_t = self.L.Integer
        self.real_t = self.L.Real
        self.L.attach_sort(self.bool_t, self.int_t)
        # MRJ: this is prone to change
        self.default_numeric_type = self.int_t

        self._types['object'] = self.L.Object


    @property
    def lang(self):
        """
        The `tarski.FirstOrderLanguage` object representing the domain theory given for the instance
        :return:
        """
        return self.L

    @property
    def types(self):
        """
        Dictionary of types defined in the PDDL program
        :return:
        """
        return self._types

    @property
    def domains(self):
        """
        Dictionary of constants defined in the PDDL program
        :return:
        """
        return self._constants

    @property
    def predicates(self):
        """
        Dictionary of predicates defined in the PDDL program
        :return:
        """
        return self._predicates

    @property
    def functions(self):
        """
        Dictionary of functions defined in the PDDL program
        :return:
        """
        return self._functions

    @property
    def actions(self):
        """
        List object with `ActionData` instances describing the elements in the definition of (instantaneous) actions
        :return:
        """
        return self._actions

    @property
    def durative(self):
        """
        List of objects with `DurativeActionData` instances describing durative actions
        :return:
        """
        return self._durative

    @property
    def derived(self):
        """
        List of objects with `DerivedPredicateData` instances describing derived predicates (PDDL axioms)
        :return:
        """
        return self._derived

    @property
    def objective(self):
        """
        Objective function
        :return:
        """
        return self._objective

    def process_supertype_definition(self, supertype, subtypes, lineno):
        """
        Processes a super type definition (e.g. a PDDL type with subtypes)
        :param supertype:
        :param subtypes:
        :param lineno: line number, used to generate errors
        :return:
        """
        added_supertype = False
        if supertype not in self.types:
            self.types[supertype] = self.L.sort(supertype, self.L.Object)
            added_supertype = True

        for subtypename in subtypes:
            if subtypename in self.types:
                if added_supertype:
                    self.L.set_parent(self.types[subtypename], self.types[supertype], overwrite=True)
                else:
                    msg = "Error processing types definition in domain: type '{}' defined via multiple inheritance, which is not supported".format(
                        subtypename)
                    raise UnsupportedFeature(lineno(), msg)
            else:
                self.types[subtypename] = self.L.sort(subtypename, self.types[supertype])

    def process_type_definition(self, type_data):
        """
        Processes a type definition
        :param type_data:
        :return:
        """
        self.types[type_data] = self.L.sort(type_data, self.L.Object)

    def process_constant_definition(self, constant_data):
        """
        Processes the definition of a constant
        :param constant_data:
        :return:
        """
        typename, constant_list = constant_data
        if typename in self.domains:
            self.domains[typename] += [self.L.constant(c, self.types[typename]) for c in constant_list]
            return

        self.domains[typename] = [self.L.constant(c, self.types[typename]) for c in constant_list]

    def process_predicate_definition(self, predicate_data):
        """
        Processes a predicate definition
        :param predicate_data:
        :return:
        """
        name, args = predicate_data
        signature = tuple([a['type'] for a in args] + [self.bool_t])
        self.predicates[name] = self.L.function(name, *signature)

    def get_variable(self, name: str, typename: str) -> Tuple[Variable, Sort]:
        """
        Returns a term (variable) and its sort for a given variable name and sort
        :param name:
        :return:
        """
        return self.L.variable(name, typename), self.L.get(typename)

    def get(self, stuff: str):
        """
        Checks if stuff is defined in the domain theory of the instance
        :param stuff:
        :return:
        """
        return self.L.get(stuff)

    def int_const(self, v: str):
        """
        Returns an Integer constant
        :param v:
        :return:
        """
        return self.L.constant(v, self.int_t)

    def real_const(self, v: str):
        """
        Returns an Integer constant
        :param v:
        :return:
        """
        return self.L.constant(v, self.real_t)

    def process_function_skeleton(self, func_data):
        """
        Processes function definition
        :param func_data:
        :return:
        """
        name = func_data['name']
        domain = [a['type'] for a in func_data['domain']]
        try:
            codomain = func_data['codomain']
        except KeyError:
            codomain = self.default_numeric_type
        signature = domain + [codomain]
        self.functions[name] = self.L.function(name, *signature)

    def process_durative_action_skeleton(self, name, parameters, body):
        """
        Processes durative action skeleton
        :param name:
        :param parameters:
        :param body:
        :return:
        """

        at_start_formulas = []
        at_end_formulas = []
        over_all_formulas = []
        for entry in body['precondition']:
            if entry['type'] == 'instant':
                if entry['offset'] == 'start':
                    phi = entry['formula']
                    phi_ref = symref(phi)
                    if phi_ref not in at_start_formulas:
                        at_start_formulas += [phi_ref]
                elif entry['offset'] == 'end':
                    phi_ref = symref(entry['formula'])
                    if phi_ref not in at_end_formulas:
                        at_end_formulas += [phi_ref]
            elif entry['type'] == 'interval':
                phi_ref = symref(entry['formula'])
                if phi_ref not in over_all_formulas:
                    over_all_formulas += [phi_ref]

        if self.debug:
            print("At start preconditions:", len(at_start_formulas))
            print("At end preconditions:", len(at_end_formulas))
            print("Over all conditions:", len(over_all_formulas))

        duration = body['duration']

        at_start_eff = []
        at_end_eff = []

        for eff_entry in body['effect']:
            if eff_entry['instant'] == 'end':
                at_end_eff += [eff_entry['effect'][0]]
                continue
            at_start_eff += [eff_entry['effect'][0]]

        self._durative += [DurativeActionData(name=name,
                                              parameters=[e['term'] for e in parameters],
                                              duration=duration,
                                              at_start=EventData(pre=at_start_formulas, post=at_start_eff),
                                              at_end=EventData(pre=at_end_formulas, post=at_end_eff),
                                              overall=over_all_formulas)]

    def process_instantaneous_action_skeleton(self, name, parameters, body):
        """
        Processes instantaneous action skeleton
        :param name:
        :param parameters:
        :param body:
        :return:
        """

        self._actions += [ActionData(name=name,
                                     parameters=[e['term'] for e in parameters],
                                     pre=body['precondition'],
                                     post=body['effect'])]

    def process_action_skeleton(self, name, parameters, body):
        """
        Processes parsed action skeleton
        :param name:
        :param parameters:
        :param body:
        :return:
        """
        if self.debug:
            print("Action:", name)
            print("parameters:", parameters)
            print("data:", body)
            print("precondition:", body['precondition'])
            print("effect:", body['effect'])

        if 'duration' in body:
            self.process_durative_action_skeleton(name, parameters, body)
            return

        self.process_instantaneous_action_skeleton(name, parameters, body)

    def process_derived_predicate_skeleton(self, head, parameters, body):
        """
        Processes skeleton of derived predicate
        """
        if self.debug:
            print("Derived predicate: head:", head)
            print("Parameters:", parameters)
            print("body:", body)

        self._derived += [DerivedPredicateData(head=head,
                                               parameters=[e['term'] for e in parameters],
                                               body=body)]

    def process_objective_definition(self, objective_data):
        """
        Processes the objective definition
        :param objective_data:
        :return:
        """
        self._objective = ObjectiveData(mode=objective_data['mode'],
                                        type=objective_data['definition']['type'],
                                        expr=objective_data['definition']['expr'])
        if self.debug:
            print("Objective: mode: {} type: {} expr: {}".format(self.objective.mode, self.objective.type, self.objective.expr))
