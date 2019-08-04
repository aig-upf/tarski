
from tarski.benchmarks.counters import generate_fstrips_counters_problem
from tarski.evaluators.simple import evaluate
from tarski.syntax import is_and


def test_counters():
    problem = generate_fstrips_counters_problem(ncounters=3)
    lang = problem.language
    value, c1 = lang.get('value', 'c1')

    problem.init.evaluator = evaluate

    # More than testing some particular property, here we want to test that the generator can run correctly
    assert is_and(problem.goal) and len(problem.goal.subformulas) == 2
    assert problem.init[value(c1)] == 0
