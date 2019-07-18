
from tarski.grounding import ProblemGrounding

from tests.common import blocksworld


def test_task_index_process_symbols_fluents_bw():
    problem = blocksworld.create_4blocks_task()
    index = ProblemGrounding(problem)
    index.process_symbols(problem)

    assert len(index.fluent_terms) == 6
    assert len(index.static_terms) == 11
