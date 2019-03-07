"""
    First-order symbols, which can be either predicate symbols or function symbols.
"""

from .sorts import Sort
from .terms import CompoundTerm
from ..errors import LanguageError, LanguageMismatch


class Symbol:
    """ A symbol is defined by its name (a string) and its sort """
    def __init__(self, symbol, language, *args):
        """ Construct a new symbol with given name, pertaining to the given language, and with sort given by
        the tuple of Sort objects in *args
        """
        _validate_expression_arguments(language, symbol, args)
        self.symbol = symbol
        self.language = language
        self.sort = tuple(args)
        self.builtin = False  # By default we assume that the symbol is not built-in

    @property
    def signature(self):
        return tuple([self.symbol] + self.sort_names())

    @property
    def arity(self):
        raise NotImplementedError()

    def sort_names(self):
        return [a.name for a in self.sort]

    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.signature == other.signature

    def __hash__(self):
        return hash(self.signature)

    def uniform_arity(self):
        return len(self.sort)

    def __str__(self):
        return "{}/{}".format(self.symbol, self.arity)

    __repr__ = __str__


class PredicateSymbol(Symbol):
    def __init__(self, symbol, language, *args):
        super().__init__(symbol, language, *args)

    @property
    def arity(self):
        return self.uniform_arity()

    def dump(self):
        return dict(symbol=self.symbol, sort=[a.name for a in self.sort])

    def __call__(self, *args):
        from .formulas import Atom  # Place import here to avoid cyclic reference. TODO Place elsewhere
        return Atom(self, args)


class FunctionSymbol(Symbol):
    def __init__(self, symbol, language, *args):
        super().__init__(symbol, language, *args)

    @property
    def domain(self):
        return self.sort[:-1]

    @property
    def codomain(self):
        return self.sort[-1]

    @property
    def arity(self):
        return len(self.sort) - 1  # The arity of a function does not count its codomain

    def dump(self):
        return dict(symbol=self.symbol, domain=[a.name for a in self.domain], codomain=self.codomain.name)

    def __call__(self, *args):
        return CompoundTerm(self, args)


def _validate_expression_arguments(language, name, sort):
    for k, a in enumerate(sort, start=1):
        if not isinstance(a, Sort):
            raise LanguageError('Argument #{} ("{}") of expression "{}" is of type "{}" instead of Sort'.format(
                k + 1, a, name, type(a)))

        if language != a.language:
            raise LanguageMismatch(a, a.language, language)
