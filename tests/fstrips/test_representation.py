from tarski.syntax import exists, land
from tests.common.blocksworld import generate_small_fstrips_bw_language
from tarski.fstrips import representation as rep


def test_basic_representation_queries():
    lang = generate_small_fstrips_bw_language(nblocks=5)
    clear, loc, b1, b2, b3 = lang.get('clear', 'loc', 'b1', 'b2', 'b3')
    x = lang.variable('x', lang.ns.block)

    assert rep.is_function_free(b1)
    assert rep.is_function_free(clear(b1))
    assert rep.is_function_free((clear(b1) & clear(b2)) | clear(b3))
    assert rep.is_function_free(exists(x, clear(x)))
    assert not rep.is_function_free(loc(b1) == b2)

    assert rep.is_conjunction_of_literals(clear(b1))
    assert rep.is_conjunction_of_literals(~clear(b1))
    assert rep.is_conjunction_of_literals(~~clear(b1))

    assert rep.is_conjunction_of_literals(clear(b1) & clear(b2))
    assert rep.is_conjunction_of_literals(clear(b1) & ~clear(b2))
    assert rep.is_conjunction_of_literals(clear(b1) & ~~clear(b2))

    assert rep.is_conjunction_of_literals(loc(b1) == b2)
    assert rep.is_conjunction_of_literals(loc(b1) != b2)
    assert rep.is_conjunction_of_literals(~(loc(b1) == b2))

    assert not rep.is_conjunction_of_literals(~(clear(b1) & clear(b2)))
    assert not rep.is_conjunction_of_literals((clear(b1) & clear(b2)) | clear(b3))
    assert not rep.is_conjunction_of_literals(exists(x, clear(x)))


def test_literal_collection():
    lang = generate_small_fstrips_bw_language(nblocks=5)
    clear, loc, b1, b2, b3 = lang.get('clear', 'loc', 'b1', 'b2', 'b3')
    x = lang.variable('x', lang.ns.block)

    assert rep.collect_literals_from_conjunction(clear(b1)) == {(clear(b1), True)}
    assert rep.collect_literals_from_conjunction(~clear(b1)) == {(clear(b1), False)}
    assert len(rep.collect_literals_from_conjunction(clear(b1) & ~clear(b2))) == 2
    assert len(rep.collect_literals_from_conjunction(land(clear(b1), clear(b2), clear(b3)))) == 3

    assert len(rep.collect_literals_from_conjunction(clear(x) & clear(b1) & clear(x))) == 2

    # These ones are not conjunctions of literals, so should return None
    assert rep.collect_literals_from_conjunction(~(clear(b1) & clear(b2))) is None
    assert rep.collect_literals_from_conjunction((clear(b1) & clear(b2)) | clear(b3)) is None
    assert rep.collect_literals_from_conjunction(exists(x, clear(x))) is None

    # ATM we don't want to deal with the complexity of nested negation, so we expect the method to return None for
    # "not not clear(b2)"
    assert rep.collect_literals_from_conjunction(clear(b1) & ~~clear(b2)) is None



