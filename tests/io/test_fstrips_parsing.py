
import pytest
from tarski.errors import SyntacticError
from tarski.io import FstripsReader
from tarski.io._fstrips.reader import ParsingError


def get_rule(name):
    return {  # TODO Move this somewhere compiling common rule names
        "domain": "domainName",
        "effect": "effect",
        "action_body": "actionDefBody",
        "predicate_definition": "single_predicate_definition",
        "function_definition": "single_function_definition",
        "init_atom": "initEl",
        "formula": "goalDesc"
    }.get(name, name)


def reader():
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True)


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


def test_blocksworld_reading():
    instance_file = "tests/data/pddl/ipc/visitall-sat11-strips/problem12.pddl"
    domain_file = "tests/data/pddl/ipc/visitall-sat11-strips/domain.pddl"
    _ = reader().read_problem(domain_file, instance_file)


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


def test_functional_effects():
    read = _setup_function_environment()
    _test_inputs([
        ("(assign (f o1) o1)", "effect"),
    ], r=read)


def _setup_function_environment():
    read = reader()
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

def _setup_numeric_environment():
    read = reader()
    read.problem.language.load_theory('arithmetic')
    # Set up a few declaration of numeric functions and objects
    _test_inputs([
        ("(:types vehicle obstacle - object)", "declaration_of_types"),
        ("(:constants v1 v2 - vehicle o1 o2 o3 - obstacle)", "constant_declaration"),
        ("(x ?o - object) - number", "function_definition"),
        ("(y ?o - object) - number", "function_definition"),
        ("(a ?o - obstacle) - number", "function_definition"),
        ("(b ?o - obstacle) - number", "function_definition"),
        ("(c ?o - obstacle) - number", "function_definition"),
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

def test_geometric_precondition():
    read = _setup_numeric_environment()
    _test_inputs([
        ("(>= (x o1) (x o2))", "formula"),
        ("(>= (+ (^ (-(x o1) (x o2)) 2.0) (^ (- (y o1) (y o2)) 2.0)) 1.5)", "formula"),
    ], r=read)

def test_geometric_constraint_syntax_error():
    read = _setup_numeric_environment()
    text = """
    (:constraint foo
        :parameters (?v1 ?v2 - vehicle)
        :condition (>= (- (x o1) (x o2)) 0.0)
    )
    """
    with pytest.raises(ParsingError):
        _test_inputs([
            ( text, "constraintDef"),
        ], r=read)

def test_geometric_constraint_good():
    read = _setup_numeric_environment()
    text = """
    (:constraint foo
        :parameters (?v1 ?v2 - vehicle)
        :condition (>= (- (x ?v1) (x ?v2)) 0.0)
    )
    """
    _test_inputs([
        ( text, "constraintDef"),
    ], r=read)


def test_geometric_action_syntax_error():
    read = _setup_numeric_environment()
    text = """
    (:action move_north
        :parameters (?v - vehicle)
        :precondition (<= (y ?o) 10.0)
        :effect (and
            (assign (x ?o) (+ (x ?o) 0.25))
        )
    )
    """
    from tarski.io._fstrips.reader import UnresolvedVariableError
    with pytest.raises(UnresolvedVariableError):
        _test_inputs([
            (text, "actionDef"),
        ], r=read)

def test_geometric_action_good():
    read = _setup_numeric_environment()
    text = """
    (:action move_north
        :parameters (?v - vehicle)
        :precondition (<= (y ?v) 10.0)
        :effect (and
            (assign (x ?v) (+ (x ?v) 0.25))
        )
    )
    """
    _test_inputs([
        (text, "actionDef"),
    ], r=read)

    assert len(read.problem.actions) == 1
