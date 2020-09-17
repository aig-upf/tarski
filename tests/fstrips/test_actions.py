import pytest

import tarski.benchmarks.blocksworld
from tarski import fstrips as fs
from tarski.syntax import *
from tarski.theories import Theory

from ..common import blocksworld


def test_action_creation():
    lang = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()

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
        _ = t1 << t2  # i.e. x := y


def test_functional_effect_valid_creation():
    lang = fs.language()
    t1 = lang.constant('x', lang.Object)
    t2 = lang.constant('y', lang.Object)
    f = lang.function('foo', lang.Object, lang.Object)

    eff = f(t1) << t2
    assert isinstance(eff, fs.FunctionalEffect)


def test_increase_effect_valid_creation():
    lang = fs.language('lang', theories=[Theory.EQUALITY, Theory.ARITHMETIC])
    lang.total_cost = lang.function('total-cost', lang.Real)
    eff = fs.IncreaseEffect(lang.total_cost(), 5)

    assert isinstance(eff, fs.IncreaseEffect)
    assert eff.rhs == 5


def test_choice_effect_invalid_creation():
    import tarski.fstrips.errors as err
    from tests.fstrips.hybrid.tasks import create_billiards_world
    prob = create_billiards_world()
    x = prob.language.get_constant('x')
    cue = prob.language.get_constant('cue')
    b = prob.language.get_constant('ball_1')
    F = prob.language.get_function('F')
    _ = prob.language.get_function('v')
    with pytest.raises(err.InvalidEffectError):
        _ = fs.ChoiceEffect(fs.OptimizationType.MAXIMIZE, Variable("z", prob.language.Real), [F(cue, x, b)])


def test_choice_effect_valid_creation():
    from tests.fstrips.hybrid.tasks import create_billiards_world
    prob = create_billiards_world()
    x = prob.language.get_constant('x')
    cue = prob.language.get_constant('cue')
    b = prob.language.get_constant('ball_1')
    F = prob.language.get_function('F')
    v = prob.language.get_function('v')
    eff = fs.ChoiceEffect(fs.OptimizationType.MAXIMIZE, v(x, b), [F(cue, x, b)])
    assert isinstance(eff, fs.ChoiceEffect)
