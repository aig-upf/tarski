from enum import Enum

# MRJ: Table with negated counterparts of builtin predicates. Used
# by the method ```complement``` of enum class BuiltinPredicateSymbol.
BuiltinPredicateSymbol_complement = {"=": "!=", "!=": "=", "<": ">=", "<=": ">", ">": "<=", ">=": "<"}


class BuiltinPredicateSymbol(Enum):
    EQ = "="
    NE = "!="
    LT = "<"
    LE = "<="
    GT = ">"
    GE = ">="

    def __str__(self):
        return self.value.lower()

    def complement(self):
        return BuiltinPredicateSymbol(BuiltinPredicateSymbol_complement[self.value])


class BuiltinFunctionSymbol(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    POW = "**"
    MOD = "%"
    MIN = "min"
    MAX = "max"
    ABS = "abs"
    SIN = "sin"
    COS = "cos"
    TAN = "tan"
    ATAN = "atan"
    EXP = "exp"
    LOG = "log"
    ERF = "erf"
    ERFC = "erfc"
    SGN = "sgn"
    SQRT = "sqrt"

    # ...

    def __str__(self):
        return self.value.lower()


def is_builtin_predicate(predicate):
    return isinstance(predicate.symbol, BuiltinPredicateSymbol)


def create_atom(lang, symbol: BuiltinPredicateSymbol, lhs, rhs):
    from .formulas import Atom
    predicate = lang.get_predicate(symbol)
    return Atom(predicate, [lhs, rhs])


def is_builtin_function(fun):
    return isinstance(fun.symbol, BuiltinFunctionSymbol)

    # language = lhs.language
    # if language != rhs.language:
    #     raise err.LanguageMismatch(rhs, rhs.language, language)


def get_equality_predicates():
    return [BuiltinPredicateSymbol.EQ, BuiltinPredicateSymbol.NE]

    # TODO AT THE MOMENT WE DO NOT CHECK FOR TYPE SAFETY WITH BUILT-IN TYPES


def get_arithmetic_predicates():
    return [BuiltinPredicateSymbol.LT, BuiltinPredicateSymbol.LE, BuiltinPredicateSymbol.GT, BuiltinPredicateSymbol.GE]


def get_arithmetic_binary_functions():
    return [BuiltinFunctionSymbol.ADD, BuiltinFunctionSymbol.SUB, BuiltinFunctionSymbol.MUL, BuiltinFunctionSymbol.DIV,\
            BuiltinFunctionSymbol.POW, BuiltinFunctionSymbol.MOD]

def get_arithmetic_unary_functions():
    return [BuiltinFunctionSymbol.SQRT]

def get_special_binary_functions():
    BFS = BuiltinFunctionSymbol
    return [BFS.MIN, BFS.MAX]

def get_special_unary_functions():
    BFS = BuiltinFunctionSymbol
    return [BFS.ABS, BFS.SIN, BFS.COS, BFS.TAN, BFS.ATAN, BFS.EXP, BFS.LOG, BFS.ERF, BFS.ERFC, BFS.SGN]


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
