
from tarski import fstrips as fs
from tarski.grounding.naive import state_variables as sv
from tarski.syntax import *
from tarski.util import IndexDictionary

from tests.common import blocksworld
from tests.common import parcprinter

def test_task_static_symbol_detection():
    prob = parcprinter.create_small_task()
    assert False

def test_task_index_create_state_variables():
    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in sv.create_all_possible_state_variables(index.fluent_symbols):
        index.state_variables.add(var)

    print(','.join([str(var) for var in index.state_variables]))
    assert len(index.state_variables) == 8
