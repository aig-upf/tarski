import pytest
from tarski.syntax.transform.errors import TransformationError
from tarski.syntax.transform.simplifications import transform_to_ground_atoms

from tests.common import blocksworld as bw


def test_ground_atom_transformation():
    problem = bw.generate_small_fstrips_bw_problem()
    lang = problem.language

    b1, b2, b3, clear, loc = lang.get('b1', 'b2', 'b3', 'clear', 'loc')
    problem.goal = (loc(b1) == b2) & (loc(b2) == b3) & (clear(b1))

    atoms = transform_to_ground_atoms((clear(b1)) & (clear(b2)))
    assert atoms == [('clear', 'b1'), ('clear', 'b2')]

    with pytest.raises(TransformationError):
        transform_to_ground_atoms((clear(b1)) | (clear(b2)))

