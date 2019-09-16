import shutil

from tarski.grounding import LPGroundingStrategy, NaiveGroundingStrategy
from tarski.syntax import neg

from tests.common.gripper import create_sample_problem
from ..io.common import reader, collect_strips_benchmarks, collect_fstrips_benchmarks

if shutil.which("gringo") is None:
    import pytest
    pytest.skip('Install the Clingo ASP solver and put the "gringo" binary on your PATH in order to test ASP-based '
                "reachability analysis", allow_module_level=True)


SAMPLE_STRIPS_INSTANCES = [
    "blocks:probBLOCKS-4-1.pddl",
    "openstacks:p15.pddl",
    "visitall-sat11-strips:problem12.pddl",
]


def pytest_generate_tests(metafunc):
    # This is called once for each test method, and allows us to pass different parameters to the test method,
    # in this case as many instances as desired, so that each instance is mapped into a different test.
    # @see http://pytest.org/latest/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration
    if metafunc.function != test_action_grounding:
        return

    argnames = ['instance_file', 'domain_file']
    argvalues = collect_strips_benchmarks(SAMPLE_STRIPS_INSTANCES)
    metafunc.parametrize(argnames, argvalues)


def test_action_grounding(instance_file, domain_file):
    problem = reader().read_problem(domain_file, instance_file)
    grounder = LPGroundingStrategy(problem)
    actions = grounder.ground_actions()

    expected = {  # A compilation of the expected values for each tested domain (including total-cost terms!)
        "BLOCKS": {'pick-up': 4, 'put-down': 4, 'stack': 16, 'unstack': 16},
        "grid-visit-all": {'move': 528},
    }[problem.domain_name]

    # Make sure that the number of possible groundings of each action schema in the domain is as expected
    assert all(len(groundings) == expected[schema] for schema, groundings in actions.items())


def test_ground_actions_for_small_gripper():
    problem = create_sample_problem()
    grounding = LPGroundingStrategy(problem)
    actions = grounding.ground_actions()
    assert len(actions['pick']) == len(actions['drop']) == 16  # 4 balls, two rooms, two grippers
    assert len(actions['move']) == 2  # 2 rooms

    as_list2 = lambda symbols: sorted(map(str, symbols))
    lpvariables = grounding.ground_state_variables()
    assert len(lpvariables) == 20

    grounding = NaiveGroundingStrategy(problem)
    naive_variables = grounding.ground_state_variables()
    # The naive grounding strategy will result in many unreachable state variables such as 'carry(left,left)'
    assert len(set(as_list2(naive_variables)) - set(as_list2(lpvariables))) == 124


def test_ground_actions_on_negated_preconditions():
    problem = create_sample_problem()

    # We negate the atoms in the precondition of some action to obtain a negative literal in the precondition
    pick_prec = problem.actions['pick'].precondition
    pick_prec.subformulas = tuple(neg(f) for f in pick_prec.subformulas)
    grounding = LPGroundingStrategy(problem)
    actions = grounding.ground_actions()
    assert len(actions['pick']) == 0
