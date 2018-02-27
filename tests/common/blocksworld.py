"""
    Generate blocksworld language elements
"""
import tarski as tsk
import tarski.model

from tarski import fstrips as fs
from tarski.syntax import *
from tarski.syntax.temporal import ltl

def generate_small_bw_language():
    lang = tsk.language()

    # The sorts
    place = lang.sort('place')
    block = lang.sort('block', [place])

    lang.predicate('clear', place)
    lang.function('loc', block, place)

    # Table and blocks
    lang.constant('table', place)
    [lang.constant('b{}'.format(k), block) for k in range(1, 5)]
    return lang

def create_small_task():
    bw = generate_small_bw_language()
    M = tarski.model.create(bw)

    block = bw.get_sort('block')
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

    src = bw.variable('src', block)
    dest = bw.variable('dest', block)

    move_schema = fs.Action(bw, name='move', \
                     parameters=[src, dest], \
                     precondition=land(clear(src), clear(dest)),
                     effects = [
                                    ltl.X(loc(src) == dest)
                               ])


    x = bw.variable('x', block)
    y = bw.variable('y', block)
    clear_constraint = forall( x, equiv( neg(clear(x)), land( x != table, exists(y, loc(y) == x ) )) )
    G = land( loc(b1) == b2, loc(b2) == b3, loc(b3) == b4, loc(b4) == table)

    P = fs.Problem( "tower-4", bw, init=M, goal=G, constraints = [clear_constraint], actions=[move_schema])

    return P
