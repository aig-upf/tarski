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
    assert isinstance(rhs, Term)  # this should not happen
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


def all_unique_nodes(expression, include_only=None):
    """ Return all nodes in the AST of the given expression, formula or term.
    If a Boolean function `include_only` is provided, only those nodes that satisfy the function are returned.
    The method returns only one copy of each node, under syntactic equivalence. """
    include_only = include_only if include_only is not None else lambda x: True
    nodes = set()

    def visit(expr):
        if isinstance(expr, Variable):
            t_ref = symref(expr)
            if t_ref not in self.quantified_vars:
                self._free_variables.add(t_ref)
        elif isinstance(expr, CompoundFormula):
            _ = [self.visit(f) for f in expr.subformulas]

        elif isinstance(expr, QuantifiedFormula):
            _ = [self.quantified_vars.add(symref(x)) for x in expr.variables]
            self.visit(expr.formula)
            _ = [self.quantified_vars.remove(symref(x)) for x in expr.variables]

        elif isinstance(expr, (Atom, CompoundTerm)):
            _ = [self.visit(f) for f in expr.subterms]



