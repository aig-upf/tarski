from .._meta import ArithmeticOperatorImplementation, RelationalOperatorImplementation

symbol_arith_op_map = {
    '+': '__add__',
    '-': '__sub__',
    '*': '__mul__',
    '@': '__matmul__',
    '/': '__truediv__',
    '//': '__floordiv__',
    '%': '__mod__',
    'divmod': '__divmod__',
    '**': '__pow__',
    '&': '__and__',
    '^': '__xor__',
    '|': '__or__'
}

symbol_rel_op_map = {
    'lt': '__lt__',
    'gt': '__gt__',
    'le': '__le__',
    'ge': '__ge__'
}


def bind_operators_to_language_components(lang):
    print('Binding operators to language: {}'.format(lang))
    # bind operators to term class
    for sym, method in symbol_arith_op_map.items():
        setattr(lang.Term, method, ArithmeticOperatorImplementation(sym))

    for sym, method in symbol_rel_op_map.items():
        setattr(lang.Term, method, RelationalOperatorImplementation(sym))

    # bind operators to subclasses

    term_classes = [lang.CompoundTerm, lang.Variable, lang.Constant]

    for class_obj in term_classes:
        for sym, method in symbol_arith_op_map.items():
            setattr(class_obj, method, ArithmeticOperatorImplementation(sym))

        for sym, method in symbol_rel_op_map.items():
            setattr(class_obj, method, RelationalOperatorImplementation(sym))
