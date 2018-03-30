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
    "visitall-sat11-strips:problem12.pddl",
    "blocks:probBLOCKS-4-1.pddl",
    "gripper:prob01.pddl",
    "trucks:p01.pddl",
    "parking-sat11-strips:pfile08-031.pddl",
    "sokoban-opt08-strips:p01.pddl",
]

SAMPLE_FSTRIPS_INSTANCES = [
    "counters-fn:instance_4.pddl",
]


def add_domains_from(metafunc, envvar, domains):
    db = get_benchmark_dir_if_exists(envvar)
    if db is None:  # Benchmarks dir not installed on the machine
        return

    for dom, ins in (x.split(":") for x in domains):
        base_dir = os.path.join(db, dom)
        metafunc.addcall(funcargs=dict(instance_file=os.path.join(base_dir, ins),
                                       domain_file=os.path.join(base_dir, "domain.pddl")))


def pytest_generate_tests(metafunc):
    # This is called once for each test method, and allows us to pass different parameters to the test method,
    # in this case as many instances as desired, so that each instance is mapped into a different test.
    # @see http://pytest.org/latest/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration
    if metafunc.function != test_pddl_instances:
        return

    add_domains_from(metafunc, "DOWNWARD_BENCHMARKS", SAMPLE_STRIPS_INSTANCES)
    add_domains_from(metafunc, "FSBENCHMARKS", SAMPLE_FSTRIPS_INSTANCES)


def test_pddl_instances(instance_file, domain_file):
    _ = reader().read_problem(domain_file, instance_file)
