"""
 Structural CSP decomposition methods
"""
import itertools
from collections import defaultdict

from ..errors import TarskiError
from ..syntax import CompoundFormula, Atom, Connective, Variable, Constant


class WrongFormalismError(TarskiError):
    pass


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
    return compute_primal_graph_from_hypergraph(compute_schema_constraint_hypergraph(action))


def compute_primal_graph_from_hypergraph(hypergraph):
    """ Compute the primal graph corresponding to the given hypergraph. """
    edges = set()
    for hyperedge in hypergraph:
        edges.update(itertools.combinations(hyperedge, 2))
    return edges


def _remove_ear_if_exists(edges, node_counts):
    """ Find and remove from the given set of edges a so-called "ear" and return True.
    If no such ear exists, return False.

    From Abiteboul, S., Hull, R. and Vianu, V (1995). Foundations of Databases:
        An ear of hypergraph F = (V, F) is an edge f ∈ F such that for some distinct f' ∈ F,
        no vertex of f − f' is in any other edge [...]. In this case, f' is called a witness that f is an ear.
        As a special case, if there is an edge f of F that intersects no other edge, then f is also considered an ear.

    Note that this implementation is possibly not the most efficient, but it should work fine for the kind of small
    hypergraphs we're interested in.
    """
    def remove_edge(edge):
        for node in edge:
            node_counts[node] -= 1
        edges.remove(edge)

    for f in edges:
        # Check first the "special case"
        if all(node_counts[node] == 1 for node in f):
            remove_edge(f)
            # print(f'Edge {f} removed because it intersects no other edge')
            return True

    for f, fprime in itertools.permutations(edges, 2):
        # Note that this includes the case where f \subseteq f'.
        # Abiteboul et al. assume that hypergraph is "reduced" and f has thus been compiled into f' at preprocessing;
        # we simply compile it away here on the fly by assuming it is indeed an ear and can be removed.
        if all(node_counts[node] == 1 for node in f-fprime):
            remove_edge(f)
            # print(f'Edge {f} removed in favor of {fprime}')
            return True
    # print(f'No more ears found in {edges}')
    return False


def check_hypergraph_acyclicity(hypergraph):
    """ Check whether the given hypergraph is acyclic by applying the GYO reduction as described in
        Abiteboul, S., Hull, R. and Vianu, V (1995). Foundations of Databases, pp.131-132.
    """
    nodes = set(itertools.chain.from_iterable(hypergraph))
    edges = set(frozenset(x) for x in hypergraph)  # simply convert the tuple into frozensets
    if len(edges) <= 1 or len(nodes) <= 1:
        return True

    # Compute a mapping storing in how many hyperedges each node appears
    node_counts = defaultdict(int)
    for edge in edges:
        for n in edge:
            node_counts[n] += 1

    # This is essentially the GYO algorithm:
    while _remove_ear_if_exists(edges, node_counts):
        pass

    return len(edges) == 0


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
            _ = [_collect_hyperedges(sub, edges) for sub in phi.subformulas]
        elif phi.connective == Connective.Not:
            _collect_hyperedges(phi.subformulas[0], edges)
        else:
            raise WrongFormalismError("Can only process conjunctive queries")
    else:
        raise WrongFormalismError("Can only process conjunctive queries")
