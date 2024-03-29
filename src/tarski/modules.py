""" A helper module to deal with import of packages that depend on the installation of certain pip extras,
to keep Tarski modular and lightweight for simple uses, but optionally heavyweight for more sophisticated uses. """

# TODO: Whenever we raise the Python requirement to Python >= 3.7, we should migrate this to a better
#       interface providing direct access to the desired package, e.g. allowing "from tarski.modules import pyrddl",
#       which can be easily achieved with the new module-level __getattr__
#       https://docs.python.org/3/reference/datamodel.html#customizing-module-attribute-access


def import_scipy_special():
    try:
        import scipy.special as sci  # pylint: disable=import-outside-toplevel
    except ImportError:
        raise ImportError('The scipy module does not seem available. '
                          'Please try installing Tarski with the "arithmetic" extra.') from None
    return sci


def import_numpy():
    try:
        import numpy as np  # pylint: disable=import-outside-toplevel
    except ImportError:
        raise ImportError('The numpy module does not seem available. '
                          'Please try installing Tarski with the "arithmetic" extra.') from None
    return np


def import_pyrddl_parser():
    try:
        from pyrddl.parser import RDDLParser  # pylint: disable=import-outside-toplevel
    except ImportError:
        raise ImportError('The pyrddl module does not seem available. '
                          'Please try installing Tarski with the "rddl" extra.') from None
    return RDDLParser
