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

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] + args[1]


class Subtraction(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('-', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] - args[1]


class Multiplication(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('*', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] * args[1]


class Division(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('/', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] / args[1]


class Power(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('**', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] ** args[1]


class Max(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('max', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return max(args[0], args[1])


class Min(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('min', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return min(args[0], args[1])


class Modulo(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('%', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return args[0] % args[1]


class ArcTangent2(ArithmeticFunction):
    def __init__(self, lang, lhs_sort, rhs_sort):
        super().__init__('atan2', lang, lhs_sort, rhs_sort, lhs_sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        assert self.domain[1].contains(args[1])
        return math.atan2(args[0], args[1])


# Unary arithmetic functions from the Standard Library

class StandardLibFunction(ArithmeticFunction):
    def __init__(self, sym, lang, sort):
        super().__init__(sym, lang, sort, sort)

    def __getitem__(self, *args):
        assert self.domain[0].contains(args[0])
        return getattr(math, self.symbol)(args[0])
