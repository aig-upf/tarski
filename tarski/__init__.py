# -*- coding: utf-8 -*-

from ._language import FOL
from ._sorts import parents, children
from ._terms import Term, Constant, Variable, Var
from ._formulas import axiom, top, bot, land, lor, neg, exists, forall
# we rename FOL to be language
language = FOL
