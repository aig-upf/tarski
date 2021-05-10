
from tarski.utils import resources


def test_timer_class():
    # Some very exciting algorithms to exercise the timing functionality
    x = 0
    with resources.timing("\tHello world"):
        x += 1
    assert x == 1
    with resources.timing("\tHello world", newline=True):
        x += 1
    assert x == 2
