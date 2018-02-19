# -*- coding: utf-8 -*-
import copy
from typing import List

from .sorts import Sort
from . import builtins
from .. import errors as err

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
        self.sort.language.language_components_frozen = True
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

        if len(subterms) != self.symbol.arity :
            raise err.ArityMismatch(symbol,subterms)
        argument_sorts = list(self.symbol.sort)[:-1]
        processed_st = []
        for k, s in enumerate(argument_sorts) :
            # @TODO Implement upcasting for non built-in compound terms
            try :
                if subterms[k].sort.name != s.name and not self.symbol.language.is_subtype(s, subterms[k].sort):
                    raise err.TypeMismatch(self.symbol,subterms[k].sort,s)
                processed_st.append(subterms[k])
            except AttributeError :
                s_k = s.cast(subterms[k])
                if s_k is None : raise err.TypeMismatch(self.symbol,subterms[k],s)
                processed_st.append(s_k)
        self.subterms = tuple(processed_st)
        self.symbol.language.language_components_frozen = True

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
        # MRJ: we don't want to print the symbol/signature
        # but rather the name.
        return '{}({})'.format(self.symbol.symbol, ', '.join([str(t) for t in self.subterms]))


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
