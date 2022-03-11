"""
    SAS+ Modeling helper
"""
from typing import List

from tarski.syntax import Term, land, symref


def make_domain(dom: List[Term], close: bool = False):
    """
    Prepares domain from list of terms
    :param dom:
    :param close: Closes the list of terms in `dom` with ``all false''/``none of the above''
    :return: list of values wrapped with `symref` plus the logical and of v = 0 for v in `dom`
    """
    values = [symref(v) for v in dom]
    closure_formula = land(*[v == 0 for v in dom])
    values += [symref(closure_formula)]
    return values
