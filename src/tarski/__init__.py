# -*- coding: utf-8 -*-
import logging
from .fol import FirstOrderLanguage
from .syntax import Function, Predicate, Formula, Term, Constant, Variable
from .errors import LanguageError

logging.getLogger(__name__).addHandler(logging.NullHandler())
def language(name = 'L'):
    lang = FirstOrderLanguage(name)
    funcsym.initialize(lang)
    return lang

class Bunch(object):
    """
    A Bunch of stuff. Handy class for grouping together
    stuff.
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
