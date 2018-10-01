from ..builtins import BuiltinFunctionSymbol as BFS
import numpy as np

def normal(mu, sigma):
    try:
        normal_func = mu.language.get_function(BFS.NORMAL)
    except AttributeError:
        try:
            normal_func = mu.language.get_function(BFS.NORMAL)
        except AttributeError:
            return np.random.normal(mu, sigma)
    return normal_func(mu, sigma)
