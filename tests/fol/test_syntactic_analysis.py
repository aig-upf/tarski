from tarski.syntax import *
from tarski.syntax.visitors import CollectFreeVariables, SymbolReference, esm
from tests.common import tarskiworld


def test_symbol_ref_in_sets_equality_is_exact_syntactic_match():
    tw = tarskiworld.create_small_world()
    x = tw.variable('x', tw.Object)
    y = tw.variable('y', tw.Object)
    x_ref = SymbolReference(x, esm)
    y_ref = SymbolReference(y, esm)
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
    v = CollectFreeVariables(tw)
    s.accept(v)
    assert len(list(v.free_variables)) == 1
