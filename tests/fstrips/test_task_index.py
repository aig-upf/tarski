from tarski import fstrips as fs

from tests.common.blocksworld import create_small_bw_task


def test_task_index_constructor():
    prob = create_small_bw_task()
    index = fs.TaskIndex(prob.language.name, prob.name)

    assert index.domain_name == prob.language.name
    assert index.instance_name == prob.name


def test_task_index_process_symbols_fluents():
    prob = create_small_bw_task()
    index = fs.TaskIndex(prob.language.name, prob.name)
    index.process_symbols(prob)

    # print(','.join([str(sym) for sym in index.fluent_symbols]))
    assert len(index.fluent_symbols) == 2


def test_task_index_process_symbols_statics():
    prob = create_small_bw_task()
    index = fs.TaskIndex(prob.language.name, prob.name)
    index.process_symbols(prob)

    # print(','.join([str(sym) for sym in index.static_symbols]))
    assert len(index.static_symbols) == 2
