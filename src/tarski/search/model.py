
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
            self.fluents = self.compute_fluents()
            self.compute_match_tree()

    def compute_fluents(self):
        """Compute all of the ground fluents (mentioned in any action, init, goal)"""
        fluents = set()
        for op in self.operators:
            fluents |= set(op.precondition.subformulas)
            fluents |= set([e.atom for e in op.effects])

        fluents |= set(self.problem.goal.subformulas)
        fluents |= set(self.problem.init.as_atoms())

        return fluents

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

        # Finally, confirm the goal is STRIPS
        return _strips_condition(self.problem.goal)

    def compute_match_tree(self):
        """ Compute the match tree for this search model """

        # Computes the score of the fluent and partitions the operators accordingly
        def _score_and_split(ops, fluent):
            split = {True: [], False: []}
            for op in ops:
                split[fluent in op.precondition.subformulas].append(op)
            tie_break = {True: 0, False: 0.5}
            assert len(split[True]) + len(split[False]) == len(ops)
            return (abs(len(split[True]) - len(split[False])) + tie_break[len(split[True]) > 0], split)

        # Finds the best fluent based on how well it splits the remaining operators
        def _best_fluent(ops, decisions):
            best_fluent = None
            best_score = 999999
            best_split = None
            for f in self.fluents:
                if f not in decisions:
                    score, split = _score_and_split(ops, f)
                    if score < best_score:
                        best_fluent = f
                        best_score = score
                        best_split = split
            assert best_fluent is not None
            return (best_fluent, best_split)

        # Recursively computes the match tree
        def _match_tree(ops, decisions):

            node = {
                'fluent'    : None,
                'applicable': set(),
                'musthold'  : None,
                'dontcare'  : None
            }

            if len(ops) == 0:
                return node

            # Find the ops that are already applicable given the decisions
            not_applicable = set()
            for op in ops:
                if all([f in decisions for f in op.precondition.subformulas]):
                    node['applicable'].add(op)
                else:
                    not_applicable.add(op)

            if len(not_applicable) == 0:
                return node

            fluent, split = _best_fluent(not_applicable, decisions)

            node['fluent'] = fluent
            node['musthold'] = _match_tree(split[True], decisions | {fluent})
            node['dontcare'] = _match_tree(split[False], decisions | {fluent})

            return node

        self._match_tree = _match_tree(self.operators, set())

    def _match_tree_applicable(self, state):
        """Compute the set of applicable operators given the state."""

        def _compute_match_tree(node, state, applicable):
            if node is None:
                return
            applicable |= node['applicable']
            if node['fluent'] in state:
                _compute_match_tree(node['musthold'], state, applicable)
            _compute_match_tree(node['dontcare'], state, applicable)

        applicable = set()
        _compute_match_tree(self._match_tree, set(state.as_atoms()), applicable)
        return applicable

    def init(self):
        return self.problem.init

    def applicable(self, state):
        """ Return a generator with all ground operators that are applicable in the given state. """
        if self._match_tree:
            return self._match_tree_applicable(state)
        else:
            return (op for op in self.operators if is_applicable(state, op))

    def successors(self, state):
        """ Return a generator with all tuples (op, successor) for successors of the given state. """
        return ((op, progress(state, op)) for op in self.applicable(state))

    def is_goal(self, state):
        """ Return whether the given state is a goal"""
        return evaluate(self.problem.goal, state)  # Just interpret the goal formula on the state
