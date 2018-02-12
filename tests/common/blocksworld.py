"""
    Generate blocksworld language elements
"""
import tarski as tsk


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
