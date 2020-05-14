""" Management of the theories (e.g. equality, etc.) associated to the FO languages """
from enum import Enum
from typing import Union, List, Optional

from tarski.errors import DuplicateTheoryDefinition
from .syntax.sorts import attach_arithmetic_sorts, attach_bool_sort
from .fol import FirstOrderLanguage
from .syntax import builtins
from . import errors as err


class Theory(Enum):
    """ """
    BOOLEAN = "boolean"
    EQUALITY = "equality"
    ARITHMETIC = "arithmetic"
    SPECIAL = "special"
    RANDOM = "random"
    SETS = "sets"

    def __str__(self):
        return self.value


def language(name='L', theories: Optional[List[Union[str, Theory]]] = None):
    """ Build a language with the given name and configure it with the given theories.
    Theories can be provided as a list of Theory objects, or as a list with their names, e.g.

    >>> l = language(theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    is equivalent to

    >>> l = language(theories=['equality', 'arithmetic'])
     """
    theories = theories or []
    lang = FirstOrderLanguage(name)
    _ = [load_theory(lang, t) for t in theories]
    return lang


def load_theory(lang, theory: Union[Theory, str]):
    """ Load one of the built-in theories into the given language """
    try:
        th = Theory(theory) if isinstance(theory, str) else theory  # Make sure we have a valid theory object
    except ValueError as e:
        raise e from None  # Just to have a nicer exception

    if th in lang.theories:
        raise DuplicateTheoryDefinition(th)

    loaders = {
        Theory.BOOLEAN: load_bool_theory,
        Theory.EQUALITY: load_equality_theory,
        Theory.ARITHMETIC: load_arithmetic_theory,
        Theory.SPECIAL: load_special_theory,
        Theory.RANDOM: load_random_theory,
        Theory.SETS: load_set_theory,
    }
    loader = loaders.get(th)
    if loader is None:
        raise err.UnknownTheory(theory)

    theories_requiring_arithmetic_sorts = {
        Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM, Theory.SETS
    }
    if th in theories_requiring_arithmetic_sorts and not lang.has_sort('Integer'):
        attach_arithmetic_sorts(lang)

    loader(lang)
    lang.theories.add(th)


def has_theory(lang, theory: Union[Theory, str]):
    th = Theory(theory) if isinstance(theory, str) else theory  # Make sure we have a valid theory object
    return th in lang.theories


def load_bool_theory(lang):
    attach_bool_sort(lang)


def load_equality_theory(lang):
    for symbol in builtins.get_equality_predicates():
        p = lang.predicate(symbol, lang.Object, lang.Object, builtin=True)
        lang.register_operator_handler(symbol, lang.Object, lang.Object, p)


def load_arithmetic_theory(lang):
    for symbol in builtins.get_arithmetic_predicates():
        p = lang.predicate(symbol, lang.Real, lang.Real, builtin=True)
        lang.register_operator_handler(symbol, lang.Real, lang.Real, p)

    for symbol in builtins.get_arithmetic_binary_functions():
        overloads = builtins.get_function_overloads(lang, symbol)
        do_overload = len(overloads) > 1
        for signature in overloads:
            domain = signature[:-1]
            fun = lang.function(symbol, *signature, builtin=True, overload=do_overload)
            lang.register_operator_handler(symbol, *domain, fun)

    for symbol in builtins.get_matrix_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, lang.Real, builtin=True)
        lang.register_operator_handler(symbol, lang.Real, lang.Real, fun)

    for symbol in builtins.get_arithmetic_unary_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, builtin=True)
        lang.register_unary_operator_handler(symbol, lang.Real, fun)

    # MRJ: ite function is now part of the Arithmetic theory
    lang.function(builtins.BuiltinFunctionSymbol.ITE, lang.Object, lang.Object, lang.Object, builtin=True)


def load_set_theory(lang):
    for symbol in builtins.get_set_predicates():
        lang.predicate(symbol, lang.Real, lang.Real, builtin=True)


def load_special_theory(lang):
    for symbol in builtins.get_special_binary_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, lang.Real, builtin=True)
        lang.register_operator_handler(symbol, lang.Real, lang.Real, fun)

    for symbol in builtins.get_special_unary_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, builtin=True)
        lang.register_unary_operator_handler(symbol, lang.Real, fun)


def load_random_theory(lang):
    for symbol in builtins.get_random_binary_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, lang.Real, builtin=True)
        lang.register_operator_handler(symbol, lang.Real, lang.Real, fun)

    for symbol in builtins.get_random_unary_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, builtin=True)
        lang.register_unary_operator_handler(symbol, lang.Real, fun)
