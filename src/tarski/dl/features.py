"""

"""
import sys
from enum import Enum

from .concepts import Concept, Role, NullaryAtom
from ..utils.algorithms import compute_min_distance
from ..utils.hashing import consistent_hash


class FeatureValueChange(Enum):
    INC = 1
    DEC = 2
    NIL = 3


class Feature:
    def denotation(self, model):
        raise NotImplementedError()

    def diff(self, x, y):
        return compute_feature_diff(x, y)

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


def compute_feature_diff(x, y):
    assert type(x) in (int, bool) and x >= 0
    assert type(y) in (int, bool) and y >= 0
    if x == y:
        return FeatureValueChange.NIL
    if x > y:
        return FeatureValueChange.DEC
    else:
        return FeatureValueChange.INC


class ConceptCardinalityFeature(Feature):
    """ A numeric feature that reflects the cardinality of a set of objects defined by a concept """
    def __init__(self, c):
        assert isinstance(c, Concept)
        self.c = c
        self.hash = consistent_hash((self.__class__, self.c))

    def denotation(self, model):
        return model.compressed_denotation(self.c).count()

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
        return model.compressed_denotation(self.c).count()

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

    def __repr__(self):
        return 'Dist[{};{};{}]'.format(self.c1, self.r, self.c2)

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
        return model.primitive_denotation(self.atom)

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


class ConditionalFeature(Feature):
    def __init__(self, condition, body):
        assert isinstance(condition, Feature)
        assert isinstance(body, Feature)
        self.condition = condition
        self.body = body
        self.hash = consistent_hash((self.__class__, condition, body))

    def denotation(self, model):
        """ The feature evaluates to self.value if self.condition is true, else evaluates to infinity """
        cd = self.condition.denotation(model)
        return self.body.denotation(model) if cd else sys.maxsize

    def __repr__(self):
        return "If{" + str(self.condition) + "}{" + str(self.body) + "}{Infty}"

    __str__ = __repr__

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.condition == other.condition and self.body == other.value)

    def complexity(self):
        return 1 + self.condition.complexity() + self.body.complexity()
