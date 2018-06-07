from tarski import fstrips as fs
from tarski.fstrips import contingent
from tarski.syntax import *

from tests.common import grid_navigation
from tests.fstrips.contingent import localize

def test_sensor_creation():

    nav = grid_navigation.generate_single_agent_language()
    y = nav.get_function('y')
    sensor = contingent.Sensor(nav, 'sense_wall_up', [], Tautology(), y == 4)
