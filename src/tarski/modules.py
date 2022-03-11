"""
This module helps lazily importing some packages that depend on the installation of certain pip extras,
and that therefore we cannot import greedily.
"""


def _import_scipy_special():
    try:
        import scipy.special  # pylint: disable=import-outside-toplevel
        return scipy.special
    except ImportError:
        raise ImportError('The scipy module does not seem available. '
                          'Install Tarski with the "arithmetic" extra: pip install "tarski[arithmetic]"') from None


def _import_numpy():
    try:
        import numpy  # pylint: disable=import-outside-toplevel
        return numpy
    except ImportError:
        raise ImportError('The numpy module does not seem available. '
                          'Install Tarski with the "arithmetic" extra: pip install "tarski[arithmetic]"') from None


def _import_pyrddl_parser():
    try:
        from pyrddl.parser import \
            RDDLParser  # pylint: disable=import-outside-toplevel
        return RDDLParser
    except ImportError:
        raise ImportError('The pyrddl module does not seem available. '
                          'Install Tarski with the "rddl" extra: pip install "tarski[rddl]"') from None


def __getattr__(name, *args, **kwargs):
    if name == 'RDDLParser':
        return _import_pyrddl_parser()
    elif name == 'numpy':
        return _import_numpy()
    elif name == 'scipy_special':
        return _import_scipy_special()
    raise ImportError(f'Module "{name}" is not available')
