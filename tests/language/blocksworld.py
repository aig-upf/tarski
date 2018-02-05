"""
    Generate blocksworld language elements
"""
from src import tarski as tsk  # TODO Fix this import, 'src' should not be there


def generate_small_bw_instance():
    lang = tsk.language()

    # The sorts
    place = lang.sort('place')
    block = lang.sort('block', [place])

    # Table and blocks
    table = lang.const('table', place)
    b1, b2, b3, b4 = lang.const(('b{}'.format(k) for k in (1, 2, 3, 4)), block)


