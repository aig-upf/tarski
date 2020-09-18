""" A Walker (Visitor) for FSTRIPS entities.

Note that there is some code duplication with the FOLWalker at syntax/walker.py,
but that one is only in charge of FOL elements and should remain agnostic wrt planning, FSTRIPS, actions, effects, etc.
"""

import copy
from enum import Enum

from ..errors import TarskiError


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
        # pylint: disable-msg=E0307  # pylint gives false positive here, since self.value is already a string
        return self.value


class WalkerContext(Enum):
    """ """
    Effect = "effect"
    Formula = "formula"

    def __str__(self):
        # pylint: disable-msg=E0307  # pylint gives false positive here, since self.value is already a string
        return self.value


class ProblemWalker:
    """ This is an experimental implementation of a visitor pattern based on single-dispatch.
    At the moment we're using the "multipledispatch" package to implement single-argument dispatching.
    It's far from perfect; it requires that the subclass declares the following "default" method:

    >>> @dispatch(object)
    >>> def visit(self, node):  # pylint: disable-msg=E0102
    >>>    return self.default_handler(node)

    Whenever we move to support Python 3.8+, we could directly use:
        https://docs.python.org/3/library/functools.html#functools.singledispatchmethod
    """
    def __init__(self, raise_on_undefined=False):
        self.default_handler = self._raise if raise_on_undefined else self._donothing
        self.context = None

    def visit(self, node):
        raise NotImplementedError()

    def _raise(self, node):
        raise NoHandlerError(node)

    def _donothing(self, node):
        return node

    def run(self, expression, inplace=True):
        from . import Action, BaseEffect, Problem  # pylint: disable=import-outside-toplevel  # Avoiding circular references
        from ..syntax import Formula, Term  # pylint: disable=import-outside-toplevel  # Avoiding circular references
        # Simply dispatch according to type
        expression = expression if inplace else copy.deepcopy(expression)
        if isinstance(expression, (Formula, Term)):
            return self.visit_expression(expression, inplace=True)
        elif isinstance(expression, BaseEffect):
            return self.visit_effect(expression, inplace=True)
        elif isinstance(expression, Action):
            return self.visit_effect(expression, inplace=True)
        elif isinstance(expression, Problem):
            return self.visit_problem(expression, inplace=True)
        raise RuntimeError(f"Unknown expression type '{expression}'")

    def visit_problem(self, problem, inplace=False):
        problem = problem if inplace else copy.deepcopy(problem)
        problem.goal = self.visit_expression(problem.goal, inplace=True)

        for aname, a in list(problem.actions.items()):
            res = self.visit_action(a, inplace=True)
            if res is WalkerAction.Supress:
                del problem.actions[aname]

        return problem

    def visit_action(self, node, inplace=False):
        node = node if inplace else copy.deepcopy(node)
        node.precondition = self.visit_expression(node.precondition, inplace=True)

        node.effects = self.accept(self.visit_effect(eff, inplace=True) for eff in node.effects)

        return node

    def visit_effect(self, effect, inplace=True):
        from . import AddEffect, DelEffect, UniversalEffect, FunctionalEffect  # pylint: disable=import-outside-toplevel
        effect = effect if inplace else copy.deepcopy(effect)

        if isinstance(effect, (AddEffect, DelEffect)):
            effect.condition = self.visit_expression(effect.condition)
            effect.atom = self.visit_effect_atom(effect.atom)

        elif isinstance(effect, FunctionalEffect):
            effect.condition = self.visit_expression(effect.condition)
            effect.lhs = self.visit_effect_atom(effect.lhs)
            effect.rhs = self.visit_effect_atom(effect.rhs)

        elif isinstance(effect, UniversalEffect):
            effect.effects = self.accept(self.visit_effect(eff, inplace=True) for eff in effect.effects)

        else:
            raise RuntimeError(f'Effect "{effect}" of type "{type(effect)}" cannot be analysed')

        return self.visit(effect)

    def visit_expression(self, node, inplace=True):
        from ..syntax import CompoundFormula, QuantifiedFormula, Atom, Tautology, Contradiction, Constant, Variable,\
            CompoundTerm, IfThenElse  # pylint: disable=import-outside-toplevel  # Avoiding circular references
        node = node if inplace else copy.deepcopy(node)

        if isinstance(node, (Variable, Constant, Contradiction, Tautology)):
            pass

        elif isinstance(node, (CompoundTerm, Atom)):
            node.subterms = self.accept(self.visit_expression(sub, inplace=True) for sub in node.subterms)

        elif isinstance(node, CompoundFormula):
            node.subformulas = self.accept(self.visit_expression(sub, inplace=True) for sub in node.subformulas)

        elif isinstance(node, IfThenElse):
            node.condition = self.visit_expression(node.condition, inplace=True)
            node.subterms = self.accept(self.visit_expression(sub, inplace=True) for sub in node.subterms)

        elif isinstance(node, QuantifiedFormula):
            node.formula = self.visit_expression(node.formula)
            node.variables = self.accept(self.visit_expression(eff, inplace=True) for eff in node.variables)
        else:
            raise RuntimeError(f'Unexpected expression "{node}" of type "{type(node)}"')

        return self.visit(node)

    def visit_effect_atom(self, node):
        self.context = WalkerContext.Effect
        x = self.visit_expression(node)
        self.context = WalkerContext.Formula
        return x

    def accept(self, iterator):
        return [x for x in iterator if x is not WalkerAction.Supress]
