import tempfile

import tarski.fstrips as fs
from tarski.fstrips import AddEffect, DelEffect
from tarski.io import FstripsWriter
from tarski.io.fstrips import print_effects, print_effect, print_objects, print_metric

from tests.common.blocksworld import generate_small_fstrips_bw_problem
from tests.common import parcprinter
from ..common.gridworld import generate_small_gridworld


def write_problem(problem):
    domain_filename = tempfile.NamedTemporaryFile(delete=True)
    instance_filename = tempfile.NamedTemporaryFile(delete=True)
    writer = FstripsWriter(problem)
    writer.write(domain_filename=domain_filename.name,
                 instance_filename=instance_filename.name)


def get_bw_elements():
    problem = generate_small_fstrips_bw_problem()
    lang = problem.language
    # writer = FstripsWriter(problem)

    loc = lang.get_function("loc")
    clear = lang.get_predicate("clear")
    b1 = lang.get_constant("b1")
    table = lang.get_constant("table")
    return problem, loc, clear, b1, table


def test_effect_writing():
    problem, loc, clear, b1, table = get_bw_elements()

    e1 = loc(b1) << table
    e2 = AddEffect(clear(b1))
    e3 = DelEffect(clear(b1))

    s1, s2, s3 = [print_effect(e) for e in [e1, e2, e3]]
    assert s1 == "(assign (loc b1) table)"
    assert s2 == "(clear b1)"
    assert s3 == "(not (clear b1))"
    assert print_effects([e1, e2, e3]) == "(and\n    {}\n    {}\n    {})".format(s1, s2, s3)


# def test_atom_writing():
#     pass


def test_objects_writing():
    problem, _, _, _, _ = get_bw_elements()
    assert print_objects(problem.language.constants()) == "b1 b2 b3 b4 - block\n        table - place"


def test_metric_writing():
    lang = fs.language('lang')
    cost = lang.function('total-cost', lang.Real)
    metric = fs.OptimizationMetric(cost(), fs.OptimizationType.MINIMIZE)
    metric_string = print_metric(metric)
    assert metric_string == '(:metric minimize (total-cost ))'


def test_gridworld_writing():
    problem = generate_small_gridworld()
    write_problem(problem)


def test_action_costs_numeric_fluents_requirements():
    problem = parcprinter.create_small_task()
    writer = FstripsWriter(problem)

    # action costs should be required if there is a metric defined.
    domain_string = writer.print_domain()
    assert 'numeric-fluents' not in domain_string
    assert 'action-costs' in domain_string
