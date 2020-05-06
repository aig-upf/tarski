import pytest

import tarski.benchmarks.blocksworld
from tarski.syntax.transform.errors import TransformationError
from tarski.syntax.transform.simplifications import transform_to_ground_atoms


def test_ground_atom_transformation():
    lang = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    b1, b2, b3, clear, loc = lang.get('b1', 'b2', 'b3', 'clear', 'loc')
    atoms = transform_to_ground_atoms((clear(b1)) & (clear(b2)))
    assert atoms == [('clear', 'b1'), ('clear', 'b2')]

    with pytest.raises(TransformationError):
        transform_to_ground_atoms((clear(b1)) | (clear(b2)))
