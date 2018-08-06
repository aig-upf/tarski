"""

"""
from enum import Enum

from .concepts import Concept, Role, NullaryAtom
from ..utils.algorithms import compute_min_distance


class FeatureValueChange(Enum):
    ADD = 1
    DEL = 2
    INC = 3
    DEC = 4
    NIL = 5


class Feature:
    def value(self, cache, state):
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

    def complexity(self):
        """ Return feature complexity value """
        raise NotImplementedError()


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
    """ A numeric feature that reflects the cardinality of a set of objects defined by a concept """
    def __init__(self, c):
        assert isinstance(c, Concept)
        self.c = c
        self.hash = hash((self.__class__, self.c))

    def value(self, cache, state):
        """ The feature value _is_ the cardinality of the extension of the represented concept"""
        ext = self.c.extension(cache, state)
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

    def complexity(self):
        # The complexity of a cardinality feature is the complexity of the underlying concept
        return self.c.size


class EmpiricalBinaryConcept(Feature):
    def __init__(self, feature):
        assert isinstance(feature, ConceptCardinalityFeature)
        self.c = feature.c
        self.hash = hash((self.__class__, self.c))

    def value(self, cache, state):
        """ The feature value _is_ whether the cardinality of the extension of the represented concept is 0 or 1 """
        ext = self.c.extension(cache, state)
        x = ext.count()
        assert x in (0, 1)  # By definition of "empirical binary concept"
        return bool(x)

    def diff(self, x, y):
        return compute_bool_feature_diff(x, y)

    def __repr__(self):
        return 'bool[{}]'.format(self.c)

    __str__ = __repr__

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c == other.c)

    def concept(self):
        return self.c

    def complexity(self):
        # The complexity of a binary feature is the complexity of the underlying concept
        return self.c.size

# NOT YET FULLY IMPLEMENTED:
#
# class IntegerVariableFeature(Feature):
#     """ A numeric feature that directly reflects the value of some integer variable of the problem """
#     def __init__(self, fun, point):
#         assert isinstance(fun, Function)
#         assert isinstance(point, tuple)
#         self.fun = fun
#         self.point = point
#         self.hash = hash((self.__class__, self.fun.symbol, point))
#
#     def value(self, cache, state):
#         """ The feature value _is_ the cardinality of the extension of the represented concept"""
#         raise RuntimeError("Unimplemented")
#         # ext = self.c.extension(cache, state)
#         # return ext.count()
#
#     def diff(self, x, y):
#         return compute_int_feature_diff(x, y)
#
#     def __repr__(self):
#         return 'int[{}]'.format(self.fun(*self.point))
#
#     __str__ = __repr__
#
#     def __hash__(self):
#         return self.hash
#
#     def __eq__(self, other):
#         return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
#                 self.fun == other.fun and self.point == other.point)
#


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

    def value(self, cache, state):
        """ The value of the feature is the min distance between any object in the extension of c1 and any object
            on the extension of c2, moving only along r-edges.
        """
        ext_c1 = self.c1.extension(cache, state)
        ext_c2 = self.c2.extension(cache, state)
        ext_r = self.r.extension(cache, state)
        return compute_min_distance(cache.uncompress(ext_c1, self.c1.ARITY),
                                    cache.uncompress(ext_r, self.r.ARITY),
                                    cache.uncompress(ext_c2, self.c2.ARITY))

    def diff(self, x, y):
        return compute_int_feature_diff(x, y)

    def __repr__(self):
        return 'min-distance[{}, {}, {}]'.format(self.c1, self.r, self.c2)

    __str__ = __repr__

    def complexity(self):
        return self.c1.size + self.r.size + self.c2.size + 1


class NullaryAtomFeature(Feature):
    def __init__(self, atom):
        assert isinstance(atom, NullaryAtom)
        self.atom = atom
        self.hash = hash((self.__class__, self.atom))

    def value(self, cache, state):
        """ The feature evaluates to true iff the nullary atom is true in the given state """
        return self.atom.extension(cache, state)

    def diff(self, x, y):
        return compute_bool_feature_diff(x, y)

    def __repr__(self):
        return 'bool[{}]'.format(self.atom)

    __str__ = __repr__

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.atom == other.atom)

    def complexity(self):
        return 1
