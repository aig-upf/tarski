from .function import Function
from .predicate import Predicate
from .sorts import Sort, Interval, inclusion_closure
from .terms import Term, Constant, Variable, CompoundTerm
from .formulas import Formula, land, lor, neg, implies, forall, exists, equiv, Connective, Atom, Formula, CompoundFormula, \
    QuantifiedFormula

from ._meta import RelationalOperatorImplementation

from .visitors import CollectVariables

symbol_rel_op_map = {
    'eq': '__eq__',
    'ne': '__ne__'
}


def bind_equality_to_language_components(lang):
    term_classes = [lang.Term, lang.CompoundTerm, lang.Variable, lang.Constant]

    for class_obj in term_classes:

        for sym, method in symbol_rel_op_map.items():
            setattr(class_obj, method, RelationalOperatorImplementation(sym))
