import copy

from ..fstrips import AddEffect, DelEffect, FunctionalEffect, UniversalEffect
from ..evaluators.simple import evaluate
from ..fstrips.representation import substitute_expression
from ..syntax.transform.substitutions import enumerate_substitutions


def is_applicable(model, operator):
    """ Check whether a given (ground) operator is applicable in the given model (state). """
    return evaluate(operator.precondition, model)


def is_effect_applicable(model, effect):
    return evaluate(effect.condition, model)


def apply_effect(model, effect):
    """ Apply the given effect to the given model. """
    if not is_effect_applicable(model, effect):
        return

    if isinstance(effect, AddEffect):
        model.add(effect.atom.predicate, *effect.atom.subterms)

    elif isinstance(effect, DelEffect):
        model.discard(effect.atom.predicate, *effect.atom.subterms)

    elif isinstance(effect, FunctionalEffect):
        model.set(effect.lhs, evaluate(effect.rhs, model))

    elif isinstance(effect, UniversalEffect):
        for subst in enumerate_substitutions(effect.variables):
            for eff in effect.effects:
                apply_effect(model, substitute_expression(eff, subst))

    else:
        raise RuntimeError(f'Don\'t know how to apply effect "{effect}"')


def progress(state, operator):
    """ Returns the progression of the given state along the effects of the given operator.
    Note that this method does not check that the operator is applicable.
    """
    # TODO This is unnecessarily expensive, but a simple copy wouldn't work either.
    #      If/when we transition towards a C++-backed model implementation, this should be improved.
    sprime = copy.deepcopy(state)

    # Let's push to the beginning the delete effect, to ensure add-after-delete semantics
    effects = sorted(operator.effects, key=lambda e: 0 if isinstance(e, DelEffect) else 1)
    for eff in effects:
        apply_effect(sprime, eff)
    return sprime
