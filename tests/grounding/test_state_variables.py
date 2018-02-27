
from tarski import fstrips as fs
from tarski import grounding as gr
from tarski.syntax import *

from ..common import blocksworld

def test_task_index_create_state_variables():
    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)
    index.process_symbols(prob)
    index.process_state_variables()
    index.state_variables |= gr.state_variables.create_all_possible_state_variables(index.fluent_symbols)

    print(','.join([str(var) for var in index.state_variables]))
    assert len(index.state_variables) == 8
