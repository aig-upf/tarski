# -*- coding: utf-8 -*-

import numpy as np
import math

from .._function import Function
from .._errors import LanguageError

class ArithmeticFunction(Function) :

    def __init__(self, lang, *args ) :
        super(ArithmeticFunction,self).__init__(lang,*args)

    def add(self, *args ) :
        raise LanguageError("Addition function is a built-in and cannot be redefined")

class Addition(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Addition,self).__init__('+', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] + args[1]

class Subtraction(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Subtraction,self).__init__('-', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] - args[1]

class Multiplication(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Multiplication,self).__init__('*', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] * args[1]

class Division(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Division,self).__init__('/', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] / args[1]

class Power(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Power,self).__init__('**', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] ** args[1]

class Max(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Max,self).__init__('max', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return max(args[0], args[1])

class Min(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Min,self).__init__('min', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return min(args[0], args[1])

class Modulo(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(Modulo,self).__init__('%', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] % args[1]

class ArcTangent2(ArithmeticFunction) :

    def __init__(self, lang, lhs_sort, rhs_sort ) :
        super(ArcTangent2,self).__init__('atan2', lang, lhs_sort, rhs_sort)

    def __getitem__(self, *args) :
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return math.atan2(args[0], args[1])

# Unary arithmetic functions from the Standard Library

class StandardLibFunction(ArithmeticFunction) :

    def __init__(self, sym, lang, sort ) :
        super(StandardLibFunction,self).__init__(sym, lang, sort)

    def __getitem__(self, *args ) :
        assert self.domain[0].contains(args[0])
        return getattr(math,sym)(args[0])
