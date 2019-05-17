
from tarski.grounding import ProblemGrounding

from tests.common import blocksworld, gripper


def test_task_index_process_symbols_fluents_bw():
    problem = blocksworld.create_4blocks_task()
    index = ProblemGrounding(problem)
    index.process_symbols(problem)

    assert len(index.fluent_terms) == 6
    assert len(index.static_terms) == 11


def test_task_index_process_symbols_fluents_bw_gripper():
    problem = gripper.create_sample_problem()
    index = ProblemGrounding(problem)
    index.process_symbols(problem)
    fluents, statics = index.compute_fluent_and_statics()
    assert len(fluents) == 4  # (free, carry, at-robby, at)
    assert len(statics) == 3  # (ball, gripper, room)
