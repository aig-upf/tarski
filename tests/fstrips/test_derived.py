import tarski.benchmarks.blocksworld
from tarski import fstrips as fs
from tarski.syntax import *

from ..common import blocksworld


def test_derived_creation():
    lang = tarski.benchmarks.blocksworld.generate_fstrips_bw_language()

    b1 = lang.variable('b1', 'block')
    b2 = lang.variable('b2', 'block')
    b3 = lang.variable('b3', 'block')

    on = lang.predicate('on', 'block', 'block')

    # Transitive closure of "on" predicate.
    above = lang.predicate('above', 'block', 'block')

    fs.Derived(lang, name='above', parameters=[b1, b2],
               formula=lor(on(b1, b2),
                           exists(b3,
                                  land(on(b1, b3),
                                       above(b3, b2)))))
