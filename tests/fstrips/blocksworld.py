import tarski.model
from tarski import fstrips as fs
from tarski.syntax import *

from tests.common.blocksworld import generate_bw_loc_and_clear


def create_4blocks_task():
    bw = generate_bw_loc_and_clear(4)
    M = tarski.model.create(bw)

    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')
    hand = bw.get_constant('hand')

    M.setx(loc(b1), b2) # loc(b1) := b2
    M.setx(loc(b2), b3) # loc(b2) := b3
    M.setx(loc(b3), table) # loc(b3) := table
    M.setx(loc(b4), table) # loc(b4) := table
    M.setx(loc(table), table)
    M.setx(loc(hand), hand)


    M.add(clear, b1) # clear(b1)
    M.add(clear, b4) # clear(b4)
    M.add(clear, hand) #handempty

    G = land(loc(b1) == b2, loc(b2) == b3, loc(b3) == b4, loc(b4) == table)

    P = fs.Problem()
    P.name = "tower4"
    P.domain_name = "blocksworld"
    P.language = bw
    P.init = M
    P.goal = G
    #P.constraints += [clear_constraint]

    # @NOTE: These are the state variables associated with the constraint above
    P.state_variables = []#[StateVariable(clear(dest), [tb]) for tb in [tb1, tb2, tb3, tb4, table]]

    b = bw.variable('b', bw.Object)
    P.action('pick_up', [b], \
        land(clear(b), clear(hand), loc(b) == table, b != hand, b != table),\
        [fs.FunctionalEffect(loc(b), hand),\
        fs.LogicalEffect(neg(clear(b))),
        fs.LogicalEffect(neg(clear(hand)))])

    P.action('put_down', [b],\
        land(loc(b) == hand, b != table, b != hand),\
        [fs.FunctionalEffect(loc(b), table),\
        fs.LogicalEffect(clear(b)),
        fs.LogicalEffect(clear(hand))])


    src = bw.variable('src', bw.Object)
    dest = bw.variable('dest', bw.Object)

    P.action('stack', [src, dest], \
        land(loc(src) == hand, clear(dest), src != dest, src != table, \
            src != hand, dest != table, dest != hand), \
        [fs.FunctionalEffect(loc(src), dest), \
        fs.LogicalEffect(neg(clear(dest))),\
        fs.LogicalEffect(clear(src)),
        fs.LogicalEffect(clear(hand))])

    P.action('unstack', [src, dest], \
        land(clear(hand), loc(src) == dest, clear(src), src != dest, src != table, \
            src != hand, dest != table, dest != hand), \
        [fs.FunctionalEffect(loc(src), hand), \
        fs.LogicalEffect(neg(clear(src))),\
        fs.LogicalEffect(clear(dest)),
        fs.LogicalEffect(neg(clear(hand)))])

    return P
