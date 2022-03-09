import operator
from functools import singledispatchmethod, reduce
from typing import Set, Union

from .walker import ProblemWalker
from ..syntax import Predicate, Function, CompoundTerm, Atom
from .problem import Problem
from . import fstrips as fs
from .derived import Derived


def collect_all_symbols(problem: Problem, include_builtin=False) -> Set[Union[Predicate, Function]]:
    """ Return a set with all predicate and function symbols that are actually used in the given problem's goal
    and actions descriptions.

    Note that these might not coincide with those declared in the language if some manipulations or simplifications
    have been performed on the problem, hence the utility of this method. If no such manipulations have been
    done, better use `get_symbols()`.
    """
    walker = AllSymbolWalker()
    walker.run(problem)
    if include_builtin:
        return walker.symbols
    return {s for s in walker.symbols if not s.builtin}


def collect_affected_symbols(problem: Problem) -> Set[Union[Predicate, Function]]:
    """ Return a set with all predicate and function symbols that are affected by some action effect, and hence
     can be considered fluent. """
    walker = AffectedSymbolWalker()
    # Let's just go straight into the effects instead of invoking walker.run(), which would go over
    # the whole problem structure for nothing
    _ = [walker.run(eff) for action in problem.actions.values() for eff in action.effects]
    return walker.symbols


class AllSymbolWalker(ProblemWalker):
    """  """
    def __init__(self):
        super().__init__()
        self.symbols = set()

    @singledispatchmethod
    def visit(self, node):
        return self.default_handler(node)

    @visit.register
    def _(self, node: CompoundTerm):
        self.symbols.add(node.symbol)
        return node

    @visit.register
    def _(self, node: Atom):
        self.symbols.add(node.symbol)
        return node


class AffectedSymbolWalker(ProblemWalker):
    """  """
    def __init__(self):
        super().__init__()
        self.symbols = set()

    @singledispatchmethod
    def visit(self, node):
        # raise NotImplementedError(f'Cannot negate node {node} with type "{type(node)}"')
        return self.default_handler(node)

    @visit.register
    def _(self, node: fs.AddEffect):
        self.symbols.add(node.atom.symbol)
        return node

    @visit.register
    def _(self, node: fs.DelEffect):
        self.symbols.add(node.atom.symbol)
        return node

    @visit.register
    def _(self, node: fs.FunctionalEffect):
        self.symbols.add(node.lhs.symbol)
        return node

    @visit.register
    def _(self, node: fs.ChoiceEffect):
        self.symbols.add(node.obj.symbol)
        return node

    @visit.register
    def _(self, node: fs.LinearEffect):
        self.symbols.update(lhs.symbol for lhs in node.y[:, 0])
        return node

    @visit.register
    def _(self, node: Derived):
        self.symbols.update(node.predicate)
        return node


def compute_number_potential_groundings(signature):
    cardinalities = [len(list(s.domain())) for s in signature]
    return reduce(operator.mul, cardinalities, 1)
