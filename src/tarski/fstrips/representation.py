
from typing import Union

from tarski.syntax import CompoundTerm, Atom, CompoundFormula, Connective
from tarski.syntax.ops import collect_unique_nodes, flatten
from .problem import Problem
from ..syntax import Formula
from .action import Action


def is_positive_normal_form_problem(problem: Problem):
    """
    A propositional planning task is positive if all its operators and its goal are positive.
    """
    raise NotImplementedError()


def is_positive_operator(action: Action):
    """
    An operator o is positive if pre(o) and all effect conditions in eff(o) are positive.
    """
    raise NotImplementedError()


def is_positive_formula(phi: Formula):
    """
    A logical formula is positive if no negation symbols appear in it.
    """
    raise NotImplementedError()


def transform_to_positive_normal_form(what: Union[Problem, Action]):
    """ """
    if isinstance(what, Problem):
        return transform_problem_to_positive_normal_form(what)
    elif isinstance(what, Action):
        return transform_operator_to_positive_normal_form(what)
    raise RuntimeError(f'Unable to transform to positive normal form object {what}')


def transform_problem_to_positive_normal_form(problem: Problem):
    """ """
    raise NotImplementedError()


def transform_operator_to_positive_normal_form(action: Action):
    """ """
    raise NotImplementedError()


def is_strips_operator(action: Action):
    """
    An operator o is a STRIPS operator if
    (1) pre(o) is a conjunction of state variables, and
    (2) eff(o) is a conflict-free conjunction of atomic effects.
    """
    raise NotImplementedError()


def is_strips_problem(problem: Problem):
    """
    A propositional planning task is a STRIPS planning task if all of its operators are STRIPS operators
    its goal is a conjunction of state variables.
    """
    raise NotImplementedError()


def transform_to_strips(what: Union[Problem, Action]):
    """ """
    if isinstance(what, Problem):
        return transform_problem_to_strips(what)
    elif isinstance(what, Action):
        return transform_operator_to_strips(what)
    raise RuntimeError(f'Unable to transform to positive normal form object {what}')


def transform_problem_to_strips(problem: Problem):
    """ """
    raise NotImplementedError()


def transform_operator_to_strips(action: Action):
    """ """
    raise NotImplementedError()


def is_literal(phi: Formula):
    """ Return true iff the given formula is a literal """
    return isinstance(phi, Atom) or \
        (isinstance(phi, CompoundFormula) and phi.connective == Connective.Not and is_literal(phi.subformulas[0]))


def is_conjunction_of_literals(phi: Formula):
    """
    Return whether the given formula is a conjunction of literals, i.e. of atoms or negations of atoms.
    """
    f = flatten(phi)
    return isinstance(f, Atom) or \
        (isinstance(f, CompoundFormula) and all(is_literal(sub) for sub in f.subformulas))


def is_function_free(phi: Formula):
    """
    Return whether the given formula is function-free, that is, has no function symbols other than constant symbols.
    """
    return len(collect_unique_nodes(phi, lambda x: isinstance(x, CompoundTerm))) == 0
