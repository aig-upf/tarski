from typing import Set, Union

from .walker import ProblemWalker
from ..syntax import Predicate, Function, CompoundTerm, Atom
from .problem import Problem
from . import fstrips as fs

# At the moment we're using the "multipledispatch" package to implement single-argument dispatching.
# Whenever we move to support Python 3.8+, we could directly use
#     https://docs.python.org/3/library/functools.html#functools.singledispatchmethod
from multipledispatch import dispatch


def collect_all_symbols(problem: Problem) -> Set[Union[Predicate, Function]]:
    """ Return a set with all predicate and function symbols that are actually used in the given problem's goal
    and actions descriptions.

    Note that these might not coincide with those declared in the language if some manipulations or simplifications
    have been performed on the problem, hence the utility of this method. If no such manipulations have been
    done, better use `get_symbols()`.
    """
    walker = AllSymbolWalker()
    walker.run(problem)
    return walker.symbols


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

    @dispatch(object)
    def visit(self, node):
        return self.default_handler(node)

    @dispatch(CompoundTerm)
    def visit(self, node):
        self.symbols.add(node.symbol)
        return node

    @dispatch(Atom)
    def visit(self, node):
        self.symbols.add(node.symbol)
        return node


class AffectedSymbolWalker(ProblemWalker):
    """  """
    def __init__(self):
        super().__init__()
        self.symbols = set()

    @dispatch(object)
    def visit(self, node):
        return self.default_handler(node)

    @dispatch(fs.AddEffect)
    def visit(self, effect):
        self.symbols.add(effect.atom.symbol)
        return effect

    @dispatch(fs.DelEffect)
    def visit(self, effect):
        self.symbols.add(effect.atom.symbol)
        return effect

    @dispatch(fs.FunctionalEffect)
    def visit(self, effect):
        self.symbols.add(effect.lhs.symbol)
        return effect

    @dispatch(fs.ChoiceEffect)
    def visit(self, effect):
        self.symbols.add(effect.obj.symbol)
        return effect

    @dispatch(fs.LinearEffect)
    def visit(self, effect):
        self.symbols.update(lhs.symbol for lhs in effect.y[:, 0])
        return effect
