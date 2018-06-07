import tarski.model
from tarski.theories import Theory
from tarski import fstrips as fs
from tarski.syntax import *
from tarski.syntax.temporal import ltl

from tests.common.blocksworld import generate_small_bw_language

def create_small_task():
    bw = generate_small_bw_language()
    M = tarski.model.create(bw)

    block = bw.get_sort('block')
    place = bw.get_sort('place')
    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')

    M.set( loc, (b1,), b2) # loc(b1) := b2
    M.set( loc, (b2,), b3) # loc(b2) := b3
    M.set( loc, (b3,), table) # loc(b3) := table
    M.set( loc, (b4,), table) # loc(b4) := table

    M.add( clear, b1) # clear(b1)
    M.add( clear, b4) # clear(b4)
    M.add( clear, table) # clear(table)

    src = bw.variable('src', block)
    dest = bw.variable('dest', place)

    x = bw.variable('x', block)
    y = bw.variable('y', block)
    clear_constraint = forall( x, equiv( neg(clear(x)), land( x != table, exists(y, loc(y) == x ) )) )
    G = land( loc(b1) == b2, loc(b2) == b3, loc(b3) == b4, loc(b4) == table)

    P = fs.Problem()
    P.name = "tower4"
    P.domain_name = "blocksworld"
    P.language = bw
    P.init = M
    P.goal = G
    P.constraints += [clear_constraint]

    P.action('move', [src,dest], land(clear(src), clear(dest)), [fs.FunctionalEffect(loc(src), dest)])

    return P
