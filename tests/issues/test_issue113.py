from tarski.io import FstripsWriter
from tests.io.common import parse_benchmark_instance


def test_issue():
    problem = parse_benchmark_instance("blocks:probBLOCKS-4-0.pddl")
    writer = FstripsWriter(problem)
    domain = writer.print_domain()
    # Simply check that an untyped problem is printed with the default object type
    assert (
        """(:types
        object
    )"""
        in domain
    )
