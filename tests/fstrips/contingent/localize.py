import tarski.model
from tarski import fstrips as fs
from tarski.fstrips import contingent
from tarski.syntax import *

from tests.common.grid_navigation import generate_single_agent_language


def create_small_task():
    nav = generate_single_agent_language()
    M0 = tarski.model.create(nav)
    M1 = tarski.model.create(nav)

    x = nav.get_function('x')
    y = nav.get_function('y')

    M0.setx(x(), 0)
    M0.setx(y(), 0)

    M1.setx(x(), 2)
    M1.setx(y(), -2)

    constraint = (-4 <= x()) & (x() <= 4) & (-4 <= y()) & (y() <= 4)

    G = land(x() == 3, y() == 3)

    P = contingent.Problem()
    P.name = "localize-4-4"
    P.domain_name = "navigation"
    P.language = nav
    P.init = [M0, M1]
    P.goal = G
    P.constraints += [constraint]

    lang = P.language

    P.action('move_up', [], Tautology(lang), [fs.FunctionalEffect(y(), y() + 1)])
    P.action('move_down', [], Tautology(lang), [fs.FunctionalEffect(y(), y() - 1)])
    P.action('move_left', [], Tautology(lang), [fs.FunctionalEffect(x(), x() - 1)])
    P.action('move_right', [], Tautology(lang), [fs.FunctionalEffect(x(), x() + 1)])

    P.sensor('sense_wall_up', [], Tautology(lang), y() == 4)
    P.sensor('sense_wall_down', [], Tautology(lang), y() == -4)
    P.sensor('sense_wall_left', [], Tautology(lang), x() == -4)
    P.sensor('sense_wall_right', [], Tautology(lang), x() == 4)

    return P
