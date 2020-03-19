"""
 Tests for the Search module
"""
from tarski.benchmarks.blocksworld import generate_fstrips_blocksworld_problem
from tarski.search import ForwardSearchModel, BreadthFirstSearch


def test_forward_search_model():
    problem = generate_fstrips_blocksworld_problem()
    model = ForwardSearchModel(problem)
    assert model.init() == problem.init

    # TODO ...


def test_basic_search():
    problem = generate_fstrips_blocksworld_problem()
    lang = problem.language

    model = ForwardSearchModel(problem)
    search = BreadthFirstSearch(model, max_expansions=10)

    # space = search.run()

    # TODO ...




