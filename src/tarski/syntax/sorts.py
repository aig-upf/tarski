from typing import List, Set
from .. import errors as err


class Sort:
    def __init__(self, name, language, builtin=False):
        self._name = name
        self.language = language
        self._domain = set()
        self.builtin = builtin

    def __str__(self):
        return 'Sort({})'.format(self.name)

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name

    def contains(self, x):
        try:
            return x.symbol in self._domain
        except AttributeError:
            return x in self._domain

    def cast(self, x):
        try:
            if x.symbol in self._domain:
                return x.symbol
        except AttributeError:
            if x in self._domain:
                return x
        return None

    def check_empty(self):
        if len(self._domain) == 0:
            raise err.LanguageError("Sort '{}' is empty!".format(self._name))

    def dump(self):
        return dict(name=self._name,
                    domain=list(self._domain))  # Copy the list

    def extend(self, constant):
        self._domain.add(constant.symbol)
        for p in parents(self):
            p.extend(constant)


class Interval(Sort):
    def __init__(self, lb, ub, encode_fn, name, lang):
        super(Interval, self).__init__(name, lang)
        self._lb = lb
        self._ub = ub
        self._encode = encode_fn
        self._domain = lambda x: self._lb <= x <= self._ub

    def extend(self, x):
        pass

    def cast(self, x):
        if isinstance(x, str):
            try:
                return getattr(self, x)
            except AttributeError:
                pass
        y = self._encode(x)  # can raise ValueError
        if not self._domain(y):
            raise ValueError(
                "Interval.cast() : symbol '{}', encoded as '{}' does not belong to the domain!".format(x, y))
        return y

    def check_empty(self):
        if self._lb > self._ub:
            raise err.LanguageError("Sort '{}' is empty!".format(self._name))

    def contains(self, x, raises_exceptions=False):
        try:
            y = self._encode(x)
        except ValueError:
            if raises_exceptions:
                raise err.SemanticError('Cannot encode "{}"'.format(x))
            return False

        # Downcasting Python literals from their type to a subtype (i.e. Real
        # to Integer) works whenever the resulting instance of the subtype belongs
        # to the domain *and* Python equality over the subtype instance and the
        # supertype instance returns true. For instance, downcasting 1.0 to
        # integers is okay, but 1.2 will not.
        relevant_supers = set(parents(self))
        while len(relevant_supers) > 0:
            p = relevant_supers.pop()
            try:
                z = p.cast(x)
            except ValueError:
                raise err.LanguageError()
            if z is not None and y != z:
                if raises_exceptions:
                    raise err.SemanticError('{} casted into y: {} and z: {}, y!=z'.format(x, y, z))
                return False
            for p2 in parents(p):
                relevant_supers.add(p2)

        return self._domain(y)

    def dump(self):
        return dict(name=self.name,
                    domain=[self._lb, self._ub])


def inclusion_closure(s: Sort) -> Set[Sort]:
    """ Calculates the inclusion closure over given sort s """
    closure = set()
    frontier = {s}
    while len(frontier) > 0:
        s = frontier.pop()
        closure.add(s)
        for p in parents(s):
            frontier.add(p)
    return closure


def parents(s: Sort) -> List[Sort]:
    """ Returns direct parent sorts in the sort hierarchy associated with
        the language
    """
    _parents = []
    for lhs, rhs in s.language.sort_hierarchy:
        if lhs == s.name:
            _parents.append(s.language.get_sort(rhs))
    return _parents


def children(s: Sort) -> List[Sort]:
    """ Return direct child sorts in the sort hierarchy associated with
        the language
    """
    _children = []
    for lhs, rhs in s.language.sort_hierarchy:
        if rhs == s:
            _children.append(s.language.sort(lhs))
    return _children
