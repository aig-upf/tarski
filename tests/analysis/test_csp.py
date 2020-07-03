"""
 Tests for the CSP analysis module
"""
from tarski.analysis.csp import compute_schema_constraint_hypergraph, check_hypergraph_acyclicity
from tests.io.common import collect_strips_benchmarks, reader


def test_hypergraph_generation():
    def compute_acyclicity(instance):
        instance_file, domain_file = collect_strips_benchmarks([instance])[0]
        problem = reader(case_insensitive=True).read_problem(domain_file, instance_file)
        hgraphs = {a.name: compute_schema_constraint_hypergraph(a) for a in problem.actions.values()}
        return {name: check_hypergraph_acyclicity(h) for name, h in hgraphs.items()}

    acyclicity = compute_acyclicity("pipesworld-notankage:p01-net1-b6-g2.pddl")
    assert acyclicity == {'PUSH-START': False, 'PUSH-END': True, 'POP-START': False,
                          'POP-END': True, 'PUSH-UNITARYPIPE': False, 'POP-UNITARYPIPE': False}

    acyclicity = compute_acyclicity("ged-opt14-strips:d-1-2.pddl")
    assert all(x is True for x in acyclicity.values())


def check_acyclicity(domain_file, instance_file):
    problem = reader(case_insensitive=True, strict_with_requirements=False).read_problem(domain_file, instance_file)
    for a in problem.actions.values():
        acyclic = check_hypergraph_acyclicity(compute_schema_constraint_hypergraph(a))
        print(f'Action {a.name} is {"acyclic" if acyclic else "cyclic"}.')
