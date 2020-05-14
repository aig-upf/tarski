from tarski.fstrips import fstrips
from tarski.syntax import sorts


def test_set_theory_loading():
    lang = fstrips.language(theories=["sets"])
    set_t = sorts.Set(lang, lang.Object)
    # lang.interval()
