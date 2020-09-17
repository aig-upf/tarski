from tarski import fstrips as fs
from tarski.fstrips import hybrid
from tarski.syntax import *
from tarski.syntax.arithmetic import summation

from tests.common.numeric import generate_numeric_instance, generate_billiards_instance


def create_particles_world():
    task = hybrid.Problem()
    particles = generate_numeric_instance()
    task.language = generate_numeric_instance()

    x, y, f = [particles.get_function(name) for name in ['x', 'y', 'f']]
    _ = [particles.get_constant(name) for name in ['p1', 'p2', 'p3', 'p4']]

    p_var = Variable('p', task.language.get_sort('particle'))
    _ = task.differential_constraint('test1', [p_var], top, x(p_var), f(p_var) * 2.0)
    cond = (x(p_var) > 0.0) & (x(p_var) < 0.5)
    _ = task.differential_constraint('test2', [p_var], cond, y(p_var), f(p_var) * 0.5)

    return task


def create_billiards_world():
    task = hybrid.Problem()
    lang = generate_billiards_instance()
    task.language = lang
    m, F, a, v, p = [lang.get_function(n) for n in ['m', 'F', 'a', 'v', 'p']]

    b = Variable('b', lang.get_sort('ball'))
    d = Variable('d', lang.get_sort('dimension'))
    ftype = Variable('ftype', lang.get_sort('force'))

    _ = task.reaction('principle_of_superposition',
                      [b, d], top, fs.FunctionalEffect(a(d, b), summation(ftype, F(ftype, d, b)) / m(b)))

    return task
