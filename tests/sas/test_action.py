import pytest

import tarski as tsk
import tarski.model
from tarski.evaluators.simple import evaluate
from tarski.sas import Schema
from tarski.sas.temporal import TemporalAction
from tarski.sas.util import ground_temporal_action
from tarski.theories import Theory


@pytest.mark.sas
def test_temporal_action():
    """
    Simple test for durative actions, based on the quantum circuit compilation benchmark
    :return:
    """
    L = tsk.language("qcc", theories=[Theory.BOOLEAN, Theory.EQUALITY, Theory.ARITHMETIC])

    # sorts
    # qbits in a quantum circuit
    qbits = [L.constant(f"n{i}", L.Object) for i in range(4)]
    # quantum state
    qstates = [L.constant(f"q{i}", L.Object) for i in range(4)]
    # used for representing quantum states that are in the process of transferring between
    # two qbits
    moving = L.constant("moving", L.Object)

    # qstate location
    location = L.function("location", L.Object, L.Object)
    # static predicate
    adj = L.predicate("adjacent", L.Object, L.Object)

    target0 = L.variable("target0", L.Object)
    target1 = L.variable("target1", L.Object)
    src = L.variable("src", L.Object)
    dst = L.variable("dst", L.Object)

    swap_0 = Schema(
        name="swap_0",
        variables=[(target0, qstates), (target1, qstates), (src, qbits), (dst, qbits)],
        constraints=[src != dst, target0 != target1, adj(src, dst)],
        transitions=[(location(target0), src, moving), (location(target1), dst, moving)],
    )
    swap_inv = Schema(
        name="swap_inv",
        variables=[(target0, qstates), (target1, qstates)],
        constraints=[target0 != target1],
        transitions=[
            (location(target0), moving, moving),
            (location(target1), moving, moving),
        ],
    )
    swap_f = Schema(
        name="swap_f",
        variables=[(target0, qstates), (target1, qstates), (src, qbits), (dst, qbits)],
        constraints=[src != dst, target0 != target1, adj(src, dst)],
        transitions=[(location(target0), moving, dst), (location(target1), moving, src)],
    )

    s = tarski.model.create(L)
    s.evaluator = evaluate

    # adj constraint
    for k in range(1, len(qbits)):
        s.add(adj, qbits[k - 1], qbits[k])
        s.add(adj, qbits[k], qbits[k - 1])

    epsilon = 0.001
    swap_schema = TemporalAction(name="swap", events=[(0.001, swap_0), (2.0, swap_inv), (0.001, swap_f)])

    swap_grounded = ground_temporal_action(L, s, swap_schema)
    assert len(swap_grounded) == 72

    swap_simple = Schema(
        name="swap_0",
        variables=[(target0, qstates), (target1, qstates), (src, qbits), (dst, qbits)],
        constraints=[src != dst, target0 != target1],
        transitions=[(location(target0), src, dst), (location(target1), dst, src)],
    )
    swap_schema2 = TemporalAction(name="swap", events=[(2.0, swap_simple)])
