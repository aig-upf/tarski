
from .. import Term
from ..errors import SortMismatch
from ..syntax import Constant, BuiltinFunctionSymbol, CompoundTerm, BuiltinPredicateSymbol, Atom, sorts
from ..syntax.sorts import Set, Enumeration


def set_emptyset(set_t: Set):
    if not isinstance(set_t, Set):
        raise ValueError(f'Incorrect set sort "{set_t}"')

    return Constant(set(), set_t)


def set_literal(set_t, *args):
    if not isinstance(set_t, Set):
        raise ValueError(f'Incorrect set sort "{set_t}"')

    literals = set()
    for elem in args:
        # This will ensure that the elements are of the appropriate type as well
        literals.add(set_t.subtype.literal(elem))

    return Constant(literals, set_t)


def set_union(*args):
    return _compound_set(BuiltinFunctionSymbol.SET_UNION, *args)


def set_intersection(*args):
    return _compound_set(BuiltinFunctionSymbol.SET_INTERSECTION, *args)


def set_difference(*args):
    if len(args) != 2:
        raise ValueError(f'Set operation "set_difference" only valid on two sets, but encountered: "{args}"')
    return _compound_set(BuiltinFunctionSymbol.SET_DIFFERENCE, *args)


def set_cardinality(s):
    check_is_set_term(s, f'Unexpected operand type for set cardinality operation: "{s}"')

    f = s.language.get_function(BuiltinFunctionSymbol.SET_CARDINALITY)
    return f(s)


def set_in(x, s):
    check_is_set_term(s, f'Unexpected operand type for set cardinality operation: "{s}"')
    lang = s.language

    if not lang.is_subtype(x.sort, s.sort.subtype):
        # Check x is a possible element of s
        raise SortMismatch(x, x.sort, s.subtype)

    # We enforce a restrictive type compliance: we only accept X in set<X>, for X either object or an interval type.
    lhs_sort = lang.Object if isinstance(x.sort, Enumeration) else x.sort
    rhs_sort = sorts.Set(lang, lhs_sort)

    op = lang._operators.get((BuiltinPredicateSymbol.SET_IN, lhs_sort, rhs_sort))
    assert op is not None
    return op(x, s)


def _compound_set(fun: BuiltinFunctionSymbol, *args):
    if len(args) < 1:
        raise ValueError(f'Set operation "{fun}" requires at least one set')

    for s in args:
        check_is_set_term(s, f'Unexpected operand type for set operation "{fun}": "{s}"')

    lang = args[0].language
    u = lang.get_function(fun)
    return CompoundTerm(u, args)


def check_is_set_term(c, error_msg=None):
    error_msg = error_msg or f'Unexpected object "{c}" where a set constant was expected'
    if not isinstance(c, Term) and isinstance(c.sort, Set):
        raise ValueError(error_msg)


def set_semantics_evaluation(lang, symbol, subterms, sort):
    literals = [c.sort.literal(c) for c in subterms]

    if symbol == BuiltinFunctionSymbol.SET_CARDINALITY:
        assert len(literals) == 1
        return Constant(len(literals[0]), lang.Natural)

    if symbol == BuiltinFunctionSymbol.SET_UNION:
        assert len(literals) >= 1
        return Constant(set().union(*literals), sort)

    if symbol == BuiltinFunctionSymbol.SET_INTERSECTION:
        assert len(literals) >= 1 and isinstance(literals[0], set)
        return Constant(literals[0].intersection(*literals[1:]), sort)
    
    if symbol == BuiltinFunctionSymbol.SET_DIFFERENCE:
        assert len(literals) == 2 and isinstance(literals[0], set)
        return Constant(literals[0] - literals[1], sort)

    if symbol == BuiltinPredicateSymbol.SET_IN:
        assert len(literals) == 2 and isinstance(literals[1], set)
        return literals[0] in literals[1]

    raise RuntimeError(f'Unknown set operation "{symbol}"')



