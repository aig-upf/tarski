
from .function import Function
from .predicate import Predicate
from .sorts import Sort, Interval, inclusion_closure
from .terms import Term, Constant, Variable, CompoundTerm
from .formulas import land, lor, neg, implies, forall, exists, equiv, Connective, Atom, Formula,\
    CompoundFormula, QuantifiedFormula, Tautology, Contradiction, top, bot, Quantifier
from .builtins import BuiltinFunctionSymbol, BuiltinPredicateSymbol
from .visitors import SymbolReference, esm

def symref(sym):
    return SymbolReference(syn, eq_fn=esm)
