
from tarski.fstrips.representation import collect_effect_free_parameters, project_away_effect_free_variables, \
    collect_effect_free_variables, project_away_effect_free_variables_from_problem, is_typed_problem
from tarski.syntax import exists, land
from tarski.fstrips import representation as rep

from tests.common import blocksworld
from tests.common.blocksworld import generate_small_fstrips_bw_language
from tests.io.common import collect_strips_benchmarks, reader


def test_basic_representation_queries():
    lang = generate_small_fstrips_bw_language(nblocks=5)
    clear, loc, b1, b2, b3 = lang.get('clear', 'loc', 'b1', 'b2', 'b3')
    x = lang.variable('x', lang.ns.block)

    assert rep.is_function_free(b1)
    assert rep.is_function_free(clear(b1))
    assert rep.is_function_free((clear(b1) & clear(b2)) | clear(b3))
    assert rep.is_function_free(exists(x, clear(x)))
    assert not rep.is_function_free(loc(b1) == b2)

    assert rep.is_conjunction_of_literals(clear(b1))
    assert rep.is_conjunction_of_literals(~clear(b1))
    assert rep.is_conjunction_of_literals(~~clear(b1))

    assert rep.is_conjunction_of_literals(clear(b1) & clear(b2))
    assert rep.is_conjunction_of_literals(clear(b1) & ~clear(b2))
    assert rep.is_conjunction_of_literals(clear(b1) & ~~clear(b2))

    assert rep.is_conjunction_of_literals(loc(b1) == b2)
    assert rep.is_conjunction_of_literals(loc(b1) != b2)
    assert rep.is_conjunction_of_literals(~(loc(b1) == b2))

    assert not rep.is_conjunction_of_literals(~(clear(b1) & clear(b2)))
    assert not rep.is_conjunction_of_literals((clear(b1) & clear(b2)) | clear(b3))
    assert not rep.is_conjunction_of_literals(exists(x, clear(x)))


def test_literal_collection():
    lang = generate_small_fstrips_bw_language(nblocks=5)
    clear, loc, b1, b2, b3 = lang.get('clear', 'loc', 'b1', 'b2', 'b3')
    x = lang.variable('x', lang.ns.block)

    assert rep.collect_literals_from_conjunction(clear(b1)) == {(clear(b1), True)}
    assert rep.collect_literals_from_conjunction(~clear(b1)) == {(clear(b1), False)}
    assert len(rep.collect_literals_from_conjunction(clear(b1) & ~clear(b2))) == 2
    assert len(rep.collect_literals_from_conjunction(land(clear(b1), clear(b2), clear(b3)))) == 3

    assert len(rep.collect_literals_from_conjunction(clear(x) & clear(b1) & clear(x))) == 2

    # These ones are not conjunctions of literals, so should return None
    assert rep.collect_literals_from_conjunction(~(clear(b1) & clear(b2))) is None
    assert rep.collect_literals_from_conjunction((clear(b1) & clear(b2)) | clear(b3)) is None
    assert rep.collect_literals_from_conjunction(exists(x, clear(x))) is None

    # ATM we don't want to deal with the complexity of nested negation, so we expect the method to return None for
    # "not not clear(b2)"
    assert rep.collect_literals_from_conjunction(clear(b1) & ~~clear(b2)) is None


def test_is_typed():
    problem = blocksworld.generate_small_fstrips_bw_problem()
    assert is_typed_problem(problem)

    problem = blocksworld.generate_small_strips_bw_problem()
    assert not is_typed_problem(problem)


def test_free_variables_in_schema_manipulations():
    problem = blocksworld.generate_small_fstrips_bw_problem()
    free = collect_effect_free_parameters(problem.get_action('move'))
    assert not free  # Move has no effect-free variable


def test_effect_free_variables_in_organic_synthesis():
    instance_file, domain_file = collect_strips_benchmarks(["organic-synthesis-opt18-strips:p01.pddl"])[0]
    problem = reader().read_problem(domain_file, instance_file)
    free = collect_effect_free_parameters(problem.get_action('additionofrohacrossgemdisubstitutedalkene'))
    names = sorted(x.expr.symbol for x in free)
    assert names == ['?h_3', '?h_4', '?r0_7', '?r1_8', '?r2_9']

    free = collect_effect_free_parameters(problem.get_action('additionofrohacrossmonosubstitutedalkene'))
    names = sorted(x.expr.symbol for x in free)
    assert names == ['?h_3', '?h_4', '?h_5', '?r0_8', '?r1_9']

    free = collect_effect_free_parameters(problem.get_action('additionofrohacrosstetrasubstitutedalkene'))
    names = sorted(x.expr.symbol for x in free)
    assert names == ['?r0_5', '?r1_6', '?r2_7', '?r3_8', '?r4_9']

    projected = project_away_effect_free_variables(problem.get_action('additionofrohacrosstetrasubstitutedalkene'))
    names = sorted(x.symbol for x in projected.parameters)
    assert names == ['?c_1', '?c_2', '?h_3', '?o_4']


def test_effect_free_variables_in_caldera():
    instance_file, domain_file = collect_strips_benchmarks(["caldera-opt18-adl:p01.pddl"])[0]
    problem = reader().read_problem(domain_file, instance_file)

    act = problem.get_action('get_domain')
    free = collect_effect_free_parameters(act)
    names = sorted(x.expr.symbol for x in free)
    assert names == ['?v00', '?v02']

    assert len(act.effects) == 1
    free = collect_effect_free_variables(act.effects[0])
    names = sorted(x.expr.symbol for x in free)
    assert names == ['?v01']

    projected = project_away_effect_free_variables(act)
    names1 = sorted(x.symbol for x in act.parameters)
    names2 = sorted(x.symbol for x in projected.parameters)
    assert names1 == ['?v00', '?v01', '?v02'] and names2 == ['?v01']

    # Check inplace argument works as expected
    problem2 = project_away_effect_free_variables_from_problem(problem, inplace=False)
    names1 = sorted(x.symbol for x in problem.get_action('get_domain').parameters)
    names2 = sorted(x.symbol for x in problem2.get_action('get_domain').parameters)
    assert names1 == ['?v00', '?v01', '?v02'] and names2 == ['?v01']

    problem2 = project_away_effect_free_variables_from_problem(problem, inplace=True)
    names1 = sorted(x.symbol for x in problem.get_action('get_domain').parameters)
    names2 = sorted(x.symbol for x in problem2.get_action('get_domain').parameters)
    assert names1 == names2 == ['?v01']
