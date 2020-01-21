import copy

from tarski.fstrips import AddEffect, DelEffect, FunctionalEffect
from ..evaluators.simple import evaluate


def is_applicable(model, operator):
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
        model.setx(effect.lhs, evaluate(effect.rhs, model))

    else:
        raise RuntimeError(f'Don\'t know how to apply effect "{effect}"')
