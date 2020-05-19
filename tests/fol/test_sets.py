from tarski import Constant
from tarski.benchmarks.storytellers import generate_problem
from tarski.evaluators.simple import evaluate
from tarski.fstrips import fstrips
from tarski.model import Model
from tarski.syntax import sorts, CompoundTerm
from tarski.theories.sets import set_union, set_emptyset, set_literal, set_intersection, set_cardinality, \
    set_difference, set_in


def _get_set_lang():
    lang = fstrips.language(theories=["sets", "arithmetic"])
    return lang, lang.constant("o1", "object"), lang.constant("o2", "object"), lang.constant("o3", "object")


def test_set_theory_syntax():
    lang, o1, o2, o3 = _get_set_lang()
    model = Model(lang, evaluator=evaluate)

    set_t = sorts.Set(lang, lang.Object)

    # Test the set constructors
    s1 = set_emptyset(set_t)
    assert isinstance(s1, Constant)

    s2 = set_literal(set_t, o1)
    assert isinstance(s2, Constant)

    s3 = set_literal(set_t, o1, o2)
    assert isinstance(s2, Constant)

    su = set_union(s1, s2)
    assert isinstance(su, CompoundTerm)

    si = set_intersection(su, s3)
    assert isinstance(su, CompoundTerm)

    si_m = model[si]
    assert set_t.literal(si_m) == si_m.symbol
    assert set_t.literal(si_m) == {'o1'}

    nelems = set_cardinality(su)
    assert isinstance(nelems, CompoundTerm) and nelems.sort == lang.Natural

    assert lang.Natural.literal(model[nelems]) == 1

    # Let's test some sets of integers
    int_set_t = sorts.Set(lang, lang.Integer)

    c1, c2, c3 = [lang.constant(x, lang.Integer) for x in (1, 2, 3)]
    s123 = set_literal(int_set_t, c1, c2, c3)

    assert isinstance(s123, Constant) and s123.sort == int_set_t

    s12 = set_literal(int_set_t, c1, c2)
    sd = set_difference(s123, s12)
    should_be_true = (sd == set_literal(int_set_t, c3))

    assert model[should_be_true] is True

    e = set_in(c3, s123)
    assert model[e] is True
    assert model[set_in(c3, s12)] is False


def test_storytellers_domain():
    prob = generate_problem(nstorytellers=3, naudiences=5, nstories=10)
    assert prob

