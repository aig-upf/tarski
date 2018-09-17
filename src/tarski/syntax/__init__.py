
from .function import Function
from .predicate import Predicate
from .sorts import Sort, Interval, inclusion_closure
from .terms import Term, Constant, Variable, CompoundTerm, TermReference
from .formulas import land, lor, neg, implies, forall, exists, equiv, Connective, Atom, Formula,\
    CompoundFormula, QuantifiedFormula, Tautology, Contradiction, top, bot, Quantifier, FormulaReference
from .builtins import BuiltinFunctionSymbol, BuiltinPredicateSymbol

def symref(sym):
    if isinstance(sym, Term):
        return TermReference(sym)
    if isinstance(sym, Formula):
        return FormulaReference(sym)
    assert False
