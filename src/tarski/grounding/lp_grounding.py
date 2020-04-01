"""
 Classes and methods related to the Logic-Program based grounding  strategy of planning problems.
"""
from ..utils.command import silentremove
from ..grounding.ops import approximate_symbol_fluency
from ..reachability import create_reachability_lp, run_clingo, parse_model
from ..reachability.asp import GOAL
from .errors import ReachabilityLPUnsolvable
from ..util import SymbolIndex
from .common import StateVariableLite


class LPGroundingStrategy:
    """ An LP problem grounding grounds actions and state variables of a lifted Tarski problem by creating a relaxed
    reachability logic program, solving it with an ASP solver, and parsing the result.
    The type of LP created depends on the value of `ground_actions`. If true, it will include atoms for obtaining
    the parameter groundings of all reachable ground actions; if false, it will not, which should result in a smaller
    and cheaper logic program.
    """
    def __init__(self, problem, ground_actions=True, include_variable_inequalities=False):
        self.problem = problem
        self.do_ground_actions = ground_actions
        self.include_variable_inequalities = include_variable_inequalities
        self.model = None  # We'll cache the solution of the LP here
        self.fluent_symbols, self.static_symbols = approximate_symbol_fluency(problem)

    def ground_state_variables(self):
        """ Create and index all state variables of the problem by exhaustively grounding all predicate and function
        symbols that are considered to be fluent with respect to the problem constants. Thus, if the problem has one
        fluent predicate "p" and one static predicate "q", and constants "a", "b", "c", the result of this operation
        will be the state variables "p(a)", "p(b)" and "p(c)".
        """
        model = self._solve_lp()

        variables = SymbolIndex()
        for symbol in self.fluent_symbols:
            lang = symbol.language
            key = 'atom_' + symbol.name
            if key in model:  # in case there is no reachable ground state variable from that fluent symbol
                for binding in model[key]:
                    binding_with_constants = tuple(lang.get(c) for c in binding)
                    variables.add(StateVariableLite(symbol, binding_with_constants))

        return variables

    def ground_actions(self):
        """  Return a dictionary mapping each action schema of the problem to the set of parameter groundings that
        make that schema a reachable ground action. """
        if not self.do_ground_actions:
            raise RuntimeError('Cannot retrieve set of ground actions from LPGroundingStrategy '
                               'configured with ground_actions=False')
        model = self._solve_lp()
        # This will take care of the case where there is not ground action from some schema
        groundings = dict()
        for k in self.problem.actions.keys():
            key = "action_" + k
            groundings[k] = model[key] if key in model else set()
        return groundings

    def iterate_over_schema_groundings(self, schema_name: str):
        """  Iterate over all reachable parameter groundings of the given action schema. """
        model = self._solve_lp()
        return (x for x in model[schema_name]) if schema_name in model else []

    def _solve_lp(self):
        if self.model is None:
            lp, tr = create_reachability_lp(self.problem, self.do_ground_actions, self.include_variable_inequalities)
            model_filename, theory_filename = run_clingo(lp)
            self.model = parse_model(model_filename, tr)

            # Remove the input and output files for Gringo
            silentremove(model_filename)
            silentremove(theory_filename)

            if len(self.model[GOAL]) != 1:
                raise ReachabilityLPUnsolvable()
        return self.model

    def __str__(self):
        return 'LPGroundingStrategy["{}"]'.format(self.problem.name)

    __repr__ = __str__


def compute_action_groundings(problem, include_variable_inequalities=False):
    grounding = LPGroundingStrategy(problem, True, include_variable_inequalities)
    return grounding.ground_actions()
