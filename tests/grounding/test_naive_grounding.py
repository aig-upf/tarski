from tarski import fstrips as fs
from tarski.grounding.naive import state_variables as sv
from tarski.grounding.naive import instantiation
from tarski.util import IndexDictionary
from tarski.grounding.naive.actions import ActionGrounder
from tarski.grounding.naive.sensors import SensorGrounder
from tarski.grounding.naive.constraints import ConstraintGrounder
from tarski.grounding.naive.diff_constraints import DifferentialConstraintGrounder
from tarski.grounding.naive.reactions import ReactionGrounder
from tests.fstrips import blocksworld
from tests.fstrips.contingent import localize
from tests.fstrips.hybrid.tasks import create_particles_world, create_billiards_world

def create_small_bw_with_index():
    prob = blocksworld.create_small_task()
    index = fs.TaskIndex(prob.language.name, prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()

    for var in sv.create_all_possible_state_variables(index.fluent_symbols):
        index.state_variables.add(var)

    return prob, index


def test_enumeration_of_action_parameters_for_small_bw():
    prob, index = create_small_bw_with_index()
    index.ground_actions = IndexDictionary()
    actions = list(prob.actions.values())
    card, syms, substs = instantiation.enumerate_groundings(prob.language, actions[0].parameters)
    assert card == 20
    assert len(syms) == 2
    assert len(substs) == 2


def test_generate_substitutions_for_small_bw():
    import itertools

    prob, index = create_small_bw_with_index()
    index.ground_actions = IndexDictionary()
    actions = list(prob.actions.values())
    card, syms, substs = instantiation.enumerate_groundings(prob.language, actions[0].parameters)
    for values in itertools.product(*substs):
        assert (len(syms) == len(values))
        subst = {syms[k]: v for k, v in enumerate(values)}
        assert len(subst) == 2


def test_ground_actions_for_small_bw():
    # import itertools, copy

    prob, index = create_small_bw_with_index()
    grounder = ActionGrounder(prob, index)
    grounder.calculate_actions()
    assert len(prob.ground_actions) == 20


def test_ground_constraints_for_small_bw():
    prob, index = create_small_bw_with_index()
    grounder = ConstraintGrounder(prob, index)
    grounder.calculate_constraints()
    assert len(prob.ground_constraints) == 1

def test_ground_sensors_for_small_contingent_problem():
    prob = localize.create_small_task()
    index = fs.TaskIndex(prob.language.name,prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()

    grounder = SensorGrounder(prob,index)
    grounder.calculate_sensors()
    assert len(prob.ground_sensors) == 4

def test_ground_differential_constraints_for_hybrid_problem():
    prob = create_particles_world()
    index = fs.TaskIndex( prob.language.name, prob.name )
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    grounder = DifferentialConstraintGrounder(prob, index)
    grounder.calculate_constraints()
    assert len(prob.ground_differential_constraints) == 8

def test_ground_reactions_for_hybrid_problem():
    prob = create_billiards_world()
    index = fs.TaskIndex(prob.language.name, prob.name)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    grounder = ReactionGrounder(prob, index)
    grounder.calculate_reactions()
    assert len(prob.ground_reactions) == 4
