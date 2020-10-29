
from tarski.reachability.asp import create_reachability_lp, LogicProgram, ReachabilityLPCompiler, LPAtom
from tarski.syntax import exists
from tarski import fstrips as fs
from tests.io.common import parse_benchmark_instance

from ..common.gripper import create_sample_problem


def create_compiler(problem):
    lp = LogicProgram()
    return ReachabilityLPCompiler(problem, lp)


def test_lp_compilation():
    problem = create_sample_problem()
    lang = problem.language

    x, y, z = [lang.variable(x, lang.Object) for x in ["x", "y", "z"]]
    room, ball, at_robby, free, at, gripper, carry = lang.get(
        "room", "ball", "at-robby", "free", "at", "gripper", "carry")

    # The conjunction results in a rule body "room(X), room(Y)", with both variable names capitalized, and room prefixed
    # with "atom" to prevent name clashes
    a1, a2 = create_compiler(problem).process_formula(room(x) & room(y))
    assert isinstance(a1, LPAtom) and a1.symbol == a2.symbol == "atom_room" and a1.args == ["X"] and a2.args == ["Y"]

    # A simple built-in equality atom results in an LPAtom
    a1, = create_compiler(problem).process_formula(x == y)
    assert isinstance(a1, LPAtom) and a1.symbol == "=" and a1.args == ["X", "Y"]

    # A disjunction results in an auxiliary atom plus two rules
    c = create_compiler(problem)
    a1, = c.process_formula(room(x) | (room(y) & room(z)))
    assert isinstance(a1, LPAtom) and len(a1.args) == 3 and c.lp.nrules() == 2

    # A nested conjunction with two subatoms
    a1, a2 = create_compiler(problem).process_formula(room(x) & (room(y) | room(z)))
    assert str(a1) == "atom_room(X)" and "__f" in str(a2)

    # An existentially quantified formula
    c = create_compiler(problem)
    a1,  = c.process_formula(exists(x, y, room(x) & room(y)))
    assert str(a1) == "__f1()" and c.lp.nrules() == 1


def test_lp_on_gripper():
    # Test on an untyped problem
    problem = create_sample_problem()
    lp, _ = create_reachability_lp(problem)
    assert lp.nrules() == 31


def test_lp_on_caldera():
    problem = parse_benchmark_instance("caldera-sat18-adl:p01.pddl")
    lp, tr = create_reachability_lp(problem, ground_actions=True)


def test_lp_translation():
    problem = create_sample_problem()
    lang = problem.language

    # Create a fake "gripper" action with same name as the "gripper" predicate
    g = lang.variable("g", lang.Object)
    gripper = lang.get("gripper")
    fake = problem.action("gripper", [g],
                          precondition=gripper(g),
                          effects=[fs.AddEffect(gripper(g))])

    lp = LogicProgram()
    compiler = ReachabilityLPCompiler(problem, lp)
    compiler.process_action(fake, lang, lp)

    # Make sure that the action and atom "gripper" have been processed independently
    assert lp.rules == [
        'action_gripper(G) :- type_object(G), atom_gripper(G).',
        'atom_gripper(G) :- action_gripper(G).']
