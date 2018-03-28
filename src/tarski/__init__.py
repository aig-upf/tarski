# -*- coding: utf-8 -*-

import logging
from .fol import language, FirstOrderLanguage
from .syntax import Function, Formula, Term, Constant, Variable
from .errors import LanguageError

logging.getLogger(__name__).addHandler(logging.NullHandler())
