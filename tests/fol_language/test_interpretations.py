"""
 This tests the type-handling module
"""

# from ..common import numeric
from ..common import blocksworld
# from tarski.evaluators.simple import evaluate
from tarski.evaluators.simple import evaluate


# def test_interpretation_instance():
#     lang = numeric.generate_numeric_instance()
#     s = lang.model()


# def test_numeric_function_set():
#     lang = numeric.generate_numeric_instance()
#     particle = lang.get_sort('particle')
#     p1 = lang.constant('p1', particle)
#     x = lang.get_function('x')
#     model = lang.model()
#     model.set(x, (0.0, ), 1.0)


def test_blocksworld_set():
    lang = blocksworld.generate_small_bw_language()
    model = lang.model()
    loc = lang.get_function('loc')
    b1, table = (lang.get_constant(s) for s in ('b1', 'table'))
    model.set(loc, (b1,), table)

    assert evaluate(loc(b1), model) == table


def test_blocksworld_add():
    lang = blocksworld.generate_small_bw_language()
    model = lang.model()
    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')
    model.add(clear, b1)
    assert evaluate(clear(b1), model) is True


def test_blocksworld_add_and_remove():
    lang = blocksworld.generate_small_bw_language()
    s = lang.model()

    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')

    s.add(clear, b1)
    s.remove(clear, b1)
    assert evaluate(clear(b1), s) is False
