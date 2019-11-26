"""
 Tests for the SDD module
"""
try:
    from tarski.sdd.sdd import process_problem
except ImportError:
    import pytest
    pytest.skip("Please install the PySDD Python module to run the full suite of tests", allow_module_level=True)


from ..common.blocksworld import generate_small_strips_bw_problem
from ..common.gripper import create_sample_problem
from ..io.common import get_benchmark_dir_if_exists, add_domains_from, reader


def test_bw_sdd():
    problem = generate_small_strips_bw_problem()
    data = process_problem(problem)
    # print(data)


def test_gripper_sdd():
    problem = create_sample_problem()
    data = process_problem(problem)
    # print(data)


def pytest_generate_tests(metafunc):
    # This is called once for each test method, and allows us to pass different parameters to the test method,
    # in this case as many instances as desired, so that each instance is mapped into a different test.
    # @see http://pytest.org/latest/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration
    if metafunc.function != test_pddl_instances:
        return

    argnames = ['instance_file', 'domain_file']
    benchdir = get_benchmark_dir_if_exists("DOWNWARD_BENCHMARKS")
    if benchdir is None:
        import pytest
        pytest.skip("Please install STRIPS/FSTRIPS benchmarks and set up environment variables (DOWNWARD_BENCHMARKS)"
                    " appropriately to run the full suite of tests".format(allow_module_level=True))
        return []

    argvalues = add_domains_from("DOWNWARD_BENCHMARKS", [
        "blocks:probBLOCKS-4-0.pddl",
        "spider-sat18-strips:p01.pddl",
        "organic-synthesis-sat18-strips:p01.pddl",
        "visitall-sat11-strips:problem12.pddl",
        "gripper:prob01.pddl",
        "elevators-opt08-strips:p01.pddl",
        "sokoban-opt08-strips:p01.pddl",
        "parking-sat11-strips:pfile08-031.pddl",
        "transport-opt08-strips:p01.pddl",

        # "settlers-sat18-adl:p01.pddl",  # Universal effect not supported ATM, but could be implemented
        # "nurikabe-sat18-adl:p01.pddl"  # Universal effect not supported ATM, but could be implemented
        # "trucks:p01.pddl",  # quantified formulas not accepted
    ])
    metafunc.parametrize(argnames, argvalues)


def test_pddl_instances(instance_file, domain_file):
    problem = reader().read_problem(domain_file, instance_file)
    data = process_problem(problem)
    # print(data)
