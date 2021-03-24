import copy

from ..fstrips import AddEffect, DelEffect, FunctionalEffect, UniversalEffect
from ..evaluators.simple import evaluate
from ..fstrips.representation import substitute_expression
from ..syntax.transform.substitutions import enumerate_substitutions


def is_applicable(model, operator):
    """ Check whether a given (ground) operator is applicable in the given model (state). """
    return evaluate(operator.precondition, model)


def apply(model, operator):
    result = copy.deepcopy(model)
    for eff in operator.effects:
        apply_effect(result, eff)
    return result


def is_effect_applicable(model, effect):
    return evaluate(effect.condition, model)


def apply_effect(model, effect):
    """ Apply the given effect to the given model. """
    if not is_effect_applicable(model, effect):
        return

    if isinstance(effect, AddEffect):
        model.add(effect.atom.predicate, *effect.atom.subterms)

    elif isinstance(effect, DelEffect):
        model.remove(effect.atom.predicate, *effect.atom.subterms)

    elif isinstance(effect, FunctionalEffect):
        model.set(effect.lhs, evaluate(effect.rhs, model))

    elif isinstance(effect, UniversalEffect):
        for subst in enumerate_substitutions(effect.variables):
            for eff in effect.effects:
                apply_effect(model, substitute_expression(eff, subst))

    else:
        raise RuntimeError(f'Don\'t know how to apply effect "{effect}"')
