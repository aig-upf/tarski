# -*- coding: utf-8 -*-

import math

from ..syntax import Function
from ..errors import LanguageError


class ArithmeticFunction(Function):
    def __init__(self, sym, lang, *args):
        super().__init__(sym, lang, *args)

    def add(self, *args):
        raise LanguageError("Addition function is a built-in and cannot be redefined")


class Addition(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('+', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K(_lhs + _rhs,self.codomain)


class Subtraction(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('-', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K(_lhs - _rhs,self.codomain)


class Multiplication(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('*', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K(_lhs * _rhs,self.codomain)


class Division(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('/', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K(_lhs / _rhs,self.codomain)


class Power(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('**', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K(_lhs ** _rhs,self.codomain)


class Max(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('max', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K( max(_lhs, _rhs),self.codomain)

class Min(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('min', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K( min(_lhs, _rhs),self.codomain)


class Modulo(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('%', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K(_lhs % _rhs,self.codomain)


class ArcTangent2(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('atan2', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        _lhs = args[0].symbol
        _rhs = args[1].symbol
        assert self.domain[0].contains(_lhs)
        assert self.domain[1].contains(_rhs)
        K = self.language.Constant
        return K( math.atan2(_lhs, _rhs),self.codomain)


# Unary arithmetic functions from the Standard Library

class StandardLibFunction(ArithmeticFunction):
    def __init__(self, sym, lang, sort):
        super().__init__(sym, lang, sort, sort)

    def __getitem__(self, args):
        _x = args.symbol
        assert self.domain[0].contains(_x)
        return K(getattr(math, self.symbol)(_x), self.codomain )
