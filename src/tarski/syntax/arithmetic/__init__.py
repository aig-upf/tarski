from .. terms import Term, CompoundTerm, Variable, Constant
from .. _meta import ArithmeticOperatorImplementation, RelationalOperatorImplementation
import copy

symbol_arith_op_map = {
    '+' : '__add__',
    '-' : '__sub__',
    '*' : '__mul__',
    '@' : '__matmul__',
    '/' : '__truediv__',
    '//' : '__floordiv__',
    '%' : '__mod__',
    'divmod' : '__divmod__',
    '**' : '__pow__',
    '<<' : '__lshift__',
    '>>' : '__rshift__',
    '&' : '__and__',
    '^' : '__xor__',
    '|' : '__or__'
}

symbol_rel_op_map = {
    'lt' : '__lt__',
    'gt' : '__gt__',
    'le' : '__le__',
    'ge' : '__ge__'
}


def bind_operators_to_language_components(L) :

    # bind operators to term class
    for sym, method in symbol_arith_op_map.items() :
        setattr(L.Term, method, ArithmeticOperatorImplementation(sym))

    for sym, method in symbol_rel_op_map.items() :
        setattr(L.Term, method, RelationalOperatorImplementation(sym))

    # bind operators to subclasses

    term_classes = [ L.CompoundTerm, L.Variable, L.Constant ]

    for class_obj in term_classes :
        for sym, method in symbol_arith_op_map.items() :
            setattr(class_obj, method, ArithmeticOperatorImplementation(sym))

        for sym, method in symbol_rel_op_map.items() :
            setattr(class_obj, method, RelationalOperatorImplementation(sym))
