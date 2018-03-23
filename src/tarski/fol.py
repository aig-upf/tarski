# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List

import scipy.constants

from . import errors as err
from .syntax import Function, Constant, Term, CompoundTerm, Variable, Sort, Interval, inclusion_closure, Predicate, \
    bind_equality_to_language_components

import tarski.syntax.builtins as syntax_builtins
from . import funcsym


def language(name='L'):
    """ A helper to construct languages"""
    lang = FirstOrderLanguage(name)
    funcsym.initialize(lang)
    return lang


class FirstOrderLanguage:
    """ A full-fledged many-sorted first-order language """

    def __init__(self, name='L'):
        self.name = name
        self._sorts = {}

        # TODO (GFM) I would refactor all of the type information into some kind of TableInfo class that keeps
        # TODO (GFM) all of the necessary data structures to retrieve parenthood, childhood, etc. information.
        # MRJ: let's represent this temporally as pairs of names of sorts,
        # lhs \sqsubseteq rhs, lhs is a subset of rhs
        self._sort_hierarchy = set()

        # _possible_promotions[t] is a set containing all supertypes of sort 't'
        self._possible_promotions = defaultdict(set)

        self._functions = {}
        self._predicates = {}
        # self._predicates_by_sort = {}
        # self._functions_by_sort = {}
        self._constants = {}
        self._variables = set()

        # Allow default builtin predicates to be enabled dynamically
        self._create_default_builtins = True
        self._symbol_table = {}
        self._operators = dict()
        self._build_builtin_sorts()

        self._element_containers = {Sort: self._sorts,
                                    Function: self._functions,
                                    Predicate: self._predicates,
                                    Variable: self._variables}
        # MRJ: https://stackoverflow.com/questions/9541025/how-to-copy-a-python-class
        # see the second most voted answer
        self.Term = type('{}_Term'.format(self.name), (Term,), {})
        self.CompoundTerm = type('{}_CompoundTerm'.format(self.name), (self.Term,), CompoundTerm.__dict__.copy())
        self.Variable = type('{}_Variable'.format(self.name), (self.Term,), Variable.__dict__.copy())
        self.Constant = type('{}_Constant'.format(self.name), (self.Term,), Constant.__dict__.copy())
        self.language_components_frozen = False
        self.theories = []
        bind_equality_to_language_components(self)

    def __deepcopy__(self,memo):
        memo[id(self)]=self
        return self

    @property
    def variables(self):
        for x in self._variables:
            yield x

    @property
    def sort_hierarchy(self):
        return self._sort_hierarchy

    @property
    def sorts(self):
        for _, s in self._sorts.items():
            yield s

    @property
    def predicates(self):
        for _, p in self._predicates.items():
            yield p

    @property
    def functions(self):
        for _, f in self._functions.items():
            yield f

    def _build_builtin_sorts(self):
        self._build_the_objects()
        self._build_the_reals()
        self._build_the_integers()
        self._build_the_naturals()

    def _build_the_reals(self):
        the_reals = Interval(-3.40282e+38, 3.40282e+38, lambda x: float(x), 'Real', self)
        the_reals.builtin = True
        the_reals.pi = scipy.constants.pi
        self._sorts['Real'] = the_reals
        self.set_parent(the_reals, self.Object)
        # self.create_builtin_predicates(the_reals)

    @property
    def Real(self):
        return self._sorts['Real']

    def _build_the_integers(self):
        the_ints = Interval(-(2 ** 31 - 1), 2 ** 31 - 1, lambda x: int(x), 'Integer', self)
        the_ints.builtin = True
        self._sorts['Integer'] = the_ints
        self.set_parent(the_ints, self.Real)
        # self.create_builtin_predicates(the_ints)

    @property
    def Integer(self):
        return self._sorts['Integer']

    def _build_the_naturals(self):
        the_nats = Interval(0, 2 ** 32 - 1, lambda x: int(x), 'Natural', self)
        the_nats.builtin = True
        self._sorts['Natural'] = the_nats
        self.set_parent(the_nats, self.Integer)
        # self.create_builtin_predicates(the_nats)

    def _build_the_objects(self):
        sort = Sort('object', self)
        self._sorts['object'] = sort
        self.create_builtin_predicates(sort)

    @property
    def Object(self):
        return self._sorts['object']

    @property
    def Natural(self):
        return self._sorts['Natural']

    def sort(self, name: str, super_sorts: List[Sort] = None):
        """
            Create new sort with given name and ancestors

            Raises err.DuplicateSortDefinition if sort already existed
        """
        if self.has_sort(name):
            raise err.DuplicateSortDefinition(name, self._sorts[name])

        sort = Sort(name, self)
        self._sorts[name] = sort

        # MRJ: setup promotions table
        osort = self.get_sort("object")
        super_sorts = super_sorts or []
        if osort not in super_sorts:  # Make sure all sorts derive from "object"
            super_sorts.append(osort)

        for parent in super_sorts:
            self.set_parent(sort, parent)

        # self.create_builtin_predicates(sort)

        return sort

    def has_sort(self, name):
        return name in self._sorts

    def get_sort(self, name):
        if not self.has_sort(name):
            raise err.UndefinedSort(name)
        return self._sorts[name]

    def variable(self, name: str, sort: Sort):
        sort = self._retrieve_object(sort, Sort)
        return self.Variable(name, sort)

    def set_parent(self, lhs: Sort, rhs: Sort):
        if rhs.language is not self:
            raise err.LanguageError("FOL.sort(): tried to set as parent a sort from a different language")
        self._sort_hierarchy.add((lhs.name, rhs.name))
        self._possible_promotions[lhs.name].update(inclusion_closure(rhs))

    def _retrieve_object(self, obj, type_):
        """
        Make sure that the given obj is either an object of a certain language type (e.g. sort, predicate, etc.)
        which has been correctly registered with the language, or the name of such an object, and return the object
        """
        if not isinstance(obj, (str, type_)):
            raise err.LanguageError("Unknown type of language element {}".format(obj))

        if isinstance(obj, type_):
            if obj.language != self:
                raise err.LanguageMismatch(obj, obj.language, self)
            return obj

        # obj must be a string, which we take as the name of a language element
        if type_ not in self._element_containers:
            raise RuntimeError("Trying to index incorrect type {}".format(type_))

        if obj not in self._element_containers[type_]:
            raise err.UndefinedElement(obj)

        return self._element_containers[type_][obj]

    def constant(self, name, sort: Sort):
        """ Create constant symbol of a given sort """
        sort = self._retrieve_object(sort, Sort)

        if sort.builtin:
            actual = sort.cast(name)
            if actual is not None:
                # MRJ: if name is a Python primitive type literal that can
                # interpreted as the underlying type of the built in sort, we
                # return a Constant object.
                # TODO: I do no't see it is desirable to store constants of
                # built in sorts.
                return self.Constant(name, sort)
            # MRJ: otherwise
            raise err.SemanticError(
                "Cannot create constant term of sort '{}' from '{}' of Python type '{}'".format(sort.name, name,
                                                                                                type(name)))

        if name in self._constants:
            raise err.DuplicateConstantDefinition(name, self._constants[name])

        self._constants[name] = self.Constant(name, sort)
        return self._constants[name]

    def has_constant(self, name):
        return name in self._constants

    def get_constant(self, name):
        if not self.has_constant(name):
            raise err.UndefinedConstant(name, 'Language constants: {}'.format(self._constants))
        return self._constants[name]

    def predicate(self, name: str, *args):
        if name in self._predicates:
            raise err.DuplicatePredicateDefinition(name, self._predicates[name])

        types = [self._retrieve_object(a, Sort) for a in args]  # Convert possible strings into Sort objects
        predicate = Predicate(name, self, *types)
        predicate.builtin = False

        self._predicates[name] = predicate
        # self._predicates_by_sort[(name,) + tuple(*args)] = predicate
        return predicate

    def has_predicate(self, name):
        return name in self._predicates

    def get_predicate(self, name):
        if not self.has_predicate(name):
            # dump predicates in language
            msg = 'Predicates in language: {}'
            msg = msg.format( ','.join([ '{},{}:{}'.format(type(k), k, str(p.symbol)) for k, p in self._predicates.items()]))
            raise err.UndefinedPredicate(name, msg)
        return self._predicates[name]

    def function(self, name: str, *args):
        if name in self._functions:
            raise err.DuplicateFunctionDefinition(name, self._functions[name])

        types = [self._retrieve_object(a, Sort) for a in args]  # Convert possible strings into Sort objects
        func = Function(name, self, *types)
        func.builtin = False

        self._functions[name] = func
        # self._functions_by_sort[(name,) + tuple(*args)] = func
        return func

    def has_function(self, name):
        return name in self._functions

    def get_function(self, name):
        if not self.has_function(name):
            msg = 'Registered functions: {}\n'.format('\n'.join([ '{}:{}'.format(str(k),str(v)) for k,v in self._functions.items()]))
            raise err.UndefinedFunction(name, msg)
        return self._functions[name]

    def dump(self):
        return dict(
            sorts=[s.dump() for _, s in self._sorts.items()],
            predicates=[p.dump() for _, p in self._predicates.items()],
            functions=[f.dump() for _, f in self._functions.items()]
        )

    def check_well_formed(self):
        for _, s in self._sorts.items():
            s.check_empty()

    def register_symbol(self, key, func_obj):
        self._symbol_table[key] = func_obj
        self._functions[key] = func_obj

    def resolve_function_symbol(self, sym: str, lhs: Sort, rhs: Sort):
        try:
            return self._symbol_table[(sym, lhs, rhs)]
        except KeyError:
            raise err.LanguageError("FOL.resolve_function_symbol(): function symbol '{}' not defined for domain ({},{})"
                                    .format(sym, lhs, rhs))

    def is_subtype(self, t, st):
        return t == st or self.is_strict_subtype(t, st)

    def is_strict_subtype(self, t, st):
        return st in self._possible_promotions[t._name]

    def load_theory(self, theory):
        if self.language_components_frozen:
            raise err.LanguageError("FOL.load_theory(): Cannot load theories once language elements have been defined")
        if theory == 'arithmetic':
            import tarski.syntax.arithmetic
            tarski.syntax.arithmetic.bind_operators_to_language_components(self)
            # MRJ: module funcsym needs to be refactored
            tarski.funcsym.initialize(self)
            self.theories.append(theory)
            print("Loaded theory '{}'".format(theory))

    def create_builtin_predicates(self, sort):
        if not self._create_default_builtins:
            return
        syntax_builtins.create_symbols_for_language(self)

        # for s in builtins.Predicates:
        #     # The name of the built-in predicate takes into account the type it is applied to, e.g. =_int
        #     name = "{}_{}".format(s.value, sort._name)
        #     self.predicate(name, sort, sort)

    def __str__(self):
        return "{}: Tarski language with {} sorts, {} function symbols, {} predicate symbols and {} variables".format(
            self.name, len(self._sorts), len(self._functions), len(self._predicates), len(self._variables))

    def register_operator_handler(self, operator, t1, t2, handler):
        self._operators[(operator, t1, t2)] = handler

    def dispatch_operator(self, operator, t1, t2, lhs, rhs):
        assert isinstance(lhs, t1)
        assert isinstance(rhs, t2)
        try:
            return self._operators[(operator, t1, t2)](lhs, rhs)
        except KeyError:
            raise err.LanguageError("Operator '{}' not defined on domain ({}, {})".format(operator, t1, t2))
