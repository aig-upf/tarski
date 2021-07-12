from tarski.io import PDDLReader
from tests.data import resolve_path


def test_x():
    reader = PDDLReader(raise_on_error=True, strict_with_requirements=False)
    reader.parse_domain(resolve_path('pddl/issue114/domain.pddl'))
    problem = reader.parse_instance(resolve_path('pddl/issue114/instance.pddl'))
