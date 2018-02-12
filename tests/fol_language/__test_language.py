"""
 This tests the parsing of particular FSTRIPS language elements and its
 mapping into appropriate JSON data structures.
"""
import pytest

from python.parser.fstrips_components import FSFormula
from python.parser.pddl.conditions import Conjunction, Atom
from python.parser.pddl.f_expression import FunctionalTerm
from .common import generate_base_fs_task, generate_fd_function, generate_fd_predicate, generate_fd_dummy_action


@pytest.fixture(scope="module")
def bw_task():
    """ This effectively generates a single BW instance per test module and allows it to be reused in different tests
        simply by declaring that the test has a 'bw_task' parameter. See https://pytest.org/latest/fixture.html. """
    task = generate_base_fs_task(objects=[('b1', 'block'), ('b2', 'block')], types=[('block', 'object')])

    loc = generate_fd_function(('loc', [('?b', 'block')], 'location'))
    val = generate_fd_function(('val', [('?c', 'counter')], 'value'))
    on = generate_fd_predicate(('on', [('?b1', 'block'), ('?b2', 'block')]))

    actions = [generate_fd_dummy_action()]
    task.process_symbols(actions, [on], [loc, val])

    return task


def check_type(element, type_):
    assert element['type'] == type_


def unwrap_conjunction(element):
    check_type(element['conditions'], 'and')
    return element['conditions']['children']


def unwrap_predicate(element):
    check_type(element, 'atom')
    return element['symbol'], element['negated'], element['children']


def unwrap_function(element):
    check_type(element, 'functional')
    return element['symbol'], element['children']


def test_predicate(bw_task):
    atom = Atom('on', ['b1', 'b2'])
    processed = FSFormula(bw_task, atom).dump()

    elements = unwrap_conjunction(processed)  # We're also testing that the atom is wrapped as a conjunction
    assert len(elements) == 1

    symbol, negated, elements = unwrap_predicate(elements[0])
    assert symbol == 'on' and len(elements) == 2 and all(elem['type'] == 'constant' for elem in elements)


def test_conjunction(bw_task):
    conjunction = Conjunction([Atom('on', ['b1', 'b2']), Atom('on', ['b2', 'b1'])])
    processed = FSFormula(bw_task, conjunction).dump()

    elements = unwrap_conjunction(processed)
    assert len(elements) == 2

    symbol0, negated0, elements0 = unwrap_predicate(elements[0])
    symbol1, negated1, elements1 = unwrap_predicate(elements[1])
    assert symbol0 == symbol1 == 'on'
    assert len(elements0) == len(elements1) == 2 and all(elem['type'] == 'constant' for elem in elements1)


def test_function(bw_task):
    conjunction = Atom('=', [FunctionalTerm('loc', ['b1']), 'b2'])
    processed = FSFormula(bw_task, conjunction).dump()

    elements = unwrap_conjunction(processed)
    assert len(elements) == 1
    symbol, negated, elements = unwrap_predicate(elements[0])
    assert symbol == '=' and len(elements) == 2 and not negated

    symbol, subterms = unwrap_function(elements[0])  # loc(a)
    check_type(elements[1], 'constant')  # b
    assert symbol == 'loc' and len(subterms) == 1
    check_type(subterms[0], 'constant')


def test_relational_expression(bw_task):
    subterms = [FunctionalTerm('val', ['b1']), FunctionalTerm('val', ['b2'])]
    atom = Atom('<', subterms)
    processed = FSFormula(bw_task, atom).dump()

    elements = unwrap_conjunction(processed)  # We're also testing that the atom is wrapped as a conjunction
    assert len(elements) == 1

    symbol, negated, elements = unwrap_predicate(elements[0])
    assert symbol == '<' and len(elements) == 2
    _, _ = unwrap_function(elements[0])
    _, _ = unwrap_function(elements[1])


# def test_existential():
#     assert False
