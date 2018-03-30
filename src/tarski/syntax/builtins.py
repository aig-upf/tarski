from enum import Enum


class BuiltinPredicateSymbol(Enum):
    EQ = "="
    NE = "!="
    LT = "<"
    LE = "<="
    GT = ">"
    GE = ">="

    def __str__(self):
        return self.value.lower()


class BuiltinFunctionSymbol(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    # ...

    def __str__(self):
        return self.value.lower()


def is_builtin_predicate(predicate):
    return isinstance(predicate.symbol, BuiltinPredicateSymbol)


def is_builtin_function(fun):
    return isinstance(fun.symbol, BuiltinFunctionSymbol)


def get_equality_predicates():
    return [BuiltinPredicateSymbol.EQ, BuiltinPredicateSymbol.NE]


def get_arithmetic_predicates():
    return [BuiltinPredicateSymbol.LT, BuiltinPredicateSymbol.LE, BuiltinPredicateSymbol.GT, BuiltinPredicateSymbol.GE]


def get_arithmetic_functions():
    return [BuiltinFunctionSymbol.ADD, BuiltinFunctionSymbol.SUB, BuiltinFunctionSymbol.MUL, BuiltinFunctionSymbol.DIV]


def get_predicate_from_symbol(symbol: str):
    return BuiltinPredicateSymbol(symbol)


def get_function_from_symbol(symbol: str):
    return BuiltinFunctionSymbol(symbol)

# def eq(lhs, rhs):
#     return create_atom(BuiltinPredicate.EQ, lhs, rhs)
#
#
# def ne(lhs, rhs):
#     return create_atom(BuiltinPredicate.NE, lhs, rhs)
#
#
# def lt(lhs, rhs):
#     return create_atom(BuiltinPredicate.LT, lhs, rhs)
#
#
# def gt(lhs, rhs):
#     return create_atom(BuiltinPredicate.GT, lhs, rhs)
#
#
# def le(lhs, rhs):
#     return create_atom(BuiltinPredicate.LE, lhs, rhs)
#
#
# def ge(lhs, rhs):
#     return create_atom(BuiltinPredicate.GE, lhs, rhs)
