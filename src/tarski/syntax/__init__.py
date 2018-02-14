
from .function import Function
from .predicate import Predicate
from .sorts import Sort, Interval, inclusion_closure
from .terms import Term, Constant, Variable, CompoundTerm
from .formulas import Formula, land, lor, neg, implies, forall, exists, Connective, Atom, Formula, CompoundFormula, \
    QuantifiedFormula


from . _meta import RelationalOperatorImplementation

symbol_rel_op_map = {
    'eq' : '__eq__',
    'ne' : '__ne__'
}

term_classes = [ Term, CompoundTerm, Variable, Constant ]

for class_obj in term_classes :

    for sym, method in symbol_rel_op_map.items() :
        setattr(class_obj, method, RelationalOperatorImplementation(sym))
