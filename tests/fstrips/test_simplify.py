import tarski.benchmarks.blocksworld
from tarski.benchmarks.counters import generate_fstrips_counters_problem
from tarski.fstrips import UniversalEffect
from tarski.fstrips.manipulation import Simplify
from tarski.fstrips.manipulation.simplify import simplify_existential_quantification
from tarski.syntax import symref, land, lor, neg, bot, top, forall, exists


def test_simplifier():
    problem = generate_fstrips_counters_problem(ncounters=3)
    lang = problem.language
    value, max_int, counter, val_t, c1 = lang.get('value', 'max_int', 'counter', 'val', 'c1')
    x = lang.variable('x', counter)
    two, three, six = [lang.constant(c, val_t) for c in (2, 3, 6)]

    s = Simplify(problem, problem.init)
    assert symref(s.simplify_expression(x)) == symref(x)
    assert symref(s.simplify_expression(value(c1) < max_int())) == symref(value(c1) < six)  # max_int evaluates to 6
    assert s.simplify_expression(two < max_int()) is True
    assert s.simplify_expression(two > three) is False

    # conjunction evaluates to false because of first conjunct:
    falseconj = land(two > three, value(c1) < max_int())
    assert s.simplify_expression(falseconj) is False
    assert s.simplify_expression(neg(falseconj)) is True

    # first conjunct gets removed:
    assert str(s.simplify_expression(land(two < three, value(c1) < max_int()))) == '<(value(c1),6)'

    # first disjunct gets removed because it is false
    assert str(s.simplify_expression(lor(two > three, value(c1) < max_int()))) == '<(value(c1),6)'

    assert str(s.simplify_expression(forall(x, value(x) < max_int()))) == 'forall x : (<(value(x),6))'
    assert s.simplify_expression(forall(x, two + three <= 6)) is True

    inc = problem.get_action('increment')
    simp = s.simplify_action(inc)
    assert str(simp.precondition) == '<(value(c),6)'
    assert str(simp.effects) == str(inc.effects)

    eff = UniversalEffect(x, [value(x) << three])
    assert str(s.simplify_effect(eff)) == '(T -> forall (x) : ((T -> value(x) := 3)))'

    simp = s.simplify()
    assert str(simp.get_action('increment').precondition) == '<(value(c),6)'

    # Make sure there is no mention to the compiled away "max_int" symbol in the language
    assert not simp.language.has_function("max_int")

    # Make sure there is no mention to the compiled away "max_int" symbol in the initial state
    exts = list(simp.init.list_all_extensions().keys())
    assert ('max_int', 'val') not in exts


def test_simplification_of_negation():
    problem = tarski.benchmarks.blocksworld.generate_strips_blocksworld_problem()
    lang = problem.language
    b1, clear, on, ontable, handempty, holding = lang.get('b1', 'clear', 'on', 'ontable', 'handempty', 'holding')

    s = Simplify(problem, problem.init)
    cb1 = clear(b1)
    assert str(s.simplify_expression(land(cb1, neg(bot)))) == 'clear(b1)'
    assert str(s.simplify_expression(cb1)) == 'clear(b1)'  # No evaluation made
    assert str(s.simplify_expression(neg(neg(cb1)))) == 'clear(b1)'  # Double negation gets removed

    assert s.simplify_expression(land(neg(bot), neg(bot))) is True
    assert s.simplify_expression(lor(neg(top), neg(bot))) is True
    assert s.simplify_expression(lor(neg(top), neg(top))) is False

    act = problem.get_action('unstack')
    simp = s.simplify_action(act)
    assert simp


def test_simplification_pruning():
    problem = generate_fstrips_counters_problem(ncounters=3)
    lang = problem.language
    value, max_int, counter, val_t, c1 = lang.get('value', 'max_int', 'counter', 'val', 'c1')
    three, six = [lang.constant(c, val_t) for c in (3, 6)]

    s = Simplify(problem, problem.init)

    a = problem.get_action('decrement')
    a.precondition = (three > six)
    # increment action must be pruned because its precondition is are statically inapplicable:
    assert len(s.simplify().actions) == 1

    a = problem.get_action('increment')
    a.effects[0].condition = (three > six)

    # increment action must be pruned because all its effects are statically inapplicable:
    assert len(s.simplify().actions) == 0


def test_simplification_of_ex_quantification():
    problem = generate_fstrips_counters_problem(ncounters=3)
    lang = problem.language
    value, max_int, counter, val_t, c1 = lang.get('value', 'max_int', 'counter', 'val', 'c1')
    x = lang.variable('x', counter)
    z = lang.variable('z', counter)
    two, three, six = [lang.constant(c, val_t) for c in (2, 3, 6)]

    phi = exists(z, land(x == z, top, value(z) < six))
    assert simplify_existential_quantification(phi, inplace=False) == land(top, value(x) < six), \
        "z has been replaced by x and removed from the quantification list, thus removing the quantifier"

    phi = exists(x, z, land(x == z, z == x, value(z) < six, flat=True))
    assert simplify_existential_quantification(phi, inplace=False) == exists(x, value(x) < six), \
        "The circular substitution dependency has been treated appropriately and only one substitution performed"


