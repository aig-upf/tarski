"""
 Tests for the CSP analysis module
"""
from tarski.analysis.csp import compute_schema_constraint_hypergraph, check_hypergraph_acyclicity
from tests.io.common import collect_strips_benchmarks, reader


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
    assert compute_acyclicity("pipesworld-notankage:p01-net1-b6-g2.pddl") ==\
           {'PUSH-START': False, 'PUSH-END': True, 'POP-START': False,
            'POP-END': True, 'PUSH-UNITARYPIPE': False, 'POP-UNITARYPIPE': False}

    assert all(x is True for x in compute_acyclicity("ged-opt14-strips:d-1-2.pddl").values())

    assert compute_acyclicity("gripper:prob01.pddl") == {'move': True, 'pick': True, 'drop': True}


def compute_acyclicity(instance):
    instance_file, domain_file = collect_strips_benchmarks([instance])[0]
    problem = reader(case_insensitive=True).read_problem(domain_file, instance_file)
    hgraphs = {a.name: compute_schema_constraint_hypergraph(a) for a in problem.actions.values()}
    return {name: check_hypergraph_acyclicity(h) for name, h in hgraphs.items()}
