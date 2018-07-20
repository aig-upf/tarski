import numpy as np
import scipy.special as sci

impl = {
    "min": lambda x, y: np.min((x, y)),
    "max": lambda x, y: np.max((x, y)),
    "sin": lambda x: np.sin(x),
    "cos": lambda x: np.cos(x),
    "tan": lambda x: np.tan(x),
    "atan": lambda x: np.arctan(x),
    "exp": lambda x: np.exp(x),
    "log": lambda x: np.log(x),
    "erf": lambda x: sci.erf(x),
    "erfc": lambda x: sci.erfc(x)
}
