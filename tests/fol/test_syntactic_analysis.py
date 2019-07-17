
from tarski.syntax import neg, land, lor, exists, symref
from tarski.syntax.ops import free_variables, flatten
from tests.common import tarskiworld
from tests.common.blocksworld import generate_bw_loc_and_clear


def test_symbol_ref_in_sets_equality_is_exact_syntactic_match():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)
    y = tw.variable('y', tw.Object)
    x_ref = symref(x)
    y_ref = symref(y)
    S = set()
    S.add(x_ref)
    assert y_ref not in S
    assert x_ref in S
    S.remove(x_ref)
    assert len(S) == 0


def test_detect_free_variables():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)
    y = tw.variable('y', tw.Object)
    s = neg(land(tw.Cube(x), exists(y, land(tw.Tet(x), tw.LeftOf(x, y)))))
    assert len(free_variables(s)) == 1


def test_formula_flattening():
    lang = generate_bw_loc_and_clear(4)

    b1, b2, b3, clear = lang.get('b1', 'b2', 'b3', 'clear')
    f1 = land(clear(b1), clear(b2), clear(b3), clear(b1), flat=True)
    f2 = land(clear(b1), clear(b2), clear(b3), clear(b1), flat=False)

    f3 = lor(clear(b1), clear(b2), clear(b3), clear(b1), flat=True)
    f4 = lor(clear(b1), clear(b2), clear(b3), clear(b1), flat=False)

    assert f1 == flatten(f1)  # both are already flat - this tests for syntactic identity
    assert f3 == flatten(f3)

    # In contrast, f3 and f4 are not flat, so flattening them will change their syntactic form
    z = flatten(f2)
    assert f2 != z and len(z.subformulas) == 4

    z = flatten(f4)
    assert f4 != z and len(z.subformulas) == 4

