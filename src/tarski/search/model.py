import copy

from .applicability import is_applicable, apply_effect
from ..evaluators.simple import evaluate


class SearchModel:
    """ A base class for search models, including the usual the textbook methods :-) """
    def init(self):
        raise NotImplementedError()

    def applicable(self, state):
        raise NotImplementedError()

    def successors(self, state):
        raise NotImplementedError()

    def is_goal(self, state):
        raise NotImplementedError()


def progress(state, operator):
    """ Returns the progression of the given state along the effects of the given operator.
    Note that this method does not check that the operator is applicable.
    """
    sprime = copy.deepcopy(state)
    for eff in operator.effects:
        apply_effect(sprime, eff)
    return sprime


class GroundForwardSearchModel:
    """ A standard forward search model that operates on a given set of ground operators, obtained through
    reachability analysis or otherwise.
    Note that this is not a particularly performant search model, but rather intended for illustrative purposes
    and for use in low-performance environments.
    """

    def __init__(self, problem, operators):
        self.problem = problem
        self.operators = operators

    def init(self):
        return self.problem.init

    def applicable(self, state):
        """ Return a generator with all ground operators that are applicable in the given state. """
        return (op for op in self.operators if is_applicable(state, op))

    def successors(self, state):
        """ Return a generator with all tuples (op, successor) for successors of the given state. """
        return ((op, progress(state, op)) for op in self.applicable(state))

    def is_goal(self, state):
        """ Return whether the given state is a goal"""
        return evaluate(self.problem.goal, state)  # Just interpret the goal formula on the state
