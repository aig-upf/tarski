
import tarski as tsk


def test_builtin_constants():
    lang = tsk.language()
    ints = lang.Integer
    two = lang.constant(2, ints)
    assert isinstance(two, tsk.Constant), "two should be the constant 2, not the integer value 2"


def test_arithmetic_terms():
    lang = tsk.language()
    ints = lang.Integer
    two, three = lang.constant(2, ints), lang.constant(3, ints)
    sum_ = two + three
    assert isinstance(sum_, tsk.Term), "sum_ should be the term +(Const(2), Const(3)), not the integer value 5"
