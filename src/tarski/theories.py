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
    SPECIAL = "special"
    RANDOM = "random"

    def __str__(self):
        return self.value


def language(name='L', theories=None):
    """ Build a language with the given name and configure it with the given theories """
    theories = theories or []
    lang = FirstOrderLanguage(name)
    _ = [load_theory(lang, t) for t in theories]
    return lang


def load_theory(lang, theory):
    """ Load one of the buillt-in theories into the given language """
    if lang.language_components_frozen:
        raise err.LanguageError("Cannot load theories once language elements have been defined")
    loaders = {
        Theory.EQUALITY: load_equality_theory,
        Theory.ARITHMETIC: load_arithmetic_theory,
        Theory.SPECIAL: load_special_theory,
        Theory.RANDOM: load_random_theory,
    }
    loader = loaders.get(theory)
    if loader is None:
        raise err.UnknownTheory(theory)

    loader(lang)
    lang.theories.append(theory)


def load_equality_theory(lang):
    # TODO We should create type-specific versions of each predicate / function.
    object_t = lang.get_sort('object')
    for pred in builtins.get_equality_predicates():
        lang.register_operator_handler(pred, Term, Term, create_casting_handler(pred, create_atom))
        p = lang.predicate(pred, object_t, object_t)
        p.builtin = True


def load_arithmetic_theory(lang):
    # MRJ: ite function is now part of the Arithmetic theory
    # "virtual function" ite (if-then-else) registered
    ite_func = lang.function('ite', lang.Object, lang.Object, lang.Object)
    ite_func.builtin = True

    fun = builtins.BuiltinFunctionSymbol.MATMUL
    lang.register_operator_handler(fun, Term, Term, create_casting_handler(fun, create_arithmetic_term))
    f = lang.function(fun, lang.Real, lang.Real, lang.Real)
    f.builtin = True

    for pred in builtins.get_arithmetic_predicates():
        lang.register_operator_handler(pred, Term, Term, create_casting_handler(pred, create_atom))
        p = lang.predicate(pred, lang.Real, lang.Real)
        p.builtin = True

    for fun in builtins.get_arithmetic_binary_functions():
        lang.register_operator_handler(fun, Term, Term, create_casting_handler(fun, create_arithmetic_term))
        f = lang.function(fun, lang.Real, lang.Real, lang.Real)
        f.builtin = True

    for fun in builtins.get_arithmetic_unary_functions():
        lang.register_unary_operator_handler(fun, Term, create_casting_handler(fun, create_arithmetic_term))
        f = lang.function(fun, lang.Real, lang.Real)
        f.builtin = True


def load_special_theory(lang):
    for fun in builtins.get_special_binary_functions():
        lang.register_operator_handler(fun, Term, Term, create_casting_handler(fun, create_arithmetic_term))
        f = lang.function(fun, lang.Real, lang.Real, lang.Real)
        f.builtin = True
    for fun in builtins.get_special_unary_functions():
        lang.register_unary_operator_handler(fun, Term, create_casting_handler(fun, create_arithmetic_term))
        f = lang.function(fun, lang.Real, lang.Real)
        f.builtin = True


def load_random_theory(lang):
    for fun in builtins.get_random_binary_functions():
        lang.register_operator_handler(fun, Term, Term, create_casting_handler(fun, create_arithmetic_term))
        f = lang.function(fun, lang.Real, lang.Real, lang.Real)
        f.builtin = True
    for fun in builtins.get_random_unary_functions():
        lang.register_unary_operator_handler(fun, Term, create_casting_handler(fun, create_arithmetic_term))
        f = lang.function(fun, lang.Real, lang.Real)
        f.builtin = True


def create_casting_handler(symbol, factory_method):
    """ """
    def handler(lhs, rhs):
        lhs, rhs = cast_to_closest_common_ancestor(lhs, rhs)
        return factory_method(symbol, lhs, rhs)
    return handler
