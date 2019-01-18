"""
    Generate blocksworld language elements
"""
import tarski as tsk
import tarski.model
from tarski import fstrips as fs
from tarski.fstrips import create_fstrips_problem
from tarski.syntax import forall, equiv, neg, land, exists
from tarski.theories import Theory


def generate_small_fstrips_bw_language():
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


def generate_small_strips_bw_language():
    # The standard, untyped version of blocksworld
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
