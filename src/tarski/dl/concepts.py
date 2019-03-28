"""

"""
from ..syntax import Predicate, Function, Sort
from ..utils.algorithms import transitive_closure
from ..utils.hashing import consistent_hash
from .errors import ArityDLMismatch


class NullaryAtom:
    ARITY = 0

    def __init__(self, predicate):
        assert isinstance(predicate, Predicate)
        _check_arity("nullary atom", 0, predicate)
        self.name = predicate.symbol
        self.depth = 0
        self.hash = consistent_hash((self.__class__, self.name))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.name == other.name)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__

    def denotation(self, model):
        return model.primitive_denotation(self)


class GoalNullaryAtom(NullaryAtom):
    def __repr__(self):
        return "{}_g".format(self.name)

    __str__ = __repr__


class Concept:
    ARITY = 1

    def __init__(self, sort, size):
        assert isinstance(sort, str)
        self.sort = sort
        self.size = size

    def denotation(self, model):
        raise NotImplementedError()

    def flatten(self):
        raise NotImplementedError()


class Role:
    ARITY = 2

    def __init__(self, sort, size):
        assert len(sort) == self.ARITY
        self.sort = sort
        self.size = size

    def denotation(self, model):
        raise NotImplementedError()

    def flatten(self):
        raise NotImplementedError()


class UniversalConcept(Concept):
    def __init__(self, universal_sort):
        Concept.__init__(self, universal_sort, 0)
        self.hash = consistent_hash((self.__class__, ))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.__class__ is other.__class__

    def denotation(self, model):
        return model.compressed(model.primitive_denotation(self), self.ARITY)

    def __repr__(self):
        return '<universe>'

    __str__ = __repr__

    def flatten(self):
        return [self]


class EmptyConcept(Concept):
    def __init__(self, universal_sort):
        Concept.__init__(self, universal_sort, 0)
        self.hash = consistent_hash((self.__class__, ))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.__class__ is other.__class__

    def denotation(self, model):
        return model.compressed(model.primitive_denotation(self), self.ARITY)

    def __repr__(self):
        return '<empty>'

    __str__ = __repr__

    def flatten(self):
        return [self]


class NominalConcept(Concept):
    def __init__(self, name, sort):
        Concept.__init__(self, sort.name, 1)
        self.name = name
        self.hash = consistent_hash((self.__class__, self.name))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.name == other.name)

    def denotation(self, model):
        return model.compressed(model.primitive_denotation(self), self.ARITY)

    def __repr__(self):
        return "Nominal({})".format(self.name)

    __str__ = __repr__

    def flatten(self):
        return [self]


class PrimitiveConcept(Concept):
    def __init__(self, predicate):
        assert isinstance(predicate, (Predicate, Function, Sort))

        if isinstance(predicate, (Predicate, Function)):
            _check_arity("concept", 1, predicate)
            Concept.__init__(self, predicate.sort[0].name, 1)
            self.name = predicate.symbol  # This is a bit aggressive, but we assume that uniqueness of names

        else:
            Concept.__init__(self, predicate.name, 1)
            self.name = predicate.name
        self.hash = consistent_hash((self.__class__, self.name))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.name == other.name)

    def denotation(self, model):
        return model.compressed(model.primitive_denotation(self), self.ARITY)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__

    def flatten(self):
        return [self]


class GoalConcept(PrimitiveConcept):
    def __repr__(self):
        return "{}_g".format(self.name)

    __str__ = __repr__


class NotConcept(Concept):
    def __init__(self, c, universal_sort):
        assert isinstance(c, Concept)
        Concept.__init__(self, universal_sort.name, 1 + c.size)
        self.c = c
        self.hash = consistent_hash((self.__class__, self.c))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c == other.c)

    def denotation(self, model):
        return ~model.compressed_denotation(self.c)

    def __repr__(self):
        return 'Not({})'.format(self.c)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.c.flatten()


class AndConcept(Concept):
    def __init__(self, c1, c2, sort):
        assert isinstance(c1, Concept)
        assert isinstance(c2, Concept)
        Concept.__init__(self, sort, 1 + c1.size + c2.size)
        self.c1 = c1
        self.c2 = c2
        self.hash = consistent_hash((self.__class__, self.c1, self.c2))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c1 == other.c1 and
                self.c2 == other.c2)

    def denotation(self, model):
        ext_c1 = model.compressed_denotation(self.c1)
        ext_c2 = model.compressed_denotation(self.c2)
        return ext_c1 & ext_c2

    def __repr__(self):
        return 'And({},{})'.format(self.c1, self.c2)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.c1.flatten() + self.c2.flatten()


class OrConcept(Concept):
    def __init__(self, c1, c2, sort):
        assert isinstance(c1, Concept)
        assert isinstance(c2, Concept)
        Concept.__init__(self, sort, 1 + c1.size + c2.size)
        self.c1 = c1
        self.c2 = c2
        self.hash = consistent_hash((self.__class__, self.c1, self.c2))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c1 == other.c1 and
                self.c2 == other.c2)

    def denotation(self, model):
        ext_c1 = model.compressed_denotation(self.c1)
        ext_c2 = model.compressed_denotation(self.c2)
        return ext_c1 | ext_c2

    def __repr__(self):
        return 'Or({},{})'.format(self.c1, self.c2)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.c1.flatten() + self.c2.flatten()


class ExistsConcept(Concept):
    def __init__(self, r, c):
        assert isinstance(r, Role)
        assert isinstance(c, Concept)
        # The sort of an exists-concept is that of the first element of the relation
        Concept.__init__(self, r.sort[0], 1 + r.size + c.size)
        self.r = r
        self.c = c
        self.hash = consistent_hash((self.__class__, self.r, self.c))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c == other.c and
                self.r == other.r)

    def denotation(self, model):
        ext_c = model.uncompressed_denotation(self.c)
        ext_r = model.uncompressed_denotation(self.r)
        # result = [x for x in objects if [z for (y, z) in ext_r if y == x and z in ext_c]]
        result = set(x for x, y in ext_r if y in ext_c)
        return model.compressed(result, self.ARITY)

    def __repr__(self):
        return 'Exists({},{})'.format(self.r, self.c)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.r.flatten() + self.c.flatten()


class ForallConcept(Concept):
    def __init__(self, r, c):
        assert isinstance(r, Role)
        assert isinstance(c, Concept)
        # The sort of a forall-concept is that of the first element of the relation # TODO Check this
        Concept.__init__(self, r.sort[0], 1 + r.size + c.size)
        self.r = r
        self.c = c
        self.hash = consistent_hash((self.__class__, self.r, self.c))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c == other.c and
                self.r == other.r)

    def denotation(self, model):
        universe = model.universe()
        ext_c = model.uncompressed_denotation(self.c)
        ext_r = model.uncompressed_denotation(self.r)
        result = set()
        for x in universe:  # TODO COULD BE OPTIMIZED, E.G. IF R HAS EMPTY EXTENSION, ETC.
            ys = ext_c.union(y for y in universe if (x, y) not in ext_r)
            if len(universe) == len(ys):  # No need to compare the sets, as objects has max possible length
                result.add(x)
        return model.compressed(result, self.ARITY)

    def __repr__(self):
        return 'Forall({},{})'.format(self.r, self.c)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.r.flatten() + self.c.flatten()


class EqualConcept(Concept):
    def __init__(self, r1, r2, sort):
        assert isinstance(r1, Role)
        assert isinstance(r2, Role)
        Concept.__init__(self, sort, 1 + r1.size + r2.size)
        self.r1 = r1
        self.r2 = r2
        self.hash = consistent_hash((self.__class__, self.r1, self.r2))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.r1 == other.r1 and
                self.r2 == other.r2)

    def denotation(self, model):
        universe = model.universe()
        ext_r1 = model.uncompressed_denotation(self.r1)
        ext_r2 = model.uncompressed_denotation(self.r2)
        result = set()
        for x in universe:
            left = set(z for (y, z) in ext_r1 if y == x)
            right = set(z for (y, z) in ext_r2 if y == x)
            if left == right:
                result.add(x)
        return model.compressed(result, self.ARITY)

    def __repr__(self):
        return 'Equal({},{})'.format(self.r1, self.r2)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.r1.flatten() + self.r2.flatten()


class PrimitiveRole(Role):
    def __init__(self, predicate):
        assert isinstance(predicate, (Predicate, Function))
        _check_arity("role", 2, predicate)

        super().__init__([s.name for s in predicate.sort], 1)
        self.name = predicate.symbol

        # This is a bit aggressive, but we assume that predicate names are unique
        self.hash = consistent_hash((self.__class__, self.name))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.name == other.name)

    def denotation(self, model):
        return model.compressed(model.primitive_denotation(self), self.ARITY)

    def __repr__(self):
        return '{}'.format(self.name)

    __str__ = __repr__

    def flatten(self):
        return [self]


class GoalRole(PrimitiveRole):
    def __repr__(self):
        return "{}_g".format(self.name)

    __str__ = __repr__


class InverseRole(Role):
    def __init__(self, r):
        assert isinstance(r, Role)
        s1, s2 = r.sort
        super().__init__([s2, s1], 1 + r.size)
        self.r = r
        self.hash = consistent_hash((self.__class__, self.r))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.r == other.r)

    def denotation(self, model):
        ext_r = model.uncompressed_denotation(self.r)
        result = set((y, x) for (x, y) in ext_r)
        return model.compressed(result, self.ARITY)

    def __repr__(self):
        return 'Inverse({})'.format(self.r)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.r.flatten()


class StarRole(Role):
    def __init__(self, r):
        assert isinstance(r, Role)
        Role.__init__(self, r.sort, 1 + r.size)
        self.r = r
        self.hash = consistent_hash((self.__class__, self.r))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.r == other.r)

    def denotation(self, model):
        ext_r = model.uncompressed_denotation(self.r)
        result = set(transitive_closure(ext_r))
        return model.compressed(result, self.ARITY)

    def __repr__(self):
        return 'Star({})'.format(self.r)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.r.flatten()


class CompositionRole(Role):
    def __init__(self, r1, r2):
        assert isinstance(r1, Role)
        assert isinstance(r2, Role)
        Role.__init__(self, [r1.sort[0], r2.sort[1]], 1 + r1.size + r2.size)
        self.r1 = r1
        self.r2 = r2
        self.hash = consistent_hash((self.__class__, self.r1, self.r2))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.r1 == other.r1 and
                self.r2 == other.r2)

    def denotation(self, model):
        ext_r1 = model.uncompressed_denotation(self.r1)
        ext_r2 = model.uncompressed_denotation(self.r2)
        result = set()
        for a, b in ext_r1:
            for x, y in ext_r2:
                if b == x:
                    result.add((a, y))
                    break  # i.e. break the inner loop
        # for (x, u) in ext_r1:
        #     result.extend((x, z) for (y, z) in ext_r2 if u == y)
        return model.compressed(result, self.ARITY)

    def __repr__(self):
        return 'Composition({},{})'.format(self.r1, self.r2)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.r1.flatten() + self.r2.flatten()


class RestrictRole(Role):
    def __init__(self, r, c):
        assert isinstance(r, Role)
        assert isinstance(c, Concept)
        Role.__init__(self, r.sort, 1 + r.size + c.size)
        self.r = r
        self.c = c
        self.hash = consistent_hash((self.__class__, self.r, self.c))

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return (hasattr(other, 'hash') and self.hash == other.hash and self.__class__ is other.__class__ and
                self.c == other.c and
                self.r == other.r)

    def denotation(self, model):
        ext_c = model.uncompressed_denotation(self.c)
        ext_r = model.uncompressed_denotation(self.r)
        result = set((x, y) for (x, y) in ext_r if y in ext_c)
        return model.compressed(result, self.ARITY)

    def __repr__(self):
        return 'Restrict({},{})'.format(self.r, self.c)

    __str__ = __repr__

    def flatten(self):
        return [self] + self.r.flatten() + self.c.flatten()


def _check_arity(term, expected_arity, predfun):
    if expected_arity != predfun.uniform_arity():
        raise ArityDLMismatch('Cannot create {} from predicate "{}"'.format(term, predfun))
