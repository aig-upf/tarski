# -*- coding: utf-8 -*-
import copy
from typing import List

from .sorts import Sort
from . import builtins


class Term(object):
    """
        Term class

        NOTE: since we are overloading operators like __eq__, etc. these objects
        may invalidate the assumptions of standard Python containers like set()
        or break methods like find(). Any container for Term and subclasses
        will need to be implemented using the comparison the id() of the instances.
    """

    # def __init__(self, sym, arguments, language):
    #     self._f = sym
    #     self.language = language
    #     self.arguments = copy.copy(arguments)
    #
    #     for a in arguments:
    #         if not isinstance(a, Term):
    #             raise LanguageError("Syntax error: argument {} is not a term".format(a))

    @property
    def language(self):
        raise NotImplementedError()  # Let the subclasses implement this

    @property
    def sort(self):
        raise NotImplementedError()  # Let the subclasses implement this

    # @property
    # def symbol(self):
    #     return self._f

    # @property
    # def type(self):
    #     return self.symbol.type

    # def __str__(self):
    #     return '{}({})'.format(self.symbol.symbol, ','.join([str(t) for t in self.arguments]))

    # def dump(self):
    #     return dict(symbol=self._f.dump(),
    #                 arguments=[t.dump() for t in self.arguments])

    def __add__(self, rhs):
        sym = self.language.resolve_function_symbol('+', self.type, rhs.type)
        return sym(self, rhs)
    #
    # def __sub__(self, rhs):
    #     sym = self.language.resolve_function_symbol('-', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __mul__(self, rhs):
    #     sym = self.language.resolve_function_symbol('*', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __matmul__(self, rhs):
    #     sym = self.language.resolve_function_symbol('@', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __truediv__(self, rhs):
    #     sym = self.language.resolve_function_symbol('/', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __floordiv__(self, rhs):
    #     sym = self.language.resolve_function_symbol('//', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __mod__(self, rhs):
    #     sym = self.language.resolve_function_symbol('%', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __divmod__(self, rhs):
    #     sym = self.language.resolve_function_symbol('divmod', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __pow__(self, rhs):
    #     sym = self.language.resolve_function_symbol('**', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __lshift__(self, rhs):
    #     sym = self.language.resolve_function_symbol('<<', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __rshift__(self, rhs):
    #     sym = self.language.resolve_function_symbol('>>', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __and__(self, rhs):
    #     sym = self.language.resolve_function_symbol('&', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __xor__(self, rhs):
    #     sym = self.language.resolve_function_symbol('^', self.type, rhs.type)
    #     return sym(self, rhs)
    #
    # def __or__(self, rhs):
    #     sym = self.language.resolve_function_symbol('|', self.type, rhs.type)
    #     return sym(self, rhs)

    def __eq__(self, rhs):
        return builtins.eq(self, rhs)

    def __ne__(self, rhs):
        return builtins.ne(self, rhs)

    def __lt__(self, rhs):
        return builtins.lt(self, rhs)

    def __gt__(self, rhs):
        return builtins.gt(self, rhs)

    def __le__(self, rhs):
        return builtins.le(self, rhs)

    def __ge__(self, rhs):
        return builtins.ge(self, rhs)

    # ???
    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_value, traceback):
    #     return exc_type is not None


# TODO DELETE
class Constant_OLD(Term):
    def __init__(self, name: str, sort: Sort, language):
        self._name = name
        super().__init__(self, [], language)
        self._sort = sort
        self._sort.extend(self)

    @property
    def symbol(self):
        return self._name

    @property
    def sort(self):
        return self._sort

    @property
    def type(self):
        return self._sort

    def dump(self):
        return dict(symbol=self.symbol, sort=self.sort.name)

    def __deepcopy__(self, memo):
        newone = type(self)(self._name, self._sort, self.language)
        memo[id(self)] = newone
        for k, v in self.__dict__.items():
            setattr(newone, k, copy.deepcopy(v, memo))
        return newone

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return str(self.symbol)


class Variable(Term):
    def __init__(self, symbol: str, sort: Sort):
        self.symbol = symbol
        self._sort = sort
        # TODO VALIDATE

    @property
    def language(self):
        return self.sort.language

    @property
    def sort(self):
        return self._sort

    # def __deepcopy__(self, memo):
    #     newone = type(self)(self.symbol, self.sort, self.language)
    #     memo[id(self)] = newone
    #     for k, v in self.__dict__.items():
    #         setattr(newone, k, copy.deepcopy(v, memo))
    #     return newone

    def __hash__(self):
        return hash((self.symbol, self.sort))

    # def dump(self):
    #     return dict(symbol=self.symbol)

    def __str__(self):
        return '{}/{}'.format(self.symbol, self.sort.name)


class CompoundTerm(Term):
    def __init__(self, symbol, subterms: List[Term]):
        self.symbol = symbol
        self.subterms = subterms
        # TODO VALIDATE
        # @TODO: check arity and type of arguments!

    @property
    def language(self):
        return self.symbol.language

    @property
    def sort(self):
        # The type of term f(x1, ..., xn) is the codomain of "f"
        return self.symbol.codomain

    # def __deepcopy__(self, memo):
    #     newone = type(self)(self.symbol, self.sort, self.language)
    #     memo[id(self)] = newone
    #     for k, v in self.__dict__.items():
    #         setattr(newone, k, copy.deepcopy(v, memo))
    #     return newone

    # @property
    # def type(self):
    #     return self.sort

    # def __hash__(self):
    #     return hash((self.symbol, self.sort))

    # def dump(self):
    #     return dict(symbol=self.symbol)

    def __str__(self):
        return '{}({})'.format(self.symbol, ', '.join([str(t) for t in self.subterms]))


class Constant(Term):
    def __init__(self, symbol, sort: Sort):
        self.symbol = symbol
        self._sort = sort
        # TODO VALIDATE

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
