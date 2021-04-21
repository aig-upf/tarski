import tarski.benchmarks.blocksworld
from tarski.benchmarks.counters import generate_fstrips_counters_problem
from tarski.fstrips.representation import collect_effect_free_parameters, project_away_effect_free_variables, \
    collect_effect_free_variables, project_away_effect_free_variables_from_problem, is_typed_problem, \
    identify_cost_related_functions, compute_delete_free_relaxation, is_delete_free, is_strips_problem, \
    is_conjunction_of_positive_atoms, is_strips_effect_set, compile_away_formula_negated_literals, \
    compile_action_negated_preconditions_away, compile_negated_preconditions_away, compute_complementary_atoms
from tarski.syntax import exists, land, neg, symref, substitute_expression, forall
from tarski.fstrips import representation as rep, AddEffect, DelEffect
from tarski.syntax.ops import flatten
from tarski.benchmarks.blocksworld import generate_fstrips_bw_language, generate_fstrips_blocksworld_problem, \
    generate_strips_blocksworld_problem
from tests.io.common import parse_benchmark_instance


def test_basic_representation_queries():
    lang = generate_fstrips_bw_language(nblocks=5)
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
    assert not rep.is_conjunction_of_literals(clear(b1) & ~~clear(b2))

    assert rep.is_conjunction_of_literals(loc(b1) == b2)
    assert rep.is_conjunction_of_literals(loc(b1) != b2)
    assert rep.is_conjunction_of_literals(~(loc(b1) == b2))

    assert not rep.is_conjunction_of_literals(~(clear(b1) & clear(b2)))
    assert not rep.is_conjunction_of_literals((clear(b1) & clear(b2)) | clear(b3))
    assert not rep.is_conjunction_of_literals(exists(x, clear(x)))


def test_literal_collection():
    lang = generate_fstrips_bw_language(nblocks=5)
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
    problem = generate_fstrips_blocksworld_problem()
    assert is_typed_problem(problem)

    problem = tarski.benchmarks.blocksworld.generate_strips_blocksworld_problem()
    assert not is_typed_problem(problem)


def test_free_variables_in_schema_manipulations():
    problem = generate_fstrips_blocksworld_problem()
    free = collect_effect_free_parameters(problem.get_action('move'))
    assert not free  # Move has no effect-free variable


def test_effect_free_variables_in_organic_synthesis():
    problem = parse_benchmark_instance("organic-synthesis-opt18-strips:p01.pddl")
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
    problem = parse_benchmark_instance("caldera-opt18-adl:p01.pddl")

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


def test_cost_function_identification():
    problem = generate_fstrips_counters_problem(ncounters=3)
    functions = identify_cost_related_functions(problem)
    assert functions == set()

    problem = parse_benchmark_instance("agricola-opt18-strips:p01.pddl")
    functions = identify_cost_related_functions(problem)
    assert functions == {"group_worker_cost"}


def test_delete_free_functions():
    problem = generate_strips_blocksworld_problem()
    relaxed = compute_delete_free_relaxation(problem)

    pickup = problem.get_action('pick-up')
    assert len(pickup.effects) == 4  # Make sure the old action is unaffected

    assert not is_delete_free(problem)
    assert is_delete_free(relaxed)

    pickup = relaxed.get_action('pick-up')
    # The new action has had its 3 delete-effects removed
    assert len(pickup.effects) == 1 and isinstance(pickup.effects[0], AddEffect)


def test_strips_analysis():
    problem = generate_strips_blocksworld_problem()
    assert is_strips_problem(problem)

    lang = problem.language
    clear, on, ontable, handempty, holding = lang.get('clear', 'on', 'ontable', 'handempty', 'holding')
    x = lang.variable('x', 'object')

    phi = clear(x) & ~ontable(x)
    assert not is_conjunction_of_positive_atoms(clear(x) & ~ontable(x))

    assert is_strips_effect_set([DelEffect(ontable(x)), DelEffect(clear(x))])
    assert is_strips_effect_set([DelEffect(ontable(x)), DelEffect(ontable(x))])
    # Not strips, as it has an effect with conditions:
    assert not is_strips_effect_set([DelEffect(ontable(x), clear(x)), AddEffect(ontable(x))])
    # Not strips, as it has two contradictory effects:
    assert not is_strips_effect_set([DelEffect(ontable(x)), AddEffect(ontable(x))])

    problem = generate_fstrips_counters_problem(ncounters=3)

    assert not is_strips_problem(problem)
    inc = problem.get_action('increment')
    assert not is_strips_effect_set(inc.effects)


def test_neg_precondition_compilation_on_formulas():
    problem = generate_strips_blocksworld_problem()
    lang = problem.language
    clear, on, ontable, handempty, holding = lang.get('clear', 'on', 'ontable', 'handempty', 'holding')
    x = lang.variable('x', 'object')
    y = lang.variable('y', 'object')

    negpreds = dict()

    comp = compile_away_formula_negated_literals(clear(x) & (x != y), negpreds)
    assert comp == clear(x) & (x != y) and not negpreds  # No change was made

    comp = compile_away_formula_negated_literals(neg(x == y), negpreds)
    assert comp == neg(x == y) and not negpreds  # No change was made

    comp = compile_away_formula_negated_literals(clear(x) & ontable(x), negpreds)
    assert comp == clear(x) & ontable(x) and not negpreds  # No change was made

    comp = compile_away_formula_negated_literals(clear(x) & ~ontable(x), negpreds)
    assert str(comp) == '(clear(x) and _not_ontable(x))'

    # Compile again to check that predicate is not declared twice, which would raise an error
    comp = compile_away_formula_negated_literals(clear(x) & ~ontable(x), negpreds)
    assert str(comp) == '(clear(x) and _not_ontable(x))'


def test_neg_precondition_compilation_on_action():
    problem = generate_strips_blocksworld_problem()
    lang = problem.language
    clear, on, ontable, handempty, holding = lang.get('clear', 'on', 'ontable', 'handempty', 'holding')
    x = lang.variable('x', 'object')

    negpreds = dict()
    
    pickup = problem.get_action('pick-up')
    pickupc = compile_action_negated_preconditions_away(pickup, negpreds)
    assert flatten(pickup.precondition) == pickupc.precondition and len(negpreds) == 0

    act1 = problem.action('act1', [x],
                          precondition=clear(x) & ~ontable(x) & handempty(),
                          effects=[DelEffect(ontable(x), ~clear(x)),
                                   AddEffect(ontable(x))])
    act1c = compile_action_negated_preconditions_away(act1, negpreds)
    assert len(negpreds) == 2  # For ontable and for clear
    assert str(act1c.precondition) == '(clear(x) and _not_ontable(x) and handempty())'
    assert str(act1c.effects[0].condition) == '_not_clear(x)'


def test_neg_precondition_compilation_on_problem():
    problem = generate_strips_blocksworld_problem()
    lang = problem.language
    b1, clear, on, ontable, handempty, holding = lang.get('b1', 'clear', 'on', 'ontable', 'handempty', 'holding')
    x = lang.variable('x', 'object')

    compiled = compile_negated_preconditions_away(problem)

    # Check that nothing was changed
    for aname, a1 in problem.actions.items():
        a2 = compiled.get_action(aname)
        assert flatten(a1.precondition) == a2.precondition

    act1 = problem.action('act1', [x],
                          precondition=clear(x) & ~ontable(x) & handempty(),
                          effects=[DelEffect(ontable(x), ~clear(x)),
                                   AddEffect(ontable(x))])
    compiled = compile_negated_preconditions_away(problem)
    assert str(compiled.get_action('act1').precondition) == '(clear(x) and _not_ontable(x) and handempty())'


def test_neg_precondition_compilation_on_problem2():
    problem = generate_strips_blocksworld_problem()
    lang = problem.language
    b1, clear, on, ontable, handempty, holding = lang.get('b1', 'clear', 'on', 'ontable', 'handempty', 'holding')

    # Change the goal to include some negated preconditions, this should trigger
    # the rewriting of some action effects
    problem.goal = ~ontable(b1) & ~handempty()
    compiled = compile_negated_preconditions_away(problem)

    # Check that indeed new effects have been added of the appropriate type and appropriate predicate
    assert str(compiled.get_action('unstack').effects[-1]) == '(T -> ADD(_not_handempty()))'
    assert str(compiled.get_action('stack').effects[-1]) == '(T -> DEL(_not_handempty()))'

    # Check the goal has been correctly rewritten
    assert str(compiled.goal) == '(_not_ontable(b1) and _not_handempty())'

    # Check the initial state has been correctly updated
    init = compiled.init
    nhe, nont = lang.get('_not_handempty', '_not_ontable')
    assert init[nont(b1)] or init[ontable(b1)]
    assert init[neg(nhe())] or init[neg(handempty())]


def test_compute_complementary_atoms():
    problem = generate_strips_blocksworld_problem()
    lang = problem.language
    testpred = lang.predicate('test')  # Try a nullary predicate

    assert list(compute_complementary_atoms(problem.init, testpred)) == [()]

    problem.init.add(testpred)
    assert list(compute_complementary_atoms(problem.init, testpred)) == []

    # assert len(list(compute_complementary_atoms(problem.init, lang.get('clear')))) == 2


def test_simple_expression_substitutions():
    lang = tarski.benchmarks.blocksworld.generate_strips_bw_language(nblocks=2)
    clear, b1, b2 = [lang.get(name) for name in ('clear', 'b1', 'b2')]
    x, y = lang.variable('x', 'object'), lang.variable('y', 'object')

    formula = clear(x)
    replaced = substitute_expression(formula, substitution={symref(x): b1}, inplace=False)
    replaced2 = substitute_expression(formula, substitution={symref(x): b2}, inplace=False)

    assert not formula.is_syntactically_equal(replaced)
    assert str(formula) == "clear(x)" and str(replaced) == "clear(b1)" and str(replaced2) == "clear(b2)"

    # Now let's do the same but inplace
    replaced = substitute_expression(formula, substitution={symref(x): b1}, inplace=True)

    assert formula.is_syntactically_equal(replaced)
    assert str(formula) == str(replaced) == "clear(b1)"

    formula = forall(x, clear(x) & clear(y))
    replaced = substitute_expression(formula, substitution={symref(x): b1, symref(y): b2}, inplace=False)
    assert str(formula) == "forall x : ((clear(x) and clear(y)))" and \
           str(replaced) == "forall b1 : ((clear(b1) and clear(b2)))"
