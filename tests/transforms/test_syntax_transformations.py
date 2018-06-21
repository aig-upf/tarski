import pytest

from tarski.syntax import *
from tests.common import blocksworld
from tests.common import tarskiworld

from tarski.syntax.transform.nnf import NNFTransformation
from tarski.syntax.transform.prenex import PrenexTransformation
from tarski.syntax.transform.univ_elim import UniversalQuantifierElimination
from tarski.syntax.transform import CNFTransformation
from tarski.syntax.transform import NegatedBuiltinAbsorption
from tarski.syntax.transform.errors import TransformationError


def test_nnf_conjunction():
    bw = blocksworld.generate_small_fstrips_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    phi = neg(land(loc(b1) != loc(b2), loc(b3) != loc(b4)))
    result = NNFTransformation.rewrite(phi)
    gamma = lor(neg(loc(b1) != loc(b2)), neg(loc(b3) != loc(b4)))

    assert str(result.nnf) == str(gamma)


def test_nnf_double_negation():
    bw = blocksworld.generate_small_fstrips_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    phi = neg(neg(loc(b1) == loc(b2)))
    result = NNFTransformation.rewrite(phi)
    gamma = loc(b1) == loc(b2)

    assert str(result.nnf) == str(gamma)


def test_nnf_quantifier_flips():
    bw = blocksworld.generate_small_fstrips_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    x = bw.variable('x', block)

    phi = neg(exists(x, loc(x) == loc(b2)))
    result = NNFTransformation.rewrite(phi)
    gamma = forall(x, neg(loc(x) == loc(b2)))

    assert str(result.nnf) == str(gamma)


def test_nnf_LPL_page_321_antecedent():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)
    y = tw.variable('y', tw.Object)
    s = forall(x, neg(land(tw.Cube(x), exists(y, land(tw.Tet(x), tw.LeftOf(x, y))))))
    result = NNFTransformation.rewrite(s)
    gamma = forall(x, lor(neg(tw.Cube(x)), forall(y, lor(neg(tw.Tet(x)), neg(tw.LeftOf(x, y))))))
    assert str(result.nnf) == str(gamma)


def test_prenex_idempotency():
    bw = blocksworld.generate_small_fstrips_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    x = bw.variable('x', block)

    phi = loc(b1) == b2
    result = PrenexTransformation.rewrite(bw, phi)
    gamma = loc(b1) == b2

    assert str(result.prenex) == str(gamma)


def test_prenex_LPL_page_321():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)

    y = tw.variable('y', tw.Object)
    s1 = exists(y, land(tw.Dodec(y), tw.BackOf(x, y)))
    s2 = land(tw.Cube(x), exists(y, land(tw.Tet(y), tw.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    result = PrenexTransformation.rewrite(tw, phi)
    yp = tw.variable("y'", tw.Object)
    gamma = NNFTransformation.rewrite(exists(yp, \
                                             forall(x, y, implies(land(tw.Cube(x), land(tw.Tet(y), tw.LeftOf(x, y))), \
                                                                  land(tw.Dodec(yp), tw.BackOf(x, yp)))))).nnf

    assert str(result.prenex) == str(gamma)


def test_universal_elimination_fails_due_to_no_constants():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)

    y = tw.variable('y', tw.Object)
    s1 = exists(y, land(tw.Dodec(y), tw.BackOf(x, y)))
    s2 = land(tw.Cube(x), exists(y, land(tw.Tet(y), tw.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    # print(str(phi))
    with pytest.raises(TransformationError):
        result = UniversalQuantifierElimination.rewrite(tw, phi)
        # print(str(result.universal_free))


def test_universal_elimination_works():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)

    y = tw.variable('y', tw.Object)

    obj1 = tw.constant('obj1', tw.Object)
    obj2 = tw.constant('obj2', tw.Object)
    obj3 = tw.constant('obj3', tw.Object)

    s1 = exists(y, land(tw.Dodec(y), tw.BackOf(x, y)))
    s2 = land(tw.Cube(x), exists(y, land(tw.Tet(y), tw.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    # print(str(phi))
    result = UniversalQuantifierElimination.rewrite(tw, phi)
    # print(str(result.universal_free))
    result2 = UniversalQuantifierElimination.rewrite(tw, result.universal_free)
    # print(str(result2.universal_free))
    assert str(result.universal_free) == str(result2.universal_free)


def test_builtin_negation_absorption():
    bw = blocksworld.generate_small_fstrips_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    x = bw.variable('x', block)

    phi = neg(loc(b1) == b2)
    psi = loc(b1) != b2

    r = NegatedBuiltinAbsorption.rewrite(bw, phi)
    assert str(r.formula) == str(psi)


def test_cnf_conversion_easy():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)

    y = tw.variable('y', tw.Object)

    obj1 = tw.constant('obj1', tw.Object)
    obj2 = tw.constant('obj2', tw.Object)
    obj3 = tw.constant('obj3', tw.Object)

    s1 = land(tw.Cube(obj1), neg(tw.Tet(obj2)))
    s2 = land(tw.Cube(obj2), neg(tw.Tet(obj1)))
    phi = lor(s1, s2)
    c1 = lor(tw.Cube(obj1), tw.Cube(obj2))
    c2 = lor(tw.Cube(obj1), neg(tw.Tet(obj1)))
    c3 = lor(neg(tw.Tet(obj2)), tw.Cube(obj2))
    c4 = lor(neg(tw.Tet(obj2)), neg(tw.Tet(obj1)))
    psi = land(land(c1, c2), land(c3, c4))
    result = CNFTransformation.rewrite(tw, phi)
    assert str(result.cnf) == str(psi)


def test_cnf_conversion_complex():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)

    y = tw.variable('y', tw.Object)

    obj1 = tw.constant('obj1', tw.Object)
    obj2 = tw.constant('obj2', tw.Object)
    obj3 = tw.constant('obj3', tw.Object)

    s1 = exists(y, land(tw.Dodec(y), tw.BackOf(x, y)))
    s2 = land(tw.Cube(x), exists(y, land(tw.Tet(y), tw.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    result = UniversalQuantifierElimination.rewrite(tw, phi)
    result2 = CNFTransformation.rewrite(tw, result.universal_free.formula)
    # print(result2.cnf)
    # print('\n'.join( [ ','.join([str(l) for l in c]) for c in result2.clauses ] ) )
    # print(len(result2.clauses))
    assert len(result2.clauses) == 34
