"""
 Tests for the SDD module
"""

from tarski.sdd.sdd import process_problem
from ..common.blocksworld import generate_small_strips_bw_problem
from ..common.gripper import create_sample_problem


def test_bw_sdd():
    problem = generate_small_strips_bw_problem()
    data = process_problem(problem)
    # print(data)


def test_gripper_sdd():
    problem = create_sample_problem()
    data = process_problem(problem)
    # print(data)

