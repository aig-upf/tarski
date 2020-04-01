
import copy
import itertools
from collections import defaultdict, OrderedDict
from typing import Union

from . import errors as err
from .syntax import Function, Constant, Variable, Sort, inclusion_closure, Predicate, Interval
from .syntax.algebra import Matrix
from . import modules


class FirstOrderLanguage:
    """ A many-sorted first-order language. """

    def __init__(self, name=None):
        self.name = name or 'anonymous'
        self._sorts = {}

        # A mapping between each sort and its single immediate parent
        self.immediate_parent = dict()

        # ancestor_sorts[t] is a set containing all supertypes of sort 't', but NOT 't'
        self.ancestor_sorts = defaultdict(set)

        self._functions = {}
        self._predicates = {}
        self._constants = OrderedDict()

        self._operators = dict()
        self._global_index = dict()
        self._element_containers = {Sort: self._sorts,
                                    Function: self._functions,
                                    Predicate: self._predicates}

        self.theories = set()

        self._attach_object_sort()

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
        return list(self._sorts.values())

    @property
    def predicates(self):
        return list(self._predicates.values())

    @property
    def functions(self):
        return list(self._functions.values())

    def _attach_object_sort(self):
        """ The `object` sort, being the root of the sort hierarchy, needs a special treatment"""
        sort = Sort('object', self)
        self._sorts['object'] = sort
        self._global_index['object'] = sort
        self.immediate_parent[sort] = None
        self.ancestor_sorts[sort] = set()

    @property
    def Object(self):
        """ A shorthand accessor for the object sort. """
        return self._sorts['object']

    @property
    def Real(self):
        """ A shorthand accessor for the Real sort. """
        return self.get_sort('Real')

    @property
    def Integer(self):
        """ A shorthand accessor for the Integer sort. """
        return self.get_sort('Integer')

    @property
    def Natural(self):
        """ A shorthand accessor for the Natural sort. """
        return self.get_sort('Natural')

    @property
    def Boolean(self):
        """ A shorthand accessor for the Boolean sort. """
        return self.get_sort('Boolean')

    def sort(self, name: str, parent: Union[Sort, str, None] = None):
        """ Create new sort with given name and parent sort. The parent sort can be given as a Sort object or as its
        name, if a Sort with that name has already been registered.
        If no parent is specified, the "object" sort is assumed as parent.

        :raises err.DuplicateSortDefinition: if a sort with the same name already existed.
        :raises err.DuplicateDefinition: f some non-sort element with the same name already existed.
        """
        parent = self.get_sort("object") if parent is None else self._retrieve_sort(parent)
        return self.attach_sort(Sort(name, self), parent)

    def attach_sort(self, sort: Sort, parent: Sort):
        """ Attach a given sort to the language. For standard creation of sorts, better use `lang.sort()`. """
        self._check_name_not_defined(sort.name, self._sorts, err.DuplicateSortDefinition)

        # Register the sort itself
        self._sorts[sort.name] = sort
        self._global_index[sort.name] = sort

        # Register the sort parent
        self.set_parent(sort, parent)

        return sort

    def has_sort(self, name: str):
        return name in self._sorts

    def get_sort(self, name: str) -> Sort:
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

    def variable(self, name: str, sort: Union[Sort, str]):
        """ Create a variable symbol with the specified sort, which can be given as a Sort object or as its name,
        if a Sort with that name has already been registered. """
        sort = self._retrieve_sort(sort)
        return Variable(name, sort)

    def set_parent(self, sort: Sort, parent: Sort):
        if parent.language is not self:
            raise err.LanguageError("Tried to set as parent a sort from a different language")

        p = self.immediate_parent.get(sort, None)
        if p is not None:
            raise err.LanguageError(f'Tried to set parent of sort "{sort}", which has already parent {p}')

        self.immediate_parent[sort] = parent
        self.ancestor_sorts[sort].update(inclusion_closure(parent))

    def _retrieve_sort(self, obj: Union[Sort, str]) -> Sort:
        return self._retrieve_object(obj, Sort)

    def _retrieve_object(self, obj, type_):
        """
        Make sure that the given obj is either an object of a certain language type (e.g. sort, predicate, etc.)
        which has been correctly registered with the language, or the name of such an object, and return the object
        """
        if not isinstance(obj, (str, type_)):
            raise err.UnexpectedElementType(obj)

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

    def constant(self, name: str, sort: Union[Sort, str]):
        """ Create a constant symbol with the specified sort, which can be given as a Sort object or as its name,
        if a Sort with that name has already been registered. """
        sort = self._retrieve_sort(sort)

        if sort.builtin:
            if sort.cast(name) is None:
                raise err.SemanticError(
                    f"Cannot create constant with sort '{sort.name}' from '{name}' of Python type '{type(name)}'")

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

    @staticmethod
    def vector(arraylike, sort: Sort):
        np = modules.import_numpy()
        return Matrix(np.reshape(arraylike, (len(arraylike), 1)), sort)

    @staticmethod
    def matrix(arraylike, sort: Sort):
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

        types = [self._retrieve_sort(a) for a in args]  # Convert possible strings into Sort objects
        predicate = Predicate(name, self, *types)
        self._predicates[name] = predicate
        self._global_index[name] = predicate
        return predicate

    def has_predicate(self, name):
        return name in self._predicates

    def get_predicate(self, name):
        if not self.has_predicate(name):
            raise err.UndefinedPredicate(name)
        return self._predicates[name]

    def function(self, name: str, *args):
        self._check_name_not_defined(name, self._functions, err.DuplicateFunctionDefinition)

        types = [self._retrieve_sort(a) for a in args]  # Convert possible strings into Sort objects
        func = Function(name, self, *types)
        self._functions[name] = func
        self._global_index[name] = func
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
        t = self._retrieve_sort(t)
        st = self._retrieve_sort(st)
        return t == st or self.is_strict_subtype(t, st)

    def is_strict_subtype(self, t, st):
        t = self._retrieve_sort(t)
        st = self._retrieve_sort(st)
        return st in self.ancestor_sorts[t]

    def are_vertically_related(self, t1, t2):
        t1 = self._retrieve_sort(t1)
        t2 = self._retrieve_sort(t2)
        return self.is_subtype(t1, t2) or self.is_subtype(t2, t1)

    def __str__(self):
        return f"{self.name}: Tarski language with {len(self._sorts)} sorts, {len(self._predicates)} predicates, " \
               f"{len(self._functions)} functions and {len(self.constants())} constants"
    __repr__ = __str__

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
        This can be a predicate or function symbol, including constants, or a sort name.
        Multiple names can be used to get different elements in one single call:

            >>> lang = FirstOrderLanguage()
            >>> lang.predicate('on', lang.get_sort('object'))
            >>> lang.function('loc', lang.get_sort('object'), lang.get_sort('object'))
            >>> on, loc = lang.get("on", "loc")
        """
        def access_next(elem):
            try:
                return self._global_index[elem]
            except KeyError:
                raise err.UndefinedElement(elem) from None

        if not args:  # The user asked for one single element, return it directly
            return access_next(first)

        # Otherwise, the user asked for multiple elements, return them as a tuple for easier unpacking
        # (we don't really expect this method to be called with huge amounts of parameters)
        return tuple(access_next(what) for what in itertools.chain([first], args))

    @property
    def ns(self):
        """ A helper to access the FOL symbols in an elegant and easy manner, to be used e.g. as in:

            >>> lang = FirstOrderLanguage()
            >>> lang.predicate('on', lang.get_sort('object'))
            >>> print(f'The predicate object "on" is: {lang.ns.on}')

        The overall idea is that the `ns` attribute (for "namespace") encapsulates access to only the symbols
        in the first-order language (sorts, predicate and function symbols, including constants),
        and nothing else (that is, it knows nothing about other class methods and attributes).
        """
        return _NamespaceAccessor(self)


class _NamespaceAccessor:
    """ A nifty helper to ease access to a language attributes """
    def __init__(self, lang: FirstOrderLanguage):
        self.lang = lang

    def __getattr__(self, name):
        return self.lang.get(name)
