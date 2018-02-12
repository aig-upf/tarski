"""
    Generate blocksworld language elements
"""
from src import tarski as tsk  # TODO Fix this import, 'src' should not be there


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
