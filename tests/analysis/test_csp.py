"""
 Tests for the CSP analysis module
"""
from tarski.analysis.csp import compute_schema_constraint_hypergraph, check_hypergraph_acyclicity
from tests.io.common import parse_benchmark_instance


def test_acyclicity_detection():
    # assert check_hypergraph_acyclicity({('room',), ('obj', 'room'), ('gripper',), ('obj',)}) is True
    # assert check_hypergraph_acyclicity({('gripper', 'obj'), ('gripper',), ('obj',), ('room',)}) is True

    # A hyperedge contained in another hyperedge is correctly marked as acyclic
    assert check_hypergraph_acyclicity({('X', ), ('X', 'Y')}) is True

    # Two repeated hyperedges are dealt with adequately
    assert check_hypergraph_acyclicity({('X', ), ('X', 'Y'), ('Y', 'X')}) is True

    # Two non-intersecting hyperedges are acyclic
    assert check_hypergraph_acyclicity({('S', 'T'), ('X', 'Y')}) is True

    # A simple cyclic hypergraph
    assert check_hypergraph_acyclicity({('X', 'Y'), ('Y', 'Z'), ('Z', 'X')}) is False

    # Now compute acyclicity over a few domain schemas
    # 1. Pipesworld-notankage using the IPC split formulation
    assert compute_acyclicity("pipesworld-notankage:p01-net1-b6-g2.pddl") ==\
           {'PUSH-START': False, 'PUSH-END': True, 'POP-START': False,
            'POP-END': True, 'PUSH-UNITARYPIPE': False, 'POP-UNITARYPIPE': False}

    # 2. Genome edit distance using the IPC version
    assert all(x is True for x in compute_acyclicity("ged-opt14-strips:d-1-2.pddl").values())

    # 3. Gripper
    assert compute_acyclicity("gripper:prob01.pddl") == {'move': True, 'pick': True, 'drop': True}


def compute_acyclicity(instance):
    problem = parse_benchmark_instance(instance, reader_options=dict(case_insensitive=True))
    hgraphs = {a.name: compute_schema_constraint_hypergraph(a) for a in problem.actions.values()}
    return {name: check_hypergraph_acyclicity(h) for name, h in hgraphs.items()}
