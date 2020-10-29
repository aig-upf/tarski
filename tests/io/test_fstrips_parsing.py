
import pytest
from tarski.errors import UndefinedSort, UndefinedPredicate
from tarski.fstrips import AddEffect, FunctionalEffect
from tarski.fstrips.errors import InvalidEffectError
from tarski.io.fstrips import ParsingError, FstripsReader
from tarski.syntax import Atom, CompoundFormula, Tautology
from tarski.syntax.util import get_symbols
from tarski.theories import Theory

from tests.common.spider import generate_spider_language
from tests.io.common import reader, parse_benchmark_instance


def get_rule(name):
    return {  # TODO Move this somewhere compiling common rule names
        "domain": "domainName",
        "effect": "effect",
        "action": "actionDef",
        "action_body": "actionDefBody",
        "predicate_definition": "single_predicate_definition",
        "function_definition": "single_function_definition",
        "init_atom": "init_element",
        "formula": "goalDesc"
    }.get(name, name)


def _test_input(string, rule, reader_):
    """ """
    return reader_.parse_string(string, get_rule(rule))


def _test_inputs(inputs, r=None):
    """
        Test a list of pairs (x, y): x is string to be parsed, y is rule name
        and return a list with the corresponding outputs of the parser.
        If no reader `r` is passed, each test is run on a different reader. This might be useful
        for avoiding duplicate name exceptions, etc, in a sequence of tests.
     """
    return [_test_input(string, rule, r or reader()) for string, rule in inputs]


def test_pddl_type_declaration():
    r = reader()
    _test_inputs([
        ("type1", "possibly_typed_name_list"),
        ("type1 type2 type3", "possibly_typed_name_list"),
        ("type1 - object", "possibly_typed_name_list"),
        ("type1 type2 type3 - object", "possibly_typed_name_list"),
    ], r=r)

    o = _test_input("type1 type2 - object type3 type4 - object type5", "possibly_typed_name_list", r)
    assert len(o) == 5 and all(parent == 'object' for typename, parent in o)

    o = _test_input("t t t t", "possibly_typed_name_list", r)
    assert len(o) == 4 and all(parent == 'object' for typename, parent in o)

    o = _test_input("t t t t - t", "possibly_typed_name_list", r)
    assert len(o) == 4 and all(parent == 't' for typename, parent in o)

    o = _test_input("t t t t - t t2 t3", "possibly_typed_name_list", r)
    assert len(o) == 6 and len(list(filter(lambda x: x == 'object', (parent for _, parent in o)))) == 2


def test_symbol_declarations():
    _test_inputs([
        # First rule defines the predicate, necessary for the rest of rules not to raise an "UndefinedPredicate" error
        ("(at)", "predicate_definition"),
        ("(at1 ?x)", "predicate_definition"),
        ("(at5 ?x1 ?x2 ?x3 ?x4 ?x5)", "predicate_definition"),
        ("(loc1 ?x) - object", "function_definition"),
    ], r=reader())

    # Some additional tests
    r = reader()
    problem = r.parse_string("(loc1 ?x) - object", get_rule("function_definition"))
    lang = problem.language
    f = lang.get_function("loc1")
    assert f.codomain == lang.get_sort('object')
    assert f.domain == (lang.get_sort('object'), )


def test_init():
    _test_inputs([
        # First rule defines the predicate, necessary for the rest of rules not to raise an "UndefinedPredicate" error
        ("(at)", "predicate_definition"),
        ("(at)", "init_atom"),
        ("(not (at))", "init_atom"),
        # ("(assign (at))", "init_atom"),
    ], r=reader())


def test_single_atom_goal():
    r = reader()
    _test_inputs([
        # First rule defines the predicate, necessary for the rest of rules not to raise an "UndefinedPredicate" error
        ("(CLEAR ?A - object)", "predicate_definition"),
        ("(:objects A B C D E)", "object_declaration"),
        ("(:goal (AND (CLEAR A)))", "goal"),
    ], r=r)
    assert isinstance(r.problem.goal, Atom)
    assert str(r.problem.goal) == "clear(a)"


def test_domain_name_parsing():
    r = reader()

    # Test a few names expected to be valid:
    for domain_name in ["BLOCKS", "blocS-woRlD", "blocks_world"]:
        tag = "(domain {})".format(domain_name)
        _ = r.parse_string(tag, get_rule("domain"))

    # And a few ones expected to be invalid
    for domain_name in ["BL#OCKS", "@mydomain", "2ndblocksworld", "blocks2.0"]:
        tag = "(domain {})".format(domain_name)

        with pytest.raises(ParsingError):
            _ = r.parse_string(tag, get_rule("domain"))


def test_formulas():
    r = reader()

    # Test a few names expected to be valid:
    for domain_name in ["BLOCKS", "blocS-woRlD", "blocks_world"]:
        tag = "(domain {})".format(domain_name)
        _ = r.parse_string(tag, get_rule("domain"))

    # And a few ones expected to be invalid
    for domain_name in ["BL#OCKS", "@mydomain", "2ndblocksworld", "blocks2.0"]:
        tag = "(domain {})".format(domain_name)

        with pytest.raises(ParsingError):
            _ = r.parse_string(tag, get_rule("domain"))


def test_predicate_effects():
    _test_inputs([
        # First rule defines the predicate, necessary for the rest of rules not to raise an "UndefinedPredicate" error
        ("(at)", "predicate_definition"),
        ("(at)", "effect"),
        ("(not (at))", "effect"),
        ("(and (not (at)))", "effect"),
        ("(and (not (at)) (at) (at))", "effect"),
        ("(forall (?x) (at))", "effect"),
        ("(when (not (at)) (at))", "effect"),
        ("(when (not (at)) (and (at) (at)))", "effect"),
    ], r=reader())  # This uses one single reader for all tests


def test_empty_precs_and_effects():
    _test_inputs([
        ("(and )", "effect"),
        ("()", "precondition"),
        ("(and )", "precondition"),
    ], r=reader())  # This uses one single reader for all tests


def test_functional_effects():
    read = _setup_function_environment(theories=[Theory.EQUALITY, Theory.ARITHMETIC])
    _test_inputs([
        ("(assign (f o1) o1)", "effect"),
        ("(assign (f o1) (f (f o2)))", "effect"),
    ], r=read)

    with pytest.raises(InvalidEffectError):
        _test_inputs([
            ("(assign (f o1) 5))", "effect"),  # RHS not compatible with LHS sort
            # ("(assign (f o1) (+ 5 15))", "effect"),  # RHS not compatible with LHS sort
        ], r=read)

    # Likely we won't check this at the grammar level
    # with pytest.raises(ParsingError):
    #     _test_inputs([
    #         ("(assign (+ 5 4) 0)", "effect"),  # Cannot redefine fixed built-in functions
    #     ], r=read)


def _setup_function_environment(theories=None):
    read = reader(theories=theories)
    # Set up a few declarations of types objects and functions/predicates
    _test_inputs([
        ("(:types t)", "declaration_of_types"),
        ("(:constants o1 o2 - t)", "constant_declaration"),
        ("(f ?o - t) - t", "function_definition"),
    ], r=read)
    return read


def _setup_predicate_environment():
    read = reader()
    # Set up a few declarations of types objects and functions/predicates
    _test_inputs([
        ("(:types t)", "declaration_of_types"),
        ("(:constants o1 o2 - t)", "constant_declaration"),
        ("(p ?o - t)", "predicate_definition"),
    ], r=read)
    return read


def test_functional_atoms():
    read = _setup_function_environment()
    _test_inputs([
        ("(= (f o1) o1)", "formula"),
        ("(= (f o1) (f (f o2)))", "formula"),
    ], r=read)


def test_strips_atoms():
    read = _setup_predicate_environment()
    _test_inputs([
        ("(p o1)", "formula"),
        ("(not (p o1))", "formula"),
        ("(and (p o1) (p o2))", "formula"),
        ("(or (p o1) (p o2))", "formula"),
        ("(imply (p o1) (p o2))", "formula"),
        ("(forall (?x - t) (p ?x))", "formula"),
        ("(exists (?x - t) (p ?x))", "formula"),
    ], r=read)


def test_types():
    _test_inputs([
        ("(:types t1 t2 t3)", "declaration_of_types"),
        ("(:types t1 t2 t3 - object)", "declaration_of_types"),
        ("(:types t1 - object\n t2 - t1\n t3 - t2)", "declaration_of_types"),
        # i.e. t4 and t5 are untyped. Ugly, but allowed by the grammar:
        ("(:types t1 t2 t3 - object t4 t5)", "declaration_of_types"),
        ("(:types t1 object t3)", "declaration_of_types"),
    ])

    with pytest.raises(UndefinedSort):
        # Cannot start  the list of types with "untyped" types and continue with typed ones
        _test_inputs([("(:types t1\n t2 - t1\n t3 - t2)", "declaration_of_types")])


def test_symbol_casing():
    """ Test the special casing for PDDL parsing. See issue #67 """
    problem = parse_benchmark_instance("spider-sat18-strips:p01.pddl")

    # PDDL parsing represents all symbols in lowercase. The PDDL contains a predicate TO-DEAL, but will get lowercased
    _ = problem.language.get_predicate("to-deal")
    with pytest.raises(UndefinedPredicate):
        _ = problem.language.get_predicate("TO-DEAL")

    # PDDL predicate current-deal remains unaffected
    _ = problem.language.get_predicate("current-deal")

    assert "to-deal" in set(x.symbol for x in get_symbols(problem.language, type_="predicate", include_builtin=False))


SPIDER_DEAL_CARD_ACTION = """
(:action deal-card
    :parameters (?c - card ?from - cardposition ?fromdeal - deal ?to - card ?totableau - tableau)
    :precondition
    (and
        (currently-dealing)
        (not (currently-updating-movable))
        (not (currently-updating-unmovable))
        (not (currently-updating-part-of-tableau))
        (not (currently-collecting-deck))
        (current-deal ?fromdeal)
        (TO-DEAL ?c ?totableau ?fromdeal ?from)
        (clear ?c)
        (on ?c ?from)
        (part-of-tableau ?to ?totableau)
        (clear ?to)
    )
    :effect
    (and
        (not (on ?c ?from))
        (on ?c ?to)
        (not (clear ?to))
        (clear ?from)
        (in-play ?c)
        (part-of-tableau ?c ?totableau)
        (movable ?c)
        (when
            (not (CAN-CONTINUE-GROUP ?c ?to))
            (and
                (currently-updating-unmovable)
                (make-unmovable ?to)
            )
        )
    )
)
"""


def test_complex_effects():
    r = FstripsReader(raise_on_error=True, lang=generate_spider_language())

    _test_inputs([
        (SPIDER_DEAL_CARD_ACTION, "action"),
    ], r=r)

    action = r.problem.get_action('deal-card')
    effs = action.effects

    assert len(effs) == 9  # Conditional effects get flattened
    assert isinstance(effs[7], AddEffect) and isinstance(effs[8].condition, CompoundFormula)
    assert isinstance(effs[8], AddEffect) and isinstance(effs[8].condition, CompoundFormula)


def test_plan_metric_parsing():
    import os
    reader = FstripsReader(raise_on_error=True)
    reader.parse_domain(os.path.join('tests', 'data', 'pddl', 'ipc', 'flashfill-sat18', 'domain-p01.pddl'))
    reader.parse_instance(os.path.join('tests', 'data', 'pddl', 'ipc', 'flashfill-sat18', 'p01.pddl'))

    assert reader.problem.plan_metric is not None


def test_increase_effects():
    output = _test_inputs([
        # First rule defines the function, necessary for the rest of rules not to raise some "Undefined" error
        ("(total-cost) - number", "function_definition"),
        ("(increase (total-cost) 1)", "effect"),
    ], r=reader(strict_with_requirements=False))  # This uses one single reader for all tests

    increase = output[1][0]
    assert isinstance(increase, FunctionalEffect) and isinstance(increase.condition, Tautology)
    assert str(increase.rhs) == '+(total-cost(), 1)'
