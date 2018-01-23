# -*- coding: utf-8 -*-
from ._errors import LanguageError
from ._sorts import Sort
from ._function import Function
from typing import List, Union
import copy

class Term(object) :

    def __init__(self, sym : Union[Function, Constant] , arguments : List[Term]  ) :
        self._f = func
        self._args = copy.deepcopy(arguments)

    @property
    def symbol(self) :
        return self._f

    @property
    def arguments(self) :
        return self._args

    @property
    def is_constant(self) :
        return isinstance(self, Constant)

    @property
    def type(self) :
        return

    def __str__(self) :
        return '{}()'.format(self.symbol, ','.join([ t.symbol for t in self.arguments ]))

    def dump(self) :
        return dict(symbol=self.symbol.dump(),\
                    arguments = [ t.dump() for t in self.arguments ])


class Constant(Term) :

    def __init__(self, name : str , sort : Sort , lang ) :

        self._name = name
        self._sort = sort
        self._sort._domain[name] = self
        self._lang = lang

    @property
    def name(self) :
        return self._name

    @property
    def sort(self) :
        return self._sort

    @property
    def type(self) :
        return self._sort
