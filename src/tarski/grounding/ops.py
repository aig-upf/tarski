
from ..syntax.util import get_symbols
from ..fstrips.ops import collect_affected_symbols


def approximate_symbol_fluency(problem, include_builtin=False):
    """ Sort out all predicate and function symbols of a given problem into static and fluent symbols.

    Fluent symbols are those whose denotation might (in principle) be affected by the effect of some action schema;
    the rest are static symbols. This methods works on a purely syntactic basis, and does not take into account any
    reachability information, nor whether the action schemas can be detected as unapplicable at preprocessing. This
    for instance means that an action a(x) with precondition False and atomic add effect "p(x)" will be taken as
    evidence that predicate symbol "p" is fluent. It also means that "fluency" is only considered at the symbol
    level (i.e. "p" is either fluent or static), not at the state variable level (where e.g. p(a) could be seen as
    static, and p(b) as fluent).

    The results of this method overapproaximate the set of symbol fluents (i.e. false positives are possible, false
    negatives are not).

    This can be used as a basis for a finer-grained analysis that can be performed e.g. with the ASP-based reachability
    grounder.
    """
    fluents = collect_affected_symbols(problem)
    allsymbols = set(get_symbols(problem.language, include_builtin=include_builtin))
    statics = allsymbols.difference(fluents)
    return fluents, statics
