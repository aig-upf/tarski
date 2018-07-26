import pytest
import tarski as tsk
from tarski import theories
from tarski.theories import Theory
from tarski import errors as err
from tarski.syntax import *

from ..common import numeric


def test_builtin_constants():
    lang = tsk.fstrips.language()
    ints = lang.Integer
    two = lang.constant(2, ints)
    assert isinstance(two, Constant), "two should be the constant 2, not the integer value 2"


def test_arithmetic_terms_fails_without_import():
    lang = tsk.fstrips.language()
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    with pytest.raises(err.LanguageError):
        # This should raise TypeError as the arithmetic module has not been loaded
        sum_ = two + three


def test_arithmetic_term_plus_float_lit_is_term():
    lang = numeric.generate_numeric_instance()
    particle = lang.get_sort('particle')
    p1 = lang.get_constant('p1')
    x = lang.get_function('x')
    t = x(p1) + 1.0
    assert isinstance(t, tsk.Term)
    assert isinstance(t.subterms[0], tsk.Term)
    assert isinstance(t.subterms[1], tsk.Term)


def test_arithmetic_terms_does_not_fail_with_load_theory():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    sum_ = two + three
    assert isinstance(sum_, tsk.Term), "sum_ should be the term +(Const(2), Const(3)), not the integer value 5"


def test_load_arithmetic_module_fails_when_language_frozen():
    lang = tsk.fstrips.language()
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)

    with pytest.raises(err.LanguageError):
        # load_theory() should raise LanguageError as we have created two constants
        theories.load_theory(lang, Theory.ARITHMETIC)
        sum_ = two + three

def test_special_terms_does_not_fail_with_load_theory():
    from tarski.syntax.builtins import BuiltinFunctionSymbol
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC,Theory.SPECIAL])
    assert Theory.SPECIAL in lang.theories
    max_func = lang.get_function(BuiltinFunctionSymbol.MAX)


def test_special_term_construction():
    from tarski.syntax.arithmetic.special import max
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC,Theory.SPECIAL])
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    max_ = max(two,three)
    assert isinstance(max_, tsk.Term), "max_ should be the term max(Const(2), Const(3)), not the integer value 3"

def test_equality_atom_from_expression():
    lang = tsk.fstrips.language('artih', [Theory.EQUALITY, Theory.ARITHMETIC])
    y = lang.function('y', lang.Integer)

    atom = y() == 4

    assert isinstance(atom, Atom)


def test_complex_atom_from_expression_function_and_constants():
    lang = tsk.fstrips.language('artih', [Theory.EQUALITY, Theory.ARITHMETIC])
    y = lang.function('y', lang.Integer)

    phi = (y() <= 4) & (-4 <= y())

    assert isinstance(phi, CompoundFormula)


def test_complex_atom_from_expression_only_functions():
    lang = tsk.fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])
    x = lang.function('x', lang.Integer)
    y = lang.function('y', lang.Integer)
    z = lang.function('z', lang.Integer)

    phi = (x() <= y()) & (y() <= z())

    assert isinstance(phi, CompoundFormula)

def test_summation_generates_compound_term():
    from tarski.syntax.arithmetic import summation
    lang = numeric.generate_billiards_instance()
    m, F, a, v, p = [lang.get_function(n) for n in ['m', 'F', 'a', 'v', 'p']]
    x = lang.get_constant('x')
    ball_1 = lang.get_constant('ball_1')

    ftype = Variable('ftype', lang.get_sort('force'))
    t = summation(ftype, F(ftype, x, ball_1))
    print(t)
    assert isinstance(t, CompoundTerm)

def test_summation_in_predicate():
    from tarski.syntax.arithmetic import summation
    lang = numeric.generate_billiards_instance()
    m, F, a, v, p = [lang.get_function(n) for n in ['m', 'F', 'a', 'v', 'p']]
    x = lang.get_constant('x')
    ball_1 = lang.get_constant('ball_1')

    ftype = Variable('ftype', lang.get_sort('force'))
    prop_ball =  a(x, ball_1) == (summation(ftype, F(ftype, x, ball_1)) / m(ball_1))
    print(prop_ball)
    assert isinstance(prop_ball, Formula)

def test_summation_in_quantified_formula():
    from tarski.syntax.arithmetic import summation
    lang = numeric.generate_billiards_instance()
    m, F, a, v, p = [lang.get_function(n) for n in ['m', 'F', 'a', 'v', 'p']]

    b = Variable('b', lang.get_sort('ball'))
    d = Variable('d', lang.get_sort('dimension'))
    ftype = Variable('ftype', lang.get_sort('force'))
    # The principle of superposition
    pos =  forall(b, d, a(d, b) == (summation(ftype, F(ftype, d, b)) / m(b)) )
    print(pos)
    assert isinstance(pos, QuantifiedFormula)
