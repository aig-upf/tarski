
import copy
import itertools
from collections import defaultdict, OrderedDict
from typing import Union

from . import errors as err
from .errors import UndefinedElement
from .syntax import Function, Constant, Variable, Sort, inclusion_closure, Predicate, Interval, BuiltinPredicateSymbol
from .syntax.algebra import Matrix
from . import modules
from .syntax.ops import cast_to_closest_common_numeric_ancestor
from .syntax.sorts import Enumeration


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

    def __eq__(self, other):
        """ A (very) shallow equality test. """
        return self.name == other.name

    def __hash__(self):
        """ A (very) shallow hash method. """
        return hash(self.name)

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
        sort = Enumeration('object', self)
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
        """ Create new enumerated sort with given name and parent sort.
        The parent sort can be given as a Sort object or as its name, if a Sort with that name is already registered.
        If no parent is specified, the "object" sort is assumed as parent.

        :raises err.DuplicateSortDefinition: if a sort with the same name already existed.
        :raises err.DuplicateDefinition: if some non-sort element with the same name already existed.
        """
        parent = self.get_sort("object") if parent is None else self.retrieve_sort(parent)
        return self.attach_sort(Enumeration(name, self), parent)

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

    def interval(self, name, parent: Interval, lower_bound, upper_bound):
        """ Create a (bound) interval sort.

        We allow only the new sort to derive from the built-in natural, integer or real sorts.
        """
        self._check_name_not_defined(name, self._sorts, err.DuplicateSortDefinition)
        parent = self.retrieve_sort(parent)

        if parent not in (self.Real, self.Natural, self.Integer):
            raise err.SemanticError("Only intervals derived or real, integer or naturals are allowed")

        # if (lower_bound is None) != (upper_bound is None):
        #     raise err.SemanticError("Either set both interval bounds or set none")

        if upper_bound <= lower_bound:
            raise err.SemanticError("Cannot create interval with upper bound is <= than the lower bound")

        sort = Interval(name, self, parent.encode, lower_bound, upper_bound)
        self._sorts[name] = sort
        self._global_index[name] = sort

        self.set_parent(sort, parent)

        return sort

    def variable(self, name: str, sort: Union[Sort, str]):
        """ Create a variable symbol with the specified sort, which can be given as a Sort object or as its name,
        if a Sort with that name has already been registered. """
        sort = self.retrieve_sort(sort)
        return Variable(name, sort)

    def set_parent(self, sort: Sort, parent: Sort):
        if parent.language is not self:
            raise err.LanguageError("Tried to set as parent a sort from a different language")

        p = self.immediate_parent.get(sort, None)
        if p is not None:
            raise err.LanguageError(f'Tried to set parent of sort "{sort}", which has already parent {p}')

        self.immediate_parent[sort] = parent
        self.ancestor_sorts[sort].update(inclusion_closure(parent))

    def retrieve_sort(self, obj: Union[Sort, str]) -> Sort:
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
            raise RuntimeError(f'Trying to index incorrect type "{type_}"')

        if obj not in self._element_containers[type_]:
            raise err.UndefinedElement(obj)

        return self._element_containers[type_][obj]

    def constant(self, name: str, sort: Union[Sort, str]):
        """ Create a constant symbol with the specified sort, which can be given as a Sort object or as its name,
        if a Sort with that name has already been registered. """
        sort = self.retrieve_sort(sort)

        if not sort.symbol_is_consistent(name):
            raise err.CastError(
                f"Cannot create constant with sort '{sort}' from element '{name}' of Python type '{type(name)}'")

        if not sort.has_extensional_storage():
            # If the sort doesn't need to be stored, we're done
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

    def predicate(self, name: str, *args, builtin=False, overload=False):
        return self._declare_symbol(Predicate, name, *args, builtin=builtin, overload=overload)

    def has_predicate(self, name):
        return name in self._predicates

    def get_predicate(self, name, signature=None):
        return self._retrieve_symbol(name, self._predicates, signature)

    def remove_symbol(self, symbol: Union[Function, Predicate]):
        if symbol.name in self._predicates:
            assert not isinstance(self._predicates[symbol.name], list)
            del self._predicates[symbol.name]
        elif symbol.name in self._functions:
            assert not isinstance(self._functions[symbol.name], list)
            del self._functions[symbol.name]
        else:
            raise UndefinedElement(symbol)

        del self._global_index[symbol.name]

    def function(self, name: str, *args, builtin=False, overload=False):
        return self._declare_symbol(Function, name, *args, builtin=builtin, overload=overload)

    def has_function(self, name):
        return name in self._functions

    def get_function(self, name, signature=None):
        return self._retrieve_symbol(name, self._functions, signature)

    def _declare_symbol(self, type_, name: str, *args, builtin=False, overload=False):
        types = [self.retrieve_sort(a) for a in args]  # Convert possible strings into Sort objects
        func = type_(name, self, *types, builtin=builtin)

        container = self._functions if type_ is Function else self._predicates

        previous = container.get(name)
        if previous is None and name in self._global_index:
            # Some other element (not a function) already declared with this name
            raise err.DuplicateDefinition(name, self._global_index[name])

        if previous is None:
            self._global_index[name] = container[name] = func
            return func

        # If we get here, we're dealing with a potential function overload
        previous = [previous] if not isinstance(previous, list) else previous

        # A function already declared with this name. We can only allow that if the caller asks for overload
        # and the signatures are different
        if not overload:
            raise err.DuplicateFunctionDefinition(name, msg=f'Duplicate definition of function "{name}". '
                                                  f'Set overload=True if you want to register a function overload')

        if func.signature in [s.signature for s in previous]:
            raise err.DuplicateFunctionDefinition(
                name, f'Cannot redeclare function "{name}" with same signature "{func.signature}"')

        if previous is not None:
            self._global_index[name] = container[name] = previous + [func]

        return func

    @staticmethod
    def _retrieve_symbol(name, container, signature=None):
        res = container.get(name)
        if res is None:
            raise err.UndefinedFunction(name)

        if isinstance(res, list):  # An overloaded function
            if signature is None:
                raise err.UndefinedElement(f"Cannot retrieve overloaded function '{name}' "
                                           f"without specifying the desired overload")
            for f in res:  # Let's do just a linear search, should never have too many overloads
                if f.sort == signature:
                    return f
            raise err.UndefinedElement(f"Cannot retrieve overloaded function '{name}': overload {signature} undefined")

        return res

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
        t = self.retrieve_sort(t)
        st = self.retrieve_sort(st)
        return t == st or self.is_strict_subtype(t, st)

    def is_strict_subtype(self, t, st):
        t = self.retrieve_sort(t)
        st = self.retrieve_sort(st)
        return st in self.ancestor_sorts[t]

    def are_vertically_related(self, t1, t2):
        t1 = self.retrieve_sort(t1)
        t2 = self.retrieve_sort(t2)
        return self.is_subtype(t1, t2) or self.is_subtype(t2, t1)

    def __str__(self):
        return f"{self.name}: Tarski language with {len(self._sorts)} sorts, {len(self._predicates)} predicates, " \
               f"{len(self._functions)} functions and {len(self.constants())} constants"
    __repr__ = __str__

    def register_operator_handler(self, operator, t1, t2, handler):
        self._operators[(operator, t1, t2)] = handler

    def register_unary_operator_handler(self, operator, t, handler):
        self._operators[(operator, t)] = handler

    def dispatch_operator(self, symbol, lhs, rhs=None):
        """ Dispatch operator with given symbol and return the expression symbol(lhs, rhs).
        Deals with symbol overloading (in a rather naive way).
        If rhs is None, the operator is assumed to be unary.
        """
        if rhs is None:
            return self._dispatch_unary_operator(symbol, lhs)

        op, lhs, rhs = self.get_operator_matching_arguments(symbol, lhs, rhs)
        return op(lhs, rhs)

    def _dispatch_unary_operator(self, symbol, lhs):
        # @ see method dispatch_operator
        sort = lhs.sort
        while sort is not None:
            op = self._operators.get((symbol, sort))
            if op is not None:
                return op(lhs)
            sort = self.immediate_parent[sort]

        raise err.LanguageError(f"Operator '{symbol}' undefined on domain ({sort})")

    def get_operator_matching_arguments(self, symbol, *args):
        lhs, rhs = cast_to_closest_common_numeric_ancestor(self, *args)

        # First check if the operator has been declared with the arguments sorts.
        op = self._operators.get((symbol, lhs.sort, rhs.sort))
        if op is not None:
            return op, lhs, rhs

        # If not, look up among possible overloads for the given symbol (e.g. +) for one overload that matches the
        # argument sorts. We simply do a linear lookup, as we don't expect a large number of subtypes.
        # The whole overload resolution strategy of course could be made more sophisticated, but at the moment we'll
        # go with this.
        sort = lhs.sort
        while sort is not None:
            op = self._operators.get((symbol, sort, sort))
            if op is not None:
                return op, lhs, rhs
            sort = self.immediate_parent[sort]
        raise err.LanguageError(f"Operator '{symbol}' undefined on domain ({lhs.sort}, {rhs.sort})")

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
            res = self._global_index.get(elem)
            if res is None:
                raise err.UndefinedElement(elem)
            elif isinstance(res, list):
                raise err.UndefinedElement(f"Attempted to retrieve element '{elem}' with several overloads")
            return res

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
