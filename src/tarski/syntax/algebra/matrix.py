import numpy as np

from ...syntax import Term, Constant
from ...syntax.sorts import Sort
from ... import errors as err


class Matrix(Term):
    def __init__(self, arraylike, sort: Sort):
        self.matrix = np.array(arraylike, dtype=np.dtype(object))
        self._sort = sort
        # verify and cast
        N, M = self.matrix.shape
        for i in range(N):
            for j in range(M):
                m_ij = self.matrix[i, j]
                if isinstance(m_ij, Term):
                    if m_ij.sort != sort:
                        raise err.SyntacticError("Matrix: all \
                        entries need to be of sort '{}', \
                        entry ({},{}) is '{}'".format(sort.name, i, j, m_ij.sort.name))
                else:
                    self.matrix[i, j] = Constant(sort.cast(m_ij), sort)

    @property
    def shape(self):
        return self.matrix.shape

    @property
    def language(self):
        return self.sort.language

    @property
    def sort(self):
        return self._sort

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __getitem__(self, arg):
        i, j = arg
        return self.matrix[i, j]

    def __str__(self):
        return '{}'.format(self.matrix)

    __repr__ = __str__

    def hash(self):
        N, M = self.matrix.shape
        syms = []
        for i in range(N):
            for j in range(M):
                syms += [self.matrix[i, j]]
        return hash(tuple(syms) + self.matrix.shape)

    def is_syntactically_equal(self, other):
        if self.__class__ is not other.__class__ or self.matrix.shape != other.matrix.shape:
            return False
        N, M = self.matrix.shape
        for i in range(N):
            for j in range(M):
                if not self.matrix[i, j].is_syntactically_equal(other.matrix[i, j]):
                    return False
        return True
