
from tarski.reachability.asp import create_reachability_lp

from ..common.gripper import create_sample_problem


def test_lp_on_bw():
    problem = create_sample_problem()
    lp = create_reachability_lp(problem)
    assert lp
