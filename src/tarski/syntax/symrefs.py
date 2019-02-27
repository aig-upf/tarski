
from .formulas import Formula
from .terms import Term


def symref(sym):
    """ Create a reference of a logical expression, formula or term """
    if isinstance(sym, Term):
        return TermReference(sym)
    if isinstance(sym, Formula):
        return FormulaReference(sym)
    assert False


class TermReference:
    """ A simple wrapper to provide a purely syntactic __eq__ operator for terms.
     To be used whenever equality and hashing is required, e.g. in dictionaries, etc.,
     since the __eq__ operator in the Term hierarchy is used for other purposes,
     namely, to construct equality atoms in a user-readable manner. """

    def __init__(self, term):
        assert isinstance(term, Term)
        self.term = term

    @property
    def expr(self):
        """
            Property shared with FormulaReference, enabling static polymorphism
        """
        return self.term

    def __hash__(self):
        return hash(self.term)

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.term.is_syntactically_equal(other.term)

    def __str__(self):
        return "TermRef[{}]".format(self.term)

    __repr__ = __str__


class FormulaReference:
    """ A simple wrapper to provide a purely syntactic __eq__ operator for formulas.
     To be used whenever equality and hashing is required, e.g. in dictionaries, etc.,
     since the __eq__ operator in the Term hierarchy is used for other purposes,
     namely, to construct equality atoms in a user-readable manner. """

    def __init__(self, phi):
        assert isinstance(phi, Formula)
        self.phi = phi

    def __hash__(self):
        return hash(self.phi)

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.phi.is_syntactically_equal(other.phi)

    def __str__(self):
        return "FormulaRef[{}]".format(self.phi)

    @property
    def expr(self):
        """
            Property shared with TermReference, enabling static polymorphism
        """
        return self.phi

    __repr__ = __str__
