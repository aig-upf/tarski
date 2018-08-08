
from tarski import fstrips as fs
from tarski.syntax import *

from ..common import blocksworld


def test_action_creation():
    lang = blocksworld.generate_small_fstrips_bw_language()

    b = lang.variable('b', 'block')
    to = lang.variable('to', 'place')

    clear = lang.get_predicate('clear')
    loc = lang.get_function('loc')

    precondition = land(clear(to), clear(b), loc(b) != to)
    effects = [neg(clear(to)), loc(b) == to, clear(loc(b))]

    fs.Action(lang, name='move', parameters=[b, to], precondition=precondition, effects=effects)


def test_effect_creation():
    lang = fs.language()
    t1 = lang.constant('x', 'object')
    t2 = lang.constant('y', 'object')
    eff = t1 << t2  # i.e. x := y
    assert isinstance(eff, fs.FunctionalEffect)


def create_noop_action():
    lang = fs.language()
    fs.Action(lang, name='noop', parameters=[], precondition=Tautology, effects=[])
