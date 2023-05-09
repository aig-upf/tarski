# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez (miquel.ramirez@pm.me)
# ----------------------------------------------------------------------------------------------------------------------
# io/pddl/instance.py
#
# PDDL parser
# ----------------------------------------------------------------------------------------------------------------------

from collections import namedtuple, OrderedDict
from typing import Tuple, List
from enum import Enum

import tarski as tsk
import tarski.model as model
import tarski.syntax
from tarski.io.pddl.errors import UnsupportedFeature
from tarski.theories import Theory
from tarski.syntax import Variable, Sort, CompoundTerm, CompoundFormula, Connective, \
    QuantifiedFormula, Quantifier, Tautology, Atom, Constant, is_and
from tarski.syntax.formulas import is_eq_atom
from tarski.syntax.sorts import Interval, int_encode_fn
from tarski.syntax import symref
from tarski.evaluators.simple import evaluate as default_evaluator
from tarski import fstrips as fs
from tarski.syntax import land, lor

AssignmentEffectData = namedtuple('AssignmentEffectData', ['lhs', 'rhs'])
EventData = namedtuple('EventData', ['pre', 'post'])
ActionData = namedtuple('ActionData', ['name', 'parameters', 'pre', 'post'])
DurativeActionData = namedtuple('DurativeActionData', ['name', 'parameters', 'at_start', 'at_end', 'overall', 'duration'])
DerivedPredicateData = namedtuple('DerivedPredicateData', ['head', 'parameters', 'body'])
ObjectiveData = namedtuple('ObjectiveData', ['mode', 'type', 'expr'])
ConflictConstraint = namedtuple('Conflict', ['scope', 'condition', 'disjunction'])


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
        self.compile_away_disjunctive_preconditions = kwargs.get('compile_away_disjunctive_preconditions', True)

        self.L = None
        self.bool_t = None
        self.int_t = None
        self.real_t = None
        self.default_numeric_type = None
        self.domain_name = None
        self.instance_name = None

        self._types = OrderedDict()
        self._constants = OrderedDict()
        self._predicates = OrderedDict()
        self._functions = OrderedDict()

        self._actions = []
        self._durative = []
        self._derived = []
        self._constraints = []

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
        List of objects with `DerivedPredicateData` instances describing derived predicates
        :return:
        """
        return self._derived

    @property
    def conflicts(self):
        """
        List of `ConflictConstraint` describing axioms that capture conflicts between fluents
        :return:
        """
        return self._constraints

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
                    raise UnsupportedFeature(lineno, msg)
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

    def extract_conflicting_atoms(self, phi: CompoundFormula):
        """
        Extracts atoms from ~A v ~B
        :param phi:
        :return:
        """
        lhs = phi.subformulas[0]
        rhs = phi.subformulas[1]
        # MRJ: note that negative literals ~P(x) are converted to f_{P}(x) = 0
        # if not isinstance(lhs, CompoundFormula) or lhs.connective != Connective.Not:
        #     raise NotImplementedError("Warning: constraint {} is disjunctive formula which does "
        #                               "not match ~A v ~B".format(lhs))
        # if not isinstance(rhs, CompoundFormula) or rhs.connective != Connective.Not:
        #     raise NotImplementedError("Warning: constraint {} is disjunctive formula which does "
        #                               "not match ~A v ~B".format(rhs))
        if not isinstance(lhs, Atom) or lhs.subterms[1].symbol != 0:
            raise NotImplementedError("Warning: constraint {} is disjunctive formula which does "
                                      "not match A(x) = 0 v B(x) = 1".format(lhs))
        if not isinstance(rhs, Atom) or rhs.subterms[1].symbol != 0:
            raise NotImplementedError("Warning: constraint {} is disjunctive formula which does "
                                      "not match A(x) = 0 v B(x) = 1".format(rhs))
        return [Atom(lhs.predicate, [lhs.subterms[0], Constant(1, lhs.subterms[1].sort)]),
                Atom(rhs.predicate, [rhs.subterms[0], Constant(1, rhs.subterms[1].sort)])]

    def simplify(self, phi: CompoundFormula):
        """
        Applies some simplification rules
        :param phi:
        :return:
        """
        if phi.connective == Connective.Not:
            if is_eq_atom(phi.subformulas[0]):
                gamma = phi.subformulas[0]
                return gamma.subterms[0] != gamma.subterms[1]

        return phi

    def flatten_conjunction(self, phi: CompoundFormula):
        """
        Flattens compound formula extracting subformulas into a list
        :param phi:
        :return:
        """
        conjuncts = []
        if phi.connective != Connective.And:
            return [phi]
        subformulas = list(phi.subformulas)
        while len(subformulas) != 0:
            if is_and(subformulas[0]):
                subformulas = list(subformulas[0].subformulas)
            conjuncts += [subformulas[0]]
            subformulas.pop(0)

        return conjuncts

    def analyze_domain_constraint(self, phi: QuantifiedFormula):
        """
        Analyses domain constraint and generates domain constraint data structure
        :param phi:
        :return:
        """
        varphi = phi.formula
        if not isinstance(varphi, CompoundFormula) or varphi.connective != Connective.Or:
            raise NotImplementedError("Warning: constraint: {} is not a disjunctive formula, so "
                                      "it is being ignored!".format(phi.formula))
        if len(varphi.subformulas) != 2:
            raise NotImplementedError("Warning: constraint {} is a disjunctive formula with more "
                                      "than two disjuncts so for now it is being "
                                      "ignored".format(phi.formula))
        lhs = varphi.subformulas[0]
        rhs = varphi.subformulas[1]
        if isinstance(rhs, CompoundFormula) and rhs.connective == Connective.Or:
            if not isinstance(lhs, CompoundFormula) or lhs.connective != Connective.Not:
                raise NotImplementedError("Warning: constraint {} is a disjunctive formula where "
                                          "the rhs is a disjunctive formula, but does not match "
                                          "what one would expect from A->B \equiv ~A v B".format(varphi))
            # It is a complex constraint
            self._constraints += [ConflictConstraint(scope=phi.variables,
                                                     condition=[self.simplify(phi)
                                                                for phi in self.flatten_conjunction(lhs.subformulas[0])],
                                                     disjunction=self.extract_conflicting_atoms(rhs))]
        else:

            self._constraints += [ConflictConstraint(scope=phi.variables,
                                                     condition=Tautology(),
                                                     disjunction=self.extract_conflicting_atoms(varphi))]

    def process_domain_constraints(self, formula):
        """
        Processes given domain constraint formula
        :param formula:
        :return:
        """
        #print("Domain constraints:")
        #print(formula)
        if not isinstance(formula, CompoundFormula) or formula.connective != Connective.And:
            raise RuntimeError("InstanceModel: domain constraints are not a conjunctive formula")
        phi = list(formula.subformulas)
        while len(phi) != 0:
            if isinstance(phi[0], CompoundFormula) and phi[0].connective == Connective.And:
                phi = list(phi[0].subformulas)

            if not isinstance(phi[0], QuantifiedFormula) or phi[0].quantifier != Quantifier.Forall:
                raise RuntimeError("InstanceModel: each constraint must be given as a universally quantified"
                                   " formula, found:", phi)
            # classify formula and determine structure
            #print("Analysing:", phi[0])
            self.analyze_domain_constraint(phi[0])
            phi.pop(0)


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
        if self.compile_away_disjunctive_preconditions:
            if isinstance(body['precondition'], tarski.syntax.CompoundFormula)\
                    and body['precondition'].connective == tarski.syntax.Connective.Or:
                print("INFO: compiling away disjunctive precondition of action schema", name)
                print(body['precondition'])
                stack = []
                phi = body['precondition'].subformulas
                while phi is not None:
                    stack += [phi[0]]
                    if isinstance(phi[1], tarski.syntax.CompoundFormula)\
                             and phi[1].connective == tarski.syntax.Connective.Or:
                        phi = phi[1]
                    else:
                        stack += [phi[1]]
                        phi = None
                for index, sub in enumerate(stack):
                    self._actions += [ActionData(name='{}-{}'.format(name, index),
                                                 parameters=[e['term'] for e in parameters],
                                                 pre=sub,
                                                 post=body['effect'])]
                return

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
            print("Objective: mode: {} type: {} expr: {}".format(self.objective.mode,
                                                                 self.objective.type,
                                                                 self.objective.expr))

    def process_initial_state(self, init_data: List[Tuple[CompoundTerm, int]]):
        """
        Process list of compound terms collected by the PDDL input parser

        :param init_data:
        :return:
        """
        if self.L is None:
            raise RuntimeError("Error processing initial state: domain theory languate is not set")

        self.init = model.create(self.L, default_evaluator)

        for idx, el in enumerate(init_data):
            if not isinstance(el[0], CompoundTerm):
                raise RuntimeError('Error processing initial state: element with index '
                                   '{} is not of type `CompoundTerm` but of type {}'.format(idx, type(el[0])))
            self.init.set(el[0], el[1])
        if self.debug:
            print("Processed {} definition elements in initial state".format(len(init_data)))

    def compile_to_functional_strips(self):
        """
        Compiles temporal actions events into actions in a PPI given in Lifted Functional STRIPS. Note that
        assignments of false (0) to Boolean terms projected away.

        :return:
        """
        def is_positive_assignment(phi: tarski.syntax.Formula):
            if isinstance(phi, tarski.syntax.Atom):
                if phi.symbol.symbol == tarski.syntax.BuiltinPredicateSymbol.EQ \
                        and phi.subterms[0].sort == self.bool_t \
                        and phi.subterms[-1] == 0:
                    return False
                return True
            return True

        def normalize_negation(phi: tarski.syntax.Formula):
            if isinstance(phi, tarski.syntax.Atom):
                if phi.symbol.symbol == tarski.syntax.BuiltinPredicateSymbol.EQ \
                        and phi.subterms[0].sort == self.bool_t \
                        and phi.subterms[-1].symbol == 0:
                    return ~(phi.subterms[0] == 1)
                return phi
            elif isinstance(phi, tarski.syntax.CompoundFormula):
                if phi.connective == tarski.syntax.Connective.And:
                    subformulas = [normalize_negation(sub) for sub in phi.subformulas]
                    return land(*subformulas)
                if phi.connective == tarski.syntax.Connective.Or:
                    subformulas = [normalize_negation(sub) for sub in phi.subformulas]
                    return lor(*subformulas)
            return phi

        if self.L is None:
            raise RuntimeError("Error compiling to FSTRIPS: language is not set")

        problem = fs.create_fstrips_problem(self.L,
                                            problem_name=self.instance_name,
                                            domain_name=self.domain_name)
        problem.goal = self.goal
        problem.init = self.init

        for act in self.actions:
            prec = []
            if isinstance(act.pre, tarski.syntax.Atom):
                prec = [normalize_negation(act.pre)]
            elif isinstance(act.pre, tarski.syntax.Tautology):
                prec = []
            elif isinstance(act.pre, tarski.syntax.CompoundFormula):
                prec = [normalize_negation(sub) for sub in act.pre.subformulas]
            elif isinstance(act.pre, tarski.syntax.QuantifiedFormula):
                raise NotImplementedError("Support for quantified formulas not implemented yet! formula,", act.pre)
            else:
                # @TODO: find a more specific exception type to raise
                raise RuntimeError("Action precondition", act.pre, "of type", type(act.pre), "are not supported")
            prec = land(*prec, flat=True)
            eff = [fs.AddEffect(eff.lhs == eff.rhs) for eff in act.post]
            problem.action(act.name, act.parameters, precondition=prec, effects=eff)

        for pred in self.derived:
            if isinstance(pred.body, tarski.syntax.CompoundFormula):
                if pred.body.connective == tarski.syntax.Connective.And:
                    prec = [normalize_negation(sub) for sub in pred.body.subformulas]
                    prec = land(*prec, flat=True)
                    eff = [fs.AddEffect(pred.head.lhs == pred.head.rhs)]
                    problem.action('axiom_{}'.format(pred.head.symbol), pred.parameters, precondition=prec, effects=eff)
                elif pred.body.connective == tarski.syntax.Connective.Not:
                    prec = [normalize_negation(pred.body)]
                    prec = land(*prec, flat=True)
                    eff = [fs.AddEffect(pred.head.lhs == pred.head.rhs)]
                    problem.action('axiom_{}'.format(pred.head.symbol), pred.parameters, precondition=prec, effects=eff)
                elif pred.body.connective == tarski.syntax.Connective.Or:
                    for idx, sub in enumerate(pred.body.subformulas):
                        if isinstance(sub, tarski.syntax.CompoundFormula):
                            if sub.connective == tarski.syntax.Connective.And:
                                prec = [normalize_negation(sub2) for sub2 in sub.subformulas]
                                prec = land(*prec, flat=True)
                                eff = [fs.AddEffect(pred.head.lhs == pred.head.rhs)]
                                problem.action('axiom_{}_{}'.format(idx, pred.head.symbol), pred.parameters, precondition=prec,
                                               effects=eff)
                            elif sub.connective == tarski.syntax.Connective.Not:
                                prec = [normalize_negation(sub)]
                                prec = land(*prec, flat=True)
                                eff = [fs.AddEffect(pred.head.lhs == pred.head.rhs)]
                                problem.action('axiom_{}_{}'.format(idx, pred.head.symbol), pred.parameters, precondition=prec,
                                               effects=eff)
                        elif isinstance(sub, tarski.syntax.Atom):
                            prec = [sub]
                            prec = land(*prec, flat=True)
                            eff = [fs.AddEffect(pred.head(*pred.parameters) == 1)]
                            problem.action('axiom_{}_{}'.format(idx, pred.head.symbol), pred.parameters, precondition=prec,
                                           effects=eff)
                        else:
                            raise RuntimeError(
                                "Error: Found axiom with quantified formula - which we do not know how ground yet")
            elif isinstance(pred.body, tarski.syntax.Atom):
                prec = [pred.body]
                prec = land(*prec, flat=True)
                eff = [fs.AddEffect(pred.head.lhs == pred.head.rhs)]
                problem.action('axiom_{}'.format(pred.head.symbol), pred.parameters, precondition=prec,
                               effects=eff)
            else:
                raise RuntimeError("Error: Found axiom with quantified formula - which we do not know how ground yet")

        for act in self.durative:
            at_start_prec = [normalize_negation(p.expr) for p in act.at_start.pre]
            fs_at_start_prec = land(*at_start_prec, flat=True)
            fs_at_start_eff = [fs.AddEffect(eff.lhs == eff.rhs) for eff in act.at_start.post]
            problem.action("{}_at_start".format(act.name), act.parameters,
                           precondition=fs_at_start_prec,
                           effects=fs_at_start_eff)

            at_end_prec = [normalize_negation(p.expr) for p in act.at_end.pre]
            at_end_prec += [normalize_negation(p.expr) for p in act.overall]
            fs_at_end_prec = land(*at_end_prec, flat=True)
            fs_at_end_eff = [fs.AddEffect(eff.lhs == eff.rhs) for eff in act.at_end.post]
            problem.action("{}_at_end".format(act.name), act.parameters,
                           precondition=fs_at_end_prec,
                           effects=fs_at_end_eff)

        if self.debug:
            print("Compiled FSTRIPS instance contains", len(problem.actions), "actions")

        return problem

