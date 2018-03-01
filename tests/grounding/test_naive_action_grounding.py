from tarski import fstrips as fs
from tarski.grounding.naive import state_variables as sv
from tarski.grounding.naive import instantiation
from tarski.syntax import *
from tarski.util import IndexDictionary

from tests.common import blocksworld

def create_small_bw_with_index():
    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()

    for var in sv.create_all_possible_state_variables(index.fluent_symbols):
        index.state_variables.add(var)

    return prob, index

def test_enumeration_of_action_parameters_for_small_bw():
    prob, index = create_small_bw_with_index()
    index.ground_actions = IndexDictionary()
    actions = list(prob.actions.values())
    K, syms, substs = instantiation.enumerate(prob.language,actions[0].parameters)
    assert K == 20
    assert len(syms)==2
    assert len(substs)==2

def test_generate_substitutions_for_small_bw():
    import itertools

    prob, index = create_small_bw_with_index()
    index.ground_actions = IndexDictionary()
    actions = list(prob.actions.values())
    K, syms, substs = instantiation.enumerate(prob.language,actions[0].parameters)
    for values in itertools.product(*substs):
        assert(len(syms)==len(values))
        subst = { syms[k] : v for k,v in enumerate(values) }
        assert len(subst)==2
