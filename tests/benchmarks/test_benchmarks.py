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

    # Now let's test the generator with given, fixed configurations:
    problem = generate_fstrips_blocksworld_problem(
        nblocks=4,
        init=[('b1', 'b2'), ('b2', 'table'), ('b3', 'b4'), ('b4', 'table')],
        goal=[('b2', 'b3'), ('b3', 'b4'), ('b4', 'b1'), ('b1', 'table')]
    )
    lang = problem.language
    loc, b1, b2, table = lang.get('loc', 'b1', 'b2', 'table')

    assert problem.init[loc(b1) == b2] and problem.init[loc(b2) == table]
    assert is_and(problem.goal) and problem.goal.subformulas[-1] == (loc(b1) == table)
