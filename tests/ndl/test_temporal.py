import pytest

import tarski as tsk
import tarski.model
from tarski.syntax import forall, equiv, neg, land, exists
from tarski.theories import Theory
from tarski.ndl import temporal

def test_resource_lock_creation():

    with pytest.raises(temporal.SyntaxError):
        req = temporal.ResourceLock(**{
                "ts": 0.0,
                "td": 1.0,
                "r": None
        })

    L = tsk.language("mylang", theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    sensor_sort = L.sort('sensor')
    camera, range, bearing = [L.constant(name, sensor_sort) for name in ('camera', 'range', 'bearing')]
    int_t = L.Integer
    engaged = L.function('engaged', sensor_sort, int_t)

    req_1 = temporal.ResourceLock(**{
        "ts": 0.0, "td": 10.0, "r": engaged(camera)
    })

    req_2 = temporal.ResourceLock(**{
        "ts": 0.0, "td": 10.0, "r": engaged(range)
    })

    req_3 = temporal.ResourceLock(**{
        "ts": 0.0, "td": 10.0, "r": engaged(bearing)
    })

def test_resource_level_creation():

    L = tsk.language("mylang", theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    platform_t = L.sort('platform')
    rov1 = L.constant('rov1', platform_t)
    int_t = L.Integer
    direction = L.function('direction', platform_t, int_t)

    req_1 = temporal.ResourceLevel(**{
        "ts": 0.0, "td": 20.0, "r": direction(rov1), "n": L.constant(0, int_t)
    })

def test_action_creation():

    L = tsk.language("mylang", theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    int_t = L.Integer

    platform_t = L.sort('platform')
    rov1 = L.constant('rov1', platform_t)
    direction = L.function('direction', platform_t, int_t)

    sensor_sort = L.sort('sensor')
    camera, range, bearing = [L.constant(name, sensor_sort) for name in ('camera', 'range', 'bearing')]
    engaged = L.function('engaged', sensor_sort, int_t)

    region_t = L.sort('region')
    p0 = L.constant('p0', region_t)
    position = L.predicate('position', platform_t, region_t)
    observed = L.predicate('observed', region_t)

    req_1 = temporal.ResourceLock(**{
        "ts": 0.0, "td": 10.0, "r": engaged(camera)
    })

    req_2 = temporal.ResourceLevel(**{
        "ts": 0.0, "td": 20.0, "r": direction(rov1), "n": L.constant(0, int_t)
    })

    act = temporal.Action(
        name='observe_poi',
        precondition=position(rov1, p0),
        requirements=[req_1, req_2],
        effects=[(21.0, observed(p0))]
    )

    assert len(act.locks) == 1
    assert len(act.levels) == 1
    assert len(act.effects) == 1

