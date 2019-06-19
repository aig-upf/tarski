"""
 Structural CSP decomposition methods
"""
import itertools

from ..syntax import CompoundFormula, Atom, Connective, Variable, Constant


def compute_schema_constraint_hypergraph(action):
    """ Compute the constraint hypergraph corresponding to the precondition of the given action schema.
    This is the hypergraph with one node v for each action parameter, and one hyperedge {v1, ..., vn} for each atom
    p(v1, ..., vn) in the conjunctive precondition of the action schema """
    hyperedges = set()
    _collect_hyperedges(action.precondition, hyperedges)
    return hyperedges


def compute_schema_primal_graph(action):
    """ Compute the primal graph corresponding to the precondition of the given action schema.
    This is the graph with one node v for each action parameter, and one edge {v1, v2} for every pair of variables
    v1, v2 that appear together in some atom p(..., v1, ..., v2, ...) in the conjunctive precondition of the schema. """
    edges = set()
    for hyperedge in compute_schema_constraint_hypergraph(action):
        edges.update(itertools.combinations(hyperedge, 2))
    return edges


def _collect_hyperedges(phi, edges):
    if isinstance(phi, Atom):
        assert all(isinstance(x, (Variable, Constant)) for x in phi.subterms)
        edge = set()
        for x in phi.subterms:
            if isinstance(x, Variable):
                edge.add(x.symbol[1:])  # Get rid of the "?" in the variable name
        if edge:  # Discard nullary and unary atoms
            edges.add(tuple(sorted(edge)))  # Sort to prevent counting both (x,y) and (y,x) as different hyperedges
    elif isinstance(phi, CompoundFormula):
        if phi.connective == Connective.And:
            [_collect_hyperedges(sub, edges) for sub in phi.subformulas]
        elif phi.connective == Connective.Not:
            _collect_hyperedges(phi.subformulas[0], edges)
        else:
            raise RuntimeError("Can only process conjunctive queries")
    else:
        raise RuntimeError("Can only process conjunctive queries")
