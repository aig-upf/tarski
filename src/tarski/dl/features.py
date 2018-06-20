"""

"""
from enum import Enum

from .concepts import Concept, Role
from ..utils.algorithms import compute_min_distance


class FeatureValueChange(Enum):
    ADD = 1
    DEL = 2
    INC = 3
    DEC = 4
    NIL = 5


class Feature(object):
    def value(self, cache, state, substitution):
        raise NotImplementedError()

    def diff(self, x, y):
        raise NotImplementedError()

    def __hash__(self):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    @staticmethod
    def bool_value(value):
        assert value >= 0
        return value > 0

    # def concept(self):
    #     raise NotImplementedError()


def compute_int_feature_diff(x, y):
    assert type(x) is int and x >= 0
    assert type(y) is int and y >= 0
    if x == y:
        return FeatureValueChange.NIL
    if x > y:
        return FeatureValueChange.DEC
    else:
        return FeatureValueChange.INC


def compute_bool_feature_diff(x, y):
    assert type(x) is bool
    assert type(y) is bool
    if y and not x:
        return FeatureValueChange.ADD
    if x and not y:
        return FeatureValueChange.DEL
    else:
        return FeatureValueChange.NIL


class ConceptCardinalityFeature(Feature):
    def __init__(self, c):
        assert isinstance(c, Concept)
        self.c = c
        self.hash = hash((self.__class__, self.c))

    def value(self, cache, state, substitution):
        """ The feature value _is_ the cardinality of the extension of the represented concept"""
        ext = self.c.extension(cache, state, substitution)
        return ext.count()

    def diff(self, x, y):
        return compute_int_feature_diff(x, y)

    def __repr__(self):
        return 'card[{}]'.format(self.c)

    __str__ = __repr__

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c == other.c)

    def concept(self):
        return self.c

    def weight(self):
        return self.concept().depth*2


class EmpiricalBinaryConcept(Feature):
    def __init__(self, f: ConceptCardinalityFeature):
        self.f = f
        self.hash = hash((self.__class__, self.f))

    def value(self, cache, state, substitution):
        """ The feature value _is_ whether the cardinality of the extension of the represented concept is 0 or 1 """
        x = self.f.value(cache, state, substitution)
        assert x == 0 or x == 1  # By definition of "empirical binary concept"
        return bool(x)

    def diff(self, x, y):
        return compute_bool_feature_diff(x, y)

    def __repr__(self):
        return 'bool[{}]'.format(self.f.c)

    __str__ = __repr__

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.f == other.f)

    def concept(self):
        return self.f.concept()

    def weight(self):
        return self.concept().depth


class MinDistanceFeature(Feature):
    def __init__(self, c1, r, c2):
        assert isinstance(c1, Concept) and isinstance(r, Role) and isinstance(c2, Concept)
        self.c1 = c1
        self.r = r
        self.c2 = c2
        self.hash = hash((self.__class__, self.c1, self.r, self.c2))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c1 == other.c1 and self.r == other.r and self.c2 == other.c2)

    def value(self, cache, state, substitution):
        """ The value of the feature is the min distance between any object in the extension of c1 and any object
            on the extension of c2, moving only along r-edges.
        """
        ext_c1 = self.c1.extension(cache, state, substitution)
        ext_c2 = self.c1.extension(cache, state, substitution)
        ext_r = self.r.extension(cache, state, substitution)
        return compute_min_distance(cache.uncompress(ext_c1, self.c1.ARITY),
                                    cache.uncompress(ext_r, self.r.ARITY),
                                    cache.uncompress(ext_c2, self.c2.ARITY),
                                    )

    def diff(self, x, y):
        return compute_int_feature_diff(x, y)

    def __repr__(self):
        return 'min-distance[{}, {}, {}]'.format(self.c1, self.r, self.c2)

    __str__ = __repr__
