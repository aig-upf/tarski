"""
    Generate blocksworld language elements
"""
import tarski as tsk
from tarski.fstrips import create_fstrips_problem
from tarski.theories import Theory


def generate_small_fstrips_bw_problem():
    return create_fstrips_problem(domain_name='blocksworld',
                                  problem_name='test-instance',
                                  language=generate_small_fstrips_bw_language())


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

def generate_bw_loc_and_clear(num_blocks):
    lang = tsk.fstrips.language("blocksworld", theories=[Theory.EQUALITY])

    lang.predicate('clear', lang.Object)
    lang.function('loc', lang.Object, lang.Object)

    # Table and blocks
    lang.constant('table', lang.Object)
    lang.constant('hand', lang.Object)
    foo = [lang.constant('b{}'.format(k), lang.Object) for k in range(1,num_blocks+1)]
    return lang
