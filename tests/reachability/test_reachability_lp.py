
from tarski.reachability.asp import create_reachability_lp, LogicProgram, ReachabilityLPCompiler, LPAtom
from tarski.syntax import exists

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

    # TODO Test also on an problem with types

