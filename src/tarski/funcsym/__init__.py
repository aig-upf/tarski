
from .. import modules


def impl(symbol):
    """ """

    if symbol in {"erf", "erfc"}:
        from ..modules import import_scipy_special
        sci = import_scipy_special()
        return {
            "erf": sci.erf,
            "erfc": sci.erfc,
        }.get(symbol)

    np = modules.import_numpy()
    return {
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
        "sgn": np.sign,
        "sqrt": np.sqrt,
        "normal": np.random.normal,
        "gamma": np.random.gamma,
    } .get(symbol)
