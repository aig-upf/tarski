
from typing import Set, Union, Tuple, Optional

from .problem import Problem
from ..syntax import Formula, CompoundTerm, Atom, CompoundFormula, is_and, is_neg
from ..syntax.ops import collect_unique_nodes, flatten
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
    return isinstance(phi, Atom) or (is_neg(phi) and is_literal(phi.subformulas[0]))


def is_conjunction_of_literals(phi: Formula):
    """
    Return whether the given formula is a conjunction of literals, i.e. of atoms or negations of atoms.
    """
    f = flatten(phi)
    return isinstance(f, Atom) or \
        (isinstance(f, CompoundFormula) and all(is_literal(sub) for sub in f.subformulas))


def collect_literals_from_conjunction(phi: Formula) -> Optional[Set[Tuple[Atom, bool]]]:
    """ Return a list of all literals in phi, if is_conjunction_of_literals(phi), or None otherwise.
    The returned list consists of one tuple (a, p) for each literal in the conjunction phi, where a is the literal atom
    and p its polarity (i.e. True if positive, False if negative)
    """
    literals = set()  # type: Set[Tuple[Atom, bool]]
    if _collect_literals_from_conjunction(phi, literals):
        return literals
    return None


def _collect_literals_from_conjunction(f, literals: Set[Tuple[Atom, bool]]):
    if isinstance(f, Atom):
        literals.add((f, True))
    elif is_neg(f) and isinstance(f.subformulas[0], Atom):
        literals.add((f.subformulas[0], False))
    elif is_and(f):
        for sub in f.subformulas:
            if not _collect_literals_from_conjunction(sub, literals):
                return False
    else:
        return False
    return True


def is_function_free(phi: Formula):
    """
    Return whether the given formula is function-free, that is, has no function symbols other than constant symbols.
    """
    return len(collect_unique_nodes(phi, lambda x: isinstance(x, CompoundTerm))) == 0
