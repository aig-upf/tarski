
import copy
import itertools
from collections import defaultdict, OrderedDict

from . import errors as err
from .syntax import Function, Constant, Variable, Sort, inclusion_closure, Predicate, Interval, sorts
from .syntax.algebra import Matrix


def language(name='L'):
    """ A helper to construct languages"""
    lang = FirstOrderLanguage(name)
    return lang


class FirstOrderLanguage:
    """ A full-fledged many-sorted first-order language """

    def __init__(self, name='L'):
        self.name = name
        self._sorts = {}

        # MRJ: let's represent this temporally as pairs of names of sorts,
        # lhs \sqsubseteq rhs, lhs is a subset of rhs
        self.immediate_parent = dict()

        # ancestor_sorts[t] is a set containing all supertypes of sort 't', but NOT 't'
        self.ancestor_sorts = defaultdict(set)

        self._functions = {}
        self._predicates = {}
        # self._predicates_by_sort = {}
        # self._functions_by_sort = {}
        self._constants = OrderedDict()

        self._operators = dict()
        self._global_index = dict()
        self._element_containers = {Sort: self._sorts,
                                    Function: self._functions,
                                    Predicate: self._predicates}

        self.language_components_frozen = False
        self.theories = []

        self._build_builtin_sorts()

    def __deepcopy__(self, memo):
        """ At the moment we forbid deep copies of this class, as they might be too expensive"""
        memo[id(self)] = self
        return self

    def deepcopy(self):
        """ Use this method instead of copy.deepcopy() if you need a true deep-copy of the language """
        memo = dict()
        newone = type(self)()
        memo[id(self)] = newone
        for k, v in self.__dict__.items():
            setattr(newone, k, copy.deepcopy(v, memo))
        return newone

    @property
    def sorts(self):
        for s in self._sorts.values():
            yield s

    @property
    def predicates(self):
        return self._predicates.values()

    @property
    def functions(self):
        return self._functions.values()

    @property
    def Object(self):
        return self._sorts['object']

    @property
    def Real(self):
        return self._sorts['Real']

    @property
    def Integer(self):
        return self._sorts['Integer']

    @property
    def Natural(self):
        return self._sorts['Natural']

    def _build_builtin_sorts(self):
        self._build_the_objects()
        self._build_the_reals()
        self._build_the_integers()
        self._build_the_naturals()

    def _build_the_reals(self):
        the_reals = sorts.build_the_reals(self)
        self._sorts['Real'] = the_reals
        self.set_parent(the_reals, self.Object)
        # self.create_builtin_predicates(the_reals)
        self._global_index['Real'] = the_reals

    def _build_the_integers(self):
        the_ints = sorts.build_the_integers(self)
        self._sorts['Integer'] = the_ints
        self.set_parent(the_ints, self.Real)
        # self.create_builtin_predicates(the_ints)
        self._global_index['Integer'] = the_ints

    def _build_the_naturals(self):
        the_nats = sorts.build_the_naturals(self)
        self._sorts['Natural'] = the_nats
        self.set_parent(the_nats, self.Integer)
        # self.create_builtin_predicates(the_nats)
        self._global_index['Natural'] = the_nats

    def _build_the_objects(self):
        sort = Sort('object', self)
        self._sorts['object'] = sort
        self.immediate_parent[sort] = None
        self.ancestor_sorts[sort] = set()

    def sort(self, name: str, parent: Sort = None):
        """
            Create new sort with given name and parent sort.
            If no parent is specified, the topmost "object" sort is assumed as parent.

            Raises err.DuplicateSortDefinition if a sort with the same name already existed,
             or err.DuplicateDefinition if some non-sort element with the same name already existed.
        """
        self._check_name_not_defined(name, self._sorts, err.DuplicateSortDefinition)

        sort = Sort(name, self)
        self._sorts[name] = sort
        self._global_index[name] = sort

        parent = parent or self.get_sort("object")
        self.set_parent(sort, parent)

        # self.create_builtin_predicates(sort)
        return sort

    def has_sort(self, name):
        return name in self._sorts

    def get_sort(self, name):
        if not self.has_sort(name):
            raise err.UndefinedSort(name)
        return self._sorts[name]

    def interval(self, name, parent: Interval, lower_bound=None, upper_bound=None):
        """ Create a (bound) interval sort.

        We allow only the new sort to derive from the built-in natural, integer or real sorts.
        """
        self._check_name_not_defined(name, self._sorts, err.DuplicateSortDefinition)

        if parent not in (self.Real, self.Natural, self.Integer):
            raise err.SemanticError("Cannot create interval that does not subclass one of "
                                    "the real, integer or natural sort")

        if upper_bound <= lower_bound:
            raise err.SemanticError("Cannot create interval where the upper bound is greater or "
                                    "equal than the lower bound")

        sort = Interval(name, self, parent.encode, lower_bound, upper_bound)
        sort.builtin = parent.builtin
        self._sorts[name] = sort
        self._global_index[name] = sort

        self.set_parent(sort, parent)

        return sort

    def variable(self, name: str, sort: Sort):
        sort = self._retrieve_object(sort, Sort)
        return Variable(name, sort)

    def set_parent(self, sort: Sort, parent: Sort):
        if parent.language is not self:
            raise err.LanguageError("Tried to set as parent a sort from a different language")

        p = self.immediate_parent.get(sort, None)
        if p is not None:
            raise err.LanguageError('Tried to set parent of sort "{}", which has already parent {}'.format(sort, p))

        self.immediate_parent[sort] = parent
        self.ancestor_sorts[sort].update(inclusion_closure(parent))

    def _retrieve_object(self, obj, type_):
        """
        Make sure that the given obj is either an object of a certain language type (e.g. sort, predicate, etc.)
        which has been correctly registered with the language, or the name of such an object, and return the object
        """
        if not isinstance(obj, (str, type_)):
            raise err.LanguageError('Unknown type of language element "{}"'.format(obj))

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
            if sort.cast(name) is None:
                raise err.SemanticError("Cannot create constant with sort '{}' from '{}' of Python type '{}'".
                                        format(sort.name, name, type(name)))

            # MRJ: if name is a Python primitive type literal that can be interpreted as the underlying
            # type of the built in sort, we return a Constant object.
            # TODO: I don't see it is desirable to store constants of built in sorts.
            # MRJ: We're not storing them anywhere, but we need the Python literals
            # to be decorated so we can use them in our ASTs
            return Constant(name, sort)

        self._check_name_not_defined(name, self._constants, err.DuplicateConstantDefinition)

        c = Constant(name, sort)
        self._constants[name] = c
        self._global_index[name] = c
        return c

    def has_constant(self, name):
        return name in self._constants

    def get_constant(self, name):
        if not self.has_constant(name):
            raise err.UndefinedConstant(name)
        return self._constants[name]

    def constants(self):
        return list(self._constants.values())

    def vector(self, arraylike, sort: Sort):
        import numpy as np
        return Matrix(np.reshape(arraylike, (len(arraylike), 1)), sort)

    def matrix(self, arraylike, sort: Sort):
        return Matrix(arraylike, sort)

    def _check_name_not_defined(self, name, where, exception):
        """ Check whether the given name is already defined in the given container, raising an exception of
        the indicated type in case it is. If not, check it is not defined in any other container, raising a
        more generic DuplicateDefinition exception if it is. """
        if name in where:
            raise exception(name, where[name])

        if name in self._global_index:
            raise err.DuplicateDefinition(name, self._global_index[name])

    def predicate(self, name: str, *args):
        self._check_name_not_defined(name, self._predicates, err.DuplicatePredicateDefinition)

        types = [self._retrieve_object(a, Sort) for a in args]  # Convert possible strings into Sort objects
        predicate = Predicate(name, self, *types)
        self._predicates[name] = predicate
        self._global_index[name] = predicate
        # self._predicates_by_sort[(name,) + tuple(*args)] = predicate
        return predicate

    def has_predicate(self, name):
        return name in self._predicates

    def get_predicate(self, name):
        if not self.has_predicate(name):
            raise err.UndefinedPredicate(name)
        return self._predicates[name]

    def function(self, name: str, *args):
        self._check_name_not_defined(name, self._functions, err.DuplicateFunctionDefinition)

        types = [self._retrieve_object(a, Sort) for a in args]  # Convert possible strings into Sort objects
        func = Function(name, self, *types)
        self._functions[name] = func
        self._global_index[name] = func
        # self._functions_by_sort[(name,) + tuple(*args)] = func
        return func

    def has_function(self, name):
        return name in self._functions

    def get_function(self, name):
        if not self.has_function(name):
            raise err.UndefinedFunction(name)
        return self._functions[name]

    def dump(self):
        return dict(
            sorts=[s.dump() for _, s in self._sorts.items()],
            predicates=[p.dump() for _, p in self._predicates.items()],
            functions=[f.dump() for _, f in self._functions.items()]
        )

    def check_well_formed(self):
        for _, s in self._sorts.items():
            if s.cardinality() == 0:
                raise err.LanguageError("Sort '{}' is empty!".format(s))

    def most_restricted_type(self, t1, t2):
        if self.is_subtype(t1, t2):
            return t1
        elif self.is_subtype(t2, t1):
            return t2
        return None

    def is_subtype(self, t, st):
        t = self._retrieve_object(t, Sort)
        st = self._retrieve_object(st, Sort)
        return t == st or self.is_strict_subtype(t, st)

    def is_strict_subtype(self, t, st):
        t = self._retrieve_object(t, Sort)
        st = self._retrieve_object(st, Sort)
        return st in self.ancestor_sorts[t]

    def are_vertically_related(self, t1, t2):
        t1 = self._retrieve_object(t1, Sort)
        t2 = self._retrieve_object(t2, Sort)
        return self.is_subtype(t1, t2) or self.is_subtype(t2, t1)

    def __str__(self):
        return "{}: Tarski language with {} sorts, {} function symbols, {} predicate symbols".format(
            self.name, len(self._sorts), len(self._functions), len(self._predicates))

    def register_operator_handler(self, operator, t1, t2, handler):
        self._operators[(operator, t1, t2)] = handler

    def register_unary_operator_handler(self, operator, t, handler):
        self._operators[(operator, t)] = handler

    def dispatch_unary_operator(self, operator, t, term):
        try:
            return self._operators[(operator, t)](term)
        except KeyError:
            raise err.LanguageError("Operator '{}' not defined on domain ({})".format(operator, t))

    def dispatch_operator(self, operator, t1, t2, lhs, rhs):
        # assert isinstance(lhs, t1)
        # assert isinstance(rhs, t2)
        op = self._operators.get((operator, t1, t2), None)
        if op is None:
            raise err.LanguageError("Operator '{}' not defined on domain ({}, {})".format(operator, t1, t2))

        return op(lhs, rhs)

    def get(self, first, *args):
        """ Return the language element with given name(s).
        This can be a predicate or function symbol, including constants, or a sort name."""
        res = []
        for what in itertools.chain([first], args):
            try:
                res.append(self._global_index[what])
            except KeyError:
                raise err.UndefinedElement(what)

        return res[0] if not args else res  # Unpack the result if only one element
