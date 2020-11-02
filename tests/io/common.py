import os
from pathlib import Path

from tarski.io import FstripsReader
from tarski.io.utils import find_domain_filename


def reader(theories=None, strict_with_requirements=True, case_insensitive=False):
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True, theories=theories,
                         strict_with_requirements=strict_with_requirements,
                         case_insensitive=case_insensitive)


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

    for dom, ins in (x.split(":") for x in domains):
        base_dir = os.path.join(db, dom)
        instance_file = os.path.join(base_dir, ins)
        if not Path(instance_file).is_file():
            raise RuntimeError(f'PDDL instance file "{instance_file}" doesn\'t exist')
        domain_file = find_domain_filename(instance_file)
        instances.append([instance_file, domain_file])
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


def parse_benchmark_instance(instance_key, source="strips", reader_options=None):
    """ Parse and generate a Tarski problem object from the standard DOWNWARD BENCHMARKS repository of IPC
    PDDL instances (source="strips"), or from the standard FSBENCHMARKS Functional STRIPS instances (source="fstrips").
    The instance key represents domain name and instance name, colon separated, e.g. "gripper:prob01.pddl".
    """
    reader_options = {} if reader_options is None else reader_options
    collector = collect_fstrips_benchmarks if source == 'fstrips' else collect_strips_benchmarks
    instance_file, domain_file = collector([instance_key])[0]
    return reader(**reader_options).read_problem(domain_file, instance_file)
