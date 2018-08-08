
import pytest
from tarski.io._fstrips.reader import ParsingError
from tarski.syntax import Atom
from tarski.theories import Theory

from tests.io.common import reader


def get_rule(name):
    return {  # TODO Move this somewhere compiling common rule names
        "domain": "domainName",
        "effect": "effect",
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
        and return a list with the corresponding outputs of the parser
     """
    r = r or reader()
    return [_test_input(string, rule, r) for string, rule in inputs]


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
        ("(assign (f o1) 10)", "effect"),
        ("(assign (f o1) (+ 5 15))", "effect"),
        ("(assign (f o1) (- 10 2))", "effect"),
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
