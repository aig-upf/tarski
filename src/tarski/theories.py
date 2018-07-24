""" Management of the theories (e.g. equality, etc.) associated to the FO languages """
from enum import Enum

from .fol import FirstOrderLanguage
from .syntax import builtins, Term
from .syntax.factory import create_atom, create_arithmetic_term
from .syntax.ops import cast_to_closest_common_ancestor
from . import errors as err


class Theory(Enum):
    """ """
    EQUALITY = "equality"
    ARITHMETIC = "arithmetic"

    def __str__(self):
        return self.value


def language(name='L', theories=None):
    """ Build a language with the given name and configure it with the given theories """
    theories = theories or []
    lang = FirstOrderLanguage(name)
    _ = [load_theory(lang, t) for t in theories]
    return lang


def load_theory(lang, theory):
    """ """
    if lang.language_components_frozen:
        raise err.LanguageError("Cannot load theories once language elements have been defined")

    # TODO We should create type-specific versions of each predicate / function.
    object_t = lang.get_sort('object')

    if theory == Theory.EQUALITY:
        for pred in builtins.get_equality_predicates():
            lang.register_operator_handler(pred, Term, Term, create_casting_handler(pred, create_atom))
            p = lang.predicate(pred, object_t, object_t)
            p.builtin = True

    elif theory == Theory.ARITHMETIC:
        for pred in builtins.get_arithmetic_predicates():
            lang.register_operator_handler(pred, Term, Term, create_casting_handler(pred, create_atom))
            p = lang.predicate(pred, object_t, object_t)
            p.builtin = True

        for fun in builtins.get_arithmetic_functions():
            lang.register_operator_handler(fun, Term, Term, create_casting_handler(fun, create_arithmetic_term))
            f = lang.function(fun, object_t, object_t, object_t)
            f.builtin = True

        # print("Loaded theory '{}'".format(theory))
    else:
        raise err.UnknownTheory(theory)

    lang.theories.append(theory)


def create_casting_handler(symbol, factory_method):
    """ """
    def handler(lhs, rhs):
        lhs, rhs = cast_to_closest_common_ancestor(lhs, rhs)
        return factory_method(symbol, lhs, rhs)
    return handler
