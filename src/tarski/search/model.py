
from ..evaluators.simple import evaluate


class SearchModel:
    def init(self):
        raise NotImplementedError()

    def successors(self, state):
        raise NotImplementedError()

    def is_goal(self, state):
        raise NotImplementedError()


class ForwardSearchModel(SearchModel):

    def __init__(self, problem):
        self.problem = problem

    def init(self):
        return self.problem.init

    def successors(self, state):
        # TODO We would need either to have the ground actions or to ground on-the-fly here
        raise NotImplementedError()

    def is_goal(self, state):
        state.evaluator = evaluate  # TODO This is a bit hacky
        return state[self.problem.goal]  # This triggers the logical interpretation of the goal formula
