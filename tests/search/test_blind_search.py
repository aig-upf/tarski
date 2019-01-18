"""
 Tests for the Search module
"""
from tarski.search import ForwardSearchModel, BreadthFirstSearch

from ..common import blocksworld


def test_forward_search_model():
    problem = blocksworld.generate_small_fstrips_bw_problem()
    model = ForwardSearchModel(problem)
    assert model.init() == problem.init

    # TODO ...


def test_basic_search():
    problem = blocksworld.create_small_bw_task()
    lang = problem.language

    model = ForwardSearchModel(problem)
    search = BreadthFirstSearch(model, max_expansions=10)

    space = search.run()




