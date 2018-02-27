
from tarski import fstrips as fs
from tarski.grounding import state_variables as sv
from tarski.syntax import *

from tests.common import blocksworld

def test_task_index_create_state_variables():
    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)
    index.process_symbols(prob)
    index.process_state_variables()
    for var in sv.create_all_possible_state_variables(index.fluent_symbols):
        index.state_variables.add(var)

    print(','.join([str(var) for var in index.state_variables]))
    assert len(index.state_variables) == 8
