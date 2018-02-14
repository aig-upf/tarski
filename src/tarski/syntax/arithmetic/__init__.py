from .. terms import Term, CompoundTerm, Variable, Constant
from .. _meta import ArithmeticOperatorImplementation, RelationalOperatorImplementation

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



# bind operators to term class
for sym, method in symbol_arith_op_map.items() :
    setattr(Term, method, ArithmeticOperatorImplementation(sym))

for sym, method in symbol_rel_op_map.items() :
    setattr(Term, method, RelationalOperatorImplementation(sym))

# bind operators to subclasses

term_classes = [ CompoundTerm, Variable, Constant ]

for class_obj in term_classes :
    for sym, method in symbol_arith_op_map.items() :
        setattr(class_obj, method, ArithmeticOperatorImplementation(sym))

    for sym, method in symbol_rel_op_map.items() :
        setattr(class_obj, method, RelationalOperatorImplementation(sym))
