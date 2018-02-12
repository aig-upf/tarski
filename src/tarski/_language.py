# -*- coding: utf-8 -*-

from typing import Set

import scipy.constants

from . import funcsym
from ._function import Function
from ._model import Model
from ._predicate import Predicate, Equality
from ._relational import EQFormula, LTFormula, GTFormula, LEQFormula, GEQFormula, NEQFormula
from ._sorts import *
from ._terms import Constant, Variable
from .errors import *


class FOL:
    formula_symbols = {
        '=': EQFormula,
        '!=': NEQFormula,
        '<': LTFormula,
        '>': GTFormula,
        '<=': LEQFormula,
        '>=': GEQFormula
    }

    def __init__(self):
        self._sorts = {}
        # MRJ: let's represent this temporally as pairs of names of sorts,
        # lhs \sqsubseteq rhs, lhs is a subset of rhs
        self._sort_hierarchy = set()
        # MRJ: this contains a table where we record possible promotions
        # between sorts (i.e. bottom up along the hierarchy)
        self._possible_promotions = {}

        self._functions = {}
        self._predicates = {}
        self._constants = {}
        self._variables = set()

        # MRJ: let's allow default equality predicates to be enabled/disabled
        # dynamically
        self._default_equality = True
        self._symbol_table = {}
        self._build_builtin_sorts()
        funcsym.initialize(self)

        self._element_containers = {Sort: self._sorts,
                                    Function: self._functions,
                                    Predicate: self._predicates,
                                    Variable: self._variables}


    def _inclusion_closure(self, s: Sort) -> Set[Sort]:
        """
            Calculates the inclusion closure over given sort s
        """
        closure = set()
        frontier = {s}
        while len(frontier) > 0:
            s = frontier.pop()
            closure.add(s)
            for p in parents(s):
                frontier.add(p)
        return closure

    @property
    def variables(self):
        for x in self._variables:
            yield x

    @property
    def sort_hierarchy(self):
        return self._sort_hierarchy

    @property
    def sorts(self):
        for s in self.sorts:
            yield s

    @property
    def predicates(self):
        for _, p in self._predicates.items():
            yield p

    @property
    def functions(self):
        for f in self._functions.items():
            yield f

    def _build_builtin_sorts(self):
        self._build_the_reals()
        self._build_the_integers()
        self._build_the_naturals()

    def _build_the_reals(self):
        the_reals = Interval(-3.40282e+38, 3.40282e+38, lambda x: float(x), 'Real', self)
        the_reals.built_in = True
        the_reals.pi = scipy.constants.pi
        self._sorts['Real'] = the_reals
        sort_eq = Equality(self, the_reals, the_reals)
        self._predicates[sort_eq.signature] = sort_eq

    @property
    def Real(self):
        return self._sorts['Real']

    def _build_the_integers(self):
        the_ints = Interval(-(2 ** 31 - 1), 2 ** 31 - 1, lambda x: int(x), 'Integer', self)
        the_ints.built_in = True
        self._sorts['Integer'] = the_ints
        self.set_parent(the_ints, self.Real)
        sort_eq = Equality(self, the_ints, the_ints)
        self._predicates[sort_eq.signature] = sort_eq

    @property
    def Integer(self):
        return self._sorts['Integer']

    def _build_the_naturals(self):
        the_nats = Interval(0, 2 ** 32 - 1, lambda x: int(x), 'Natural', self)
        the_nats.built_in = True
        self._sorts['Natural'] = the_nats
        self.set_parent(the_nats, self.Integer)
        sort_eq = Equality(self, the_nats, the_nats)
        self._predicates[sort_eq.signature] = sort_eq

    @property
    def Natural(self):
        return self._sorts['Natural']

    def sort(self, name: str, super_sorts: List[Sort] = []):
        """
            Create new sort with given name and ancestors

            Raises DuplicateSortDefinition if sort already existed
        """
        if self.has_sort(name):
            raise DuplicateSortDefinition(name, self._sorts[name])

        sort_obj = Sort(name, self)
        self._sorts[name] = sort_obj

        # MRJ: setup promotions table
        if super_sorts is None:
            self._possible_promotions[name] = set()  # no possible promotions
        else :
            for parent in super_sorts: self.set_parent(sort_obj, parent)

        # MRJ: create equality
        if self._default_equality:
            sort_eq = Equality(self, sort_obj, sort_obj)
            self._predicates[sort_eq.signature] = sort_eq
        return sort_obj

    def has_sort(self, name):
        return name in self._sorts

    def get_sort(self, name):
        if not self.has_sort(name):
            raise UndefinedSort(name)
        return self._sorts[name]

    def variable(self, name: str, sort: Sort):
        sort = self._retrieve_object(sort, Sort)
        return Variable(name, sort, self)

    def set_parent(self, lhs: Sort, rhs: Sort):
        if rhs.language is not self:
            raise LanguageError("FOL.sort(): tried to set as parent a sort from a different language")
        self._sort_hierarchy.add((lhs.name, rhs.name))
        self._possible_promotions[lhs.name] = self._inclusion_closure(rhs)

    def _retrieve_object(self, obj, type_):
        """
        Make sure that the given obj is either an object of a certain language type (e.g. sort, predicate, etc.)
        which has been correctly registered with the language, or the name of such an object, and return the object
        """
        if not isinstance(obj, (str, type_)):
            raise LanguageError("Unknown type of language element {}".format(obj))

        if isinstance(obj, type_):
            if obj._language != self:
                raise MismatchingLanguage(obj, obj._language, self)
            return obj

        # obj must be a string, which we take as the name of a language element
        if type_ not in self._element_containers:
            raise RuntimeError("Trying to index incorrect type {}".format(type_))

        if obj not in self._element_containers[type_]:
            raise UndefinedElement(obj)

        return self._element_containers[type_][obj]

    def constant(self, name, sort: Sort):
        """ Create constant symbol of a given sort """
        sort = self._retrieve_object(sort, Sort)

        # TODO - CLARIFY THE LOGIC OF BUILT-INS HERE
        if sort.built_in:
            return sort.cast(name)

        if name in self._constants:
            raise DuplicateConstantDefinition(name, self._constants[name])

        self._constants[name] = Constant(name, sort, self)
        return self._constants[name]

    def has_constant(self, name):
        return name in self._constants

    def get_constant(self, name):
        if not self.has_constant(name):
            raise UndefinedConstant(name)
        return self._constants[name]

    def predicate(self, name: str, *args):
        if name in self._predicates:
            raise DuplicatePredicateDefinition(name, self._predicates[name])

        self._predicates[name] = Predicate(name, self, *args)
        return self._predicates[name]

    def has_predicate(self, name):
        return name in self._predicates

    def get_predicate(self, name):
        if not self.has_predicate(name):
            raise UndefinedPredicate(name)
        return self._predicates[name]

    def function(self, name: str, *args):
        if name in self._functions:
            raise DuplicateFunctionDefinition(name, self._functions[name])

        self._functions[name] = Function(name, self, *args)
        return self._functions[name]

    def has_function(self, name):
        return name in self._functions

    def get_function(self, name):
        if not self.has_function(name):
            raise UndefinedFunction(name)
        return self._functions[name]

    def model(self):
        return Model(self)

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

    def resolve_function_symbol_2(self, sym: str, lhs: Sort, rhs: Sort):
        try:
            return self._symbol_table[(sym, lhs, rhs)]
        except KeyError:
            raise LanguageError(
                "FOL.resolve_function_symbol_2(): function symbol '{}' is not defined for domain ({},{})"
                .format(sym, lhs, rhs))

    def resolve_formula_symbol(self, symbol):
        return self.formula_symbols[symbol]
