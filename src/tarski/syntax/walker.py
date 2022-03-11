""" A Walker (Visitor) for syntax expressions. """

import copy
from enum import Enum

from ..errors import TarskiError


class WalkerError(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'Unspecified error while executing SyntaxWalker'
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


class FOLWalker:
    """
    This is an experimental implementation of a visitor pattern based on single-dispatch.
    To use it, you need to subclass it and "overload" the `visit` function using the
    `functools.singledispatchmethod` decorator, as it is done, for instance, in the class AllSymbolWalker.
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
        # Simply dispatch according to type
        expression = expression if inplace else copy.deepcopy(expression)
        return self.visit_expression(expression, inplace=True)

    def visit_expression(self, node, inplace=True):
        # pylint: disable=import-outside-toplevel  # Avoiding circular references
        from .formulas import (Atom, CompoundFormula, Contradiction,
                               QuantifiedFormula, Tautology)
        from .terms import (  # pylint: disable=import-outside-toplevel
            CompoundTerm, Constant, IfThenElse, Variable)
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
            node.formula = self.visit_expression(node.formula, inplace=True)
            node.variables = self.accept(self.visit_expression(eff, inplace=True) for eff in node.variables)
        else:
            raise RuntimeError(f'Unexpected expression "{node}" of type "{type(node)}"')

        return self.visit(node)

    def accept(self, iterator):
        return [x for x in iterator if x is not WalkerAction.Supress]
