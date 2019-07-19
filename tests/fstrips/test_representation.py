from tarski.syntax import exists
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


