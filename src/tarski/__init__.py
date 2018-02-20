# -*- coding: utf-8 -*-

from .fol import FirstOrderLanguage
from .syntax import Function, Formula, Term, Constant, Variable
from .errors import LanguageError
from . import funcsym


def language(name = 'L'):
    lang = FirstOrderLanguage(name)
    funcsym.initialize(lang)
    return lang
