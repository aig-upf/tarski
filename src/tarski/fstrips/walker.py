
import copy
from enum import Enum
from functools import singledispatch, update_wrapper

from ..syntax.formulas import CompoundFormula, QuantifiedFormula, Atom, Tautology, Contradiction
from ..syntax.terms import Constant, Variable, CompoundTerm
from ..errors import TarskiError
from . import AddEffect, DelEffect, UniversalEffect, FunctionalEffect


def dispatch(func):
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


class WalkerError(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'Unspecified error while executing ProblemWalker'
        super().__init__(msg)


class NoHandlerError(WalkerError):
    def __init__(self, node):
        super().__init__(f'ProblemWalker: No handler was specified for node "{node}" of type "{type(node)}"')


class WalkerAction(Enum):
    """ """
    Supress = "supress"

    def __str__(self):
        return self.value


class WalkerContext(Enum):
    """ """
    Effect = "effect"
    Formula = "formula"

    def __str__(self):
        return self.value


class ProblemWalker:
    """
    """
    def __init__(self, problem, raise_on_undefined=False):
        self.problem = problem
        self.default_handler = self._raise if raise_on_undefined else self._donothing
        self.context = None

    def _raise(self, node):
        raise NoHandlerError(node)

    def _donothing(self, node):
        return node

    @dispatch
    def visit(self, node):
        return self.default_handler(node)

    def run(self, inplace=False):
        problem = self.problem if inplace else copy.deepcopy(self.problem)
        problem.goal = self.visit_expression(problem.goal, inplace=True)

        for aname, a in list(problem.actions.items()):
            res = self.visit_action(a, inplace=True)
            if res is WalkerAction.Supress:
                del problem.actions[aname]

        # TODO Deal with problem.init? Makes less sense, as there is no AST there.

        return problem

    def visit_action(self, node, inplace=False):
        node = node if inplace else copy.deepcopy(node)
        node.precondition = self.visit_expression(node.precondition, inplace=True)

        node.effects = self._filter(self.visit_effect(eff, inplace=True) for eff in node.effects)

        return node

    def visit_effect(self, effect, inplace=True):
        effect = effect if inplace else copy.deepcopy(effect)

        if isinstance(effect, (AddEffect, DelEffect)):
            effect.condition = self.visit_expression(effect.condition)
            effect.atom = self.visit_effect_atom(effect.atom)

        elif isinstance(effect, FunctionalEffect):
            effect.condition = self.visit_expression(effect.condition)
            effect.lhs = self.visit_effect_atom(effect.lhs)
            effect.rhs = self.visit_effect_atom(effect.rhs)

        elif isinstance(effect, UniversalEffect):
            effect.effects = self._filter(self.visit_effect(eff, inplace=True) for eff in effect.effects)

        else:
            raise RuntimeError(f'Effect "{effect}" of type "{type(effect)}" cannot be analysed')

        return self.visit(effect)

    def visit_expression(self, node, inplace=True):
        node = node if inplace else copy.deepcopy(node)

        if isinstance(node, (Variable, Constant, Contradiction, Tautology)):
            pass

        elif isinstance(node, (CompoundTerm, Atom)):
            node.subterms = self._filter(self.visit_expression(eff, inplace=True) for eff in node.subterms)

        elif isinstance(node, CompoundFormula):
            node.subformulas = self._filter(self.visit_expression(eff, inplace=True) for eff in node.subformulas)

        elif isinstance(node, QuantifiedFormula):
            node.formula = self.visit_expression(node.formula)
            node.variables = self._filter(self.visit_expression(eff, inplace=True) for eff in node.variables)
        else:
            raise RuntimeError(f'Unexpected expression "{node}" of type "{type(node)}"')

        return self.visit(node)

    def visit_effect_atom(self, node):
        self.context = WalkerContext.Effect
        x = self.visit_expression(node)
        self.context = WalkerContext.Formula
        return x

    @staticmethod
    def _filter(iterator):
        return [x for x in iterator if x is not WalkerAction.Supress]
