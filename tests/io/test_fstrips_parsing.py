
import pytest
from tarski.io import FstripsReader
from tarski.io._fstrips.reader import ParsingError


rule_names = {  # TODO Move this somewhere compiling common rule names
    "domain": "domainName",
    "effect": "effect",
    "action_body": "actionDefBody"
}


def reader():
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True)


def XXXtest_blocksworld_reading():
    instance_file = "/home/frances/projects/code/downward-benchmarks/visitall-sat11-strips/problem12.pddl"
    domain_file = "/home/frances/projects/code/downward-benchmarks/visitall-sat11-strips/domain.pddl"
    _ = reader().read_problem(domain_file, instance_file)


def XXXtest_domain_name_parsing():
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


def XXXtest_formulas():
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
    r = reader()

    effects = [
        # ":precondition (and (at a)) :effect (and (not (at a)))"
        "(at)"
    ]

    for effect in effects:
        _ = r.parse_string(effect, rule_names["effect"])

