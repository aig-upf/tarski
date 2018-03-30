"""
    Generate blocksworld language elements
"""
import tarski as tsk
from tarski.theories import Theory


def generate_small_bw_language():
    lang = tsk.fstrips.language("blocksworld", theories=[Theory.EQUALITY])

    # The sorts
    place = lang.sort('place')
    block = lang.sort('block', [place])

    lang.predicate('clear', place)
    lang.function('loc', block, place)

    # Table and blocks
    lang.constant('table', place)
    [lang.constant('b{}'.format(k), block) for k in range(1, 5)]
    return lang
