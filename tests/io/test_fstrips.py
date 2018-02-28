
import pytest
import tarski as tsk
from tarski.io import FstripsReader


def test_blocksworld_reading():
    instance_file = "/home/frances/projects/code/downward-benchmarks/visitall-sat11-strips/problem12.pddl"
    domain_file = "/home/frances/projects/code/downward-benchmarks/visitall-sat11-strips/domain.pddl"

    reader = FstripsReader(domain_file, instance_file)
    problem = reader.read()
