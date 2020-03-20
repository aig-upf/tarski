"""
    Generate different variants of Blocks-world problems
"""
import random

import tarski as tsk
from tarski import fstrips as fs
from tarski.fstrips import DelEffect, AddEffect
from ..fstrips import create_fstrips_problem
from ..syntax import land
from ..theories import Theory


BASE_DOMAIN_NAME = "blocksworld"


def generate_strips_bw_language(nblocks=4):
    """ The standard, untyped version of blocksworld, with a predicate handempty. """
    lang = tsk.fstrips.language(BASE_DOMAIN_NAME)

    object_t = lang.get_sort('object')

    lang.predicate('handempty')
    lang.predicate('on', object_t, object_t)
    [lang.predicate(p, object_t) for p in "ontable clear holding".split()]

    [lang.constant('b{}'.format(k), object_t) for k in range(1, nblocks+1)]
    return lang


def generate_fstrips_bw_language(nblocks=4):
    """ A typed FSTRIPS blocksworld encoding with one single move action. """
    lang = tsk.fstrips.language(BASE_DOMAIN_NAME, theories=[Theory.EQUALITY])

    # The sorts
    place = lang.sort('place')
    block = lang.sort('block', place)

    lang.predicate('clear', place)
    lang.function('loc', block, place)

    # Table and blocks
    lang.constant('table', place)
    [lang.constant('b{}'.format(k), block) for k in range(1, nblocks+1)]
    return lang


def generate_strips_blocksworld_problem(nblocks=4, init="random", goal="random", use_inequalities=True):
    """ Generate the standard BW encoding, untyped and with 4 action schemas """
    lang = generate_strips_bw_language(nblocks=nblocks)
    problem = create_fstrips_problem(lang, domain_name='blocksworld', problem_name='test-instance')

    clear, on, ontable, handempty, holding = lang.get('clear', 'on', 'ontable', 'handempty', 'holding')

    # Generate init pattern
    clearplaces, locations = generate_random_bw_pattern(lang)
    for x, y in locations:
        if y == 'table':
            problem.init.add(ontable, lang.get(x))
        else:
            problem.init.add(on, lang.get(x), lang.get(y))
    for x in clearplaces:
        if x != 'table':
            problem.init.add(clear, lang.get(x))
    problem.init.add(handempty)

    # Generate goal pattern
    _, locations = generate_random_bw_pattern(lang)
    conjuncts = []
    for x, y in locations:
        if y == 'table':
            conjuncts.append(ontable(lang.get(x)))
        else:
            conjuncts.append(on(lang.get(x), lang.get(y)))
    problem.goal = land(*conjuncts, flat=True)

    x = lang.variable('x', 'object')
    y = lang.variable('y', 'object')

    problem.action('pick-up', [x],
                   precondition=clear(x) & ontable(x) & handempty(),
                   effects=[fs.DelEffect(ontable(x)),
                            fs.DelEffect(clear(x)),
                            fs.DelEffect(handempty()),
                            fs.AddEffect(holding(x))])

    problem.action('put-down', [x],
                   precondition=holding(x),
                   effects=[fs.AddEffect(ontable(x)),
                            fs.AddEffect(clear(x)),
                            fs.AddEffect(handempty()),
                            fs.DelEffect(holding(x))])

    problem.action('unstack', [x, y],
                   precondition=on(x, y) & clear(x) & handempty(),
                   effects=[fs.DelEffect(on(x, y)),
                            fs.AddEffect(clear(y)),
                            fs.DelEffect(clear(x)),
                            fs.DelEffect(handempty()),
                            fs.AddEffect(holding(x))])

    prec = holding(x) & clear(y)
    if use_inequalities:
        prec = prec & (x != y)
    problem.action('stack', [x, y],
                   precondition=prec,
                   effects=[fs.AddEffect(on(x, y)),
                            fs.DelEffect(clear(y)),
                            fs.AddEffect(clear(x)),
                            fs.AddEffect(handempty()),
                            fs.DelEffect(holding(x))])

    return problem


def generate_fstrips_blocksworld_problem(nblocks=4, init="random", goal="random"):
    lang = generate_fstrips_bw_language(nblocks=nblocks)
    problem = create_fstrips_problem(lang, domain_name=BASE_DOMAIN_NAME, problem_name='test-instance')

    block, place, clear, loc, table = lang.get('block', 'place', 'clear', 'loc', 'table')

    # Generate init pattern
    if init == 'random':
        clearplaces, locations = generate_random_bw_pattern(lang)
    else:
        if len(init) != nblocks:
            raise ValueError(f"Blocksworld configuration ({init}) does not match given number of blocks ({nblocks})")
        locations = init
        clearplaces = compute_clear_from_pattern(lang, locations)

    for x, y in locations:
        problem.init.setx(loc(lang.get(x)), lang.get(y))
    for x in clearplaces:
        problem.init.add(clear, lang.get(x))

    # Generate goal pattern
    if goal == 'random':
        clearplaces, locations = generate_random_bw_pattern(lang)
    else:
        if len(goal) != nblocks:
            raise ValueError(f"Blocksworld configuration ({goal}) does not match given number of blocks ({nblocks})")
        locations = goal

    problem.goal = land(*(loc(lang.get(x)) == lang.get(y) for x, y in locations), flat=True)

    # Generate move action: move x to y
    x = lang.variable('x', block)
    y = lang.variable('y', place)

    problem.action('move', [x, y],
                   precondition=land(x != y, loc(x) != y, clear(x), clear(y)),
                   effects=[
                       loc(x) << y,
                       AddEffect(clear(loc(x))),
                       DelEffect(clear(y), condition=(y != table))])
    return problem


def generate_random_bw_pattern(lang):
    """ Generate a random pattern for blocksworld, i.e. the location for every block. This is returned
    in the form of a list of pairs (x, y) that denotes that x is on y. """
    table = 'table'
    blocks = [x.name for x in lang.constants() if x.name != table]
    clearplaces = {table}

    random.shuffle(blocks)
    pattern = []
    for b in blocks:
        target, = random.sample(clearplaces, 1)  # A bit of a hack - cannot random.choice from set
        pattern.append((b, target))
        if target != table:
            clearplaces.remove(target)  # target is no longer clear!
        clearplaces.add(b)
    return clearplaces, pattern


def compute_clear_from_pattern(lang, locations):
    unclear = {y for x, y in locations}
    clearplaces = {x.name for x in lang.constants() if x.name not in unclear}
    clearplaces.add('table')  # Table is always clear!
    return clearplaces

