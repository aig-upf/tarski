from types import MethodType
from . import builtins as syntax_builtins

class ArithmeticOperatorImplementation :

    def __init__(self, sym):
        self._symbol = sym

    def __call__( self, lhs, rhs ) :
        if isinstance(rhs, lhs.language.Term) :
            sym = lhs.language.resolve_function_symbol(self._symbol, lhs.sort, rhs.sort)
        else :
            rhs = lhs.sort.cast(rhs)
            sym = lhs.language.resolve_function_symbol(self._symbol, lhs.sort, lhs.sort)
        return sym(lhs, rhs)

    def __get__(self, instance, owner):
        return MethodType(self, instance) if instance else self


class RelationalOperatorImplementation :
    def __init__(self, sym):
        self._symbol = sym

    def __call__( self, lhs, rhs ) :
        if  isinstance(rhs, lhs.language.Term) :
            return getattr(syntax_builtins,self._symbol)(lhs,rhs)
        else :
            return getattr(syntax_builtins,self._symbol)(lhs,lhs.sort.cast(rhs))

    def __get__(self, instance, owner):
        return MethodType(self, instance) if instance else self
