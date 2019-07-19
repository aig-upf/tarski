import pytest

from tarski import FirstOrderLanguage, errors


def test_namespace_accessor():
    lang = FirstOrderLanguage()

    # Let's test different ways of accessing the same things
    assert lang.get_sort('object') == lang.get("object") == lang.ns.object

    on = lang.predicate('on', lang.ns.object)
    assert on == lang.ns.on == lang.get_predicate("on") == lang.get("on")

    loc = lang.function('loc', lang.ns.object, lang.ns.object)
    assert loc == lang.ns.loc == lang.get_function("loc") == lang.get("loc")

    block = lang.sort('block')
    assert block == lang.ns.block == lang.get_sort("block") == lang.get("block")

    assert tuple(lang.get('loc', 'on', 'object')) == (lang.ns.loc, lang.ns.on, lang.ns.object)

    # Make sure all accessors raise the same exception
    with pytest.raises(errors.UndefinedElement):
        _ = lang.ns.foo

    with pytest.raises(errors.UndefinedElement):
        _ = lang.get('foo')


