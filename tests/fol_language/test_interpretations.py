"""
 This tests the type-handling module
"""
import tarski
import tarski.model
from tarski.model import Model

from ..common import blocksworld, numeric
from tarski.evaluators.simple import evaluate
from tarski.syntax import Constant


def test_interpretation_instance():
    lang = numeric.generate_numeric_instance()
    s = tarski.model.create(lang)


def test_numeric_function_set():
    lang = numeric.generate_numeric_instance()
    particle = lang.get_sort('particle')
    p1 = lang.get_constant('p1')
    x = lang.get_function('x')
    model = tarski.model.create(lang)
    model.set(x, (p1,), 1.0)


def test_numeric_builtin_addition():
    lang = numeric.generate_numeric_instance()
    p1 = lang.get_constant('p1')
    x = lang.get_function('x')
    model = tarski.model.create(lang)
    model.evaluator = evaluate
    model.set(x, (p1,), 1.0)

    expr = model[x(p1) + 1.0]

    assert isinstance(expr, Constant)
    assert expr.symbol == 2.0


def test_numeric_rel_formula_evaluation():
    lang = numeric.generate_numeric_instance()
    p1 = lang.get_constant('p1')
    p2 = lang.get_constant('p2')
    x = lang.get_function('x')
    model = tarski.model.create(lang)
    model.evaluator = evaluate
    model.set(x, (p1,), 1.0)
    model.set(x, (p2,), 2.0)

    assert model[x(p1) < x(p2)]


def test_blocksworld_set():
    lang = blocksworld.generate_small_fstrips_bw_language()
    model = Model(lang)
    loc = lang.get_function('loc')
    b1, table = (lang.get_constant(s) for s in ('b1', 'table'))
    model.set(loc, (b1,), table)

    assert evaluate(loc(b1), model) == table


def test_blocksworld_set_via_square_brackets():
    lang = blocksworld.generate_small_fstrips_bw_language()
    model = Model(lang)
    model.evaluator = evaluate
    loc = lang.get_function('loc')
    b1, table = (lang.get_constant(s) for s in ('b1', 'table'))
    model.set(loc, (b1,), table)

    assert model[loc(b1)] == table


def test_blocksworld_add():
    lang = blocksworld.generate_small_fstrips_bw_language()
    model = Model(lang)
    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')
    model.add(clear, b1)
    assert evaluate(clear(b1), model) is True


def test_blocksworld_add_and_remove():
    lang = blocksworld.generate_small_fstrips_bw_language()
    model = Model(lang)

    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')

    model.add(clear, b1)
    model.remove(clear, b1)
    assert evaluate(clear(b1), model) is False


def test_zero_ary_predicate_set():
    L = tarski.language()

    P = L.predicate('P')

    M = Model(L)
    M.add(P)

    assert evaluate(P(), M) is True
