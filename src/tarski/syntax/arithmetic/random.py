
import numpy as np

from ..builtins import BuiltinFunctionSymbol as BFS


def normal(mu, sigma):
    try:
        normal_func = mu.language.get_function(BFS.NORMAL)
    except AttributeError:
        try:
            normal_func = mu.language.get_function(BFS.NORMAL)
        except AttributeError:
            return np.random.normal(mu, sigma)
    return normal_func(mu, sigma)


def gamma(shape, scale):
    try:
        gamma_func = shape.language.get_function(BFS.GAMMA)
    except AttributeError:
        try:
            gamma_func = scale.language.get_function(BFS.GAMMA)
        except AttributeError:
            return np.random.gamma(shape, scale)
    return gamma_func(shape, scale)
