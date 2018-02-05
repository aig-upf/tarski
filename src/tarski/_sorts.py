
from typing import List
from ._errors import LanguageError


class Sort:
    def __init__(self, name, lang):
        self._name = name
        self._language = lang
        self._domain = set()
        self._built_in = False

    def __str__(self):
        return 'Sort({})'.format(self.name)

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @property
    def language(self):
        return self._language

    @property
    def built_in(self):
        return self._built_in

    @built_in.setter
    def built_in(self, v):
        assert isinstance(v, bool)
        self._built_in = v

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
            raise LanguageError("Sort '{}' is empty!".format(self._name))

    def dump(self):
        return dict(name=self._name,
                    domain=self._domain.copy())

    def extend(self, constant):
        self._domain.add(constant.symbol)
        for p in parents(self):
            p.extend(constant)


def parents(s: Sort) -> List[Sort]:
    """ Returns direct parent sorts in the sort hierarchy associated with
        the language
    """
    _parents = []
    for lhs, rhs in s.language.sort_hierarchy:
        if lhs == s.name:
            _parents.append(s.language.sort(rhs))
    return _parents


def children(s: Sort) -> List[Sort]:
    """ Return direct child sorts in the sort hierarchy associated with
        the language
    """
    _children = []
    for lhs, rhs in s.language.sort_hierarchy:
        if rhs == sort:
            _children.append(s.language.sort(lhs))
    return _children


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

    def contains(self, x):
        try:
            y = self._encode(x)
        except ValueError:
            return False
        return self._domain(y)

    def dump(self):
        return dict(name=self.name,
                    domain=[self._lb, self._ub])
