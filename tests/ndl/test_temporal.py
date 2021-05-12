import pytest

import tarski as tsk
from tarski.model import Model
from tarski.evaluators.simple import evaluate
from tarski.syntax import forall, equiv, neg, land, exists
from tarski.theories import Theory
from tarski.ndl import temporal
from tarski.ndl.temporal import TimedEffect, SetLiteralEffect

def test_resource_lock_creation():

    with pytest.raises(temporal.NDLSyntaxError):
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
        parameters = [],
        precondition=position(rov1, p0),
        requirements=[TimedEffect(0.0, req_1), TimedEffect(0.0, req_2)],
        timed_effects=[TimedEffect(21.0, SetLiteralEffect(observed(p0), True))],
        untimed_effects=[]
    )

    assert len(act.locks) == 1
    assert len(act.levels) == 1

@pytest.mark.skip(reason="Instance class and interface still work in progress")
def test_instance_creation():

    L = tsk.language("mylang", theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    int_t = L.Integer
    obj_t = L.Object

    platform_t = L.sort('platform')
    rov1 = L.constant('rov1', platform_t)
    direction = L.function('direction', platform_t, int_t)

    sensor_sort = L.sort('sensor')
    camera, range, bearing = [L.constant(name, sensor_sort) for name in ('camera', 'range', 'bearing')]
    engaged = L.function('engaged', sensor_sort, int_t)

    region_t = L.sort('region')
    p0 = L.constant('p0', region_t)
    p1 = L.constant('p1', region_t)
    p2 = L.constant('p2', region_t)

    t0 = L.constant('t0', obj_t)
    t1 = L.constant('t1', obj_t)
    t2 = L.constant('t2', obj_t)
    #t0, t1, t2 = [L.constant('t{}'.format(i), obj_t)
    #                for i in range(3)]

    position = L.predicate('position', obj_t, region_t)
    observed = L.predicate('observed', obj_t)
    estimated_range = L.predicate('estimated_range', obj_t)
    estimated_bearing = L.predicate('estimated_bearing', obj_t)

    req_1 = temporal.ResourceLock(**{
        "ts": 0.0, "td": 10.0, "r": engaged(camera)
    })

    req_2 = temporal.ResourceLock(**{
        "ts": 0.0, "td": 10.0, "r": engaged(range)
    })

    req_3 = temporal.ResourceLock(**{
        "ts": 0.0, "td": 10.0, "r": engaged(bearing)
    })

    req_4 = temporal.ResourceLevel(**{
        "ts": 0.0, "td": 20.0, "r": direction(rov1), "n": L.constant(0, int_t)
    })

    a1 = temporal.Action(
        name='localize_t0',
        parameters=[],
        precondition=position(rov1, p0),
        requirements=[
            TimedEffect(0.0, req_2),
            TimedEffect(0.0, req_3)],
        timed_effects=[
            TimedEffect(15.0, estimated_range(t0)),
            TimedEffect(20.0, estimated_bearing(t0))],
        untimed_effects=[]
    )

    a2 = temporal.Action(
        name='observed_t0',
        parameters=[],
        precondition=land(position(rov1, p0), estimated_range(t0), estimated_bearing(t0)),
        requirements=[
            TimedEffect(0.0, req_1),
            TimedEffect(0.0, req_2)],
        timed_effects=[
            TimedEffect(21.0, observed(t0))],
        untimed_effects=[]
    )

    initial = Model(L)
    initial.add(position, rov1, p0)
    initial.evaluator = evaluate

    inst = temporal.Instance(
        L=L,
        X=[position(rov1, p0),
           estimated_range(t0), estimated_bearing(t0), observed(t0),
           estimated_range(t1), estimated_bearing(t1), observed(t1),
           estimated_range(t2), estimated_bearing(t2), observed(t2)],
        I=initial,
        A=[a1, a2],
        G=observed(t0)
    )

    assert len(inst.R) == 3