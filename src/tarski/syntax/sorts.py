import itertools
from typing import Generator, Set

from .. import errors as err


class Sort:
    """ A logical sort (aka type)
        Sorts are uniquely identified by their name (i.e. we don't allow two sorts with different characteristics
        but the same name). Hence, implementation-wise, we can hash and compare them based on name alone.
    """
    def __init__(self, name, language, builtin=False):
        self.name = name
        self.language = language
        self._domain = set()
        self.builtin = builtin

    def __str__(self):
        return 'Sort({})'.format(self.name)

    __repr__ = __str__

    def __deepcopy__(self, memo):
        """ At the moment we forbid deep copies of this class, as they might be too expensive"""
        memo[id(self)] = self
        return self

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def contains(self, x):
        """ Return true iff the current sort contains a constant with the given value  """
        # TODO - Refactor this, we shouldn't be checking for two different ways of representing a value
        try:
            return x.symbol in self._domain
        except AttributeError:
            return x in self._domain

    def cast(self, x):
        # TODO - Refactor this, we shouldn't be checking for two different ways of representing a value
        try:
            if x.symbol in self._domain:
                return x.symbol
        except AttributeError:
            if x in self._domain:
                return x
            raise ValueError(f"Cast: Symbol '{x}' does not belong to domain {self}") from None
        return None

    def to_constant(self, x):
        """ Cast the given element to a constant of this sort. """
        from . import Constant, Variable  # pylint: disable=import-outside-toplevel  # Avoiding circular references
        if isinstance(x, (Constant, Variable)) and x.sort == self:
            return x
        if x not in self._domain:
            raise ValueError(f"Cast: Symbol '{x}' does not belong to domain {self}")
        return Constant(x, self)

    def cardinality(self):
        return len(self._domain)

    def dump(self):
        return dict(name=self.name,
                    domain=list(self._domain))  # Copy the list

    def extend(self, constant):
        """ Extend the domain of the current sort, and recursively of the parent sorts, with a new constant. """
        self._domain.add(constant.symbol)
        for p in ancestors(self):
            p.extend(constant)

    def domain(self):
        return (self.language.get_constant(v) for v in self._domain)


class Interval(Sort):
    def __init__(self, name, lang, encode_fn, lower_bound, upper_bound, builtin=False):
        super().__init__(name, lang, builtin=builtin)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.encode = encode_fn

    def is_within_bounds(self, x):
        """ Check whether a given value is within the bounds of the interval """
        if self.lower_bound is None or self.upper_bound is None:
            raise err.SemanticError("Attempted to check for belonging to Interval type with no bounds set yet")
        return self.lower_bound <= x <= self.upper_bound

    def set_bounds(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def extend(self, constant):
        # Overload to avoid doing any extension.
        # TODO Better would be to subclass not from Sort but from a different, common baseclass
        pass

    def cardinality(self):
        return self.upper_bound - self.lower_bound + 1

    def cast(self, x):
        """ Casts the given value as an element of the current domain,
        or raise ValueError if it does not belong to it """
        # if isinstance(x, str):
        #     try:
        #         return getattr(self, x)  # TODO: WHAT IS THIS?? ANSWER: MADNESS
        #     except AttributeError:
        #         pass
        y = self.encode(x)  # can raise ValueError
        if not self.is_within_bounds(y):
            raise ValueError("Cast: Symbol '{}' (encoded '{}') outside of defined interval bounds".format(x, y))
        return y

    def to_constant(self, x):
        """ Cast the given element to a constant of this sort. """
        from . import Constant, Variable  # pylint: disable=import-outside-toplevel  # Avoiding circular references
        if isinstance(x, (Constant, Variable)) and x.sort == self:
            return x
        return Constant(self.cast(x), self)

    def contains(self, x):
        """ Returns true iff the given value belongs to the current domain """
        try:
            y = self.encode(x)
        except ValueError:
            return False
        return self.is_within_bounds(y)

    def _downcast(self, x):
        """ Check whether the given value belongs to the current sort _or_ can be downcasted to it.
        e.g. Integer.downcast(1.0) would return 1; whereas Integer.downcast(1.4) would return None. """
        # TODO (GFM) - Not sure we need this, and not sure whether the method works as it is
        # TODO (GFM) - If noone is using this we should remove it soon
        if self.contains(x):
            return self.encode(x)

        # Downcasting Python literals from their type to a subtype (i.e. Real to Integer) works
        # whenever the resulting instance of the subtype belongs
        # to the domain *and* Python equality over the subtype instance and the
        # supertype instance returns true.
        p = parent(self)
        while p is not None:
            try:
                z = p.cast(x)
            except ValueError as e:
                raise err.LanguageError() from e
            if z is not None and x != z:
                return None
            p = parent(p)

    def dump(self):
        return dict(name=self.name, domain=[self.lower_bound, self.upper_bound])

    def domain(self):
        if self.builtin or self.upper_bound - self.lower_bound > 9999:  # Yes, very hacky
            raise err.TarskiError(f'Cannot iterate over interval with range [{self.lower_bound}, {self.upper_bound}]')
        from . import Constant  # pylint: disable=import-outside-toplevel  # Avoiding circular references
        return (Constant(x, self) for x in range(self.lower_bound, self.upper_bound+1))


def inclusion_closure(s: Sort) -> Generator[Sort, None, None]:
    """ Return the set of all parents of the given sort `s`, including itself, as a generator """
    while s is not None:
        yield s
        s = parent(s)


def parent(s: Sort) -> Sort:
    """ Return the direct parent of the given sort `s`, or None if `s` is the root sort "object" """
    assert s in s.language.immediate_parent
    return s.language.immediate_parent[s]


def ancestors(s: Sort) -> Set[Sort]:
    """ Return the set of all ancestors of `s` along the sort hierarchy, but not `s` itself """
    assert s in s.language.ancestor_sorts
    return s.language.ancestor_sorts[s]


def children(s: Sort) -> Set[Sort]:
    """ Return the direct children of the given sort """
    result = set()
    for child, par in s.language.immediate_parent.items():
        if par is not None and par == s:
            result.add(child)
    return result


def int_encode_fn(x):
    if isinstance(x, float) and not x.is_integer():
        raise ValueError(x)  # We don't want 1.2 to get encoded as an int
    return int(x)


def float_encode_fn(x):
    return float(x)


def build_the_bools(lang):
    bools = lang.sort('Boolean')
    # TODO: we really should be setting builtin to True, but at the moment this is undesirable, as in many places in
    #       the code we seem to assume that "builtin" sorts are kind of "numeric" sorts, which leads us to try to do
    #       things with the new Bool sort that cannot be done, e.g. to cast string object "True" to a value, etc.
    # bools.builtin = True
    lang.constant('True', bools)
    lang.constant('False', bools)
    return bools


def build_the_naturals(lang):
    the_nats = Interval('Natural', lang, int_encode_fn, 0, 2 ** 32 - 1, builtin=True)
    the_nats.builtin = True
    return the_nats


def build_the_integers(lang):
    the_ints = Interval('Integer', lang, int_encode_fn, -(2 ** 31 - 1), 2 ** 31 - 1, builtin=True)
    the_ints.builtin = True
    return the_ints


def build_the_reals(lang):
    reals = Interval('Real', lang, float_encode_fn, -3.40282e+38, 3.40282e+38, builtin=True)
    reals.builtin = True
    return reals


def attach_arithmetic_sorts(lang):
    real_t = lang.attach_sort(build_the_reals(lang), lang.ns.object)
    int_t = lang.attach_sort(build_the_integers(lang), real_t)
    _ = lang.attach_sort(build_the_naturals(lang), int_t)


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
    for par in inclusion_closure(s):
        if par.builtin:
            return par
    return None
