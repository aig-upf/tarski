# -*- coding: utf-8 -*-

from .language import FOL
from .sorts import parents, children
from .function import Function
from .terms import Term, Constant, Variable
from .errors import LanguageError
from .formulas import Formula
# we rename FOL to be language
language = FOL
