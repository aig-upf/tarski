import pytest
import tarski as tsk
from tarski.theories import Theory
from tarski.syntax import land, symref
from tarski.sas import Effect, Action, Variable, TemporalAction
from itertools import combinations, permutations

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
    qbits = [L.constant('n{}'.format(i), qbit_t) for i in range(8)]
    qstates = [L.constant('q{}'.format(i), qstate_t) for i in range(8)]

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





