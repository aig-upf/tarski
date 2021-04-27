
import copy
from collections import defaultdict

import pytest

from tarski import theories, Term, Constant
from tarski.benchmarks.blocksworld import generate_strips_bw_language
from tarski.fstrips import fstrips
from tarski.syntax import symref, CompoundFormula, Atom, ite, AggregateCompoundTerm, CompoundTerm, lor, Tautology, \
    Contradiction, land, top, bot
from tarski.theories import Theory
from tarski import errors as err
from tarski import fstrips as fs
from tarski.syntax.algebra import Matrix

from ..common import numeric


def test_language_creation():
    lang = theories.language()
    sorts = sorted(x.name for x in lang.sorts)
    assert sorts == ['object']

    lang = fstrips.language("test", theories=[])
    sorts = sorted(x.name for x in lang.sorts)
    assert sorts == ['object']

    lang = fstrips.language("test")
    sorts = sorted(x.name for x in lang.sorts)
    assert sorts == ['object']  # The default equality theory should not import the arithmetic sorts either


def test_builtin_constants():
    lang = fstrips.language(theories=[Theory.ARITHMETIC])
    ints = lang.Integer
    two = lang.constant(2, ints)
    assert isinstance(two, Constant), "two should be the constant 2, not the integer value 2"


def test_arithmetic_term_plus_float_lit_is_term():
    lang = numeric.generate_numeric_instance()
    _ = lang.get_sort('particle')
    p1 = lang.get_constant('p1')
    x = lang.get_function('x')
    t = x(p1) + 1.0
    assert isinstance(t, CompoundTerm)
    assert isinstance(t.subterms[0], Term)
    assert isinstance(t.subterms[1], Term)


def test_arithmetic_terms_does_not_fail_with_load_theory():
    lang = fstrips.language(theories=[Theory.ARITHMETIC])
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    sum_ = two + three
    assert isinstance(sum_, Term), "sum_ should be the term +(Const(2), Const(3)), not the integer value 5"


def test_load_arithmetic_module_fails_when_language_frozen():
    lang = fstrips.language(theories=[Theory.ARITHMETIC])
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)

    with pytest.raises(err.DuplicateTheoryDefinition):
        # load_theory() should raise exception since arithmetic theory is already loaded
        theories.load_theory(lang, Theory.ARITHMETIC)


def test_load_booleans():
    lang = fstrips.language(theories=["boolean"])
    assert len(list(lang.get('Boolean').domain())) == 2


def test_special_terms_does_not_fail_with_load_theory():
    from tarski.syntax.builtins import BuiltinFunctionSymbol
    lang = fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    assert Theory.SPECIAL in lang.theories
    _ = lang.get_function(BuiltinFunctionSymbol.MAX)


def test_special_term_construction():
    from tarski.syntax.arithmetic.special import max
    lang = fstrips.language(theories=[Theory.ARITHMETIC, Theory.SPECIAL])
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    max_ = max(two, three)
    assert isinstance(max_, Term), "max_ should be the term max(Const(2), Const(3)), not the integer value 3"


def test_equality_atom_from_expression():
    lang = fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])
    y = lang.function('y', lang.Integer)
    assert isinstance(y() == 4, Atom)


def test_complex_atom_from_expression_function_and_constants():
    lang = fstrips.language('artih', [Theory.EQUALITY, Theory.ARITHMETIC])
    y = lang.function('y', lang.Integer)

    phi = (y() <= 4) & (-4 <= y())
    assert isinstance(phi, CompoundFormula)


def test_complex_atom_from_expression_only_functions():
    lang = fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])
    x = lang.function('x', lang.Integer)
    y = lang.function('y', lang.Integer)
    z = lang.function('z', lang.Integer)

    phi = (x() <= y()) & (y() <= z())
    assert isinstance(phi, CompoundFormula)


def test_copying_and_equality():
    lang = fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])

    c = lang.constant(1, lang.Integer)

    x = lang.function('x', lang.Integer)
    y = lang.function('y', lang.Integer)
    _ = lang.function('f', lang.Integer, lang.Integer, lang.Integer)

    _ = copy.deepcopy(c)

    phi = (x() <= y()) & (y() <= x())
    shallow = copy.copy(phi)
    deep = copy.deepcopy(phi)
    # phi3 = (x() <= y()) & (y() <= x())
    assert isinstance(phi, CompoundFormula)
    assert isinstance(shallow, CompoundFormula)
    assert isinstance(deep, CompoundFormula)
    assert shallow.connective == phi.connective
    assert id(shallow.connective) == id(phi.connective)
    assert id(shallow.subformulas) == id(phi.subformulas)
    assert id(shallow.subformulas[0]) == id(phi.subformulas[0])

    assert deep.connective == phi.connective
    assert id(deep.subformulas) != id(phi.subformulas)
    assert id(deep.subformulas[0]) != id(phi.subformulas[0])

    # TODO Test equality


def test_duplicate_detection_and_global_getter():
    lang = fstrips.language("test")

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
    assert (all(id(x) == id(y) for x, y in zip([t1, c1, f1, p1], lang.get('t1', 'c1', 'f1', 'p1'))))


def test_term_refs():
    lang = fstrips.language(theories=[Theory.ARITHMETIC])
    _ = lang.function('f', lang.Object, lang.Integer)
    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)

    tr1 = symref(o1)
    tr2 = symref(o1)
    tr3 = symref(o2)

    assert tr1 == tr2
    assert tr1 != tr3


def test_object_function_arity():
    fol = fstrips.language()
    block = fol.sort('block')
    # MRJ: Note that first argument is name of function, following arguments
    # denote the domain and codomain of the function. The previous definition
    # loc = fol.function('loc', 'block')
    # actually defines a 0-arity term, which denotes one element of the sort
    # block, or a mapping between the symbol loc() and a constant of sort block.
    # I think that  what was intended, was an actual function like
    # loc: block -> block, a mapping between elements of the sort block.
    loc = fol.function('loc', 'block', 'block')

    b1 = fol.constant('b1', block)
    b2 = fol.constant('b2', block)

    _ = (loc(b1) == b2)


def test_term_refs_compound():
    lang = fstrips.language(theories=[Theory.ARITHMETIC])
    f = lang.function('f', lang.Object, lang.Integer)
    o1 = lang.constant("o1", lang.Object)
    o2 = lang.constant("o2", lang.Object)
    _ = lang.get('f')

    t1 = f(o1)
    t2 = f(o1)
    t3 = f(o2)
    assert t1.symbol == t2.symbol
    tr1 = symref(t1)
    tr2 = symref(t2)
    tr3 = symref(t3)

    assert tr1 == tr2
    assert tr1 != tr3


def test_formula_refs():
    lang = fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])

    _ = lang.constant(1, lang.Integer)

    x = lang.function('x', lang.Integer)
    y = lang.function('y', lang.Integer)

    phi = (x() <= y()) & (y() <= x())
    psi = (x() >= y()) & (y() <= x())
    gamma = (x() <= y()) & (y() <= x())

    fr1 = symref(phi)
    fr2 = symref(psi)
    fr3 = symref(gamma)

    assert fr1 == fr3
    assert fr1 != fr2


def test_ite():
    lang = fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])

    _ = lang.constant(1, lang.Integer)

    x = lang.function('x', lang.Integer)
    y = lang.function('y', lang.Integer)

    phi = (x() <= y()) & (y() <= x())

    t1 = x() + 2
    t2 = y() + 3

    tau = ite(phi, t1, t2)

    assert tau.condition.is_syntactically_equal(phi)
    assert tau.subterms[0].is_syntactically_equal(t1)
    assert tau.subterms[1].is_syntactically_equal(t2)
    assert tau.sort == t1.sort


def test_sumterm():
    from tarski.syntax.arithmetic import sumterm

    lang = fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])

    _ = lang.constant(1, lang.Integer)
    _ = lang.constant('o1', lang.Object)
    _ = lang.constant('o2', lang.Object)

    x = lang.function('x', lang.Object, lang.Integer)
    y = lang.function('y', lang.Object, lang.Integer)

    o = lang.variable('o', lang.Object)

    summation = sumterm(o, x(o) + y(o))
    assert isinstance(summation, AggregateCompoundTerm)


def test_prodterm():
    from tarski.syntax.arithmetic import prodterm
    lang = fstrips.language('arith', [Theory.EQUALITY, Theory.ARITHMETIC])

    _ = lang.constant(1, lang.Integer)
    _ = lang.constant('o1', lang.Object)
    _ = lang.constant('o2', lang.Object)

    x = lang.function('x', lang.Object, lang.Integer)
    y = lang.function('y', lang.Object, lang.Integer)

    o = lang.variable('o', lang.Object)

    product = prodterm(o, x(o) + y(o))
    assert isinstance(product, AggregateCompoundTerm)


def test_matrices_constants():
    lang = fstrips.language('test', [Theory.EQUALITY, Theory.ARITHMETIC])
    A = lang.matrix([[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]], lang.Real)
    assert isinstance(A, Matrix)
    N, M = A.shape
    for i in range(N):
        for j in range(M):
            assert isinstance(A.matrix[i, j], Term)


def test_term_hash_raises_exception():
    # from tarski.fstrips import language
    # from tarski.syntax import symref
    lang = fs.language("test")
    counter = defaultdict(int)

    c = lang.constant('c', 'object')
    f = lang.function('f', 'object', 'object')

    # Trying to use associative containers on terms raises a standard TypeError
    with pytest.raises(TypeError):
        counter[c] += 2

    with pytest.raises(TypeError):
        counter[f(c)] += 2

    # Using symrefs instead works correctly:
    counter[symref(c)] += 2
    assert counter[symref(c)] == 2

    counter[symref(f(c))] += 2
    assert counter[symref(f(c))] == 2

    # Atoms and in general formulas can be used without problem
    atom = f(c) == c
    counter[atom] += 2
    assert counter[atom] == 2


def test_syntax_shorthands():
    assert lor(*[]) == Contradiction(), "a lor(·) of no disjuncts is False"
    assert land(*[]) == Tautology(), "a land(·) of no conjuncts is True"
    assert land(bot & top) == bot & top, "A land(·) of a single element returns that single element"


def test_numeric_sort_deduction():
    lang = fstrips.language(theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    plus0 = Constant(1, lang.Integer) + 1
    # Disable the test temporarily until we address issue #93
    # assert plus0.sort == lang.Integer

    # The sorts
    particle = lang.sort('bowl')

    eggs = lang.function('eggs', lang.Object, lang.Integer)
    bowl_1 = lang.constant('bowl_1', particle)
    plus1 = eggs(bowl_1) + 1

    # Disable the test temporarily until we address issue #93
    # assert plus1.sort == lang.Integer


def test_language_equality():
    lang1 = generate_strips_bw_language(nblocks=2)
    lang2 = generate_strips_bw_language(nblocks=2)

    # At the moment it's not clear what kind of FOL language object comparison we want.
    # Ideally we'd want to make sure that the language contains exactly the same vocabulary,
    # including the same objects/constants, the same sorts, etc. But this is too expensive to
    # compare on the fly. To alleviate this, we could "freeze" the language objects and compute and store a hash
    # But so far it's not clear it's worth the effort, as we don't have an obvious use case where this would be
    # necessary.
    # assert lang1 == lang2
    #
    # lang1.constant('c', 'object')
    # assert lang1 != lang2
