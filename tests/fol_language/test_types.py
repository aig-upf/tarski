import pytest
import tarski as tsk
import tarski.errors as err

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
    lang = tsk.language()
    lang.get_sort("object")


def test_type_retrieval():
    lang = tsk.language()
    s = lang.sort("foobar")
    assert s == lang.get_sort("foobar")


def test_nonexisting_type():
    lang = tsk.language()
    with pytest.raises(err.UndefinedSort):
        lang.get_sort('foobar')


def test_duplicate_type():
    lang = tsk.language()
    lang.sort('person')

    # Adding two sorts with the same name should raise some type of error
    with pytest.raises(err.LanguageError):
        lang.sort('person')


def test_parent_types():
    lang, human, animal, being = get_children_parent_types()

    assert len(tsk.parents(human)) == 2  # i.e. including the top "object" sort
    assert animal in tsk.parents(human)


def test_is_subtype_of():
    lang, human, animal, being = get_children_parent_types()

    assert lang.is_strict_subtype(human, lang.get_sort('object'))
    assert lang.is_strict_subtype(human, being)
    assert lang.is_strict_subtype(human, animal)
    assert lang.is_subtype(human, animal)
    assert lang.is_subtype(animal, human) is False


def get_children_parent_types():
    lang = tsk.language()
    being = lang.sort('being')
    animal = lang.sort('animal', [being])
    human = lang.sort('human', [animal])
    return lang, human, animal, being
