import logging
from collections import deque

from .model import ForwardSearchModel


class BreadthFirstSearch:
    """ Apply Breadth-First search to a FSTRIPS problem """
    def __init__(self, model: ForwardSearchModel, max_expansions=-1):
        self.model = model
        self.max_expansions = max_expansions

    def run(self):
        return self.search(self.model.init())

    def search(self, s0):
        # create obj to track state space
        space = SearchSpace()

        iteration = 0
        num_goals_found = 0

        open_ = deque()  # fifo-queue storing the nodes which are next to explore
        closed = set()

        open_.append(make_root_node(s0))

        node_id = 0
        while open_:
            iteration += 1
            # logging.debug("brfs: Iteration {}, #unexplored={}".format(iteration, len(open_)))

            node = open_.popleft()
            is_goal = self.model.is_goal(node.state)

            space.expand(node)

            # we manage the closed list here to allow the parents update
            if node.state in closed:
                continue

            closed.add(node.state)

            node_id += 1

            # exploring the node or if it is a goal node extracting the plan
            if is_goal:
                num_goals_found += 1
                logging.info("Goal found after {} expansions. Number of goal states found: {}".format(
                    node_id, num_goals_found))

            if 0 <= self.max_expansions <= node_id:
                logging.info("Max. expansions reached. # expanded: {}, # goals: {}".format(node_id, num_goals_found))
                return space

            for operator, successor_state in self.model.successors(node.state):
                open_.append(make_child_node(node, operator, successor_state))

        logging.info("Search space exhausted. # expanded: {}, # goals: {}".format(node_id, num_goals_found))
        space.complete = True
        return space


class SearchNode:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class SearchSpace:
    """ A representation of a search space / transition system corresponding to some planning problem """
    def __init__(self):
        self.nodes = set()
        self.last_node_id = 0
        self.complete = False  # Whether the state space contains all states reachable from the initial state

    def expand(self, node: SearchNode):
        self.nodes.add(node)


def make_root_node(state):
    """ Construct the initial root node without parent nor action """
    return SearchNode(state, None, None)


def make_child_node(parent_node, action, state):
    """ Construct an child search node """
    return SearchNode(state, parent_node, action)
