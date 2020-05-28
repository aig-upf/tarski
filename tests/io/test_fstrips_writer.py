import tempfile
from typing import Optional, List

import tarski.fstrips as fs
from tarski.benchmarks.blocksworld import generate_fstrips_blocksworld_problem
from tarski.benchmarks.counters import get_counters_elements, generate_fstrips_counters_problem
from tarski.fstrips import AddEffect, DelEffect, FunctionalEffect, UniversalEffect
from tarski.io import FstripsWriter
from tarski.io._fstrips.common import get_requirements_string
from tarski.io.fstrips import print_effects, print_effect, print_objects, print_metric, print_formula, print_term
from tarski.syntax import forall, exists, Constant
from tarski.theories import Theory

from tests.common import parcprinter
from tests.io.common import reader
from ..common.gridworld import generate_small_gridworld


def write_problem(problem, domain_constants: Optional[List[Constant]] = None):
    domain_filename = tempfile.NamedTemporaryFile(delete=True)
    instance_filename = tempfile.NamedTemporaryFile(delete=True)
    writer = FstripsWriter(problem)
    writer.write(domain_filename=domain_filename.name,
                 instance_filename=instance_filename.name,
                 domain_constants=domain_constants)
    return domain_filename, instance_filename


def get_bw_elements():
    problem = generate_fstrips_blocksworld_problem()
    loc, clear, b1, table = problem.language.get("loc", "clear", "b1", "table")
    return problem, loc, clear, b1, table


def test_formula_writing1():
    problem, loc, clear, b1, table = get_bw_elements()
    lang = problem.language

    assert print_formula(clear(b1)) == "(clear b1)"
    assert print_formula(loc(b1) == table) == "(= (loc b1) table)"
    assert print_formula(loc(b1) != table) == "(not (= (loc b1) table))"

    assert print_formula(clear(b1) | clear(table)) == "(or (clear b1) (clear table))"

    b = lang.variable('B', lang.ns.block)
    assert print_formula(forall(b, clear(b))) == "(forall (?B - block) (clear ?B))"
    assert print_formula(exists(b, clear(b))) == "(exists (?B - block) (clear ?B))"


def test_formula_writing2():
    problem, lang, value, max_int, c1, c2 = get_counters_elements(ncounters=2)

    assert print_term(value(c1)) == "(value c1)"

    assert print_formula(value(c1) <= max_int()) == '(<= (value c1) (max_int ))'
    assert print_formula(value(c1) > value(c2)) == '(> (value c1) (value c2))'
    assert print_formula(value(c1) != 0) == '(not (= (value c1) 0))'


def test_effect_writing():
    problem, loc, clear, b1, table = get_bw_elements()
    block_var = problem.language.variable("b", "block")

    e1 = loc(b1) << table
    e2 = AddEffect(clear(b1))
    e3 = DelEffect(clear(b1))

    s1, s2, s3 = [print_effect(e) for e in [e1, e2, e3]]
    assert s1 == "(assign (loc b1) table)"
    assert s2 == "(clear b1)"
    assert s3 == "(not (clear b1))"
    assert print_effects([e1, e2, e3]) == "(and\n    {}\n    {}\n    {})".format(s1, s2, s3)

    e4 = UniversalEffect([block_var], [AddEffect(clear(block_var))])
    s4 = print_effect(e4)

    assert s4 == "(forall (?b - block) (clear ?b))"

    e5 = UniversalEffect([block_var], [AddEffect(clear(block_var)), loc(block_var) << table])
    s5 = print_effect(e5)

    assert s5 == "(forall (?b - block) (and\n    (clear ?b)\n    (assign (loc ?b) table)))"

    e6 = UniversalEffect([block_var], [FunctionalEffect(loc(block_var), table, condition=clear(block_var))])
    s6 = print_effect(e6)

    assert s6 == "(forall (?b - block) (when (clear ?b) (assign (loc ?b) table)))"


def test_objects_writing():
    problem, _, _, _, _ = get_bw_elements()
    assert print_objects(problem.language.constants()) == "b1 b2 b3 b4 - block\n        table - place"


def test_metric_writing():
    lang = fs.language('lang', theories=[Theory.ARITHMETIC])
    cost = lang.function('total-cost', lang.Real)
    metric = fs.OptimizationMetric(cost(), fs.OptimizationType.MINIMIZE)
    metric_string = print_metric(metric)
    assert metric_string == '(:metric minimize (total-cost ))'


def test_gridworld_writing():
    problem = generate_small_gridworld()
    write_problem(problem)


def test_blocksworld_writing():
    problem, _, _, _, table = get_bw_elements()
    domf, instf = write_problem(problem, domain_constants=[table])

    # Make sure that the printed-out problem can be parsed again
    problem2 = reader().read_problem(domf.name, instf.name)
    assert len(problem.actions) == len(problem2.actions)  # Some silly checks


def test_blocksworld_writing_with_different_constants():
    problem, loc, clear, b1, table = get_bw_elements()
    writer = FstripsWriter(problem)
    instance_model_string = writer.print_instance()
    domain_model_string = writer.print_domain()
    assert "b1" not in domain_model_string
    assert "b1 b2 b3 b4 - block\n        table - place" in instance_model_string

    constant_objects = [b1, table]
    instance_model_string = writer.print_instance(constant_objects=constant_objects)
    domain_model_string = writer.print_domain(constant_objects=constant_objects)

    assert "b1 - block" in domain_model_string
    assert "table - place" in domain_model_string
    assert """(:objects
        b2 b3 b4 - block
    )""" in instance_model_string


def test_requirements_string():
    problem = parcprinter.create_small_task()

    # action costs should be required if there is a metric defined, but if "total-cost" is the only arithmetic
    # function, we don't print the ':numeric-fluents' requirement
    assert sorted(get_requirements_string(problem)) == [':action-costs', ':equality', ':typing']

    problem, loc, clear, b1, table = get_bw_elements()
    assert sorted(get_requirements_string(problem)) == [':equality', ':typing']

    problem = generate_fstrips_counters_problem()
    assert sorted(get_requirements_string(problem)) == [':equality', ':numeric-fluents', ':typing']

