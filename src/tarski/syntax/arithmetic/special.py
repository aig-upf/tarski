from ..builtins import BuiltinFunctionSymbol as BFS


def min(x, y):
    try:
        min_func = x.language.get_function(BFS.MIN)
    except AttributeError:
        try:
            min_func = y.language.get_function(BFS.MIN)
        except AttributeError:
            return min(x, y)
    return min_func(x, y)


def max(x, y):
    try:
        max_func = x.language.get_function(BFS.MAX)
    except AttributeError:
        try:
            max_func = y.language.get_function(BFS.MAX)
        except AttributeError:
            return max(x, y)
    return max_func(x, y)


def abs(x):
    abs_func = x.language.get_function(BFS.ABS)
    return abs_func(x)


def sin(x):
    sin_func = x.language.get_function(BFS.SIN)
    return sin_func(x)


def cos(x):
    cos_func = x.language.get_function(BFS.COS)
    return cos_func(x)


def tan(x):
    tan_func = x.language.get_function(BFS.TAN)
    return tan_func(x)


def atan(x):
    atan_func = x.language.get_function(BFS.ATAN)
    return atan_func(x)


def asin(x):
    asin_func = x.language.get_function(BFS.ASIN)
    return asin_func(x)


def exp(x):
    exp_func = x.language.get_function(BFS.EXP)
    return exp_func(x)


def log(x):
    log_func = x.language.get_function(BFS.LOG)
    return log_func(x)


def erf(x):
    erf_func = x.language.get_function(BFS.ERF)
    return erf_func(x)


def erfc(x):
    erfc_func = x.language.get_function(BFS.ERFC)
    return erfc_func(x)


def sgn(x):
    sgn_func = x.language.get_function(BFS.SGN)
    return sgn_func(x)
