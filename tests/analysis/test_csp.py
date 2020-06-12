"""
 Tests for the CSP analysis module
"""
from tarski.analysis.csp import compute_schema_constraint_hypergraph, check_hypergraph_acyclicity
from tests.io.common import collect_strips_benchmarks, reader


def test_hypergraph_generation():
    instance_file, domain_file = collect_strips_benchmarks(["pipesworld-notankage:p01-net1-b6-g2.pddl"])[0]
    problem = reader().read_problem(domain_file, instance_file)
    hgraphs = {a.name: compute_schema_constraint_hypergraph(a) for a in problem.actions.values()}
    acyclicity = {name: check_hypergraph_acyclicity(h) for name, h in hgraphs.items()}

    assert acyclicity == {'PUSH-START': False, 'PUSH-END': True, 'POP-START': False,
                          'POP-END': True, 'PUSH-UNITARYPIPE': False, 'POP-UNITARYPIPE': False}

