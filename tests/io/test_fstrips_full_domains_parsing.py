from tarski.fstrips.representation import is_unit_cost_problem, is_unit_cost_action, is_zero_cost_action, \
    is_constant_cost_action
from .common import reader, collect_strips_benchmarks, collect_fstrips_benchmarks

SAMPLE_STRIPS_INSTANCES = [
    "visitall-sat11-strips:problem12.pddl",
    "trucks:p01.pddl",  # quantified formulas
    "blocks:probBLOCKS-4-1.pddl",
    "gripper:prob01.pddl",
    "elevators-opt08-strips:p01.pddl",  # action costs
    "sokoban-opt08-strips:p01.pddl",  # action costs
    "parking-sat11-strips:pfile08-031.pddl",  # action costs
    "transport-opt08-strips:p01.pddl",  # action costs
    "settlers-sat18-adl:p01.pddl",
    "spider-sat18-strips:p01.pddl",
    "organic-synthesis-sat18-strips:p01.pddl",
    "nurikabe-sat18-adl:p01.pddl"
]

SAMPLE_FSTRIPS_INSTANCES = [
    "counters-fn:instance_4.pddl",  # functions, ints
    # "blocksworld-pattern-fn-ex:sample.pddl"  # @alldiff
]


def pytest_generate_tests(metafunc):
    # This is called once for each test method, and allows us to pass different parameters to the test method,
    # in this case as many instances as desired, so that each instance is mapped into a different test.
    # @see http://pytest.org/latest/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration
    if metafunc.function != test_pddl_instances:
        return

    argnames = ['instance_file', 'domain_file']
    argvalues = collect_strips_benchmarks(SAMPLE_STRIPS_INSTANCES) + \
        collect_fstrips_benchmarks(SAMPLE_FSTRIPS_INSTANCES)
    metafunc.parametrize(argnames, argvalues)


def test_pddl_instances(instance_file, domain_file):
    _ = reader().read_problem(domain_file, instance_file)


def test_action_cost_parsing():
    instance_file, domain_file = collect_strips_benchmarks(["spider-opt18-strips:p01.pddl"])[0]
    problem = reader().read_problem(domain_file, instance_file)

    # spider is not unit-cost, since it has some actions with explicit additive cost 1,
    # and some other actions where no cost is specified, hence 0 is assumed
    assert not is_unit_cost_problem(problem)

    assert is_unit_cost_action(problem.get_action('start-dealing'))
    assert is_zero_cost_action(problem.get_action('deal-card'))

    instance_file, domain_file = collect_strips_benchmarks(["transport-opt11-strips:p01.pddl"])[0]
    problem = reader().read_problem(domain_file, instance_file)

    assert not is_unit_cost_problem(problem)

    drive = problem.get_action('drive')
    pickup = problem.get_action('pick-up')
    drop = problem.get_action('drop')

    assert not is_constant_cost_action(drive)
    assert is_unit_cost_action(pickup)
    assert is_unit_cost_action(drop)

