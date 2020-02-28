"""
    Elimination of first-order universal and existential quantifiers.
"""
import copy

from .substitutions import enumerate_substitutions
from ..formulas import Tautology
from ..transform import term_substitution


def expand_universal_effect(effect):
    """ Expands the given effect, if universal, in place. """
    from ...fstrips import UniversalEffect
    if not isinstance(effect, UniversalEffect):
        return [effect]

    assert isinstance(effect.condition, Tautology)  # TODO Lift this restriction
    expanded = []
    for subst in enumerate_substitutions(effect.variables):
        for sub in effect.effects:
            expanded.append(term_substitution(sub, subst))
    return expanded


def compile_universal_effects_away(problem, inplace=False):
    processed = copy.deepcopy(problem) if not inplace else problem

    for _, action in processed.actions.items():
        expanded = []
        for eff in action.effects:
            expanded += expand_universal_effect(eff)
        action.effects = expanded
    return processed

