import pytest
import tarski as tsk
from tarski.theories import Theory
from tarski.syntax import land, symref
from tarski.sas import Schema, Action
from tarski.sas.temporal import TemporalAction
from itertools import combinations, permutations


@pytest.mark.sas
def test_temporal_action():
    """
    Simple test for durative actions, based on the quantum circuit compilation benchmark
    :return:
    """
    L = tsk.language("qcc", theories=[Theory.BOOLEAN, Theory.EQUALITY, Theory.ARITHMETIC])

    # sorts
    # qbits in a quantum circuit
    qbits = [L.constant('n{}'.format(i), L.Object) for i in range(8)]
    # quantum state
    qstates = [L.constant('q{}'.format(i), L.Object) for i in range(8)]
    # used for representing quantum states that are in the process of transferring between
    # two qbits
    moving = L.constant('moving', L.Object)

    # qstate location
    location = L.function('location', L.Object, L.Object)

    target0 = L.variable('target0', L.Object)
    target1 = L.variable('target1', L.Object)
    src = L.variable('src', L.Object)
    dst = L.variable('dst', L.Object)

    swap_0 = Schema(name='swap_0',
                    variables=[(target0, qstates), (target1, qstates), (src, qbits), (dst, qbits)],
                    constraints=[src != dst, target0 != target1],
                    transitions=[
                        (location(target0), src, moving),
                        (location(target1), dst, moving)
                    ])
    swap_inv = Schema(name='swap_inv',
                      variables=[(target0, qstates), (target1, qstates)],
                      constraints=[target0 != target1],
                      transitions=[
                          (location(target0), moving, moving),
                          (location(target1), moving, moving),
                      ])
    swap_f = Schema(name='swap_f',
                    variables=[(target0, qstates), (target1, qstates), (src, qbits), (dst, qbits)],
                    constraints=[src != dst, target0 != target1],
                    transitions=[
                        (location(target0), moving, dst),
                        (location(target1), moving, src)
                    ])

    epsilon = 0.001
    swap_schema = TemporalAction(name='swap', events=[(swap_0, 0.001), (swap_inv, 2.0), (swap_f, 0.001)])

    swap_simple = Schema(name='swap_0',
                        variables=[(target0, qstates), (target1, qstates), (src, qbits), (dst, qbits)],
                        constraints=[src != dst, target0 != target1],
                        transitions=[
                            (location(target0), src, dst),
                            (location(target1), dst, src)
                        ])
    swap_schema2 = TemporalAction(name='swap', events=[(swap_simple, 2.0)])

    # constant objects
    if False:
        assert len(swap_actions) == 1568





