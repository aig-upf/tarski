from itertools import combinations, permutations

import pytest

import tarski as tsk
from tarski.sas import Action, Effect, TemporalAction, Variable
from tarski.syntax import land, symref
from tarski.theories import Theory


@pytest.mark.sas
def test_variable_interface():
    """
        Creates manually a SAS+ instance without domain constraints/axioms, following the example
        Fast-Downward translator output described here:
            - https://www.fast-downward.org/TranslatorOutputFormat4
    """
    L = tsk.language("mylang", theories=[Theory.BOOLEAN, Theory.EQUALITY, Theory.ARITHMETIC])

    # Types
    ball_t = L.sort('ball', L.Object)
    gripper_t = L.sort('gripper', L.Object)
    room_t = L.sort('room', L.Object)

    # Constant objects
    none = L.constant("none", L.Object)
    the_balls = [L.constant(f'ball{i}', ball_t) for i in range(5)]
    grippers = [L.constant(gripper_name, gripper_t) for gripper_name in ('left', 'right')]
    the_rooms = [L.constant(f'room{i}', room_t) for i in ('a', 'b')]

    # predicates
    carry = L.function('carry', ball_t, gripper_t, L.Integer)
    free = L.function('free', gripper_t, L.Integer)
    at_ball = L.function('at_ball', ball_t, room_t, L.Integer)
    at_robot = L.function('at_robot', room_t, L.Integer)

    var0 = Variable(id=0,
                    symbol=L.function('var0', L.Integer),
                    domain=[carry(the_balls[0], grippers[1]),
                            carry(the_balls[1], grippers[1]),
                            carry(the_balls[2], grippers[1]),
                            free(grippers[1]),
                            carry(the_balls[3], grippers[1])])

    assert var0.index(symref(free(grippers[1]))) == 3

    var3 = Variable(id=3,
                    symbol=L.function('var3', L.Integer),
                    domain=[at_ball(the_balls[2], the_rooms[0]),
                            at_ball(the_balls[2], the_rooms[1])],
                    needs_closure=True)

    assert var3.index(symref(at_ball(the_balls[2], the_rooms[1]))) == 1
    assert var3.index(None) == -1

@pytest.mark.sas
def test_gripper():
    """
        Creates manually a SAS+ instance without domain constraints/axioms, following the example
        Fast-Downward translator output described here:
            - https://www.fast-downward.org/TranslatorOutputFormat4
    """
    L = tsk.language("mylang", theories=[Theory.BOOLEAN, Theory.EQUALITY, Theory.ARITHMETIC])

    # Types
    ball_t = L.sort('ball', L.Object)
    gripper_t = L.sort('gripper', L.Object)
    room_t = L.sort('room', L.Object)

    # Constant objects
    none = L.constant("none", L.Object)
    the_balls = [L.constant(f'ball{i}', ball_t) for i in range(5)]
    grippers = [L.constant(gripper_name, gripper_t) for gripper_name in ('left', 'right')]
    the_rooms = [L.constant(f'room{i}', room_t) for i in ('a', 'b')]

    # predicates
    carry = L.function('carry', ball_t, gripper_t, L.Integer)
    free = L.function('free', gripper_t, L.Integer)
    at_ball = L.function('at_ball', ball_t, room_t, L.Integer)
    at_robot = L.function('at_robot', room_t, L.Integer)

    var0 = Variable(id=0,
                    symbol=L.function('var0', L.Integer),
                    domain=[carry(the_balls[0], grippers[1]),
                            carry(the_balls[1], grippers[1]),
                            carry(the_balls[2], grippers[1]),
                            free(grippers[1]),
                            carry(the_balls[3], grippers[1])])

    var1 = Variable(id=1,
                    symbol=L.function('var1', L.Integer),
                    domain=[carry(the_balls[2], grippers[0]),
                            free(grippers[0]),
                            carry(the_balls[1], grippers[0]),
                            carry(the_balls[0], grippers[0]),
                            carry(the_balls[3], grippers[0])])

    var2 = Variable(id=2,
                    symbol=L.function('var2', L.Integer),
                    domain=[at_ball(the_balls[3], the_rooms[0]),
                            at_ball(the_balls[3], the_rooms[1])],
                    needs_closure=True)

    var3 = Variable(id=3,
                    symbol=L.function('var3', L.Integer),
                    domain=[at_ball(the_balls[2], the_rooms[0]),
                            at_ball(the_balls[2], the_rooms[1])],
                    needs_closure=True)

    var4 = Variable(id=4,
                    symbol=L.function('var4', L.Integer),
                    domain=[at_ball(the_balls[0], the_rooms[0]),
                            at_ball(the_balls[0], the_rooms[1])],
                    needs_closure=True)

    var5 = Variable(id=5,
                    symbol=L.function('var5', L.Integer),
                    domain=[at_ball(the_balls[1], the_rooms[0]),
                            at_ball(the_balls[1], the_rooms[1])],
                    needs_closure=True)

    var6 = Variable(id=6,
                    symbol=L.function('var6', L.Integer),
                    domain=[at_robot(the_rooms[0]),
                            at_robot(the_rooms[1])])

    pick_ball = L.function('pick_ball', ball_t, gripper_t, room_t, L.Integer)

    # Sample action encoding
    act = Action(name=pick_ball(the_balls[0], grippers[0], the_rooms[0]),
                 effects=[
                     Effect(var=var1, pre=free(grippers[0]), post=carry(the_balls[0], grippers[0])),
                     Effect(var=var4, pre=at_ball(the_balls[0], the_rooms[0]), post=None)
                 ])


@pytest.mark.sas
def test_temporal_action():
    """
    Simple test for durative actions, based on the quantum circuit compilation benchmark
    :return:
    """
    L = tsk.language("qcc", theories=[Theory.BOOLEAN, Theory.EQUALITY, Theory.ARITHMETIC])

    # sorts
    qbit_t = L.sort('qbit', L.Object)
    qstate_t = L.sort('qstate', L.Object)

    # constant objects
    qbits = [L.constant(f'n{i}', qbit_t) for i in range(8)]
    qstates = [L.constant(f'q{i}', qstate_t) for i in range(8)]

    # predicates
    at = L.function('at', qstate_t, qbit_t, L.Integer)

    X = []

    qstate_loc = L.function('qstate_loc', qstate_t, qbit_t)

    for i, qstate in enumerate(qstates):

        values = [at(qstates[i], qbit) for qbit in qbits]
        qstate_i_loc = Variable(id=i,
                                symbol=qstate_loc(qstates[i]),
                                domain=values,
                                needs_closure=True)
        X += [qstate_i_loc]

    assert len(X) == 8

    swap_evt0 = L.function('swap_evt_0', qstate_t, qstate_t, qbit_t, qbit_t, L.Integer)
    swap_evt1 = L.function('swap_evt_1', qstate_t, qstate_t, qbit_t, qbit_t, L.Integer)
    swap_act = L.function('swap', qstate_t, qstate_t, qbit_t, qbit_t, L.Integer)

    swap_actions = []
    for qs1, qs2 in combinations(range(len(qstates)), 2):

        for qb1, qb2 in permutations(range(len(qbits)), 2):

            evt0 = Action(name=swap_evt0(qstates[qs1], qstates[qs2], qbits[qb1], qbits[qb2]),
                          effects=[
                              Effect(var=X[qs1], pre=at(qstates[qs1], qbits[qb1]), post=None),
                              Effect(var=X[qs2], pre=at(qstates[qs2], qbits[qb2]), post=None)
                          ])
            evt1 = Action(name=swap_evt1(qstates[qs1], qstates[qs2], qbits[qb1], qbits[qb2]),
                          effects=[
                              Effect(var=X[qs1], pre=None, post=at(qstates[qs1], qbits[qb2])),
                              Effect(var=X[qs2], pre=None, post=at(qstates[qs2], qbits[qb1]))
                          ])
            swap_action = TemporalAction(name=swap_act(qstates[qs1], qstates[qs2], qbits[qb1], qbits[qb2]),
                                        events=[(0.0, evt0), (3.0, evt1)])
            swap_actions += [swap_action]

    assert len(swap_actions) == 1568





