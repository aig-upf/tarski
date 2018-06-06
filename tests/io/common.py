
from tarski.io import FstripsReader


def reader(theories=None):
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True, theories=theories)
