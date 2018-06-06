from .terms import Term, Constant


def cast_to_closest_common_ancestor(lhs, rhs):
    # TODO - THIS CLEARLY DOES NOT COVER ALL POSSIBLE CASES (E.G. "1.0 + 2", ETC.)
    # TODO - WE NEED TO FINISH AND UNIT-TEST THIS. DOCUMENT IT AS WELL.
    assert isinstance(lhs, Term)
    if isinstance(rhs, Term):
        pass
    else:
        rhs = Constant(lhs.sort.cast(rhs), lhs.sort)

    return lhs, rhs


def infer_numeric_sort(value, language):
    # Note that this will only work in Python 3, which is fine.
    if isinstance(value, int):
        return language.Integer
    elif isinstance(value, float):
        return language.Real
    return None


def cast_to_number(rhs):
    assert isinstance(rhs, Constant)
    return rhs.symbol
