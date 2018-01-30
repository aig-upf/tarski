# -*- coding: utf-8 -*-
from ._errors import LanguageError
from ._formulas import AtomicFormula

from enum import Enum
from typing import List

class RelationalFormulaSymbol(Enum) :
    EQ = "="
    NEQ = "!="
    LT = "<"
    LEQ = "<="
    GT = ">"
    GEQ = ">="

class RelationalFormula(AtomicFormula) :

    def __init__( self, symbol, lhs, rhs ) :
        super(RelationalFormula,self).__init__(lhs,rhs)
        self._lhs = lhs
        self._rhs = rhs
        self._symbol = symbol

    @property
    def symbol(self) :
        return self._symbol

    @property
    def lhs(self) :
        return self._lhs

    @property
    def rhs(self) :
        return self._rhs

    def __str__(self) :
        return '{}{}{}'.format(str(self.lhs,self.symbol,self.rhs))

class EQFormula(RelationalFormula) :

    def __init__(self,lhs,rhs) :
        super(EQFormula,self).__init__(RelationalFormulaSymbol.EQ, lhs, rhs)

class NEQFormula(RelationalFormula) :

    def __init__(self,lhs,rhs) :
        super(NEQFormula,self).__init__(RelationalFormulaSymbol.NEQ, lhs, rhs)

class LTFormula(RelationalFormula) :

    def __init__(self,lhs,rhs) :
        super(LTFormula,self).__init__(RelationalFormulaSymbol.LT, lhs, rhs)

class GTFormula(RelationalFormula) :

    def __init__(self,lhs,rhs) :
        super(GTFormula,self).__init__(RelationalFormulaSymbol.GT, lhs, rhs)

class LEQFormula(RelationalFormula) :

    def __init__(self,lhs,rhs) :
        super(LEQFormula,self).__init__(RelationalFormulaSymbol.LEQ, lhs, rhs)

class GEQFormula(RelationalFormula) :

    def __init__(self,lhs,rhs) :
        super(GEQFormula,self).__init__(RelationalFormulaSymbol.GEQ, lhs, rhs)
