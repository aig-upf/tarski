from tarski.fstrips import hybrid
from tarski.syntax import *

from tests.common.numeric import generate_numeric_instance


def test_diff_constraint_creation():
    particles = generate_numeric_instance()

    x, y, f = [particles.get_function(name) for name in ['x', 'y', 'f']]
    p1, p2, p3, p4 = [particles.get_constant(name) for name in ['p1', 'p2', 'p3', 'p4']]

    constraint = hybrid.DifferentialConstraint(particles, 'test', [], top, x(p1), f(p1) * 2.0)
    assert isinstance(constraint, hybrid.DifferentialConstraint)
