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
        return self.symbol.type

    @property
    def language(self) :
        return self._lang

    def __str__(self) :
        return '{}({})'.format(self.symbol.symbol, ','.join([ str(t) for t in self.arguments ]))

    def dump(self) :
        return dict(symbol=self.f.dump(),\
                    arguments = [ t.dump() for t in self.arguments ])

    def __add__(self, rhs ) :
        self.language.resolve_function_symbol_2( '+', self.type, rhs.type )

    def __sub__(self, rhs ) :
        self.language.resolve_function_symbol_2( '-', self.type, rhs.type )

    def __mul__(self, rhs ) :
        self.language.resolve_function_symbol_2( '*', self.type, rhs.type )

    def __matmul__(self, rhs ) :
        self.language.resolve_function_symbol_2( '@', self.type, rhs.type )

    def __truediv__(self, rhs ) :
        self.language.resolve_function_symbol_2( '/', self.type, rhs.type )

    def __floordiv__(self, rhs ) :
        self.language.resolve_function_symbol_2( '//', self.type, rhs.type )

    def __mod__(self, rhs ) :
        self.language.resolve_function_symbol_2( '%', self.type, rhs.type )

    def __divmod__(self, rhs ) :
        self.language.resolve_function_symbol_2( 'divmod', self.type, rhs.type )

    def __pow__(self, rhs ) :
        self.language.resolve_function_symbol_2( '**', self.type, rhs.type )

    def __lshift__(self, rhs ) :
        self.language.resolve_function_symbol_2( '<<', self.type, rhs.type )

    def __rshift__(self, rhs ) :
        self.language.resolve_function_symbol_2( '>>', self.type, rhs.type )

    def __and__(self, rhs ) :
        self.language.resolve_function_symbol_2( '&', self.type, rhs.type )

    def __xor__(self, rhs ) :
        self.language.resolve_function_symbol_2( '^', self.type, rhs.type )

    def __or__(self, rhs ) :
        self.language.resolve_function_symbol_2( '|', self.type, rhs.type )




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

    @property
    def language(self) :
        return self._lang

    def __str__(self) :
        return str(self.symbol)

    def dump(self) :
        return dict( symbol = self.symbol )

    def __add__(self, rhs : Term ) :
        return super(Constant,self).__add__(rhs)

    def __sub__(self, rhs : Term ) :
        return super(Constant,self).__sub__(rhs)

    def __mul__(self, rhs : Term ) :
        return super(Constant,self).__mul__(rhs)

    def __matmul__(self, rhs : Term ) :
        return super(Constant,self).__matmul__(rhs)

    def __truediv__(self, rhs : Term ) :
        return super(Constant,self).__truediv__(rhs)

    def __floordiv__(self, rhs : Term ) :
        return super(Constant,self).__floordiv__(rhs)

    def __mod__(self, rhs : Term ) :
        return super(Constant,self).__mod__(rhs)

    def __divmod__(self, rhs : Term ) :
        return super(Constant,self).__divmod__(rhs)

    def __pow__(self, rhs : Term ) :
        return super(Constant,self).__pow__(rhs)

    def __lshift__(self, rhs : Term ) :
        return super(Constant,self).__lshift__(rhs)

    def __rshift__(self, rhs : Term ) :
        return super(Constant,self).__rshift__(rhs)

    def __and__(self, rhs : Term ) :
        return super(Constant,self).__and__(rhs)

    def __xor__(self, rhs : Term ) :
        return super(Constant,self).__xor__(rhs)

    def __or__(self, rhs : Term ) :
        return super(Constant,self).__or__(rhs)


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

    @property
    def language(self) :
        return self._lang

    def dump(self) :
        return dict( symbol = self.symbol )

    def __str__(self) :
        return '?{}'.format(str(self.symbol))

    def __add__(self, rhs : Term ) :
        return super(Variable,self).__add__(rhs)

    def __sub__(self, rhs : Term ) :
        return super(Variable,self).__sub__(rhs)

    def __mul__(self, rhs : Term ) :
        return super(Variable,self).__mul__(rhs)

    def __matmul__(self, rhs : Term ) :
        return super(Variable,self).__matmul__(rhs)

    def __truediv__(self, rhs : Term ) :
        return super(Variable,self).__truediv__(rhs)

    def __floordiv__(self, rhs : Term ) :
        return super(Variable,self).__floordiv__(rhs)

    def __mod__(self, rhs : Term ) :
        return super(Variable,self).__mod__(rhs)

    def __divmod__(self, rhs : Term ) :
        return super(Variable,self).__divmod__(rhs)

    def __pow__(self, rhs : Term ) :
        return super(Variable,self).__pow__(rhs)

    def __lshift__(self, rhs : Term ) :
        return super(Variable,self).__lshift__(rhs)

    def __rshift__(self, rhs : Term ) :
        return super(Variable,self).__rshift__(rhs)

    def __and__(self, rhs : Term ) :
        return super(Variable,self).__and__(rhs)

    def __xor__(self, rhs : Term ) :
        return super(Variable,self).__xor__(rhs)

    def __or__(self, rhs : Term ) :
        return super(Variable,self).__or__(rhs)



Var = Variable
