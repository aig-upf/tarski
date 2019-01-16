import pytest

from tarski.fstrips import contingent
from tarski.syntax import *

from tests.common import grid_navigation
from tests.fstrips.contingent import localize


def test_sensor_creation():
    nav = grid_navigation.generate_single_agent_language()
    y = nav.get_function('y')
    _ = contingent.Sensor(nav, 'sense_wall_up', [], Tautology(), y() == 4)


def test_sensor_duplicate():
    task = localize.create_small_task()
    y = task.language.get_function('y')
    with pytest.raises(contingent.errors.DuplicateSensorDefinition):
        _ = task.sensor('sense_wall_up', [], Tautology(), y() == 4)
