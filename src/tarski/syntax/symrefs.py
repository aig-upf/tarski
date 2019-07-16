
from .formulas import Formula
from .terms import Term


def symref(sym):
    """ Create a reference of a logical expression, formula or term """
    if isinstance(sym, Term):
        return TermReference(sym)
    if isinstance(sym, Formula):
        # Formulas are hashable and indexable by themselves, but we wrap them in a Ref object for uniformity reasons
        return TermReference(sym)
    raise RuntimeError("Unexpected symbol type \"{}\"".format(type(sym)))


class TermReference:
    """ A simple wrapper to provide a purely syntactic __eq__ operator for terms.
     To be used whenever equality and hashing is required, e.g. in dictionaries, etc.,
     since the __eq__ operator in the Term hierarchy is used for other purposes,
     namely, to construct equality atoms in a user-readable manner. """

    def __init__(self, expression):
        self.expr = expression

    def __hash__(self):
        return self.expr.hash()

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.expr.is_syntactically_equal(other.expr)

    def __str__(self):
        return "symref[{}]".format(self.expr)

    __repr__ = __str__
