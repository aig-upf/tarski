"""

"""
from enum import Enum

from .concepts import Concept, Role, NullaryAtom
from ..utils.algorithms import compute_min_distance
from ..utils.hashing import consistent_hash


class FeatureValueChange(Enum):
    ADD = 1
    DEL = 2
    INC = 3
    DEC = 4
    NIL = 5
    INC_OR_NIL = 6
    ADD_OR_NIL = 7


class Feature:
    def denotation(self, model):
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


def are_feature_changes_analogous(x, y):
    return x == y or \
           (x == FeatureValueChange.DEL and y == FeatureValueChange.DEC) or \
           (x == FeatureValueChange.DEC and y == FeatureValueChange.DEL) or \
           (x == FeatureValueChange.ADD and y == FeatureValueChange.INC) or \
           (x == FeatureValueChange.INC and y == FeatureValueChange.ADD)


class ConceptCardinalityFeature(Feature):
    """ A numeric feature that reflects the cardinality of a set of objects defined by a concept """
    def __init__(self, c):
        assert isinstance(c, Concept)
        self.c = c
        self.hash = consistent_hash((self.__class__, self.c))

    def denotation(self, model):
        return model.compressed_denotation(self.c).count()

    def diff(self, x, y):
        return compute_int_feature_diff(x, y)

    def __repr__(self):
        return 'Num[{}]'.format(self.c)

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
        assert isinstance(feature, (ConceptCardinalityFeature, EmpiricalBinaryConcept))
        self.c = feature.c
        self.hash = consistent_hash((self.__class__, self.c))

    def denotation(self, model):
        val = model.compressed_denotation(self.c).count()
        assert val in (0, 1)  # By definition of "empirical binary concept"
        return bool(val)

    def diff(self, x, y):
        return compute_bool_feature_diff(x, y)

    def __repr__(self):
        return 'Bool[{}]'.format(self.c)

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
#         self.hash = consistent_hash((self.__class__, self.fun.symbol, point))
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
        self.hash = consistent_hash((self.__class__, self.c1, self.r, self.c2))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c1 == other.c1 and self.r == other.r and self.c2 == other.c2)

    def denotation(self, model):
        """ The value of the feature is the min distance between any object in the extension of c1 and any object
            on the extension of c2, moving only along r-edges.
        """
        ext_c1 = model.uncompressed_denotation(self.c1)
        ext_c2 = model.uncompressed_denotation(self.c2)
        ext_r = model.uncompressed_denotation(self.r)

        # (Debugging)
        # ec1 = sorted(cache.universe.value(x) for x in cache.uncompress(ext_c1, self.c1.ARITY))
        # ec2 = sorted(cache.universe.value(x) for x in cache.uncompress(ext_c2, self.c2.ARITY))
        # er1 = sorted((cache.universe.value(x), cache.universe.va
        # for x, y in cache.uncompress(ext_r, self.r.ARITY))

        return compute_min_distance(ext_c1, ext_r, ext_c2)

    def diff(self, x, y):
        return compute_int_feature_diff(x, y)

    def __repr__(self):
        return 'Dist[{}, {}, {}]'.format(self.c1, self.r, self.c2)

    __str__ = __repr__

    def complexity(self):
        return self.c1.size + self.r.size + self.c2.size + 1


class NullaryAtomFeature(Feature):
    def __init__(self, atom):
        assert isinstance(atom, NullaryAtom)
        self.atom = atom
        self.hash = consistent_hash((self.__class__, self.atom))

    def denotation(self, model):
        """ The feature evaluates to true iff the nullary atom is true in the given state """
        # return self.atom.extension(cache, state)
        return model.primitive_denotation(self.atom)

    def diff(self, x, y):
        return compute_bool_feature_diff(x, y)

    def __repr__(self):
        return 'Atom[{}]'.format(self.atom)

    __str__ = __repr__

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.atom == other.atom)

    def complexity(self):
        return 1
