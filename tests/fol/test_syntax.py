
import copy

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


def test_equality_atom_from_expression():
    lang = tsk.fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])
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


def test_copying_and_equality():
    lang = tsk.fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])

    c = lang.constant(1, lang.Integer)

    x = lang.function('x', lang.Integer)
    y = lang.function('y', lang.Integer)
    f = lang.function('f', lang.Integer, lang.Integer, lang.Integer)

    deep = copy.deepcopy(c)
    # deep = copy.deepcopy(x)

    phi = (x() <= y()) & (y() <= x())
    shallow = copy.copy(phi)
    deep = copy.deepcopy(phi)
    # phi3 = (x() <= y()) & (y() <= x())

    assert shallow.connective == phi.connective
    assert id(shallow.connective) == id(phi.connective)
    assert id(shallow.subformulas) == id(phi.subformulas)
    assert id(shallow.subformulas[0]) == id(phi.subformulas[0])

    assert deep.connective == phi.connective
    assert id(deep.subformulas) != id(phi.subformulas)
    assert id(deep.subformulas[0]) != id(phi.subformulas[0])

    # TODO Test equality


def test_duplicate_detection_and_global_getter():
    lang = tsk.FirstOrderLanguage("test")

    t1 = lang.sort('t1')
    c1 = lang.constant('c1', lang.Object)
    f1 = lang.function('f1', lang.Object)
    p1 = lang.predicate('p1')

    # Redeclaring things raises exceptions of appropriate types
    with pytest.raises(err.DuplicateSortDefinition):
        lang.sort('t1')
    with pytest.raises(err.DuplicateConstantDefinition):
        lang.constant('c1', lang.Object)
    with pytest.raises(err.DuplicateFunctionDefinition):
        lang.function('f1', lang.Object)
    with pytest.raises(err.DuplicatePredicateDefinition):
        lang.predicate('p1')

    # Declaring any language element with same name as a language element of a different type also  raises exception
    with pytest.raises(err.DuplicateDefinition):
        lang.sort('p1')
    with pytest.raises(err.DuplicateDefinition):
        lang.constant('t1', lang.Object)
    with pytest.raises(err.DuplicateDefinition):
        lang.function('c1', lang.Object)
    with pytest.raises(err.DuplicateDefinition):
        lang.predicate('f1')

    assert id(lang.get('t1')) == id(t1)
    assert id(lang.get('c1')) == id(c1)
    assert id(lang.get('f1')) == id(f1)
    assert id(lang.get('p1')) == id(p1)

    assert len(lang.get('t1', 'c1', 'f1', 'p1')) == 4
    assert(all(id(x) == id(y) for x, y in zip([t1, c1, f1, p1], lang.get('t1', 'c1', 'f1', 'p1'))))


def test_term_refs():
    lang = tsk.language()
    f = lang.function('f', lang.Object, lang.Integer)
    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)

    tr1 = TermReference(o1)
    tr2 = TermReference(o1)
    tr3 = TermReference(o2)

    assert tr1 == tr2
    assert tr1 != tr3
