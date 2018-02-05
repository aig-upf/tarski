"""
 This tests the type-handling module
"""

from . import blocksworld
from . import numeric

def test_something():
    lang = blocksworld.generate_small_bw_instance()
    pass

def test_intrepretation_instance() :
    lang = numeric.generate_numeric_instance()
    s = lang.model()

def test_numeric_function_set() :
    lang = numeric.generate_numeric_instance()
    particle = lang.get_sort('particle')
    p1 = lang.const('p1', particle)
    x = lang.function('x', particle, lang.Real )
    s = lang.model()
    s.set( x, 0.0 )
