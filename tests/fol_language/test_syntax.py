import pytest
import tarski as tsk


def test_builtin_constants():
    lang = tsk.language()
    ints = lang.Integer
    two = lang.constant(2, ints)
    assert isinstance(two, tsk.Constant), "two should be the constant 2, not the integer value 2"


def test_arithmetic_terms_fails_without_import():
    lang = tsk.language()
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    # MRJ: Test should be failing, but it doesn't ??? Who's modifying the class objects?
    with pytest.raises(TypeError):
        # sum_ = two + three should raise TypeError as the arithmetic module has
        # not been loaded
        sum_ = two + three


def test_arithmetic_terms_does_not_fail_with_load_module():
    lang = tsk.language()
    lang.load_module('arithmetic')
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    sum_ = two + three
    assert isinstance(sum_, tsk.Term), "sum_ should be the term +(Const(2), Const(3)), not the integer value 5"

def test_load_arithmetic_module_fails_when_language_frozen() :
    import tarski.errors as err
    lang = tsk.language()
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)

    with pytest.raises(err.LanguageError) :
        # load_module() should raise LanguageError as we have created two constants
        lang.load_module('arithmetic')
        sum_ = two + three
