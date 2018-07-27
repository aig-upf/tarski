import pytest

from tarski import fstrips as fs
from tarski.syntax import *
from tests.fstrips.hybrid.tasks import create_billiards_world

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


def test_functional_effect_invalid_creation():
    import tarski.fstrips.errors as err
    lang = fs.language()
    t1 = lang.constant('x', 'object')
    t2 = lang.constant('y', 'object')
    with pytest.raises(err.InvalidEffectError):
        eff = t1 << t2  # i.e. x := y

def test_functional_effect_valid_creation():
    import tarski.fstrips.errors as err
    lang = fs.language()
    t1 = lang.constant('x', lang.Object)
    t2 = lang.constant('y', lang.Object)
    f = lang.function('foo', lang.Object, lang.Object)

    eff = f(t1) << t2
    assert isinstance(eff, fs.FunctionalEffect)

def test_choice_effect_invalid_creation():
    import tarski.fstrips.errors as err
    prob = create_billiards_world()
    x = prob.language.get_constant('x')
    cue = prob.language.get_constant('cue')
    b = prob.language.get_constant('ball_1')
    F = prob.language.get_function('F')
    v = prob.language.get_function('v')
    with pytest.raises(err.InvalidEffectError):
        eff = fs.ChoiceEffect(fs.OptimizationType.MAXIMIZE, Variable(0.0, prob.language.Real), [F(cue, x, b)])

def test_choice_effect_valid_creation():
    import tarski.fstrips.errors as err
    prob = create_billiards_world()
    x = prob.language.get_constant('x')
    cue = prob.language.get_constant('cue')
    b = prob.language.get_constant('ball_1')
    F = prob.language.get_function('F')
    v = prob.language.get_function('v')
    eff = fs.ChoiceEffect(fs.OptimizationType.MAXIMIZE, v(x, b), [F(cue, x, b)])
    assert isinstance(eff,fs.ChoiceEffect)
