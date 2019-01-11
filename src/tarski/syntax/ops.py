from .terms import Term, Constant
import numpy as np
from tarski.syntax.algebra import Matrix

def cast_to_closest_common_ancestor(lhs, rhs):

    if isinstance(lhs, Term):
        if isinstance(rhs, np.ndarray):
            # lhs is scalar, rhs is matrix
            return lhs.language.matrix([[lhs]], lhs.sort), rhs
        if not isinstance(rhs, Term):
            rhs = Constant(lhs.sort.cast(rhs), lhs.sort)
        return lhs, rhs
    if isinstance(lhs, np.ndarray):
        # lhs is matrix
        if isinstance(rhs, Term):
            return lhs, rhs.language.matrix([[rhs]])
    if not isinstance(rhs, Term):
        assert False # this should not happen
    lhs = Constant(rhs.sort.cast(lhs), rhs.sort)

    return lhs, rhs


def infer_numeric_sort(value, language):
    # Note that this will only work in Python 3, which is fine.
    if isinstance(value, int):
        return language.Integer
    elif isinstance(value, float):
        return language.Real
    return None


def cast_to_number(rhs):
    assert isinstance(rhs, Constant)
    return rhs.symbol
