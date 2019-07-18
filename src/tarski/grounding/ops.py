
from ..syntax.util import get_symbols
from ..fstrips.ops import collect_affected_symbols


def classify_symbols(problem, include_builtin=False):
    """ Return a tuple (F, S) of two disjoint sets containing, all fluent (F) and static (S) function and predicate
    symbols in the problem. A symbol is considered fluent if the effect of some action affects its denotation, and
    static otherwise.
    """
    fluents = collect_affected_symbols(problem)
    allsymbols = set(get_symbols(problem.language, include_builtin=include_builtin))
    statics = allsymbols.difference(fluents)
    return fluents, statics
