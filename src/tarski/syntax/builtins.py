from enum import Enum

# A table with the negated counterparts of builtin predicates.
symbol_complements = {"=": "!=", "!=": "=", "<": ">=", "<=": ">", ">": "<=", ">=": "<"}


class BuiltinPredicateSymbol(Enum):
    EQ = "="
    NE = "!="
    LT = "<"
    LE = "<="
    GT = ">"
    GE = ">="

    SET_IS_EMPTY = "set_is_empty"
    SET_IN = "set_in"

    def __str__(self):
        return self.value.lower()

    def complement(self):
        return BuiltinPredicateSymbol(symbol_complements[self.value])


class BuiltinFunctionSymbol(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    MATMUL = "@"
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
    ASIN = "asin"
    EXP = "exp"
    LOG = "log"
    ERF = "erf"
    ERFC = "erfc"
    SGN = "sgn"
    SQRT = "sqrt"
    NORMAL = "normal"
    GAMMA = "gamma"
    KRON = "kron"
    DIRAC = "dirac"
    BERNOULLI = "bernoulli"
    DISCRETE = "discrete"
    POISSON = "poisson"

    ITE = "ite"  # If-then-else

    # SET_EMPTYSET = "set_emptyset"  # ATM we consider this as a language constant
    SET_INTERSECTION = "set_intersection"
    SET_UNION = "set_union"
    SET_DIFFERENCE = "set_difference"
    SET_CARDINALITY = "set_cardinality"

    def __str__(self):
        return self.value.lower()


def is_builtin_predicate(predicate):
    return isinstance(predicate.symbol, BuiltinPredicateSymbol)


def create_atom(lang, symbol: BuiltinPredicateSymbol, lhs, rhs):
    from .formulas import Atom
    predicate = lang.get_predicate(symbol)
    return Atom(predicate, [lhs, rhs])


def negate_builtin_atom(atom):
    """ Given an atom based on a built-in predicate, return an equivalent atom with the negation absorbed.
    If the atom is not based on a built-in predicate, return the atom unchanged.
    """
    from .formulas import Atom
    if isinstance(atom, Atom) and atom.predicate.builtin:
        pred = atom.predicate
        return create_atom(pred.language, pred.symbol.complement(), *atom.subterms)
    return atom


def is_builtin_function(fun):
    return isinstance(fun.symbol, BuiltinFunctionSymbol)


def get_equality_predicates():
    return [BuiltinPredicateSymbol.EQ, BuiltinPredicateSymbol.NE]


def get_arithmetic_predicates():
    return [BuiltinPredicateSymbol.LT, BuiltinPredicateSymbol.LE, BuiltinPredicateSymbol.GT, BuiltinPredicateSymbol.GE]


def get_real_signature(lang):
    return lang.Real, lang.Real, lang.Real


def get_int_signature(lang):
    return lang.Integer, lang.Integer, lang.Integer


def get_natural_signature(lang):
    return lang.Natural, lang.Natural, lang.Natural


def get_function_overloads(lang, symbol):
    real_only_signature = [get_real_signature(lang)]
    int_only_signature = [get_int_signature(lang)]
    real_and_int_signature = real_only_signature + int_only_signature

    return {
        BuiltinFunctionSymbol.ADD: real_and_int_signature + [get_natural_signature(lang)],
        BuiltinFunctionSymbol.SUB: real_and_int_signature,
        BuiltinFunctionSymbol.MUL: real_and_int_signature,
        BuiltinFunctionSymbol.DIV: real_only_signature,
        BuiltinFunctionSymbol.POW: real_and_int_signature,
        BuiltinFunctionSymbol.MOD: int_only_signature,
    }.get(symbol, real_only_signature)


def get_arithmetic_binary_functions():
    return {BuiltinFunctionSymbol.ADD, BuiltinFunctionSymbol.SUB, BuiltinFunctionSymbol.MUL, BuiltinFunctionSymbol.DIV,
            BuiltinFunctionSymbol.POW, BuiltinFunctionSymbol.MOD}


def get_arithmetic_unary_functions():
    return {BuiltinFunctionSymbol.SQRT}


def get_arithmetic_functions():
    return get_arithmetic_binary_functions() | get_arithmetic_unary_functions()


def get_set_symbols():
    return {BuiltinFunctionSymbol.SET_CARDINALITY, BuiltinFunctionSymbol.SET_UNION,
            BuiltinFunctionSymbol.SET_INTERSECTION, BuiltinFunctionSymbol.SET_DIFFERENCE,
            BuiltinPredicateSymbol.SET_IN}


def get_matrix_functions():
    return [BuiltinFunctionSymbol.MATMUL]


def get_special_binary_functions():
    BFS = BuiltinFunctionSymbol
    return [BFS.MIN, BFS.MAX]


def get_special_unary_functions():
    BFS = BuiltinFunctionSymbol
    return [BFS.ABS, BFS.SIN, BFS.COS, BFS.TAN, BFS.ATAN, BFS.ASIN, BFS.EXP, BFS.LOG, BFS.ERF, BFS.ERFC, BFS.SGN]


def get_random_binary_functions():
    BFS = BuiltinFunctionSymbol
    return [BFS.NORMAL, BFS.GAMMA]


def get_random_unary_functions():
    return []


def get_predicate_from_symbol(symbol: str):
    return BuiltinPredicateSymbol(symbol)


def get_function_from_symbol(symbol: str):
    return BuiltinFunctionSymbol(symbol)
