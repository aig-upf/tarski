from .. import errors as err
from .formulas import Atom
from .terms import Term
from .builtins import BuiltinPredicateSymbol, BuiltinFunctionSymbol


def check_same_language(lhs, rhs):
    language = lhs.language
    if language != rhs.language:
        raise err.LanguageMismatch(rhs, rhs.language, language)
    return language


def create_atom(symbol: BuiltinPredicateSymbol, lhs, rhs):
    assert isinstance(lhs, Term) and isinstance(rhs, Term)

    language = check_same_language(lhs, rhs)

    # s1, s2 = lhs.type, rhs.type
    # if language.is_subtype(s1, s2):
    #     return Atom("xxx", [lhs, rhs])

    # TODO AT THE MOMENT WE DO NOT CHECK FOR TYPE SAFETY WITH BUILT-IN TYPES

    predicate = language.get_predicate(symbol)
    return Atom(predicate, [lhs, rhs])


def create_arithmetic_term(symbol: BuiltinFunctionSymbol, lhs, rhs):
    language = check_same_language(lhs, rhs)
    fun = language.get_function(symbol)
    return fun(lhs, rhs)
