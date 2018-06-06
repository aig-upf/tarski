# -*- coding: utf-8 -*-

import logging
from .fol import FirstOrderLanguage
from .theories import language
from .syntax import Function, Predicate, Formula, Term, Constant, Variable
from .errors import LanguageError
from . import fstrips

logging.getLogger(__name__).addHandler(logging.NullHandler())
