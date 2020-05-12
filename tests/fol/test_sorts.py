import pytest

import tarski as tsk
import tarski.benchmarks.blocksworld
import tarski.errors as err
from tarski.benchmarks.counters import generate_fstrips_counters_problem
from tarski.syntax import symref
from tarski.syntax.ops import compute_sort_id_assignment
from tarski.syntax.sorts import parent, ancestors, compute_signature_bindings, compute_direct_sort_map
from tarski.theories import Theory


def test_object_type():
    lang = tsk.fstrips.language()
    lang.get_sort("object")


def test_type_retrieval():
    lang = tsk.fstrips.language()
    s = lang.sort("foobar")
    assert s == lang.get_sort("foobar")


def test_nonexisting_type():
    lang = tsk.fstrips.language()
    with pytest.raises(err.UndefinedSort):
        lang.get_sort('foobar')


def test_duplicate_type():
    lang = tsk.fstrips.language()
    lang.sort('person')

    # Adding two sorts with the same name raises an error
    with pytest.raises(err.LanguageError):
        lang.sort('person')


def test_parent_types():
    lang, human, animal, being = get_children_parent_types()

    assert parent(human) == animal
    assert parent(animal) == being
    assert parent(being) == lang.Object
    assert parent(lang.Object) is None

    assert len(ancestors(human)) == 3  # i.e. including the top "object" sort
    assert being in ancestors(human)
    assert lang.Object in ancestors(human)

    # Adding two different parents to the same sort raises an error
    with pytest.raises(err.LanguageError):
        lang.set_parent(being, lang.Object)


def test_is_subtype_of():
    lang, human, animal, being = get_children_parent_types()

    assert lang.is_strict_subtype(human, lang.get_sort('object'))
    assert lang.is_strict_subtype(human, being)
    assert lang.is_strict_subtype(human, animal)
    assert lang.is_subtype(human, animal)
    assert lang.is_subtype(animal, human) is False


def get_children_parent_types():
    lang = tsk.fstrips.language()
    being = lang.sort('being')
    animal = lang.sort('animal', being)
    human = lang.sort('human', animal)
    return lang, human, animal, being


def test_ints():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    ints = lang.Integer
    assert ints.contains(1)
    assert ints.contains(0)
    assert ints.contains(-999)
    assert ints.contains(1.0)  # Implicit downcasting
    assert not ints.contains(1.2)


def test_naturals():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    nats = lang.Natural
    assert nats.contains(999)
    assert not nats.contains(-12)
    assert not nats.contains(1.3)


def test_reals():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    reals = lang.Real
    assert reals.contains(1000.36)
    assert reals.contains(-17)


def test_integer_subtypes():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    nats = lang.Natural
    _ = lang.sort("counter", nats)


def test_interval_types_valid():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    assert interval_sort.lower_bound == 0
    assert interval_sort.upper_bound == 10
    assert not interval_sort.builtin


def test_interval_types_invalid():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    int_t = lang.Integer
    with pytest.raises(err.SemanticError):
        _ = lang.interval('I', int_t, 10, 0)


def test_interval_types_create_valid_constant():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    ii = tsk.syntax.Constant(3, interval_sort)
    assert isinstance(ii, tsk.syntax.Constant)


def test_interval_types_create_invalid_constant():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    with pytest.raises(ValueError):
        _ = tsk.syntax.Constant(-2, interval_sort)


def test_interval_types_create_invalid_constant2():
    lang = tsk.fstrips.language(theories=[Theory.ARITHMETIC])
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    with pytest.raises(ValueError):
        _ = lang.constant(-2, interval_sort)


def test_signature_bindings():
    bw = tarski.benchmarks.blocksworld.generate_fstrips_bw_language(nblocks=2)
    bindings = list(compute_signature_bindings([bw.get('block'), bw.get('place')]))
    assert len(bindings) == 6


def test_sort_id_assignment():
    lang = tsk.fstrips.language(theories=[])

    # Create some sort hierarchy
    lang.sort("s1", "object")
    lang.sort("s2", "object")
    lang.sort("t1", "s2")
    lang.sort("t2", "s2")

    # Create some objects in a sequence that alternates types
    lang.constant("a1", "s1")
    lang.constant("o1", "object")
    lang.constant("a2", "s1")
    lang.constant("b3", "t1")
    lang.constant("a3", "s1")
    lang.constant("o2", "object")
    lang.constant("b1", "s2")
    lang.constant("b2", "t1")
    lang.constant("b4", "s2")

    sortmap = compute_direct_sort_map(lang)
    cards = {s.name: len(objs) for s, objs in sortmap.items()}
    assert cards == {'object': 2, 's1': 3, 's2': 2, 't1': 2, 't2': 0}
    bounds, ids = compute_sort_id_assignment(lang)

    assert bounds[lang.Object] == (0, 9)
    assert {ids[symref(lang.get('o1'))], ids[symref(lang.get('o2'))]} == {7, 8}
    # Note that the following relies on dict (the dict of sort parents) iterating over its elements in insertion sort.
    # see https://stackoverflow.com/a/39980744
    assert {ids[symref(lang.get('a1'))], ids[symref(lang.get('a2'))], ids[symref(lang.get('a3'))]} == {0, 1, 2}


def test_sort_id_assignment_on_lang_with_intervals():
    problem = generate_fstrips_counters_problem(ncounters=6)
    lang = problem.language

    sortmap = compute_direct_sort_map(lang)
    cards = {s.name: len(objs) for s, objs in sortmap.items()}
    assert cards == {'object': 0, 'counter': 6, 'val': 0}  # Make sure 'object' doesn't include integer constants
    bounds, ids = compute_sort_id_assignment(lang)

    assert bounds[lang.Object] == bounds[lang.get('counter')] == (0, 6)


def test_sort_domain_retrieval():
    problem = generate_fstrips_counters_problem(ncounters=6)
    lang = problem.language

    assert len(list(lang.get("counter").domain())) == 6
    assert len(list(lang.get("val").domain())) == 13, "Val must range from 0 to 12, both included"

    with pytest.raises(err.TarskiError):
        lang.Integer.domain()  # Domain too large to iterate over it
