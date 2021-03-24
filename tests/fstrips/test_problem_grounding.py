from collections import OrderedDict

from tarski.fstrips import DelEffect, UniversalEffect, AddEffect
from tarski.fstrips.action import PlainOperator
from tarski.fstrips.representation import is_ground
from tarski.grounding import ProblemGrounding
from tarski.grounding.lp_grounding import ground_problem_schemas_into_plain_operators
from tarski.syntax import symref
from tarski.syntax.transform.action_grounding import ground_schema_into_plain_operator, \
    ground_schema_into_plain_operator_from_grounding
from tarski.benchmarks.blocksworld import generate_strips_blocksworld_problem

from tests.common import blocksworld


def test_task_index_process_symbols_fluents_bw():
    problem = blocksworld.create_4blocks_task()
    index = ProblemGrounding(problem)
    index.process_symbols(problem)

    assert len(index.fluent_terms) == 6
    assert len(index.static_terms) == 11


def test_action_grounding_bw():
    problem = generate_strips_blocksworld_problem()
    b1, b2, b3, clear, on, ontable, handempty, holding = \
        problem.language.get('b1', 'b2', 'b3', 'clear', 'on', 'ontable', 'handempty', 'holding')
    unstack = problem.get_action("unstack")
    x1, x2 = [symref(x) for x in unstack.parameters]  # Unstack has two parameters
    ground = ground_schema_into_plain_operator(unstack, {x1: b1, x2: b2})  # i.e. the operator unstack(b1, b2)
    assert isinstance(ground, PlainOperator) and \
           str(ground.precondition) == '(on(b1,b2) and clear(b1) and handempty())'

    # assert is_applicable(problem.init, ground)
    # successor = apply(problem.init, ground)
    # assert successor[holding(b1)]
    # assert successor[clear(b2)]


def test_action_grounding_on_parameterless_action():
    problem = generate_strips_blocksworld_problem()
    lang = problem.language
    handempty = lang.get('handempty')

    problem.actions = OrderedDict()
    problem.goal = ~handempty()
    action = problem.action('fake', [],
                            precondition=handempty(),
                            effects=[DelEffect(handempty())])

    actions = ground_problem_schemas_into_plain_operators(problem)
    assert len(actions) == 1


def test_complex_action_grounding():
    problem = generate_strips_blocksworld_problem(nblocks=1)
    lang = problem.language
    handempty, clear, b1 = lang.get('handempty', 'clear', 'b1')

    problem.actions = OrderedDict()
    problem.goal = ~handempty()  # Just to make the goal reachable

    x = lang.variable('x', 'object')

    ue = UniversalEffect([], effects=[AddEffect(clear(x)), DelEffect(handempty())])
    action = problem.action('fake', [x],
                            precondition=handempty(),
                            effects=[ue])

    op = ground_schema_into_plain_operator_from_grounding(action, (b1, ))

    assert len(op.effects) == 1
    eff = op.effects[0]

    assert all(is_ground(sube.atom) for sube in eff.effects)
