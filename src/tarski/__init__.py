import logging
import sys

from . import fstrips
from .errors import LanguageError
from .fol import FirstOrderLanguage
from .syntax import Constant, Formula, Function, Predicate, Term, Variable
from .theories import Theory as Theories
from .theories import language
from .version import __version__, __version_info__

logging.getLogger(__name__).addHandler(logging.NullHandler())


if sys.version_info < (3, 8, 0):
    raise OSError(f'Tarski requires Python>=3.8, but yours is {sys.version_info}')

__all__ = ['__version__', '__version_info__', 'FirstOrderLanguage', 'language', 'Theories',
           'Function', 'Predicate', 'Formula', 'Term', 'Constant', 'Variable', 'LanguageError', 'fstrips']
