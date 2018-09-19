
import pytest
import tarski
from tarski.theories import Theory
from tarski.syntax import *
from tarski.io import rddl

def test_language_init_mars_rovers():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'simple_mars_rover'
    # create sorts and initialize constants
    domain = mr_reader.rddl_model.domain
    non_fluents = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None

    # try to construct expression without triggering any exceptions
    snap_picture = mr_reader.language.get('snapPicture')
    delta_x = mr_reader.language.get('xMove')
    delta_y = mr_reader.language.get('yMove')
    phi = implies(snap_picture(), (delta_x() == 0.0) & (delta_y() == 0.0))

def test_language_init_navigation():
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')
    assert nav_reader.rddl_model is not None

def test_language_init_reservoir():
    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')
    assert res_reader.rddl_model is not None
