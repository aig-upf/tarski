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
        will need to be implemented by comparing the return value of id()
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
    """
        Combinations of a functional symbol and a list of terms.
        Argument symbol needs to be an instance of Function of have
        Function-like interface.
    """
    def __init__(self, symbol, subterms: List[Term]):

        self.symbol = symbol
        self.subterms = subterms
        if len(subterms) != self.symbol.arity :
            raise err.ArityMismatch(symbol,subterms)
        argument_sorts = list(self.symbol.sort)[:-1]
        for k, s in enumerate(argument_sorts) :
            # @TODO Implement upcasting for non built-in compound terms
            if subterms[k].sort.name != s.name :
                raise err.TypeMismatch(self.symbol,subterms[k].sort,s)

    @property
    def language(self):
        return self.symbol.language

    @property
    def sort(self):
        return self.symbol.codomain

    # def __deepcopy__(self, memo):
    #     newone = type(self)(self.symbol, self.sort, self.language)
    #     memo[id(self)] = newone
    #     for k, v in self.__dict__.items():
    #         setattr(newone, k, copy.deepcopy(v, memo))
    #     return newone

    def __str__(self):
        return '{}({})'.format(self.symbol, ', '.join([str(t) for t in self.subterms]))


class Constant(Term):
    def __init__(self, symbol, sort: Sort):
        self.symbol = symbol
        self._sort = sort
        # symbol validation
        if not self._sort.builtin :
            # construction of constants extends the domain
            # of sorts
            self._sort.extend(self)
        else :
            self.symbol = self._sort.cast(self.symbol)

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
