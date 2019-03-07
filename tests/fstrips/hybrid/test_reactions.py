from tarski import fstrips as fs
from tarski.fstrips import hybrid
from tarski.syntax import *

import tests.common.numeric as numeric


def test_reaction_creation():
    from tarski.syntax.arithmetic import summation
    lang = numeric.generate_billiards_instance()
    m, F, a, v, p = [lang.get_function(n) for n in ['m', 'F', 'a', 'v', 'p']]

    b = Variable('b', lang.get_sort('ball'))
    d = Variable('d', lang.get_sort('dimension'))
    ftype = Variable('ftype', lang.get_sort('force'))

    constraint = hybrid.Reaction(lang, 'principle_of_superposition',
                                 [b, d, ftype], top,
                                 fs.FunctionalEffect(a(d, b), summation(ftype, F(ftype, d, b)) / m(b)))
    # print(constraint)
    assert isinstance(constraint, hybrid.Reaction)
