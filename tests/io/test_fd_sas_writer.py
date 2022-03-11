import pytest

import tarski as tsk
from tarski.theories import Theory
from tarski.syntax import land, symref
from tarski.io.sas.fd import Writer
from tarski.util import SymbolIndex

@pytest.mark.sas
def test_gripper_instance():
    """
    Follows the example given in:

    https://www.fast-downward.org/TranslatorOutputFormat4
    """

    # Gripper domain theory
    L = tsk.language("gripper", theories=[Theory.BOOLEAN, Theory.EQUALITY, Theory.ARITHMETIC])

    # Types
    ball_t = L.sort('ball', L.Object)
    gripper_t = L.sort('gripper', L.Object)
    room_t = L.sort('room', L.Object)

    # Constant objects
    none = L.constant("none", L.Object)
    the_balls = [L.constant('ball{}'.format(i), ball_t) for i in range(5)]
    grippers = [L.constant(gripper_name, gripper_t) for gripper_name in ('left', 'right')]
    the_rooms = [L.constant('room{}'.format(i), room_t) for i in ('a', 'b')]

    # predicates
    carry = L.function('carry', ball_t, gripper_t, L.Integer)
    free = L.function('free', gripper_t, L.Integer)
    at_ball = L.function('at_ball', ball_t, room_t, L.Integer)
    at_robot = L.function('at_robot', room_t, L.Integer)

    # SAS instance data structures
    # variable set
    X = SymbolIndex()
    # domains
    D = {}

    # Theory that results from Helmert's invariant detection algorithm

    # Constants
    L2 = tsk.language("mv-gripper", theories=[Theory.EQUALITY])
    none = L2.constant("<none of those>")

    var0 = L2.function("var0", L.Object)
    var0_domain = [
        L2.constant(str(carry(the_balls[0], grippers[1])), L.Object),
        L2.constant(str(carry(the_balls[1], grippers[1])), L.Object),
        L2.constant(str(carry(the_balls[2], grippers[1])), L.Object),
        L2.constant(str(free(grippers[1])), L.Object),
        L2.constant(str(carry(the_balls[3], grippers[1])), L.Object)
    ]

    X.add(symref(var0))
    D[symref(var0)] = SymbolIndex()
    for v in var0_domain:
        D[symref(var0)].add(symref(v))

    var1 = L2.function("var1", L.Object)
    var1_domain = [
        L2.constant(str(carry(the_balls[2], grippers[0])), L.Object),
        L2.constant(str(free(grippers[0])), L.Object),
        L2.constant(str(carry(the_balls[1], grippers[0])), L.Object),
        L2.constant(str(carry(the_balls[0], grippers[0])), L.Object),
        L2.constant(str(carry(the_balls[3], grippers[0])), L.Object)
    ]

    X.add(symref(var1))
    D[symref(var1)] = SymbolIndex()
    for v in var1_domain:
        D[symref(var1)].add(symref(v))

    var2 = L2.function("var2", L.Object)
    var2_domain = [
        L2.constant(str(at_ball(the_balls[3], the_rooms[0])), L.Object),
        L2.constant(str(at_ball(the_balls[3], the_rooms[1])), L.Object),
        none
    ]

    X.add(symref(var2))
    D[symref(var2)] = SymbolIndex()
    for v in var2_domain:
        D[symref(var2)].add(symref(v))

    var3 = L2.function("var3", L.Object)
    var3_domain = [
        L2.constant(str(at_ball(the_balls[2], the_rooms[0])), L.Object),
        L2.constant(str(at_ball(the_balls[2], the_rooms[1])), L.Object),
        none
    ]

    X.add(symref(var3))
    D[symref(var3)] = SymbolIndex()
    for v in var3_domain:
        D[symref(var3)].add(symref(v))

    var4 = L2.function("var4", L.Object)
    var4_domain = [
        L2.constant(str(at_ball(the_balls[0], the_rooms[0])), L.Object),
        L2.constant(str(at_ball(the_balls[0], the_rooms[1])), L.Object),
        none
    ]

    X.add(symref(var4))
    D[symref(var4)] = SymbolIndex()
    for v in var4_domain:
        D[symref(var4)].add(symref(v))

    var5 = L2.function("var5", L.Object)
    var5_domain = [
        L2.constant(str(at_ball(the_balls[1], the_rooms[0])), L.Object),
        L2.constant(str(at_ball(the_balls[1], the_rooms[1])), L.Object),
        none
    ]

    X.add(symref(var5))
    D[symref(var5)] = SymbolIndex()
    for v in var5_domain:
        D[symref(var5)].add(symref(v))

    var6 = L2.function("var6", L.Object)
    var6_domain = [
        L2.constant(str(at_robot(the_rooms[1])), L.Object),
        L2.constant(str(at_robot(the_rooms[0])), L.Object)
    ]

    X.add(symref(var6))
    D[symref(var6)] = SymbolIndex()
    for v in var6_domain:
        D[symref(var6)].add(symref(v))


    # initial state
    # note that here we diverge from the example in https://www.fast-downward.org/TranslatorOutputFormat4 which
    # does not give sensible values for the state variables given
    initial_state = [
        (var0, var0_domain[0]), # robot carries ball1 on right gripper
        (var1, var1_domain[0]), # robot carries ball3 on left gripper
        (var2, var2_domain[0]), # ball 4 is at room a
        (var3, var3_domain[2]), # ball 3 is <none of those>
        (var4, var4_domain[2]), # ball 1 is <none of those>
        (var5, var5_domain[0]), # ball 2 is at room a
        (var6, var6_domain[0]), # robot is at room b
    ]

    goal_state = [
        (var2, var2_domain[1]), # ball 4 is at room b
        (var3, var3_domain[1]), # ball 3 is at room b
        (var4, var4_domain[1]), # ball 1 is at room b
        (var5, var5_domain[1]), # ball 2 is at room b
    ]

