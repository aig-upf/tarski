
from ...reachability import create_reachability_lp, run_clingo, parse_model
from ...reachability.asp import SOLVABLE


def ground_actions(problem):
    """ """
    lp, tr = create_reachability_lp(problem)
    model_filename = run_clingo(lp)
    model = parse_model(model_filename, tr)

    if len(model[SOLVABLE]) != 1:
        # The goal of the problem is not relaxed reachable, hence the problem is unsolvable
        return "unsolvable"

    return {k: model[k] for k in problem.actions.keys()}