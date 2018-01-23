# -*- coding: utf-8 -*-
from ._errors import LanguageError
from ._sorts import Sort
from typing import List, Union
import copy

class Term(object) :

    def __init__(self, sym, arguments ) :
        self._f  = sym
        for a in arguments :
            if not isinstance(a,Term) :
                raise LanguageError("Syntax error: argument {} is not a term".format(a))

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
        return self.symbo.type

    def __str__(self) :
        return '{}({})'.format(self.symbol.symbol, ','.join([ str(t) for t in self.arguments ]))

    def dump(self) :
        return dict(symbol=self.f.dump(),\
                    arguments = [ t.dump() for t in self.arguments ])


class Constant(Term) :

    def __init__(self, name : str , sort : Sort , lang ) :
        super(Constant, self).__init__(self, [])
        self._name = name
        self._sort = sort
        self._sort._domain[name] = self
        self._lang = lang

    @property
    def symbol(self) :
        return self._name

    @property
    def sort(self) :
        return self._sort

    @property
    def type(self) :
        return self._sort

    def __str__(self) :
        return str(self.symbol)

    def dump(self) :
        return dict( symbol = self.symbol )

class Variable(Term) :

    def __init__(self, name : str , sort : Sort , lang ) :
        super(Variable, self).__init__(self, [])
        self._name = name
        self._sort = sort
        self._lang = lang
        # MRJ: not sure if this is completely necessary yet...
        self._lang._variables.add( self )

    @property
    def symbol(self) :
        return self._name

    @property
    def sort(self) :
        return self._sort

    @property
    def type(self) :
        return self._sort

    def dump(self) :
        return dict( symbol = self.symbol )

    def __str__(self) :
        return '?{}'.format(str(self.symbol))

Var = Variable
