
import pytest
from tarski.io import FstripsReader
from tarski.io._fstrips.reader import ParsingError


rule_names = {  # TODO Move this somewhere compiling common rule names
    "domain": "domainName",
    "effect": "effect",
    "action_body": "actionDefBody",
    "predicate_definition": "single_predicate_definition",
    "function_definition": "single_function_definition",
    "init_atom": "initEl",
}


def reader():
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True)


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
    problem = r.parse_string("(loc1 ?x) - object", rule_names["function_definition"])
    lang = problem.language
    f = lang.get_function("loc1")
    assert f.codomain == lang.get_sort('object')
    assert f.domain == (lang.get_sort('object'), )


def _test_inputs(inputs, r=None):
    """ Tests all inputs, which air pairs (x, y): x is string to be parsed, y is rule name """
    r = r or reader()
    for string, rule in inputs:
        _ = r.parse_string(string, rule_names[rule])


def test_init():
    _test_inputs([
        # First rule defines the predicate, necessary for the rest of rules not to raise an "UndefinedPredicate" error
        ("(at)", "predicate_definition"),
        ("(at)", "init_atom"),
        ("(not (at))", "init_atom"),
        # ("(assign (at))", "init_atom"),
    ], r=reader())


def test_blocksworld_reading():
    instance_file = "/home/frances/projects/code/downward-benchmarks/visitall-sat11-strips/problem12.pddl"
    domain_file = "/home/frances/projects/code/downward-benchmarks/visitall-sat11-strips/domain.pddl"
    _ = reader().read_problem(domain_file, instance_file)


def test_domain_name_parsing():
    r = reader()

    # Test a few names expected to be valid:
    for domain_name in ["BLOCKS", "blocS-woRlD", "blocks_world"]:
        tag = "(domain {})".format(domain_name)
        _ = r.parse_string(tag, rule_names["domain"])

    # And a few ones expected to be invalid
    for domain_name in ["BL#OCKS", "@mydomain", "2ndblocksworld", "blocks2.0"]:
        tag = "(domain {})".format(domain_name)

        with pytest.raises(ParsingError):
            _ = r.parse_string(tag, rule_names["domain"])


def test_formulas():
    r = reader()

    # Test a few names expected to be valid:
    for domain_name in ["BLOCKS", "blocS-woRlD", "blocks_world"]:
        tag = "(domain {})".format(domain_name)
        _ = r.parse_string(tag, rule_names["domain"])

    # And a few ones expected to be invalid
    for domain_name in ["BL#OCKS", "@mydomain", "2ndblocksworld", "blocks2.0"]:
        tag = "(domain {})".format(domain_name)

        with pytest.raises(ParsingError):
            _ = r.parse_string(tag, rule_names["domain"])


def test_effects():
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


