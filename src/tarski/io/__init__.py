from .fstrips import FstripsReader, FstripsWriter
from .utils import find_domain_filename

# Just a shortcut, turns out they're both the same! :-)
PDDLReader = FstripsReader

__all__ = [
    "FstripsReader",
    "FstripsWriter",
    "find_domain_filename",
    "PDDLReader",
]
