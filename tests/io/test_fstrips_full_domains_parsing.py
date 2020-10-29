from tarski.fstrips.representation import is_unit_cost_problem, is_unit_cost_action, is_zero_cost_action, \
    is_constant_cost_action
from tests.common.benchmarks import get_lenient_benchmarks
from .common import reader, collect_strips_benchmarks, collect_fstrips_benchmarks, parse_benchmark_instance

# Let's make sure we can correctly parse all benchmarks from the IPC competitions in 2008, 2011, 2014, 2018.
# We have chosen optimal track benchmarks, which one would expect to be the smallest between optimal / satisficing
# track versions, and discarded repeated appearances of the same domain across different IPCs
SAMPLE_STRIPS_INSTANCES = [
    # Some classics
    "trucks:p01.pddl",  # quantified formulas
    "blocks:probBLOCKS-4-1.pddl",
    "gripper:prob01.pddl",

    # IPC 08
    "elevators-opt08-strips:p01.pddl",  # action costs
    "openstacks-opt08-adl:p01.pddl",
    "parcprinter-08-strips:p01.pddl",
    "pegsol-08-strips:p01.pddl",
    "scanalyzer-08-strips:p01.pddl",
    "sokoban-opt08-strips:p01.pddl",  # action costs
    "transport-opt08-strips:p01.pddl",  # action costs
    "woodworking-opt08-strips:p01.pddl",

    # IPC 11, minus those already appearing in IPC 08
    "barman-opt11-strips:pfile01-001.pddl",
    "floortile-opt11-strips:opt-p01-001.pddl",
    "nomystery-opt11-strips:p01.pddl",
    "parking-opt11-strips:pfile03-011.pddl",   # action costs
    # "tidybot-opt11-strips:p01.pddl",  # "cart" used both as type name and object name, which we don't support
    "visitall-sat11-strips:problem12.pddl",

    # IPC 14, minus those already appearing in IPC 08,11
    "ged-opt14-strips:d-1-2.pddl",
    "cavediving-14-adl:testing01_easy.pddl",
    "childsnack-opt14-strips:child-snack_pfile01.pddl",
    "citycar-opt14-adl:p2-2-2-1-2.pddl",
    "hiking-opt14-strips:ptesting-1-2-3.pddl",
    "maintenance-opt14-adl:maintenance-1-3-010-010-2-000.pddl",
    "tetris-opt14-strips:p01-6.pddl",

    # IPC 18, minus action-split versions
    'agricola-opt18-strips:p01.pddl',
    'caldera-opt18-adl:p01.pddl',
    'data-network-opt18-strips:p01.pddl',
    "nurikabe-sat18-adl:p01.pddl",
    "organic-synthesis-sat18-strips:p01.pddl",
    'petri-net-alignment-opt18-strips:p01.pddl',
    "settlers-sat18-adl:p01.pddl",
    'snake-opt18-strips:p01.pddl',
    "spider-sat18-strips:p01.pddl",
    'termes-opt18-strips:p01.pddl',
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
    lenient = any(d in domain_file for d in get_lenient_benchmarks())
    reader_ = reader(strict_with_requirements=not lenient, case_insensitive=lenient)
    _ = reader_.read_problem(domain_file, instance_file)  # Simply parse the problem


def test_action_cost_parsing():
    problem = parse_benchmark_instance("spider-opt18-strips:p01.pddl")

    # spider is not unit-cost, since it has some actions with explicit additive cost 1,
    # and some other actions where no cost is specified, hence 0 is assumed
    assert not is_unit_cost_problem(problem)

    assert is_unit_cost_action(problem.get_action('start-dealing'))
    assert is_zero_cost_action(problem.get_action('deal-card'))

    problem = parse_benchmark_instance("transport-opt11-strips:p01.pddl")
    assert not is_unit_cost_problem(problem)

    drive = problem.get_action('drive')
    pickup = problem.get_action('pick-up')
    drop = problem.get_action('drop')

    assert not is_constant_cost_action(drive)
    assert is_unit_cost_action(pickup)
    assert is_unit_cost_action(drop)

