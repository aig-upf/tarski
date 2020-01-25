
import itertools


def get_symbols(lang, type_="all", include_builtin=True, include_total_cost=False):
    """ Return all symbols of the given type (function/predicate), and including or excluding builtins as desired """
    if type_ == "predicate":
        iterate_over = lang.predicates
    elif type_ == "function":
        iterate_over = lang.functions
    else:
        assert type_ == "all"
        iterate_over = itertools.chain(lang.predicates, lang.functions)

    if not include_builtin:
        iterate_over = (x for x in iterate_over if not x.builtin)

    if not include_total_cost:
        iterate_over = (x for x in iterate_over if x.symbol != "total-cost")

    return iterate_over


def termlists_are_equal(terms1, terms2):
    """ Check whether two given lists of terms are (syntactic-wise) equal. """
    return len(terms1) == len(terms2) and all(x.is_syntactically_equal(y) for x, y in zip(terms1, terms2))


def termlist_hash(terms):
    """ Return a ready-to-hash tuple with the hashes of a list of terms. """
    return tuple(x.hash() for x in terms)
