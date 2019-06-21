
from .formulas import Formula
from .terms import Term


def symref(sym):
    """ Create a reference of a logical expression, formula or term """
    if isinstance(sym, Term):
        return TermReference(sym)
    if isinstance(sym, Formula):
        return FormulaReference(sym)
    raise RuntimeError("Unexpected symbol type \"{}\"".format(type(sym)))


class TermReference:
    """ A simple wrapper to provide a purely syntactic __eq__ operator for terms.
     To be used whenever equality and hashing is required, e.g. in dictionaries, etc.,
     since the __eq__ operator in the Term hierarchy is used for other purposes,
     namely, to construct equality atoms in a user-readable manner. """

    def __init__(self, term):
        assert isinstance(term, Term)
        self.expr = term

    def __hash__(self):
        return hash(self.expr)

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.expr.is_syntactically_equal(other.expr)

    def __str__(self):
        return "TermRef[{}]".format(self.expr)

    __repr__ = __str__


class FormulaReference:
    """ A simple wrapper to provide a purely syntactic __eq__ operator for formulas.
     To be used whenever equality and hashing is required, e.g. in dictionaries, etc.,
     since the __eq__ operator in the Term hierarchy is used for other purposes,
     namely, to construct equality atoms in a user-readable manner. """

    def __init__(self, phi):
        assert isinstance(phi, Formula)
        self.expr = phi

    def __hash__(self):
        return hash(self.expr)

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.expr.is_syntactically_equal(other.expr)

    def __str__(self):
        return "FormulaRef[{}]".format(self.expr)

    __repr__ = __str__
