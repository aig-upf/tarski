
import tarski
import tarski.benchmarks.blocksworld
import tarski.model
from tarski.fstrips import language
from tarski.model import Model
from tarski import errors

from ..common import numeric
from tarski.evaluators.simple import evaluate
from tarski.syntax import Constant, ite, symref
from tarski.theories import Theory
from tarski.modules import import_scipy_special

import pytest

try:
    sci = import_scipy_special()
except ImportError:
    pytest.skip('Please install the "arithmetic" extra to run the full suite of tests', allow_module_level=True)


def test_interpretation_instance():
    lang = numeric.generate_numeric_instance()
    tarski.model.create(lang)


def test_numeric_function_set():
    lang = numeric.generate_numeric_instance()
    lang.get_sort('particle')
    p1 = lang.get_constant('p1')
    x = lang.get_function('x')
    model = tarski.model.create(lang)
    model.set(x(p1), 1.0)


def test_numeric_builtin_addition():
    lang = numeric.generate_numeric_instance()
    p1 = lang.get_constant('p1')
    x = lang.get_function('x')
    model = tarski.model.create(lang)
    model.evaluator = evaluate
    model.set(x(p1), 1.0)

    expr = model[x(p1) + 1.0]

    assert isinstance(expr, Constant)
    assert expr.symbol == 2.0


def test_numeric_builtin_addition_int():
    lang = language(theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    # The sorts
    particle = lang.sort('bowl')

    eggs = lang.function('eggs', lang.Object, lang.Integer)
    bowl_1 = lang.constant('bowl_1', particle)
    model = tarski.model.create(lang)
    model.evaluator = evaluate
    model.set(eggs(bowl_1), 1)
    expr = model[eggs(bowl_1) + 1]

    assert isinstance(expr, Constant)
    assert isinstance(expr.symbol, int)
    assert expr.symbol == 2


def test_numeric_rel_formula_evaluation():
    lang = numeric.generate_numeric_instance()
    p1 = lang.get_constant('p1')
    p2 = lang.get_constant('p2')
    x = lang.get_function('x')
    model = tarski.model.create(lang)
    model.evaluator = evaluate
    model.set(x(p1), 1.0)
    model.set(x(p2), 2.0)

    assert model[x(p1) < x(p2)] is True


def test_blocksworld_set():
    lang = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    model = Model(lang)
    loc = lang.get_function('loc')
    b1, table = (lang.get_constant(s) for s in ('b1', 'table'))
    model.set(loc(b1), table)

    assert evaluate(loc(b1), model) == table


def test_blocksworld_set_via_square_brackets():
    lang = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    model = Model(lang)
    model.evaluator = evaluate
    loc = lang.get_function('loc')
    b1, table = (lang.get_constant(s) for s in ('b1', 'table'))
    model.set(loc(b1), table)

    assert model[loc(b1)] == table


def test_special_function_max():
    from tarski.syntax.arithmetic.special import max
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    a, b = lang.constant(3.14, reals), lang.constant(1.24, reals)

    assert model[max(a, b)].symbol == 3.14


def test_special_function_min():
    from tarski.syntax.arithmetic.special import min
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    a, b = lang.constant(3.14, reals), lang.constant(1.24, reals)
    assert model[min(a, b)].symbol == 1.24


def test_special_function_abs():
    from tarski.syntax.arithmetic.special import abs
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    a = lang.constant(5.01, reals)
    b = lang.constant(-5.01, reals)
    c = lang.constant(0.001, reals)
    assert model[abs(a)].symbol == 5.01
    assert model[abs(b)].symbol == 5.01
    assert model[abs(a) > c] is True
    assert model[abs(b) > c] is True


def test_special_function_pow():
    import numpy as np
    from tarski.syntax.arithmetic import pow
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[pow(alpha, 2.0)].symbol == np.power(0.5, 2.0)


def test_special_function_sin():
    import numpy as np
    from tarski.syntax.arithmetic.special import sin
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[sin(alpha)].symbol == np.sin(0.5)


def test_special_function_sqrt():
    import numpy as np
    from tarski.syntax.arithmetic import sqrt
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[sqrt(alpha)].symbol == np.sqrt(0.5)


def test_special_function_cos():
    import numpy as np
    from tarski.syntax.arithmetic.special import cos
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[cos(alpha)].symbol == np.cos(0.5)


def test_special_function_tan():
    import numpy as np
    from tarski.syntax.arithmetic.special import tan
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[tan(alpha)].symbol == np.tan(0.5)


def test_special_function_atan():
    import numpy as np
    from tarski.syntax.arithmetic.special import atan
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[atan(alpha)].symbol == np.arctan(0.5)


def test_special_function_exp():
    import numpy as np
    from tarski.syntax.arithmetic.special import exp
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[exp(alpha)].symbol == np.exp(0.5)


def test_special_function_log():
    import numpy as np
    from tarski.syntax.arithmetic.special import log
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[log(alpha)].symbol == np.log(0.5)


def test_special_function_erf():
    from tarski.syntax.arithmetic.special import erf
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    x = lang.constant(0.5, reals)
    assert model[erf(x)].symbol == sci.erf(0.5)


def test_special_function_erfc():
    from tarski.syntax.arithmetic.special import erfc
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    x = lang.constant(0.5, reals)
    assert model[erfc(x)].symbol == sci.erfc(0.5)


def test_special_function_sgn():
    import numpy as np
    from tarski.syntax.arithmetic.special import sgn
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    x = lang.constant(0.5, reals)
    assert model[sgn(x)].symbol == np.sign(0.5)


def test_random_function_normal():
    import numpy as np
    from tarski.syntax.arithmetic.random import normal
    np.random.seed(1234)  # for repeatability
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    mu = lang.constant(0.5, reals)
    sigma = lang.constant(1.0, reals)
    the_term = normal(mu, sigma)
    assert isinstance(the_term, tarski.syntax.Term)
    assert model[normal(mu, sigma)].symbol == 0.9714351637324931


def test_random_function_gamma():
    import numpy as np
    from tarski.syntax.arithmetic.random import gamma
    np.random.seed(1234)  # for repeatability
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    shape = lang.constant(1.0, reals)
    scale = lang.constant(5.0, reals)
    the_term = gamma(shape, scale)
    assert isinstance(the_term, tarski.syntax.Term)
    assert model[gamma(shape, scale)].symbol == 1.0629932880924005


def test_arcsin():
    import numpy as np
    from tarski.syntax.arithmetic.special import asin
    lang = tarski.fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    model = Model(lang)
    model.evaluator = evaluate
    reals = lang.Real
    alpha = lang.constant(0.5, reals)
    assert model[asin(alpha)].symbol == np.arcsin(0.5)


def test_blocksworld_add():
    lang = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    model = Model(lang)
    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')
    b2 = lang.get_constant('b2')
    model.add(clear, b1)
    assert evaluate(clear(b1), model) is True
    assert evaluate(clear(b2), model) is False


def test_blocksworld_add_and_remove():
    lang = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    model = Model(lang)

    clear = lang.get_predicate('clear')
    b1 = lang.get_constant('b1')
    b2 = lang.get_constant('b2')

    model.add(clear, b1)
    model.add(clear, b2)
    model.remove(clear, b1)
    assert evaluate(clear(b1), model) is False


def test_zero_ary_predicate_set():
    L = tarski.language()

    P = L.predicate('P')

    M = Model(L)
    M.add(P)

    assert evaluate(P(), M) is True


def test_predicate_extensions():
    lang = tarski.language()
    pred = lang.predicate('pred', lang.Object, lang.Object)

    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)

    model = Model(lang)

    with pytest.raises(errors.ArityMismatch):
        # This should raise an error, as the predicate is binary
        model.add(pred)

    with pytest.raises(ValueError):
        # This should raise an error, as the predicate sort does not coincide with the sort of the parameters
        model.add(pred, 1, 2)

    model.add(pred, o1, o2)
    assert not model.holds(pred, (o2, o1))  # Make sure the order in which the elements were added is respected!
    assert model.holds(pred, (o1, o2))

    with pytest.raises(KeyError):
        # This should raise an error, as the tuple does not belong to the predicate's extension
        model.remove(pred, o2, o1)

    model.remove(pred, o1, o2)
    with pytest.raises(KeyError):
        # This should raise an error, as the tuple has been removed
        model.remove(pred, o1, o2)


def test_predicate_without_equality():
    lang = tarski.language(theories=[Theory.ARITHMETIC])
    leq = lang.predicate('leq', lang.Integer, lang.Integer)
    f = lang.function('f', lang.Object, lang.Integer)
    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)

    model = Model(lang)
    model.evaluator = evaluate

    model.set(f(o1), 1)
    model.set(f(o2), 2)
    for x in range(0, 5):
        for y in range(x, 5):
            model.add(leq, x, y)

    assert model[leq(f(o1), f(o2))] is True
    assert model[leq(f(o2), f(o1))] is False


def test_model_list_extensions():
    lang = tarski.language(theories=[])
    p = lang.predicate('p', lang.Object, lang.Object)
    f = lang.function('f', lang.Object, lang.Object)
    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)

    model = Model(lang)
    model.evaluator = evaluate

    # Test that empty extensions are also returned by `list_all_extensions`
    extensions = model.list_all_extensions()
    assert extensions[p.signature] == set()
    assert len(extensions[f.signature]) == 0

    model.set(f(o1), o2)
    model.add(p, o1, o2)

    extensions = model.list_all_extensions()
    ext_f = extensions[f.signature]
    ext_p = extensions[p.signature]

    # We want to test that the `list_all_extensions` method correctly unwraps all TermReferences in the internal
    # representation of the model and returns _only_ actual Tarski terms. Testing this is a bit involved, as of
    # course we cannot just check for (o1, o2) in ext_f, because that will trigger the wrong __eq__ and __hash__
    # methods - in other words, to test this we precisely need to wrap things back into TermReferences, so that we can
    # compare them properly

    assert len(ext_f) == 1 and len(ext_p) == 1
    p, v = ext_f[0]
    assert symref(p) == symref(o1) and symref(v) == symref(o2)
    v1, v2 = ext_p[0]
    assert symref(v1) == symref(o1) and symref(v2) == symref(o2)


def test_model_as_atoms():
    lang = tarski.language(theories=[])
    p = lang.predicate('p', lang.Object, lang.Object)
    f = lang.function('f', lang.Object, lang.Object)
    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)

    model = Model(lang)
    model.evaluator = evaluate

    model.set(f(o1), o2)
    model.add(p, o1, o2)

    atoms = model.as_atoms()

    patom, fatom = atoms
    assert patom.is_syntactically_equal(p(o1, o2))
    term, value = fatom
    assert term.is_syntactically_equal(f(o1)) and value.is_syntactically_equal(o2)


def test_predicate_without_equality_reals():
    import numpy

    lang = tarski.language(theories=[Theory.ARITHMETIC])
    leq = lang.predicate('leq', lang.Real, lang.Real)
    w = lang.function('w', lang.Object, lang.Real)
    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)

    model = Model(lang)
    model.evaluator = evaluate

    model.set(w(o1), 1.0)
    model.set(w(o2), 2.0)
    for x in numpy.arange(0.0, 5.0):
        for y in numpy.arange(x, 5.0):
            model.add(leq, x, y)

    assert model[leq(w(o1), w(o2))] is True
    assert model[leq(w(o2), w(o1))] is False


def test_ite():
    lang = tarski.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])

    c = lang.constant(1, lang.Integer)

    x = lang.function('x', lang.Integer)
    y = lang.function('y', lang.Integer)

    phi = (x() <= y()) & (y() <= x())

    t1 = x() + 2
    t2 = y() + 3

    tau = ite(phi, t1, t2)

    model = Model(lang)
    model.evaluator = evaluate

    model.set(x(), 1)
    model.set(y(), 2)

    assert model[tau].symbol == 5


def test_matrix_evaluation_case_1():
    from tarski.syntax.arithmetic import one
    lang = tarski.language('double_integrator', [Theory.EQUALITY, Theory.ARITHMETIC])
    I = lang.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], lang.Real)
    x0 = Model(lang)
    x0.evaluator = evaluate
    assert x0[I][0, 0].is_syntactically_equal(one(lang.Real))


def test_matrix_evaluation_case_2():
    lang = tarski.language('double_integrator', [Theory.EQUALITY, Theory.ARITHMETIC])
    I = lang.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]], lang.Real)
    x = lang.function('x', lang.Real)
    y = lang.function('y', lang.Real)
    z = lang.function('z', lang.Real)

    v = lang.vector([x(), y(), z()], lang.Real)

    x0 = Model(lang)
    x0.evaluator = evaluate

    x0.set(x(), 1.0)
    x0.set(y(), 2.0)
    x0.set(z(), 3.0)
    # print(x0[I @ v][2, 0])
    assert x0[I @ v][2, 0].is_syntactically_equal(lang.constant(3.0, lang.Real))
