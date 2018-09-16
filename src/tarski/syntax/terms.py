# -*- coding: utf-8 -*-
from typing import Tuple

from .sorts import Sort
from .. import errors as err
from .builtins import BuiltinPredicateSymbol, BuiltinFunctionSymbol


class Term:
    """ A logical Term.

        Since we overload the equality operator `__eq__`, containers relying on that method
        such as dictionaries or sets will not work correctly. In order to use them, terms
        need to be wrapped within a `TermReference`.
    """

    @property
    def language(self):
        raise NotImplementedError()  # Let the subclasses implement this

    @property
    def sort(self):
        raise NotImplementedError()  # Let the subclasses implement this

    # required to support scoped declaration of variables
    # with bw.var('x',block) as x, bw.var('y',block) as y do :
    #   ... declarations using x and y
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return exc_type is not None

    def __lshift__(self, rhs):
        return self.language.dispatch_operator('<<', Term, Term, self, rhs)

    def __rshift__(self, rhs):
        return self.language.dispatch_operator('>>', Term, Term, self, rhs)

    def __eq__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.EQ, Term, Term, self, rhs)

    def __ne__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.NE, Term, Term, self, rhs)

    def __lt__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.LT, Term, Term, self, rhs)

    def __gt__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.GT, Term, Term, self, rhs)

    def __le__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.LE, Term, Term, self, rhs)

    def __ge__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.GE, Term, Term, self, rhs)

    def __add__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.ADD, Term, Term, self, rhs)

    def __sub__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.SUB, Term, Term, self, rhs)

    def __mul__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.MUL, Term, Term, self, rhs)

    def __truediv__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.DIV, Term, Term, self, rhs)

    # TODO - THE OPERATORS BELOW PROBABLY NEED TO BE REFACTORED
    def __matmul__(self, rhs):
        return self.language.dispatch_operator('@', Term, Term, self, rhs)

    def __floordiv__(self, rhs):
        return self.language.dispatch_operator('//', Term, Term, self, rhs)

    def __mod__(self, rhs):
        return self.language.dispatch_operator('%', Term, Term, self, rhs)

    def __divmod__(self, rhs):
        return self.language.dispatch_operator('divmod', Term, Term, self, rhs)

    def __pow__(self, rhs):
        return self.language.dispatch_operator('**', Term, Term, self, rhs)

    def __and__(self, rhs):
        return self.language.dispatch_operator('&', Term, Term, self, rhs)

    def __xor__(self, rhs):
        return self.language.dispatch_operator('^', Term, Term, self, rhs)

    def __or__(self, rhs):
        return self.language.dispatch_operator('|', Term, Term, self, rhs)

    def accept(self, visitor):
        """ Visitor pattern """
        visitor.visit(self)

    def is_syntactically_equal(self, other):
        """ Strict syntactic equivalence, which would tipically be in `__eq__`,
        but here we use `__eq__` for a different purpose """
        raise NotImplementedError()  # To be subclassed


class Variable(Term):

    def __init__(self, symbol: str, sort: Sort):
        self.symbol = symbol
        self._sort = sort
        self.sort.language.language_components_frozen = True
        # TODO VALIDATE

    @property
    def language(self):
        return self.sort.language

    @property
    def sort(self):
        return self._sort

    def __str__(self):
        return '{}/{}'.format(self.symbol, self.sort.name)

    __repr__ = __str__

    def __hash__(self):
        return hash((self.symbol, self.sort.name))

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ and self.symbol == other.symbol and self.sort.name == other.sort.name


class CompoundTerm(Term):
    """
        Combinations of a functional symbol and a list of terms.
        Argument symbol needs to be an instance of Function of have
        Function-like interface.
    """

    def __init__(self, symbol, subterms: Tuple[Term]):

        self.symbol = symbol

        if len(subterms) != self.symbol.arity:
            raise err.ArityMismatch(symbol, subterms)
        argument_sorts = list(self.symbol.sort)[:-1]
        processed_st = []
        for k, s in enumerate(argument_sorts):
            # @TODO Implement upcasting for non built-in compound terms
            try:
                if subterms[k].sort.name != s.name and not self.symbol.language.is_subtype(subterms[k].sort, s):
                    raise err.SortMismatch(self.symbol, subterms[k].sort, s)
                processed_st.append(subterms[k])
            except AttributeError:
                s_k = s.cast(subterms[k])
                if s_k is None:
                    raise err.SortMismatch(self.symbol, subterms[k], s)
                processed_st.append(s_k)
        self.subterms = tuple(processed_st)
        self.symbol.language.language_components_frozen = True

    @property
    def language(self):
        return self.symbol.language

    @property
    def sort(self):
        return self.symbol.codomain

    def __str__(self):
        return '{}({})'.format(self.symbol.symbol, ', '.join([str(t) for t in self.subterms]))

    __repr__ = __str__

    def __hash__(self):
        return hash((self.symbol.symbol, tuple(x for x in self.subterms)))

    def is_syntactically_equal(self, other):
        if (self.__class__ is not other.__class__ or self.symbol != other.symbol
                or len(self.subterms) != len(other.subterms)):
            return False

        # Else we just need to recursively check if all subterms are syntactically equal
        return all(x.is_syntactically_equal(y) for x, y in zip(self.subterms, other.subterms))


class Constant(Term):
    def __init__(self, symbol, sort: Sort):
        self.symbol = symbol
        self._sort = sort
        # symbol validation
        if not self._sort.builtin:
            # construction of constants extends the domain of sorts
            self._sort.extend(self)
        else:
            self.symbol = self._sort.cast(self.symbol)
        self.sort.language.language_components_frozen = True

    @property
    def language(self):
        return self.sort.language

    @property
    def sort(self):
        return self._sort

    def __str__(self):
        return '{}'.format(self.symbol)

    def __repr__(self):
        return '{} ({})'.format(self.symbol, self.sort.name)

    def __hash__(self):
        return hash((self.symbol, self.sort))

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ and self.symbol == other.symbol and self.sort == other.sort


def create_term(symbol: BuiltinFunctionSymbol, lhs, rhs):
    assert isinstance(lhs, Term) and isinstance(rhs, Term)
    from . import Atom

    language = lhs.language
    if language != rhs.language:
        raise err.LanguageMismatch(rhs, rhs.language, language)

    # s1, s2 = lhs.type, rhs.type
    # if language.is_subtype(s1, s2):
    #     return Atom("xxx", [lhs, rhs])

    # TODO AT THE MOMENT WE DO NOT CHECK FOR TYPE SAFETY WITH BUILT-IN TYPES

    predicate = language.get_predicate(symbol)
    return Atom(predicate, [lhs, rhs])


class TermReference:
    """ A simple wrapper to provide a purely syntactic __eq__ operator for terms.
     To be used whenever equality and hashing is required, e.g. in dictionaries, etc.,
     since the __eq__ operator in the Term hierarchy is used for other purposes,
     namely, to construct equality atoms in a user-readable manner. """

    def __init__(self, term):
        assert isinstance(term, Term)
        self.term = term

    def __hash__(self):
        return hash(self.term)

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.term.is_syntactically_equal(other.term)

    def __str__(self):
        return "TermRef[{}]".format(self.term)

    __repr__ = __str__
