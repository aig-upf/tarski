
from tarski import fstrips as fs
from tarski.syntax import *

from ..common import blocksworld


def test_task_index_constructor():

    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)

    assert index.domain_name == prob.language.name
    assert index.instance_name == prob.name

def test_task_index_process_symbols_fluents():
    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)
    index.process_symbols(prob)

    print(','.join([str(sym) for sym in index.fluent_symbols]))
    assert len(index.fluent_symbols) == 2

def test_task_index_process_symbols_statics():
    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)
    index.process_symbols(prob)

    print(','.join([str(sym) for sym in index.static_symbols]))
    assert len(index.static_symbols) == 2
