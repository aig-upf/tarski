
import itertools
from typing import List

from multipledispatch import dispatch

from ..symrefs import symref
from ..terms import Variable
from ..walker import FOLWalker


class ExpressionSubstitutionWalker(FOLWalker):
    """  A simple walker that performs expression substitutions based on an input dictionary of replacements """
    def __init__(self, substitution):
        super().__init__(raise_on_undefined=False)
        self.substitution = substitution

    @dispatch(object)
    def visit(self, node):  # pylint: disable-msg=E0102
        x = self.substitution.get(symref(node))
        return node if x is None else x


def substitute_expression(expression, substitution, inplace=False):
    """ Apply the given syntactic substitution to the given FOL expression (a term or a formula).
    :param expression: A FOL formula or term.
    :param substitution: A dictionary from TermReferences to other expressions.
    :param inplace: If true, the given element is modified in place; otherwise a different object is returned.
    :return: The result of applying the substitution to the element.
    """
    walker = ExpressionSubstitutionWalker(substitution)
    return walker.run(expression, inplace=inplace)


def create_substitution(symbols, values):
    return {symref(symbols[k]): v for k, v in enumerate(values)}


def enumerate_substitutions(variables: List[Variable]):
    """ Enumerates all possible substitutions for the given variables. """
    assert all(isinstance(var, Variable) for var in variables)
    domains = [var.sort.domain() for var in variables]
    for values in itertools.product(*domains):
        yield create_substitution(variables, values)
