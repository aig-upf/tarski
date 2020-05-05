from tarski.benchmarks.blocksworld import generate_fstrips_bw_language
from tarski.fstrips import create_fstrips_problem, AddEffect
from tarski.fstrips.ops import collect_all_symbols
from tarski.grounding.ops import approximate_symbol_fluency
from tarski.syntax import top

from ..common import parcprinter, gripper


def test_symbol_classification_in_parcprinter():
    prob = parcprinter.create_small_task()
    fluent, static = approximate_symbol_fluency(prob)
    assert (len(fluent), len(static)) == (4, 3)


def test_symbol_classification_in_gripper():
    prob = gripper.create_sample_problem()
    fluent, static = approximate_symbol_fluency(prob)
    assert (len(fluent), len(static)) == (4, 3)

    fluent, static = approximate_symbol_fluency(prob, include_builtin=True)
    assert (len(fluent), len(static)) == (4, 5)  # Same as before plus "=" and "!="


def test_symbol_classification_with_nested_effect_heads():
    lang = generate_fstrips_bw_language(nblocks=3)
    problem = create_fstrips_problem(lang, domain_name='blocksworld', problem_name='test-instance')
    block, place, clear, loc, table = lang.get('block', 'place', 'clear', 'loc', 'table')

    x = lang.variable('x', 'block')
    problem.action('dummy-action', [x],
                   precondition=loc(x) == table,
                   effects=[AddEffect(clear(loc(x)))])

    fluent, static = approximate_symbol_fluency(problem, include_builtin=True)
    assert loc in static and clear in fluent, "loc has not been detected as fluent even though it " \
                                              "appears (nested) in the head of an effect"


def test_symbol_collection():
    lang = generate_fstrips_bw_language(nblocks=3)
    problem = create_fstrips_problem(lang, domain_name='blocksworld', problem_name='test-instance')
    block, place, clear, loc, table = lang.get('block', 'place', 'clear', 'loc', 'table')

    x = lang.variable('x', 'block')
    problem.action('dummy-action1', [x],
                   precondition=(loc(x) == table),
                   effects=[loc(x) << table])  # dummy indeed :-)
    problem.goal = top

    assert clear not in collect_all_symbols(problem), "clear doesn't appear in any action or goal"

    problem.goal = clear(table)
    assert {loc, clear}.issubset(collect_all_symbols(problem)), "clear should now be collected: it appears in the goal"

