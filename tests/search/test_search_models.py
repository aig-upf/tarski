"""
 Tests for the Search module
"""
from tarski.benchmarks.blocksworld import generate_strips_blocksworld_problem
from tarski.grounding.lp_grounding import ground_problem_schemas_into_plain_operators
from tarski.search import GroundForwardSearchModel, BreadthFirstSearch
from tarski.search.model import progress
from tarski.syntax.transform.action_grounding import ground_schema_into_plain_operator_from_grounding
from tarski.utils import parse_model
from tests.io.common import parse_benchmark_instance


def test_forward_search_model():
    problem = parse_benchmark_instance("gripper:prob01.pddl")
    model = GroundForwardSearchModel(problem, ground_problem_schemas_into_plain_operators(problem))

    assert model.init() == problem.init

    s0 = problem.init
    assert len(list(model.applicable(s0))) == 10  # 8 possible pickups plus move(A, B) and move(A, A)
    assert not model.is_goal(s0)

    s1 = parse_model(problem.language,
                     ['room(rooma)', 'room(roomb)',
                      'gripper(left)', 'gripper(right)',
                      'ball(ball4)', 'ball(ball1)', 'ball(ball3)', 'ball(ball2)',
                      'at-robby(roomb)', 'free(left)', 'free(right)',
                      'at(ball4,rooma)', 'at(ball3,rooma)', 'at(ball2,rooma)', 'at(ball1,rooma)'])

    move = problem.get_action('move')
    moveright_op = ground_schema_into_plain_operator_from_grounding(move, ('rooma', 'roomb'))
    assert s1 == progress(s0, moveright_op)

    successors = set(succ for op, succ in model.successors(s0))
    assert s1 in successors

    # Let's test add-after-delete semantics are correctly enforced. The move(x, y) action in Gripper doesn't
    # test that x != y. When x=y, it adds and deletes the same atom `at-robby(x)`; in which case the model
    # will only be correct if the add is performed after the delete.
    nullmove = ground_schema_into_plain_operator_from_grounding(move, ('rooma', 'rooma'))
    s1 = progress(s0, nullmove)
    assert s1 == s0


def test_basic_search():
    problem = generate_strips_blocksworld_problem(nblocks=2)

    model = GroundForwardSearchModel(problem, ground_problem_schemas_into_plain_operators(problem))

    search = BreadthFirstSearch(model)
    space, stats = search.run()
    assert stats.nexpansions == 5

    search = BreadthFirstSearch(model, max_expansions=3)
    space, stats = search.run()
    assert stats.nexpansions == 3




