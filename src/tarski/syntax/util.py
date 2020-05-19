
import itertools

from ..errors import LanguageMismatch, SortMismatch, ArityMismatch


def get_symbols(lang, type_="all", include_builtin=True, include_total_cost=False):
    """ Return all symbols of the given type (function/predicate), and including or excluding builtins as desired """
    if type_ == "predicate":
        iterate_over = lang.predicates
    elif type_ == "function":
        iterate_over = lang.functions
    else:
        assert type_ == "all"
        iterate_over = itertools.chain(lang.predicates, lang.functions)

    iterate_over = _chain_possibly_nested_iterator(iterate_over)

    if not include_builtin:
        iterate_over = (x for x in iterate_over if not x.builtin)

    if not include_total_cost:
        iterate_over = (x for x in iterate_over if x.symbol != "total-cost")

    return iterate_over


def _chain_possibly_nested_iterator(iterator):
    for x in iterator:
        if isinstance(x, list):
            for y in x:
                yield y
        else:
            yield x


def termlists_are_equal(terms1, terms2):
    """ Check whether two given lists of terms are (syntactic-wise) equal. """
    return len(terms1) == len(terms2) and all(x.is_syntactically_equal(y) for x, y in zip(terms1, terms2))


def termlist_hash(terms):
    """ Return a ready-to-hash tuple with the hashes of a list of terms. """
    return tuple(x.hash() for x in terms)


def validate_compound_expression(head, subterms):
    # Let's check all subterms are of some sort consistent with the declared sort of the function,
    # and if they are Python literals, cast them to appropriate Constant objects
    from ..syntax import Term

    if len(subterms) != head.arity:
        raise ArityMismatch(head, subterms)

    lang = head.language

    # We'll return None for predicates, as they of course have fixed codomain type (Boolean)
    expression_sort = head.codomain if hasattr(head, "codomain") else None

    if hasattr(head, "sort_inference"):
        # A bit of a hack: if the function or predicate has an especial method "sort_inference", we delegate
        # the casting and type-checking of arguments to this method
        processed, expression_sort = head.sort_inference(head, subterms)

    else:
        processed = []
        for st, s in zip(subterms, head.domain):
            if not isinstance(st, Term):
                # Treat the subterm as a Python literal and cast it to a Constant
                processed.append(s.cast(st))
            else:
                # Check languages match
                if st.language != lang:
                    raise LanguageMismatch(st, st.language, lang)

                if not lang.is_subtype(st.sort, s):
                    raise SortMismatch(st, st.sort, s)
                processed.append(st)

    return tuple(processed), expression_sort
