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

def test_blocksworld_add() :
    lang = blocksworld.generate_small_bw_instance()
    s = lang.model()
    s.add( lang.clear, lang.b1 )
    s.add( lang.clear, lang.b2 )
    assert s[lang.clear(lang.b1)] == True
    assert s[lang.clear(lang.b2)] == True

def test_blocksworld_add_and_remove() :
    lang = blocksworld.generate_small_bw_instance()
    s = lang.model()
    s.add( lang.clear, lang.b1 )
    s.remove( lang.clear, lang.b1 )
    assert s[lang.clear(lang.b1)] == False
