from tarski.syntax import *
from tests.common import blocksworld
from tests.common import tarskiworld

from tarski.syntax.transform.nnf import NNFTransformation
from tarski.syntax.transform.prenex import PrenexTransformation

def test_nnf_conjunction():

    bw = blocksworld.generate_small_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    phi = neg( land( loc(b1) != loc(b2), loc(b3) != loc(b4)))
    result = NNFTransformation.rewrite(phi)
    gamma = lor( neg(loc(b1)!=loc(b2)), neg(loc(b3)!=loc(b4)))

    assert str(result.nnf) == str(gamma)

def test_nnf_double_negation():

    bw = blocksworld.generate_small_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    phi = neg( neg( loc(b1) == loc(b2)))
    result = NNFTransformation.rewrite(phi)
    gamma = loc(b1)==loc(b2)

    assert str(result.nnf) == str(gamma)

def test_nnf_quantifier_flips():

    bw = blocksworld.generate_small_bw_language()
    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    x = bw.variable('x', block)

    phi = neg( exists( x, loc(x) == loc(b2)))
    result = NNFTransformation.rewrite(phi)
    gamma = forall(x, neg(loc(x) == loc(b2)))

    assert str(result.nnf) == str(gamma)

def test_prenex_idempotency():

    bw = blocksworld.generate_small_bw_language()
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
    s1 = exists( y, land( tw.Dodec(y), tw.BackOf(x,y) ) )
    s2 = land( tw.Cube(x), exists( y, land(tw.Tet(y), tw.LeftOf(x,y)) ) )
    phi = forall( x, implies(s2,s1))
    result = PrenexTransformation.rewrite(tw, phi)
    yp = tw.variable("y'",tw.Object)
    gamma = NNFTransformation.rewrite(exists( yp,\
                forall( x,y, implies( land( tw.Cube(x), land(tw.Tet(y), tw.LeftOf(x,y))),\
                                        land(tw.Dodec(yp),tw.BackOf(x,yp)))))).nnf

    assert str(result.prenex) == str(gamma)
