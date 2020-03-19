from tarski.benchmarks.blocksworld import generate_fstrips_blocksworld_problem, generate_strips_blocksworld_problem
from tarski.benchmarks.counters import generate_fstrips_counters_problem
from tarski.syntax import is_and


def test_counters():
    problem = generate_fstrips_counters_problem(ncounters=3)
    lang = problem.language
    value, c1 = lang.get('value', 'c1')

    # More than testing some particular property, here we want to test that the generator can run correctly
    assert is_and(problem.goal) and len(problem.goal.subformulas) == 2
    assert problem.init[value(c1)] == 0


def test_blocksworld():
    problem = generate_strips_blocksworld_problem(nblocks=5)
    assert problem

    problem = generate_fstrips_blocksworld_problem(nblocks=5)
    assert problem
