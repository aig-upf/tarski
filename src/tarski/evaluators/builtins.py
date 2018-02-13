
from enum import Enum

# from .._model import Model
from .. import errors as err


class BuiltinPredicate(Enum):
    EQ = "="
    NE = "!="
    LT = "<"
    LE = "<="
    GT = ">"
    GE = ">="


def is_builtin_predicate(predicate):
    return isinstance(predicate.symbol, BuiltinPredicate)


def create_symbols_for_language(lang):
    obj = lang.get_sort('object')
    for s in BuiltinPredicate:
        lang.predicate(s, obj, obj)


def create_atom(symbol: BuiltinPredicate, lhs, rhs):
    from tarski.syntax import Term
    from ..syntax import Atom

    assert isinstance(lhs, Term) and isinstance(rhs, Term)

    language = lhs.language
    if language != rhs.language:
        raise err.LanguageMismatch(rhs, rhs.language, language)

    # s1, s2 = lhs.type, rhs.type
    # if language.is_subtype(s1, s2):
    #     return Atom("xxx", [lhs, rhs])

    # TODO AT THE MOMENT WE DO NOT CHECK FOR TYPE SAFETY WITH BUILT-IN TYPES

    predicate = language.get_predicate(symbol)
    return Atom(predicate, [lhs, rhs])


def eq(lhs, rhs):
    return create_atom(BuiltinPredicate.EQ, lhs, rhs)


def ne(lhs, rhs):
    return create_atom(BuiltinPredicate.NE, lhs, rhs)


def lt(lhs, rhs):
    return create_atom(BuiltinPredicate.LT, lhs, rhs)


def gt(lhs, rhs):
    return create_atom(BuiltinPredicate.GT, lhs, rhs)


def le(lhs, rhs):
    return create_atom(BuiltinPredicate.LE, lhs, rhs)


def ge(lhs, rhs):
    return create_atom(BuiltinPredicate.GE, lhs, rhs)


def evaluate(formula, model, sigma):
    from .simple import evaluate as ev
    _evaluators = {
        BuiltinPredicate.EQ: lambda f, m, s: ev(f.subterms[0], m, s) == ev(f.subterms[1], m, s),
        BuiltinPredicate.NE: lambda f, m, s: ev(f.subterms[0], m, s) != ev(f.subterms[1], m, s),
        BuiltinPredicate.LT: lambda f, m, s: ev(f.subterms[0], m, s) < ev(f.subterms[1], m, s),
        BuiltinPredicate.LE: lambda f, m, s: ev(f.subterms[0], m, s) <= ev(f.subterms[1], m, s),
        BuiltinPredicate.GT: lambda f, m, s: ev(f.subterms[0], m, s) > ev(f.subterms[1], m, s),
        BuiltinPredicate.GE: lambda f, m, s: ev(f.subterms[0], m, s) >= ev(f.subterms[1], m, s),
    }

    return _evaluators[formula.symbol](formula, model, sigma)
