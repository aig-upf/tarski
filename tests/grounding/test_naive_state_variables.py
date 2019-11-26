
from tarski.grounding import ProblemGrounding, NaiveGroundingStrategy, create_all_possible_state_variables
from tarski.util import IndexDictionary

from tests.common.blocksworld import create_4blocks_task, generate_small_strips_bw_problem, \
    generate_small_fstrips_bw_problem
from tests.common import parcprinter
from tests.fstrips.hybrid.tasks import create_billiards_world


def test_problem_grounding_on_two_domains():

    # Test some grounding routines on parcprinter
    problem = parcprinter.create_small_task()
    grounding = NaiveGroundingStrategy(problem)

    as_list1 = lambda symbols: sorted(s.symbol for s in symbols)
    # ATM we consider the grounding should not be responsible for including / discarding "total-cost"
    assert as_list1(grounding.static_symbols) == ['Prevsheet', 'Sheetsize', 'Uninitialized']
    assert as_list1(grounding.fluent_symbols) == ['Available', 'Location', 'Stackedin', 'total-cost']

    as_list2 = lambda symbols: sorted(map(str, symbols))
    variables = grounding.ground_state_variables()
    # Make sure that Uninitialized is also grounded, even though it is a nullary symbol
    assert ['Available(Finisher2-RSRC)', 'Location(dummy-sheet,Finisher2_Entry-Finisher1_Exit)',
            'Location(dummy-sheet,Finisher2_Tray)', 'Location(dummy-sheet,Some_Feeder_Tray)',
            'Location(dummy-sheet,Some_Finisher_Tray)', 'Location(sheet1,Finisher2_Entry-Finisher1_Exit)',
            'Location(sheet1,Finisher2_Tray)', 'Location(sheet1,Some_Feeder_Tray)',
            'Location(sheet1,Some_Finisher_Tray)', 'Stackedin(dummy-sheet,Finisher2_Entry-Finisher1_Exit)',
            'Stackedin(dummy-sheet,Finisher2_Tray)', 'Stackedin(dummy-sheet,Some_Feeder_Tray)',
            'Stackedin(dummy-sheet,Some_Finisher_Tray)', 'Stackedin(sheet1,Finisher2_Entry-Finisher1_Exit)',
            'Stackedin(sheet1,Finisher2_Tray)', 'Stackedin(sheet1,Some_Feeder_Tray)',
            'Stackedin(sheet1,Some_Finisher_Tray)', 'total-cost()'] == as_list2(variables)

    # Test some grounding routines on a STRIPS blocksworld
    problem = generate_small_strips_bw_problem()
    grounding = NaiveGroundingStrategy(problem)
    assert as_list1(grounding.static_symbols) == []
    assert as_list1(grounding.fluent_symbols) == ['clear', 'handempty', 'holding', 'on', 'ontable']

    variables = grounding.ground_state_variables()
    assert len(variables) == 29

    # Test some grounding routines on a (typed) Functional STRIPS blocksworld
    problem = generate_small_fstrips_bw_problem()
    grounding = NaiveGroundingStrategy(problem)
    assert as_list1(grounding.static_symbols) == []
    assert as_list1(grounding.fluent_symbols) == ['clear', 'loc']

    variables = grounding.ground_state_variables()
    assert ['clear(b1)', 'clear(b2)', 'clear(b3)', 'clear(b4)', 'clear(table)', 'loc(b1)', 'loc(b2)', 'loc(b3)',
            'loc(b4)'] == as_list2(variables)


def test_all_state_variables_can_be_evaluated_in_init_parcprinter():
    prob = parcprinter.create_small_task()
    index = ProblemGrounding(prob)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in create_all_possible_state_variables(index.fluent_terms):
        index.state_variables.add(var)
    for var in index.state_variables:
        val = prob.init[var.ground]
        assert val in (True, False, 0.0)


def test_task_index_create_state_variables_blocksworld():
    prob = create_4blocks_task()
    index = ProblemGrounding(prob)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in create_all_possible_state_variables(index.fluent_terms):
        index.state_variables.add(var)

    # print(','.join([str(var) for var in index.state_variables]))
    assert len(index.state_variables) == 12


def test_create_state_variables_for_hybrid_problem_with_reactions():
    prob = create_billiards_world()
    index = ProblemGrounding(prob)
    index.process_symbols(prob)
    index.state_variables = IndexDictionary()
    for var in create_all_possible_state_variables(index.fluent_terms):
        index.state_variables.add(var)
    assert len(index.state_variables) == 4
