""" Management of the theories (e.g. equality, etc.) associated to the FO languages """

from enum import Enum
from typing import Union, List, Optional

from ..syntax import builtins, BuiltinFunctionSymbol, BuiltinPredicateSymbol, Term
from ..syntax.sorts import attach_arithmetic_sorts, attach_bool_sort, Set
from ..fol import FirstOrderLanguage
from .. import errors as err


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
        return

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

    if th in (Theory.SETS, ):
        load_theory(lang, Theory.EQUALITY)
        load_theory(lang, Theory.ARITHMETIC)

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
            fun.sort_inference = _infer_arithmetic_sort

    for symbol in builtins.get_matrix_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, lang.Real, builtin=True)
        lang.register_operator_handler(symbol, lang.Real, lang.Real, fun)

    for symbol in builtins.get_arithmetic_unary_functions():
        fun = lang.function(symbol, lang.Real, lang.Real, builtin=True)
        lang.register_unary_operator_handler(symbol, lang.Real, fun)
        fun.sort_inference = _infer_arithmetic_sort

    # MRJ: ite function is now part of the Arithmetic theory
    lang.function(BuiltinFunctionSymbol.ITE, lang.Object, lang.Object, lang.Object, builtin=True)


def load_set_theory(lang):
    set_of_object = Set(lang, lang.Object)
    set_of_int = Set(lang, lang.Integer)

    lang.predicate(BuiltinPredicateSymbol.SET_IS_EMPTY, set_of_object, builtin=True)

    fun = lang.predicate(BuiltinPredicateSymbol.SET_IN, lang.Object, set_of_object, builtin=True, overload=True)
    lang.register_operator_handler(BuiltinPredicateSymbol.SET_IN, lang.Object, set_of_object, fun)

    fun = lang.predicate(BuiltinPredicateSymbol.SET_IN, lang.Integer, set_of_int, builtin=True, overload=True)
    lang.register_operator_handler(BuiltinPredicateSymbol.SET_IN, lang.Integer, set_of_int, fun)

    fun = lang.function(BuiltinFunctionSymbol.SET_UNION, set_of_object, set_of_object, set_of_object, builtin=True)
    fun.sort_inference = _infer_set_sort

    fun = lang.function(BuiltinFunctionSymbol.SET_INTERSECTION, set_of_object, set_of_object, set_of_object, builtin=True)
    fun.sort_inference = _infer_set_sort

    fun = lang.function(BuiltinFunctionSymbol.SET_DIFFERENCE, set_of_object, set_of_object, set_of_object, builtin=True)
    fun.sort_inference = _infer_set_sort

    fun = lang.function(BuiltinFunctionSymbol.SET_CARDINALITY, set_of_object, lang.Natural, builtin=True)


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


def _infer_arithmetic_sort(symbol, subterms):
    from ..syntax.ops import cast_to_closest_common_numeric_ancestor

    # For builtin arithmetic functions, we want the sort of compound terms to be that of the closest common
    # ancestor sort
    if len(subterms) == 2:
        subterms = cast_to_closest_common_numeric_ancestor(symbol.language, *subterms)
        sort = subterms[0].sort
    else:
        sort = symbol.codomain

    # Let's check all subterms are of some sort consistent with the declared sort of the function,
    # and if they are Python literals, cast them to appropriate Constant objects
    processed = []
    for st, s in zip(subterms, symbol.domain):
        if not isinstance(st, Term):
            # Treat the subterm as a Python literal and cast it to a Constant
            processed.append(s.cast(st))
        else:
            # Just check the type matches with the type of the function
            if not symbol.language.is_subtype(st.sort, s):
                raise err.SortMismatch(symbol, st.sort, s)
            processed.append(st)

    return processed, sort


def _infer_set_sort(symbol, subterms):
    # For set operations, we don't allow at the moment mixing sets of different sorts,
    # even if there is some inheritance relation between the set sorts.
    st1, st2 = subterms

    if st1.sort != st2.sort:
        raise ValueError(f'Sort operations can only be applied to sets of the exact same type')

    if not isinstance(st1.sort, Set):
        raise ValueError(f'Attempted to apply set operation to non-set types: {st1}, {st2}')

    return subterms, st1.sort
