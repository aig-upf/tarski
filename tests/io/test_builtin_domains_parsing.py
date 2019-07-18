import os

from .common import reader


_this_dir = os.path.dirname(os.path.realpath(__file__))
_data_dir = os.path.join(_this_dir, "..", "data", "pddl")


BUILTIN_INSTANCES = [
    "grid:grid3x3.pddl",  # universally-quantified effects
]


def add_instances_from_dir(directory, instance_names):
    instances = []

    for dom, ins in (x.split(":") for x in instance_names):
        base_dir = os.path.join(directory, dom)
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
    argvalues = collect_benchmarks()
    metafunc.parametrize(argnames, argvalues)


def collect_benchmarks():
    return add_instances_from_dir(_data_dir, BUILTIN_INSTANCES)


def test_pddl_instances(instance_file, domain_file):
    _ = reader().read_problem(domain_file, instance_file)


if __name__ == "__main__":
    for instance, domain in collect_benchmarks():
        test_pddl_instances(instance, domain)
    print("Tests passed")
