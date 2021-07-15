
from .operations import is_applicable, progress
from ..evaluators.simple import evaluate

from ..syntax.formulas import Atom, Connective

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


class GroundForwardSearchModel:
    """ A standard forward search model that operates on a given set of ground operators, obtained through
    reachability analysis or otherwise.
    Note that this is not a particularly performant search model, but rather intended for illustrative purposes
    and for use in low-performance environments.
    """

    def __init__(self, problem, operators):
        self.problem = problem
        self.operators = operators
        self.is_strips = self.check_strips()

        if self.is_strips:
            self.compute_match_tree()

    def check_strips(self):
        """Confirms if this operator is a STRIPS operator"""
        def _strips_condition(c):
            return isinstance(c, Atom) or \
                (c.connective == Connective.And and \
                 all([isinstance(p, Atom) for p in c.subformulas]))

        # Confirm the operators are all STRIPS
        for op in self.operators:
            if not _strips_condition(op.precondition):
                return False

        # Confirm the goal is STRIPS
        if not _strips_condition(self.problem.goal):
            return False

        return True

    def compute_match_tree(self):
        """ Compute the match tree for this search model """

        # 
        def _score_and_split(ops, fluent):
            split = {True: [], False: []}
            for op in ops:
                split[fluent in ops.precondition.subformulas].append(op)
            assert len(split[True]) + len(split[False]) == len(ops)
            return (abs(len(split[True]) - len(split[False])), split)

        def _best_fluent(ops, decisions):
            best_fluent = None
            best_score = 999999
            for f in self.problem.fluents:
                if f not in decisions:
                    score, split = _score_and_split(ops, f)
                    if score < best_score:
                        best_fluent = f
                        best_score = score
            assert best_fluent is not None
            return (best_fluent, split)

        def _match_tree(ops, decisions):
            pass

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
