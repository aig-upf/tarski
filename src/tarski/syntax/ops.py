import itertools

from .walker import FOLWalker
from .. import modules
from .sorts import children, compute_direct_sort_map, Interval
from .visitors import CollectFreeVariables
from .terms import Term, Constant, Variable
from .formulas import CompoundFormula, Connective
from .symrefs import symref


def cast_to_closest_common_numeric_ancestor(lang, lhs, rhs):
    """ Cast both given operands to the sort that is their closest common ancestor, e.g. when
    applied to a 3 and Constant(2, Int), it should return Constant(3, Int), Constant(2, Int).
    Non-arithmetic objects should be left unchanged.
    """
    if isinstance(lhs, Term) and isinstance(rhs, Term):
        return lhs, rhs

    np = modules.import_numpy()
    if isinstance(lhs, Term):
        if isinstance(rhs, np.ndarray):  # lhs is scalar, rhs is matrix
            return lhs.language.matrix([[lhs]], lhs.sort), rhs

        return lhs, Constant(lhs.sort.cast(rhs), lhs.sort)

    if isinstance(lhs, np.ndarray):  # lhs is matrix
        if isinstance(rhs, Term):
            return lhs, rhs.language.matrix([[rhs]])

    if isinstance(rhs, Term):
        return Constant(rhs.sort.cast(lhs), rhs.sort), rhs

    # Otherwise, we can only cast to generic int or real types
    if isinstance(lhs, int) and isinstance(rhs, int):
        return lang.constant(lhs, lang.Integer), lang.constant(rhs, lang.Integer)
    return lang.constant(lhs, lang.Real), lang.constant(rhs, lang.Real)


def infer_numeric_sort(value, language):
    if isinstance(value, int):
        return language.Integer
    elif isinstance(value, float):
        return language.Real
    return None


def cast_to_number(rhs):
    assert isinstance(rhs, Constant)
    return rhs.symbol


def free_variables(formula):
    """ Return a list with all variables in the given formula that appear free."""
    visitor = CollectFreeVariables()
    visitor.visit(formula)
    return [x.expr for x in visitor.free_variables]  # Unpack the symrefs


def all_variables(formula):
    """ Return a list with all variables that appear in the given formula."""
    return collect_unique_nodes(formula, lambda x: isinstance(x, Variable))


def flatten(formula):
    """ Flatten the given formula recursively, if possible, by applying associativity of and/or connectives
    Thus, a formula like (a or (b or (c or d))) becomes (a or b or c or d)
    """
    if not isinstance(formula, CompoundFormula) or formula.connective not in (Connective.And, Connective.Or):
        return formula
    return CompoundFormula(formula.connective, _flatten(formula, formula.connective))


def _flatten(formula, parent_connective):
    """ Return a list with all AST nodes of the given formula recursively flattened, i.e. where compound formulas
    with the given connective have been flattened themselves.
    """
    if not isinstance(formula, CompoundFormula) or formula.connective != parent_connective:
        return (formula,)  # (returns a tuple)
    return tuple(itertools.chain.from_iterable(_flatten(sub, parent_connective) for sub in formula.subformulas))


def collect_unique_nodes(expression, filter_=None):
    """ Return all nodes in the AST of the given expression, formula or term.
    If a Boolean function `filter_` is provided, only those nodes that satisfy the function are returned.
    The method returns only one copy of each node, under syntactic equivalence. """
    walker = NodeCollectionWalker(filter_)
    walker.run(expression)
    return list(x.expr for x in walker.nodes)  # Unpack the symrefs


class NodeCollectionWalker(FOLWalker):
    """ A walker that simply collects all visited nodes into a set (i.e. w/o repetitions). """
    def __init__(self, filter_=None):
        super().__init__()
        self.nodes = set()
        self.filter_ = filter_ if filter_ is not None else lambda x: True  # by default we collect all nodes

    def visit(self, node):
        if self.filter_ is not None and self.filter_(node):
            self.nodes.add(symref(node))
        return node


def compute_sort_id_assignment(lang, start=0):
    """ An experimental method to compute ID layouts for all the constants of a language, so that all
    sorts get assigned a closed interval.

    The method performs a DFS traversal of the sort hierarchy and assigns consecutive IDs to each object,
    from bottom up. It returns a tuple (bounds, ids).
    `ids` returns a map between objects and numerical ids, starting at 0.
    `bounds` maps each sort to an interval [x, y) of the IDs assigned to the objects of that sort
    (including objects of child sorts), so that any such object o has an id x <= ids[o] < y.
    """
    bounds, ids = {}, {}
    _compute_id_assignment(lang, lang.Object, ids, bounds, compute_direct_sort_map(lang), start=start)
    return bounds, ids


def _compute_id_assignment(lang, sort, ids, bounds, direct_objects, start):
    lb = start
    for c in sorted(children(sort), key=lambda x: x.name):
        if isinstance(c, Interval):
            continue  # Don't assign IDs to interval, which already have their natural integer interpretation
        cub = lb + len(list(c.domain()))
        _compute_id_assignment(lang, c, ids, bounds, direct_objects, start=lb)
        lb = cub

    # Now assign ids to the objects that are directly assigned to sort `current`
    for o in sorted(direct_objects[sort], key=lambda x: x.name):
        ids[symref(o)] = lb
        lb += 1

    # Finally set the whole bounds for this sort
    bounds[sort] = (start, lb)
