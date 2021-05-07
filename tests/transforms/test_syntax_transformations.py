import pytest

import tarski.benchmarks.blocksworld
from tarski.fstrips.representation import is_quantifier_free
from tarski.syntax import *
from tests.common import tarskiworld

from tarski.syntax.transform.nnf import NNFTransformation
from tarski.syntax.transform.cnf import to_conjunctive_normal_form_clauses
from tarski.syntax.transform.prenex import to_prenex_negation_normal_form
from tarski.syntax.transform import CNFTransformation, QuantifierElimination, remove_quantifiers, \
    QuantifierEliminationMode
from tarski.syntax.transform import NegatedBuiltinAbsorption
from tarski.syntax.transform.errors import TransformationError


def test_nnf_conjunction():
    bw = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    _ = bw.get_sort('block')
    _ = bw.get_sort('place')
    loc = bw.get_function('loc')
    _ = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    _ = bw.get_constant('table')

    phi = neg(land(loc(b1) != loc(b2), loc(b3) != loc(b4)))
    result = NNFTransformation.rewrite(phi)
    gamma = lor(neg(loc(b1) != loc(b2)), neg(loc(b3) != loc(b4)))

    assert str(result.nnf) == str(gamma)


def test_nnf_double_negation():
    bw = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    _ = bw.get_sort('block')
    _ = bw.get_sort('place')
    loc = bw.get_function('loc')
    _ = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    _ = bw.get_constant('table')

    phi = neg(neg(loc(b1) == loc(b2)))
    result = NNFTransformation.rewrite(phi)
    gamma = loc(b1) == loc(b2)

    assert str(result.nnf) == str(gamma)


def test_nnf_quantifier_flips():
    bw = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    block = bw.get_sort('block')
    loc = bw.get_function('loc')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]

    x = bw.variable('x', block)

    phi = neg(exists(x, loc(x) == loc(b2)))
    result = NNFTransformation.rewrite(phi)
    gamma = forall(x, neg(loc(x) == loc(b2)))

    assert str(result.nnf) == str(gamma)


def test_nnf_lpl_page_321_antecedent():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)
    y = tw.variable('y', tw.Object)
    s = forall(x, neg(land(tw.Cube(x), exists(y, land(tw.Tet(x), tw.LeftOf(x, y))))))
    result = NNFTransformation.rewrite(s)
    gamma = forall(x, lor(neg(tw.Cube(x)), forall(y, lor(neg(tw.Tet(x)), neg(tw.LeftOf(x, y))))))
    assert str(result.nnf) == str(gamma)


def test_prenex_idempotency():
    bw = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    loc = bw.get_function('loc')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]

    phi = loc(b1) == b2
    assert str(to_prenex_negation_normal_form(bw, phi, do_copy=True)) == str(phi)


def test_prenex_lpl_page_321():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)

    y = tw.variable('y', tw.Object)
    s1 = exists(y, land(tw.Dodec(y), tw.BackOf(x, y)))
    s2 = land(tw.Cube(x), exists(y, land(tw.Tet(y), tw.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))

    yp = tw.variable("y'", tw.Object)
    gamma = NNFTransformation.rewrite(exists(yp, forall(
        x, y, implies(land(tw.Cube(x), land(tw.Tet(y), tw.LeftOf(x, y))), land(tw.Dodec(yp), tw.BackOf(x, yp)))))).nnf

    assert str(to_prenex_negation_normal_form(tw, phi, do_copy=True)) == str(gamma)


def test_quantifier_elimination_fails_due_to_no_constants():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)
    y = tw.variable('y', tw.Object)
    s1 = exists(y, land(tw.Dodec(y), tw.BackOf(x, y)))
    s2 = land(tw.Cube(x), exists(y, land(tw.Tet(y), tw.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    with pytest.raises(TransformationError):
        QuantifierElimination.rewrite(tw, phi, QuantifierEliminationMode.All)


def test_universal_elimination_works():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)

    y = tw.variable('y', tw.Object)

    _ = tw.constant('obj1', tw.Object)
    _ = tw.constant('obj2', tw.Object)
    _ = tw.constant('obj3', tw.Object)

    s1 = exists(y, land(tw.Dodec(y), tw.BackOf(x, y)))
    s2 = land(tw.Cube(x), exists(y, land(tw.Tet(y), tw.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    # print(str(phi))
    result = remove_quantifiers(tw, phi, QuantifierEliminationMode.Forall)
    result2 = remove_quantifiers(tw, result, QuantifierEliminationMode.Forall)
    assert str(result) == str(result2)


def create_small_world_elements(numobjects=3):
    lang = tarskiworld.create_small_world()
    x, y = lang.variable('x', lang.Object), lang.variable('y', lang.Object)
    _ = [lang.constant(f'obj{i}', lang.Object) for i in range(1, numobjects + 1)]
    return lang, x, y


def test_existential_elimination1():
    lang, x, y = create_small_world_elements(2)
    obj1, obj2 = lang.get("obj1"), lang.get("obj2")

    phi = exists(y, land(lang.Dodec(y), lang.BackOf(x, y)))
    result = remove_quantifiers(lang, phi, QuantifierEliminationMode.Exists)

    # We cannot guarantee in which order the expansion of the exists will be done, so we check for both possibilities:
    assert result == (lang.Dodec(obj1) & lang.BackOf(x, obj1)) | (lang.Dodec(obj2) & lang.BackOf(x, obj2)) or \
        result == (lang.Dodec(obj2) & lang.BackOf(x, obj2)) | (lang.Dodec(obj1) & lang.BackOf(x, obj1))


def test_existential_elimination2():
    lang, x, y = create_small_world_elements(2)

    s1 = exists(y, land(lang.Dodec(y), lang.BackOf(x, y)))
    s2 = land(lang.Cube(x), exists(y, land(lang.Tet(y), lang.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    result = remove_quantifiers(lang, phi, QuantifierEliminationMode.All)
    assert is_quantifier_free(result)


def test_builtin_negation_absorption():
    bw = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()
    block = bw.get_sort('block')
    _ = bw.get_sort('place')
    loc = bw.get_function('loc')
    _ = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    _ = bw.get_constant('table')

    _ = bw.variable('x', block)

    phi = neg(loc(b1) == b2)
    psi = loc(b1) != b2

    r = NegatedBuiltinAbsorption.rewrite(bw, phi)
    assert str(r.formula) == str(psi)


def test_cnf_conversion_easy():
    tw = tarskiworld.create_small_world()

    obj1 = tw.constant('obj1', tw.Object)
    obj2 = tw.constant('obj2', tw.Object)
    _ = tw.constant('obj3', tw.Object)

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
    lang, x, y = create_small_world_elements(2)

    s1 = exists(y, land(lang.Dodec(y), lang.BackOf(x, y)))
    s2 = land(lang.Cube(x), exists(y, land(lang.Tet(y), lang.LeftOf(x, y))))
    phi = forall(x, implies(s2, s1))
    result = remove_quantifiers(lang, phi, QuantifierEliminationMode.All)
    assert len(to_conjunctive_normal_form_clauses(lang, result)) == 30

    # Now remove the quantifiers after tranforming to PNNF
    result = remove_quantifiers(lang, to_prenex_negation_normal_form(lang, phi), QuantifierEliminationMode.All)
    assert len(to_conjunctive_normal_form_clauses(lang, result)) == 126
