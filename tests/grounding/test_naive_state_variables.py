from tarski import fstrips as fs
from tarski.grounding.naive import state_variables as sv
from tarski.util import IndexDictionary

from tests.common.blocksworld import create_4blocks_task
from tests.common import parcprinter
from tests.fstrips.hybrid.tasks import create_billiards_world


def test_task_static_symbol_detection():
    prob = parcprinter.create_small_task()
    index = fs.TaskIndex(prob.language.name, prob.name)
    index.process_symbols(prob)
    assert len(index.static_terms) == 3
    assert len(index.fluent_terms) == 5


def test_task_index_create_state_variables_parcprinter():
    prob = parcprinter.create_small_task()
    index = fs.TaskIndex(prob.language, prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in sv.create_all_possible_state_variables(index.fluent_terms):
        index.state_variables.add(var)

    assert len(index.state_variables) == 8


def test_all_state_variables_can_be_evaluated_in_init_parcprinter():
    prob = parcprinter.create_small_task()
    index = fs.TaskIndex(prob.language, prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in sv.create_all_possible_state_variables(index.fluent_terms):
        index.state_variables.add(var)
    for var in index.state_variables:
        # print("type: {} expr: {} value: {}".format(type(var.ground), str(var.ground), prob.init[var.ground]))
        assert (prob.init[var.ground] is True or
                prob.init[var.ground] is False or
                prob.init[var.ground] == 0.0)


def test_task_index_create_state_variables_blocksworld():
    prob = create_4blocks_task()
    index = fs.TaskIndex(prob.language.name, prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in sv.create_all_possible_state_variables(index.fluent_terms):
        index.state_variables.add(var)

    # print(','.join([str(var) for var in index.state_variables]))
    assert len(index.state_variables) == 12


def test_create_state_variables_for_hybrid_problem_with_reactions():
    prob = create_billiards_world()
    index = fs.TaskIndex(prob.language.name, prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in sv.create_all_possible_state_variables(index.fluent_terms):
        index.state_variables.add(var)
    assert len(index.state_variables) == 4
