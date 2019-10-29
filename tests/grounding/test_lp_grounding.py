import shutil
import pytest

from tarski.grounding import LPGroundingStrategy, NaiveGroundingStrategy
from tarski.grounding.errors import ReachabilityLPUnsolvable
from tarski.grounding.lp_grounding import compute_action_groundings
from tarski.syntax import neg

from tests.common.gripper import create_sample_problem
from tests.common.simple import create_simple_problem
from ..io.common import reader, collect_strips_benchmarks, collect_fstrips_benchmarks

if shutil.which("gringo") is None:
    pytest.skip('Install the Clingo ASP solver and put the "gringo" binary on your PATH in order to test ASP-based '
                "reachability analysis", allow_module_level=True)


SAMPLE_STRIPS_INSTANCES = [
    "blocks:probBLOCKS-4-1.pddl",
    "openstacks:p01.pddl",
    "visitall-sat11-strips:problem12.pddl",
    "parcprinter-08-strips:p01.pddl",
    "floortile-opt11-strips:opt-p01-001.pddl",
    "pipesworld-notankage:p01-net1-b6-g2.pddl",
    "pipesworld-tankage:p01-net1-b6-g2-t50.pddl",
    "pathways:p01.pddl",

    # Buggy domains that will raise some parsing exception:
    # "storage:p01.pddl", # type "area" is declared twice
    # "tidybot-opt11-strips:p01.pddl",  # "cart" used both as type name and object name, which we don't support
    # "ged-opt14-strips:d-1-2.pddl",  # "DEFINE" used in caps. The PDDL grammar doesn't mention it is case-insensitive
]

# Domains that require non-strict PDDL parsing because of missing requirement flags or similar that would
# otherwise result in a parsing error
LENIENT_DOMAINS = ['floortile-opt11-strips']


def pytest_generate_tests(metafunc):
    # This is called once for each test method, and allows us to pass different parameters to the test method,
    # in this case as many instances as desired, so that each instance is mapped into a different test.
    # @see http://pytest.org/latest/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration
    if metafunc.function != test_action_grounding_on_standard_benchmarks:
        return

    argnames = ['instance_file', 'domain_file']
    argvalues = collect_strips_benchmarks(SAMPLE_STRIPS_INSTANCES)
    metafunc.parametrize(argnames, argvalues)


def test_action_grounding_on_standard_benchmarks(instance_file, domain_file):
    lenient = any(d in domain_file for d in LENIENT_DOMAINS)

    problem = reader(strict_with_requirements=not lenient).read_problem(domain_file, instance_file)
    grounder = LPGroundingStrategy(problem)
    actions = grounder.ground_actions()

    expected = {  # A compilation of the expected values for each tested domain
        "BLOCKS": {'pick-up': 4, 'put-down': 4, 'stack': 16, 'unstack': 16},
        "grid-visit-all": {'move': 528},
        'openstacks-sequencedstrips': {'setup-machine': 30, 'make-product': 30, 'start-order': 25,
                                       'ship-order': 25, 'open-new-stack': 5},  # TODO Revise this figures
        # Parcprinter:
        'upp': {'initialize': 1, 'EndCap-Move-Letter': 1, 'HtmOverBlack-Move-Letter': 1,
                'ColorContainer-ToIME-Letter': 1, 'ColorContainer-FromIME-Letter': 1, 'ColorPrinter-Simplex-Letter': 0,
                'ColorPrinter-SimplexMono-Letter': 2, 'ColorFeeder-Feed-Letter': 1, 'BlackFeeder-Feed-Letter': 1,
                'Down-MoveTop-Letter': 1, 'Down-MoveBottom-Letter': 1, 'Down-MoveDown-Letter': 1,
                'HtmOverColor-Move-Letter': 1, 'BlackContainer-ToIME-Letter': 1, 'BlackContainer-FromIME-Letter': 1,
                'BlackPrinter-Simplex-Letter': 2, 'BlackPrinter-SimplexAndInvert-Letter': 2, 'Up-MoveTop-Letter': 1,
                'Up-MoveUp-Letter': 1, 'Finisher1-PassThrough-Letter': 1, 'Finisher1-Stack-Letter': 1,
                'Finisher2-PassThrough-Letter': 1, 'Finisher2-Stack-Letter': 1},
        'floor-tile': {'change-color': 8, 'paint-up': 36, 'paint-down': 36, 'up': 27, 'down': 27, 'right': 24,
                       'left': 24},
        # This works for both versions of pipesworld:
        "pipesworld_strips": {'PUSH-START': 0, 'PUSH-END': 0, 'POP-START': 0, 'POP-END': 0,
                              'PUSH-UNITARYPIPE': 64, 'POP-UNITARYPIPE': 64},
        'Pathways-Propositional': {'choose': 48, 'initialize': 16, 'associate': 7, 'associate-with-catalyze': 5,
                                   'synthesize': 0, 'DUMMY-ACTION-1': 1},
    }[problem.domain_name]

    # Make sure that the number of possible groundings of each action schema in the domain is as expected
    # (check at runtime with: {schema: len(groundings) for schema, groundings in actions.items()} )
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

    # We negate all atoms in the precondition, which makes all 8^3 combinations of objects be a valid grounding,
    # since all precondition atoms are ignored
    pick_prec = problem.actions['pick'].precondition
    pick_prec.subformulas = tuple(neg(f) for f in pick_prec.subformulas)
    actions = compute_action_groundings(problem)
    assert len(actions['pick']) == 512


def test_ground_actions_on_negated_preconditions2():
    problem = create_simple_problem()
    lang = problem.language
    p, q, a = lang.get("p", "q", "a")

    # p(a) is true in initial state, so negate(a) should be reachable
    actions = compute_action_groundings(problem)
    assert actions["negate"] == {('a', )}

    # If on the contrary p(a) is not true in initial state, action negate(a) should not be reachable,
    # but note that the problem will still be relaxed-reachable because goal is -p(a), which is assumed to be true
    problem.init.remove(p, a)

    actions = compute_action_groundings(problem)
    assert actions["negate"] == set()

    # If the goal is now "p(a)", the whole problem becomes relaxed unreachable
    problem.goal = p(a)
    with pytest.raises(ReachabilityLPUnsolvable):
        actions = compute_action_groundings(problem)

