import pytest

import tarski as tsk
import tarski.errors as err
from tarski.syntax.sorts import parent, ancestors

# TODO NOT SURE WE WANT TO DISALLOW EMPTY TYPES. I HAVE TEMPORARILY DISABLED THE CHECK
# TODO ALSO, WE SHOULDN'T HAVE TO CALL ANY "CHECK WELL FORMED" METHOD EXPLICITLY
# def test_empty_type():
#     lang = tsk.language()
#     s = lang.sort('person')
#     with pytest.raises(tsk.LanguageError):
#         lang.check_well_formed()
#
#     lang.constant('Miquel', s)
#     lang.check_well_formed()


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
    lang = tsk.fstrips.language()
    ints = lang.Integer
    assert ints.contains(1)
    assert ints.contains(0)
    assert ints.contains(-999)
    assert ints.contains(1.0)  # Implicit downcasting
    assert not ints.contains(1.2)


def test_naturals():
    lang = tsk.fstrips.language()
    nats = lang.Natural
    assert nats.contains(999)
    assert not nats.contains(-12)
    assert not nats.contains(1.3)


def test_reals():
    lang = tsk.fstrips.language()
    reals = lang.Real
    assert reals.contains(1000.36)
    assert reals.contains(-17)


def test_integer_subtypes():
    lang = tsk.fstrips.language()
    nats = lang.Natural
    _ = lang.sort("counter", nats)

def test_interval_types_valid():
    lang = tsk.fstrips.language()
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    assert interval_sort.lower_bound == 0
    assert interval_sort.upper_bound == 10
    assert interval_sort.builtin

def test_interval_types_invalid():
    lang = tsk.fstrips.language()
    int_t = lang.Integer
    with pytest.raises(err.SemanticError):
        interval_sort = lang.interval('I', int_t, 10, 0)

def test_interval_types_create_valid_constant():
    lang = tsk.fstrips.language()
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    ii = tsk.syntax.Constant(3, interval_sort)
    assert isinstance(ii, tsk.syntax.Constant)

def test_interval_types_create_invalid_constant():
    lang = tsk.fstrips.language()
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    with pytest.raises(ValueError):
        ii = tsk.syntax.Constant(-2, interval_sort)

def test_interval_types_create_invalid_constant2():
    lang = tsk.fstrips.language()
    int_t = lang.Integer
    interval_sort = lang.interval('I', int_t, 0, 10)
    with pytest.raises(ValueError):
        ii = lang.constant(-2, interval_sort)
