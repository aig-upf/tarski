from tarski import fstrips as fs

from tests.fstrips import blocksworld, gripper


def test_task_index_constructor():
    prob = blocksworld.create_4blocks_task()
    index = fs.TaskIndex(prob.language.name, prob.name)

    assert index.domain_name == prob.language.name
    assert index.instance_name == prob.name


def test_task_index_process_symbols_fluents_bw():
    problem = blocksworld.create_4blocks_task()
    index = fs.TaskIndex(problem.language.name, problem.name)
    index.process_symbols(problem)

    # print(','.join([str(sym) for sym in index.fluent_terms]))
    # print(','.join([str(sym) for sym in index.static_terms]))
    assert len(index.fluent_terms) == 6
    assert len(index.static_terms) == 11


def test_task_index_process_symbols_fluents_bw_gripper():
    problem = gripper.create_sample_problem()
    index = fs.TaskIndex(problem.language.name, problem.name)
    index.process_symbols(problem)
    assert len(index.fluent_terms) == 4  # (free, carry, at-robby, at)
    assert len(index.static_terms) == 3  # (ball, gripper, room)
