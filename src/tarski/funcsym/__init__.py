import numpy as np
import scipy.special as sci

impl = {
    "min": lambda x, y: np.min((x, y)),
    "max": lambda x, y: np.max((x, y)),
    "pow": np.power,
    "abs": np.abs,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "asin": np.arcsin,
    "atan": np.arctan,
    "exp": np.exp,
    "log": np.log,
    "erf": sci.erf,
    "erfc": sci.erfc,
    "sgn": np.sign,
    "sqrt": np.sqrt,
    "normal": np.random.normal,
    "gamma": np.random.gamma,
}
