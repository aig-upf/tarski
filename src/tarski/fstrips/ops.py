
from .problem import Problem
from . import fstrips as fs


def collect_affected_symbols(problem: Problem):
    """ Return a set with all predicate and function symbols that are affected by some action effect, and hence
     can be considered fluent. """
    fluents = set()
    for action in problem.actions.values():
        _ = [collect_affected_symbols_in_effect(eff, fluents) for eff in action.effects]
    return fluents


def collect_affected_symbols_in_effect(effect, fluents: set):
    if isinstance(effect, (fs.AddEffect, fs.DelEffect)):
        fluents.add(effect.atom.symbol)
    elif isinstance(effect, fs.LiteralEffect):
        raise NotImplementedError()
    elif isinstance(effect, fs.FunctionalEffect):
        fluents.add(effect.lhs.symbol)
    elif isinstance(effect, fs.ChoiceEffect):
        fluents.add(effect.obj.symbol)
    elif isinstance(effect, fs.UniversalEffect):
        # Go recursively to the universally quantified effects
        _ = [collect_affected_symbols_in_effect(eff, fluents) for eff in effect.effects]

    else:
        raise RuntimeError(f'Effect "{effect}" of type "{type(effect)}" cannot be analysed')
