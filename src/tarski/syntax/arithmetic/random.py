
from ..builtins import BuiltinFunctionSymbol as bfs
from ... import modules


def normal(mu, sigma):
    try:
        normal_func = mu.language.get_function(bfs.NORMAL)
    except AttributeError:
        try:
            normal_func = mu.language.get_function(bfs.NORMAL)
        except AttributeError:
            np = modules.import_numpy()
            return np.random.normal(mu, sigma)
    return normal_func(mu, sigma)


def gamma(shape, scale):
    try:
        gamma_func = shape.language.get_function(bfs.GAMMA)
    except AttributeError:
        try:
            gamma_func = scale.language.get_function(bfs.GAMMA)
        except AttributeError:
            np = modules.import_numpy()
            return np.random.gamma(shape, scale)
    return gamma_func(shape, scale)
