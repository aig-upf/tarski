import os

from .common import reader


def get_benchmark_dir_if_exists(envvar):
    if envvar not in os.environ:
        return None

    d = os.environ[envvar]
    if not os.path.isdir(d):
        return None

    return d


SAMPLE_STRIPS_INSTANCES = [
    "trucks:p01.pddl",  # quantified formulas
    # "visitall-sat11-strips:problem12.pddl",
    # "blocks:probBLOCKS-4-1.pddl",
    # "gripper:prob01.pddl",
    # "parking-sat11-strips:pfile08-031.pddl",
    # "sokoban-opt08-strips:p01.pddl",
]

SAMPLE_FSTRIPS_INSTANCES = [
    # "counters-fn:instance_4.pddl",
]


def add_domains_from(metafunc, envvar, domains, benchmark_prefix=None):
    db = get_benchmark_dir_if_exists(envvar)
    if db is None:  # Benchmarks dir not installed on the machine
        return

    db = db if benchmark_prefix is None else os.path.join(db, benchmark_prefix)

    instances = []

    for dom, ins in (x.split(":") for x in domains):
        base_dir = os.path.join(db, dom)
        instances.append([
            os.path.join(base_dir, ins),
            os.path.join(base_dir, "domain.pddl")
        ])

    return instances


def pytest_generate_tests(metafunc):
    # This is called once for each test method, and allows us to pass different parameters to the test method,
    # in this case as many instances as desired, so that each instance is mapped into a different test.
    # @see http://pytest.org/latest/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration
    if metafunc.function != test_pddl_instances:
        return

    argnames = ['instance_file', 'domain_file']
    argvalues = add_domains_from(metafunc, "DOWNWARD_BENCHMARKS", SAMPLE_STRIPS_INSTANCES)
    argvalues += add_domains_from(metafunc, "FSBENCHMARKS", SAMPLE_FSTRIPS_INSTANCES, benchmark_prefix='benchmarks')
    metafunc.parametrize(argnames, argvalues)


def test_pddl_instances(instance_file, domain_file):
    _ = reader().read_problem(domain_file, instance_file)
