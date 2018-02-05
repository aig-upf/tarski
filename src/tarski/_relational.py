# -*- coding: utf-8 -*-
from ._formulas import RelationalFormula

from enum import Enum


class ArithmeticFormulaSymbol(Enum):
    EQ = "="
    NEQ = "!="
    LT = "<"
    LEQ = "<="
    GT = ">"
    GEQ = ">="


class ArithmeticFormula(RelationalFormula):
    def __init__(self, symbol: ArithmeticFormulaSymbol, lhs, rhs):
        super(ArithmeticFormula, self).__init__(symbol, lhs, rhs)

    @property
    def lhs(self):
        return self.subterms[0]

    @property
    def rhs(self):
        return self.subterms[1]

    def __str__(self):
        try:
            # if symbol is Enum
            return '{} {} {}'.format(str(self.lhs), self.symbol.value, str(self.rhs))
        except AttributeError:
            return '{} {} {}'.format(str(self.lhs), str(self.symbol), str(self.rhs))


class EQFormula(ArithmeticFormula):
    def __init__(self, lhs, rhs):
        super(EQFormula, self).__init__(ArithmeticFormulaSymbol.EQ, lhs, rhs)

    def satisfiable(self, s):
        return s[self.lhs].symbol == s[self.rhs].symbol


class NEQFormula(ArithmeticFormula):
    def __init__(self, lhs, rhs):
        super(NEQFormula, self).__init__(ArithmeticFormulaSymbol.NEQ, lhs, rhs)

    def satisfiable(self, s):
        return s[self.lhs].symbol != s[self.rhs].symbol


class LTFormula(ArithmeticFormula):
    def __init__(self, lhs, rhs):
        super(LTFormula, self).__init__(ArithmeticFormulaSymbol.LT, lhs, rhs)

    def satisfiable(self, s):
        return s[self.lhs].symbol < s[self.rhs].symbol


class GTFormula(ArithmeticFormula):
    def __init__(self, lhs, rhs):
        super(GTFormula, self).__init__(ArithmeticFormulaSymbol.GT, lhs, rhs)

    def satisfiable(self, s):
        return s[self.lhs].symbol > s[self.rhs].symbol


class LEQFormula(ArithmeticFormula):
    def __init__(self, lhs, rhs):
        super(LEQFormula, self).__init__(ArithmeticFormulaSymbol.LEQ, lhs, rhs)

    def satisfiable(self, s):
        return s[self.lhs].symbol <= s[self.rhs].symbol


class GEQFormula(ArithmeticFormula):
    def __init__(self, lhs, rhs):
        super(GEQFormula, self).__init__(ArithmeticFormulaSymbol.GEQ, lhs, rhs)

    def satisfiable(self, s):
        return s[self.lhs].symbol >= s[self.rhs].symbol
