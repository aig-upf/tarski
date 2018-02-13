
from tarski import fstrips as fs
from tarski.syntax import *

from ..common import blocksworld


def test_action_creation():
    lang = blocksworld.generate_small_bw_language()

    b = lang.variable('b', 'block')
    to = lang.variable('to', 'place')

    clear = lang.get_predicate('clear')
    loc = lang.get_function('loc')

    precondition = land(clear(to), clear(b), loc(b) != to)
    effects = [neg(clear(to)), loc(b) == to, clear(loc(b))]

    fs.Action(lang, name='move', parameters=[b, to], precondition=precondition, effects=effects)

