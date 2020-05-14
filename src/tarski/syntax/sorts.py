import itertools
from typing import Generator, Set as SetT

from .. import errors as err
from ..errors import InvalidSortError


def _extract_python_literal(x):
    from .terms import Constant
    return x.symbol if isinstance(x, Constant) else x


class Sort:
    """ A logical sort (aka type).
        Sorts are uniquely identified by their name (i.e. we don't allow two sorts with different characteristics
        but the same name). Hence, implementation-wise, we can hash and compare them based on name alone.
    """
    def __init__(self, name, language, builtin=False):
        self.name = name
        self.language = language
        self.builtin = builtin

    def __eq__(self, other):
        return self.name == other.name and self.language == other.language

    def __hash__(self):
        return hash((self.name, self.language))

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()

    def __deepcopy__(self, memo):
        """ At the moment we forbid deep copies of Sort objects, as they might be too expensive"""
        memo[id(self)] = self
        return self

    def contains(self, element):
        """ Return true iff the current sort contains the specified element. """
        raise NotImplementedError

    def literal(self, element):
        """ Return the Python object corresponding to the given element if the element belongs to this sort.
        Thus a Constant(10, Integer) will cast as the Python 10 int object, whereas a Constant("b1", Block)
        will be casted as a Block as the Python string "b1".
        If the element does not belong to this sort, a CastError is raised.
        This can happen for instance if we attempt to get the literal corresponding to a block "b1" that has not been
        created as a constant of sort "Block", or if we attempt to retrieve an int literal from an object 3.14159.
        """
        raise NotImplementedError

    def cast(self, element):
        """ Cast the given element to a constant of this sort. """
        raise NotImplementedError

    def cardinality(self):
        raise NotImplementedError

    def dump(self):
        raise NotImplementedError

    def extend(self, symbol):
        """ Register the given symbol as a constant of this sort. """
        raise NotImplementedError

    def domain(self):
        """ Return an iterator over all constants defined in this sort. """
        raise NotImplementedError

    def symbol_is_consistent(self, element):
        """ Return whether the given element is a-priori consistent with this sort. """
        raise NotImplementedError

    def has_extensional_storage(self):
        """ Return whether this sort requires to to store all constants that are created in the language register. """
        raise NotImplementedError


class Enumeration(Sort):
    """ A finite-domain sort with no arithmetic/scalar meaning, i.e. an enumeration sort, such as
    "block" in blocksworld, or "stone" in Sokoban. """

    def __init__(self, name, language, builtin=False):
        super().__init__(name, language, builtin)
        self._domain = set()

    def __str__(self):
        return f'Enumeration({self.name})'

    def contains(self, x):
        return _extract_python_literal(x) in self._domain

    def literal(self, x):
        value = _extract_python_literal(x)
        if value in self._domain:
            return value
        raise err.CastError(f'Cannot convert "{x}" to literal of sort {self}')

    def cast(self, x):
        from .terms import Constant
        return Constant(self.literal(x), self)

    def cardinality(self):
        return len(self._domain)

    def dump(self):
        return dict(name=self.name,
                    domain=list(self._domain))  # Copy the list

    def extend(self, symbol):
        """ Extend the domain of the current sort, and recursively of the parent sorts, with a new constant. """
        self._domain.add(symbol)
        for p in ancestors(self):
            p.extend(symbol)
        return symbol

    def domain(self):
        return (self.language.get_constant(v) for v in self._domain)

    def symbol_is_consistent(self, element):
        return isinstance(element, str)

    def has_extensional_storage(self):
        return True


class Interval(Sort):
    """ An (bounded) real or integer interval type. The Integers and the Reals, for instance, are
    (built-in) interval sorts, with large predefined bounds. User-created intervals should be defined
    through the FirstOrderLanguage.interval() function. """

    def __init__(self, name, language, encode_fn, lower_bound, upper_bound, builtin=False):
        """ Create an interval defined by the range [lower_bound, upper_bound], i.e. both inclusive.
        `encode_fn` should be a function able to encode string objects into the Python arithmetic object that
         underlies this sort (e.g. the int function, that can be invoked as int("34")).
        """
        super().__init__(name, language, builtin)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.encode = encode_fn

    def __str__(self):
        return f'Interval({self.name})'

    def is_within_bounds(self, x):
        """ Check whether a given value is within the bounds of the interval """
        if self.lower_bound is None or self.upper_bound is None:
            raise err.SemanticError("Attempted to check for belonging to Interval type with no bounds set yet")
        return self.lower_bound <= x <= self.upper_bound

    def set_bounds(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def extend(self, symbol):
        """ Intervals simply cast to literal. """
        return self.literal(symbol)

    def cardinality(self):
        # Note that the range is inclusive, hence we add 1
        return self.upper_bound - self.lower_bound + 1

    def symbol_is_consistent(self, element):
        try:
            self.literal(element)
            return True
        except err.CastError:
            return False

    def literal(self, x):
        # Check that the python literal is compatible with this sort, and within the sort range
        try:
            x = self.encode(_extract_python_literal(x))
        except TypeError:
            raise err.CastError(f'Cannot convert "{x}" to literal of sort {self}') from None
        if not self.is_within_bounds(x):
            raise err.CastError(f'Cannot convert "{x}" to literal of sort {self},'
                                f' as it lies outside the defined interval bounds')
        return x

    def cast(self, x):
        """ Cast the given element to a constant of this sort. """
        from .terms import Constant
        return Constant(self.literal(x), self)

    def contains(self, x):
        """ Returns true iff the given value belongs to the current domain """
        try:
            y = self.encode(x)
        except TypeError:
            return False
        return self.is_within_bounds(y)

    def dump(self):
        return dict(name=self.name, domain=[self.lower_bound, self.upper_bound])

    def domain(self):
        if self.builtin or self.upper_bound - self.lower_bound > 9999:  # Yes, very hacky
            raise err.TarskiError(f'Cannot iterate over interval with range [{self.lower_bound}, {self.upper_bound}]')
        from .terms import Constant
        return (Constant(x, self) for x in range(self.lower_bound, self.upper_bound+1))

    def has_extensional_storage(self):
        return False


class Set(Sort):
    """ A parametrized "set of X" type, where X is a primitive type, i.e. either an enumerated or an interval sort. """

    def __init__(self, language, subtype):
        """
        """
        subtype = language.retrieve_sort(subtype)
        if not isinstance(subtype, (Enumeration, Interval)):
            raise InvalidSortError(f"Cannot create a set of {subtype} objects")
        super().__init__(name=f"Set-of-{subtype.name}", language=language, builtin=False)
        self.subtype = subtype

    def __str__(self):
        return self.name

    def extend(self, symbol):
        return self.literal(symbol)

    def cardinality(self):
        """ Return the cardinality of the sort (not of the set!). """
        return 2 ** self.subtype.cardinality()

    def symbol_is_consistent(self, element):
        try:
            self.literal(element)
            return True
        except err.CastError:
            return False

    def literal(self, x):
        try:
            x = self.encode(x)
        except ValueError:
            raise err.CastError(f'Cannot convert "{x}" to literal of sort {self}')
        if not self.is_within_bounds(x):
            raise err.CastError(f'Cannot convert "{x}" to literal of sort {self},'
                                f' as it lies outside the defined interval bounds')
        return x

    def cast(self, x):
        """ Cast the given element to a constant of this sort. """
        from .terms import Constant
        return Constant(self.literal(x), self)

    def contains(self, x):
        """ Returns true iff the given value belongs to the current domain """
        try:
            y = self.encode(x)
        except ValueError:
            return False
        return self.is_within_bounds(y)

    def dump(self):
        return dict(name=self.name, domain=[self.lower_bound, self.upper_bound])

    def domain(self):
        if self.builtin or self.upper_bound - self.lower_bound > 9999:  # Yes, very hacky
            raise err.TarskiError(
                f'Cannot iterate over interval with range [{self.lower_bound}, {self.upper_bound}]')
        from .terms import Constant
        return (Constant(x, self) for x in range(self.lower_bound, self.upper_bound + 1))

    def has_extensional_storage(self):
        return False


def inclusion_closure(s: Sort) -> Generator[Sort, None, None]:
    """ Return the set of all parents of the given sort `s`, including itself, as a generator """
    while s is not None:
        yield s
        s = parent(s)


def parent(s: Sort) -> Sort:
    """ Return the direct parent of the given sort `s`, or None if `s` is the root sort "object" """
    assert s in s.language.immediate_parent
    return s.language.immediate_parent[s]


def ancestors(s: Sort) -> SetT[Sort]:
    """ Return the set of all ancestors of `s` along the sort hierarchy, but not `s` itself """
    assert s in s.language.ancestor_sorts
    return s.language.ancestor_sorts[s]


def children(s: Sort) -> SetT[Sort]:
    """ Return the direct children of the given sort """
    result = set()
    for child, par in s.language.immediate_parent.items():
        if par is not None and par == s:
            result.add(child)
    return result


def int_encode_fn(x):
    # We don't want 1.2, not even 1.0 to get encoded as an int
    if isinstance(x, float):
        raise TypeError()
    return int(x)


def float_encode_fn(x):
    return float(x)


def build_the_naturals(lang):
    return Interval('Natural', lang, int_encode_fn, 0, 2 ** 32 - 1, builtin=True)


def build_the_integers(lang):
    return Interval('Integer', lang, int_encode_fn, -(2 ** 31 - 1), 2 ** 31 - 1, builtin=True)


def build_the_reals(lang):
    return Interval('Real', lang, float_encode_fn, -3.40282e+38, 3.40282e+38, builtin=True)


def attach_arithmetic_sorts(lang):
    real_t = lang.attach_sort(build_the_reals(lang), lang.ns.object)
    int_t = lang.attach_sort(build_the_integers(lang), real_t)
    _ = lang.attach_sort(build_the_naturals(lang), int_t)


def attach_bool_sort(lang):
    bools = Enumeration('Boolean', lang, builtin=True)
    lang.attach_sort(bools, lang.ns.object)
    lang.constant('True', bools)
    lang.constant('False', bools)


def compute_signature_bindings(signature):
    """ Return an exhaustive list of all possible bindings compatible with the given signature, i.e.
    list of sorts. """
    domains = [s.domain() for s in signature]
    for binding in itertools.product(*domains):
        yield binding


def compute_direct_sort_map(lang):
    """ Return a map from each sort s to a list of the objects that have s as their direct sort
     (i.e. ignoring parent sorts). """
    res = {s: [] for s in lang.sorts if not s.builtin}
    _ = [res[o.sort].append(o) for o in lang.constants()]
    return res


def get_closest_builtin_sort(s: Sort):
    for s in inclusion_closure(s):
        if s.builtin:
            break
    return s
