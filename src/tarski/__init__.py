# -*- coding: utf-8 -*-

from ._language import FOL
from ._sorts import parents, children
from ._function import Function
from ._terms import Term, Constant, Variable, Var
from .errors import LanguageError
from ._formulas import Formula
# we rename FOL to be language
language = FOL
