import logging
import sys as sys

from .version import __version__, __version_info__
from .fol import FirstOrderLanguage
from .theories import language
from .theories import Theory as Theories
from .syntax import Function, Predicate, Formula, Term, Constant, Variable
from .errors import LanguageError
from . import fstrips

logging.getLogger(__name__).addHandler(logging.NullHandler())


if sys.version_info < (3, 8, 0):
    raise OSError(f'Tarski requires Python>=3.8, but yours is {sys.version_info}')

__all__ = ['__version__', '__version_info__', 'FirstOrderLanguage', 'language', 'Theories',
           'Function', 'Predicate', 'Formula', 'Term', 'Constant', 'Variable', 'LanguageError', 'fstrips']
