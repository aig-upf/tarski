from tarski.fstrips.action import PlainOperator
from tarski.grounding import ProblemGrounding
from tarski.syntax import symref
from tarski.syntax.transform.action_grounding import ground_schema_into_plain_operator

from tests.common import blocksworld


def test_task_index_process_symbols_fluents_bw():
    problem = blocksworld.create_4blocks_task()
    index = ProblemGrounding(problem)
    index.process_symbols(problem)

    assert len(index.fluent_terms) == 6
    assert len(index.static_terms) == 11


def test_action_grounding_bw():
    problem = blocksworld.generate_small_strips_bw_problem()
    b1, b2 = problem.language.get("b1", "b2")
    unstack = problem.get_action("unstack")
    x1, x2 = [symref(x) for x in unstack.parameters]  # Unstack has two parameters
    ground = ground_schema_into_plain_operator(unstack, {x1: b1, x2: b2})
    assert isinstance(ground, PlainOperator) and \
        str(ground.precondition) == '((on(b1,b2) and clear(b1)) and handempty())'
