"""
    Elimination of first-order universal and existential quantifiers.
"""
import copy

from .substitutions import enumerate_substitutions
from ..formulas import Tautology
from ..transform import term_substitution


def expand_universal_effect(effect, do_copy=False):
    from ...fstrips import UniversalEffect
    if not isinstance(effect, UniversalEffect):
        return [copy.deepcopy(effect)] if do_copy else [effect]

    assert isinstance(effect.condition, Tautology)  # TODO Lift this restriction
    expanded = []
    for subst in enumerate_substitutions(effect.variables):
        for sub in effect.effects:
            expanded.append(term_substitution(sub, subst))
    return expanded

