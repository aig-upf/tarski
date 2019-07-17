import itertools

import numpy as np

from .visitors import CollectFreeVariables, CollectVariables
from .terms import Term, Constant
from .formulas import CompoundFormula, Connective


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
        assert False  # this should not happen
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


def free_variables(formula):
    visitor = CollectFreeVariables()
    visitor.visit(formula)
    return list(visitor.free_variables)


def all_variables(formula):
    visitor = CollectVariables()
    visitor.visit(formula)
    return list(visitor.variables)


def flatten(formula):
    """ Flatten the given formula recursively, if possible, by applying associativity of and/or connectives
    Thus, a formula like (a or (b or (c or d))) becomes (a or b or c or d)
    """
    if not isinstance(formula, CompoundFormula) or formula.connective not in (Connective.And, Connective.Or):
        return formula
    return CompoundFormula(formula.connective, _flatten(formula, formula.connective))


def _flatten(formula, parent_connective):
    """ Return a list with all AST nodes of the given formula recursively flattened, i.e. where compound formulas
    with the given connective have been flattened themselves.
    """
    if not isinstance(formula, CompoundFormula) or formula.connective != parent_connective:
        return formula,  # (returns a tuple)
    return tuple(itertools.chain.from_iterable(_flatten(sub, parent_connective) for sub in formula.subformulas))
