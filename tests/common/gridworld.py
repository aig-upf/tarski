
from tarski.fstrips import create_fstrips_problem, language
from tarski.theories import Theory
from tarski.syntax import Tautology, land


def generate_small_gridworld():
    lang = language(theories=[Theory.EQUALITY, Theory.ARITHMETIC])
    problem = create_fstrips_problem(domain_name='grid-circles',
                                     problem_name='10x10',
                                     language=lang)

    coord_t = lang.interval('coordinate', lang.Integer, 1, 10)
    xpos = lang.function('X', coord_t)
    ypos = lang.function('Y', coord_t)

    problem.action(name='move-up', parameters=[],
                   precondition=Tautology(),
                   # effects=[fs.FunctionalEffect(ypos(), ypos() + 1)])
                   effects=[ypos() << ypos() + 1])

    problem.init.set(xpos(), 1)
    problem.init.set(ypos(), 10)

    problem.goal = land(xpos() == 2, ypos() == 3)

    return problem
