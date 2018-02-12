"""
 This tests the type-handling module
"""

from ..common import numeric
from ..common import blocksworld


def test_intrepretation_instance():
    lang = numeric.generate_numeric_instance()
    s = lang.model()


def test_numeric_function_set():
    lang = numeric.generate_numeric_instance()
    particle = lang.get_sort('particle')
    p1 = lang.constant('p1', particle)
    x = lang.get_function('x')
    s = lang.model()
    s.set(x, 0.0)


def test_blocksworld_add():
    lang = blocksworld.generate_small_bw_language()
    s = lang.model()
    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')
    s.add(clear, b1)
    assert s[clear(b1)] is True


def test_blocksworld_add_and_remove():
    lang = blocksworld.generate_small_bw_language()
    s = lang.model()

    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')

    s.add(clear, b1)
    s.remove(clear, b1)
    assert s[clear(b1)] is False
