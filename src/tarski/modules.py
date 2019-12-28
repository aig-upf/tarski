""" """


def import_sdd():
    try:
        from pysdd import sdd
    except ImportError as _:
        raise ImportError('The tarski.sdd module is not available, could not import pysdd module. '
                          'Please try installing Tarski with the "sdd" extra, or installing pysdd by hand.') from None
    return sdd


def import_scipy_special():
    try:
        import scipy.special as sci
    except ImportError as err:
        raise ImportError('The tarski.scipy module does not seem available. '
                          'Please try installing Tarski with the "scipy" extra.') from None
    return sci

