import tarski.model
from tarski import fstrips as fs
from tarski.fstrips import contingent, FSFactory
from tarski.syntax import *

from tests.common.grid_navigation import generate_single_agent_language


def create_small_task():
    nav = generate_single_agent_language()
    fsf = FSFactory(nav)
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

    P.action('move_up', [], Tautology(nav), [fsf.functional_effect(y(), y() + 1)])
    P.action('move_down', [], Tautology(nav), [fsf.functional_effect(y(), y() - 1)])
    P.action('move_left', [], Tautology(nav), [fsf.functional_effect(x(), x() - 1)])
    P.action('move_right', [], Tautology(nav), [fsf.functional_effect(x(), x() + 1)])

    P.sensor('sense_wall_up', [], Tautology(nav), y() == 4)
    P.sensor('sense_wall_down', [], Tautology(nav), y() == -4)
    P.sensor('sense_wall_left', [], Tautology(nav), x() == -4)
    P.sensor('sense_wall_right', [], Tautology(nav), x() == 4)

    return P
