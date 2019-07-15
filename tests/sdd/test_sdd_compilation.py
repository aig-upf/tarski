"""
 Tests for the SDD module
"""
import pytest

from tarski.sdd.sdd import process_problem
from ..common.blocksworld import generate_small_strips_bw_problem


def test_bw_sdd():
    problem = generate_small_strips_bw_problem()
    data = process_problem(problem)
    print(data)

