"""
 Classes and methods related to the Logic-Program based grounding  strategy of planning problems.
"""
from ..reachability import create_reachability_lp, run_clingo, parse_model
from ..reachability.asp import SOLVABLE
from .errors import ReachabilityLPUnsolvable
from ..util import IndexDictionary
from .common import StateVariableLite, approximate_symbol_fluency


class LPGroundingStrategy:
    """ An LP problem grounding grounds actions and state variables of a lifted Tarski problem by creating a relaxed
    reachability logic program, solving it with an ASP solver, and parsing the result.
    """
    def __init__(self, problem):
        self.problem = problem
        self.model = None  # We'll cache the solution of the LP here
        self.fluent_symbols, self.static_symbols = approximate_symbol_fluency(problem)

    def ground_state_variables(self):
        """ Create an index all state variables of the problem by exhaustively grounding all predicate and function
        symbols that are considered to be fluent with respect to the problem constants. Thus, if the problem has one
        fluent predicate "p" and one static predicate "q", and constants "a", "b", "c", the result of this operation
        will be the state variables "p(a)", "p(b)" and "p(c)".
        """
        variables = IndexDictionary()
        model = self._solve_lp()

        for symbol in self.fluent_symbols:
            lang = symbol.language
            for binding in model[symbol.symbol]:
                binding_with_constants = tuple(lang.get(c) for c in binding)
                variables.add(StateVariableLite(symbol, binding_with_constants))

        return variables

    def ground_actions(self):
        """  """
        model = self._solve_lp()
        return {k: model[k] for k in self.problem.actions.keys()}

    def iterate_over_schema_groundings(self, schema_name: str):
        """  """
        model = self._solve_lp()
        return (x for x in model[schema_name])

    def _solve_lp(self):
        if self.model is None:
            lp, tr = create_reachability_lp(self.problem)
            model_filename = run_clingo(lp)
            self.model = parse_model(model_filename, tr)

            if len(self.model[SOLVABLE]) != 1:
                raise ReachabilityLPUnsolvable()
        return self.model

    def __str__(self):
        return 'LPGroundingStrategy["{}"]'.format(self.problem.name)

    __repr__ = __str__
