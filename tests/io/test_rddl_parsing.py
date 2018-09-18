
import pytest
import tarski
from tarski.theories import Theory
from tarski.syntax import *
from tarski.io import rddl

def test_language_init_mars_rovers():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    assert mr_reader.rddl_model is not None
    print(type(mr_reader.rddl_model))
    assert mr_reader.rddl_model.domain.name == 'simple_mars_rover'


def test_language_init_navigation():
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')
    assert nav_reader.rddl_model is not None

def test_language_init_reservoir():
    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')
    assert res_reader.rddl_model is not None
