import os

from tarski.io import FstripsReader


def reader(theories=None):
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True, theories=theories)


def get_benchmark_dir_if_exists(envvar):
    if envvar not in os.environ:
        return None

    d = os.environ[envvar]
    if not os.path.isdir(d):
        return None

    return d


def add_domains_from(envvar, domains, benchmark_prefix=None):
    db = get_benchmark_dir_if_exists(envvar)
    if db is None:  # Benchmarks dir not installed on the machine
        return []

    db = db if benchmark_prefix is None else os.path.join(db, benchmark_prefix)

    instances = []

    # This works only if the domain is called domain.pddl TODO Extend to infer other domain names automatically
    for dom, ins in (x.split(":") for x in domains):
        base_dir = os.path.join(db, dom)
        instances.append([
            os.path.join(base_dir, ins),
            os.path.join(base_dir, "domain.pddl")
        ])

    return instances


def skip_tests_because_of_benchmarks():
    import pytest
    pytest.skip("Please install STRIPS/FSTRIPS benchmarks and set up environment variables ($DOWNWARD_BENCHMARKS, "
                "$FSBENCHMARKS) appropriately to run the full suite of tests", allow_module_level=True)


def collect_strips_benchmarks(instances):
    if get_benchmark_dir_if_exists("DOWNWARD_BENCHMARKS") is None:
        skip_tests_because_of_benchmarks()
        return []

    return add_domains_from("DOWNWARD_BENCHMARKS", instances)


def collect_fstrips_benchmarks(instances):
    if get_benchmark_dir_if_exists("FSBENCHMARKS") is None:
        skip_tests_because_of_benchmarks()
        return []

    return add_domains_from("FSBENCHMARKS", instances, benchmark_prefix='benchmarks')
