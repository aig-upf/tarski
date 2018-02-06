"""
    Generate blocksworld language elements
"""
from src import tarski as tsk  # TODO Fix this import, 'src' should not be there


def generate_small_bw_instance():
    lang = tsk.language()

    # The sorts
    lang.place = lang.sort('place')
    lang.block = lang.sort('block', [lang.place])

    lang.clear = lang.predicate('clear', lang.block)
    lang.loc = lang.function('loc', lang.block, lang.place)

    # Table and blocks
    lang.table = lang.const('table', lang.place)
    lang.b1, lang.b2, lang.b3, lang.b4 = lang.const(('b{}'.format(k) for k in (1, 2, 3, 4)), lang.block)

    return lang
