from ..builtins import BuiltinFunctionSymbol as BFS

def min(x, y):
    min_func = x.language.get_function(BFS.MIN)
    return min_func(x, y)

def max(x, y):
    max_func = x.language.get_function(BFS.MAX)
    return max_func(x, y)

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
