import numpy as np
import scipy.special as sci

impl = {
    "min": lambda x, y: np.min((x, y)),
    "max": lambda x, y: np.max((x, y)),
    "pow": lambda x, y: np.pow(x, y),
    "abs": lambda x: np.abs(x),
    "sin": lambda x: np.sin(x),
    "cos": lambda x: np.cos(x),
    "tan": lambda x: np.tan(x),
    "asin": lambda x: np.arcsin(x),
    "atan": lambda x: np.arctan(x),
    "exp": lambda x: np.exp(x),
    "log": lambda x: np.log(x),
    "erf": lambda x: sci.erf(x),
    "erfc": lambda x: sci.erfc(x),
    "sgn": lambda x: np.sign(x),
    "sqrt": lambda x: np.sqrt(x),
    "normal": lambda u, s: np.random.normal(u, s),
    "gamma": lambda shape, scale: np.random.gamma(shape, scale)
}
