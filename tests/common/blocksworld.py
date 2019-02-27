"""
    Generate blocksworld language elements
"""
import tarski as tsk
import tarski.model
from tarski import fstrips as fs
from tarski.fstrips import create_fstrips_problem
from tarski.syntax import forall, equiv, neg, land, exists
from tarski.theories import Theory


def generate_small_strips_bw_language():
    """ The standard, untyped version of blocksworld, with a predicate handempty """
    lang = tsk.fstrips.language("blocksworld")

    # The sorts
    object_t = lang.get_sort('object')

    lang.predicate('handempty')
    lang.predicate('on', object_t, object_t)

    unary_predicates = ["ontable", "clear", "holding"]
    [lang.predicate(p, object_t) for p in unary_predicates]

    # A few blocks
    [lang.constant('b{}'.format(k), object_t) for k in range(1, 5)]
    return lang


def generate_small_fstrips_bw_language():
    """ A sample FSTRIPS BW encoding, with no need of handempty """
    lang = tsk.fstrips.language("blocksworld-fn", theories=[Theory.EQUALITY])

    # The sorts
    place = lang.sort('place')
    block = lang.sort('block', place)

    lang.predicate('clear', place)
    lang.function('loc', block, place)

    # Table and blocks
    lang.constant('table', place)
    [lang.constant('b{}'.format(k), block) for k in range(1, 5)]
    return lang


def generate_small_fstrips_bw_problem():
    lang = generate_small_fstrips_bw_language()
    problem = create_fstrips_problem(domain_name='blocksworld', problem_name='test-instance', language=lang)
    b1, b2, b3, clear, loc = lang.get('b1', 'b2', 'b3', 'clear', 'loc')
    problem.goal = (loc(b1) == b2) & (loc(b2) == b3) & (clear(b1))
    return problem


def create_small_bw_task():
    lang = generate_small_fstrips_bw_language()
    init = tarski.model.create(lang)

    b1, b2, b3, b4, clear, loc, table = lang.get('b1', 'b2', 'b3', 'b4', 'clear', 'loc', 'table')
    block, place = lang.get('block', 'place')

    init.set(loc, b1, b2)  # loc(b1) := b2
    init.set(loc, b2, b3)  # loc(b2) := b3
    init.set(loc, b3, table)  # loc(b3) := table
    init.set(loc, b4, table)  # loc(b4) := table

    init.add(clear, b1)  # clear(b1)
    init.add(clear, b4)  # clear(b4)
    init.add(clear, table)  # clear(table)

    src = lang.variable('src', block)
    dest = lang.variable('dest', place)

    x = lang.variable('x', block)
    y = lang.variable('y', block)
    clear_constraint = forall(x, equiv(neg(clear(x)), land(x != table, exists(y, loc(y) == x))))
    G = land(loc(b1) == b2, loc(b2) == b3, loc(b3) == b4, loc(b4) == table)

    problem = fs.Problem()
    problem.name = "tower4"
    problem.domain_name = "blocksworld"
    problem.language = lang
    problem.init = init
    problem.goal = G
    problem.constraints += [clear_constraint]
    problem.action('move', [src, dest], land(clear(src), clear(dest)), [fs.FunctionalEffect(loc(src), dest)])
    return problem


def generate_bw_loc_and_clear(num_blocks):
    lang = tsk.fstrips.language("blocksworld", theories=[Theory.EQUALITY])

    lang.predicate('clear', lang.Object)
    lang.function('loc', lang.Object, lang.Object)

    # Table and blocks
    lang.constant('table', lang.Object)
    lang.constant('hand', lang.Object)
    _ = [lang.constant('b{}'.format(k), lang.Object) for k in range(1, num_blocks + 1)]
    return lang


def create_4blocks_task():
    bw = generate_bw_loc_and_clear(4)
    M = tarski.model.create(bw)

    loc = bw.get_function('loc')
    clear = bw.get_predicate('clear')
    b1, b2, b3, b4 = [bw.get_constant('b{}'.format(k)) for k in range(1, 5)]
    table = bw.get_constant('table')
    hand = bw.get_constant('hand')

    M.setx(loc(b1), b2)  # loc(b1) := b2
    M.setx(loc(b2), b3)  # loc(b2) := b3
    M.setx(loc(b3), table)  # loc(b3) := table
    M.setx(loc(b4), table)  # loc(b4) := table
    M.setx(loc(table), table)
    M.setx(loc(hand), hand)

    M.add(clear, b1)  # clear(b1)
    M.add(clear, b4)  # clear(b4)
    M.add(clear, hand)  # handempty

    G = land(loc(b1) == b2, loc(b2) == b3, loc(b3) == b4, loc(b4) == table)

    P = fs.Problem()
    P.name = "tower4"
    P.domain_name = "blocksworld"
    P.language = bw
    P.init = M
    P.goal = G
    # P.constraints += [clear_constraint]

    # @NOTE: These are the state variables associated with the constraint above
    P.state_variables = []  # [StateVariable(clear(dest), [tb]) for tb in [tb1, tb2, tb3, tb4, table]]

    b = bw.variable('b', bw.Object)
    P.action('pick_up', [b],
             land(clear(b), clear(hand), loc(b) == table, b != hand, b != table),
             [fs.FunctionalEffect(loc(b), hand),
              fs.LogicalEffect(neg(clear(b))),
              fs.LogicalEffect(neg(clear(hand)))])

    P.action('put_down', [b],
             land(loc(b) == hand, b != table, b != hand),
             [fs.FunctionalEffect(loc(b), table),
              fs.LogicalEffect(clear(b)),
              fs.LogicalEffect(clear(hand))])

    src = bw.variable('src', bw.Object)
    dest = bw.variable('dest', bw.Object)

    P.action('stack', [src, dest],
             land(loc(src) == hand, clear(dest), src != dest, src != table,
                  src != hand, dest != table, dest != hand),
             [fs.FunctionalEffect(loc(src), dest),
              fs.LogicalEffect(neg(clear(dest))),
              fs.LogicalEffect(clear(src)),
              fs.LogicalEffect(clear(hand))])

    P.action('unstack', [src, dest],
             land(clear(hand), loc(src) == dest, clear(src), src != dest, src != table,
                  src != hand, dest != table, dest != hand),
             [fs.FunctionalEffect(loc(src), hand),
              fs.LogicalEffect(neg(clear(src))),
              fs.LogicalEffect(clear(dest)),
              fs.LogicalEffect(neg(clear(hand)))])

    return P
