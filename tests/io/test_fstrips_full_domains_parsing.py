
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
    # "organic-synthesis-sat18-strips:p01.pddl",  # No domain.pddl file for this one
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
    return reader().read_problem(domain_file, instance_file)


if __name__ == "__main__":
    benchmarks = collect_strips_benchmarks(SAMPLE_STRIPS_INSTANCES) + \
        collect_fstrips_benchmarks(SAMPLE_FSTRIPS_INSTANCES)
    for instance, domain in benchmarks:
        test_pddl_instances(instance, domain)
    print("Tests passed")
