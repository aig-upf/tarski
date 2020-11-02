import os
import tempfile

import tarski
from tarski.theories import Theory
from tarski.syntax import *
from tarski.io import rddl
from tarski.syntax.arithmetic import *
from tarski.syntax.arithmetic.special import *
from tarski.syntax.arithmetic.random import *
from tarski.rddl import Task


def test_simple_rddl_model():
    lang = tarski.language('lqr_nav_1d', [Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL])
    the_task = Task(lang, 'lqr_nav_1d', 'instance_001')

    the_task.requirements = [rddl.Requirements.CONTINUOUS, rddl.Requirements.REWARD_DET]

    the_task.parameters.discount = 1.0
    the_task.parameters.horizon = 10
    the_task.parameters.max_nondef_actions = 1

    # variables
    x = lang.function('x', lang.Real)
    v = lang.function('v', lang.Real)
    u = lang.function('u', lang.Real)
    t = lang.function('t', lang.Real)

    # non fluents
    dt = lang.function('dt', lang.Real)
    gx = lang.function('gx', lang.Real)

    # cpfs
    the_task.add_cpfs(t(), t() + dt())
    the_task.add_cpfs(v(), v() + dt() * u())
    the_task.add_cpfs(x(), x() + dt() * v())

    # constraints
    the_task.add_constraint((u() >= -1.0) & (u() <= 1.0), rddl.ConstraintType.ACTION)
    the_task.add_constraint((v() >= -5.0) & (v() <= 5.0), rddl.ConstraintType.STATE)
    the_task.add_constraint((x() >= -100.0) & (x() <= 100.0), rddl.ConstraintType.STATE)

    # cost function
    Q = (x() - gx()) * (x() - gx())
    # MRJ: RDDL does not support the abs() algebraic construct
    R = ite(abs(x() - gx()) > 0.0, u() * u() * 0.01, lang.constant(0.0, lang.Real))
    # R = u() * u() * 0.01
    the_task.reward = Q + R

    # definitions
    the_task.x0.set(x(), 0.0)
    the_task.x0.set(v(), 0.0)
    the_task.x0.set(u(), 0.0)
    the_task.x0.set(t(), 0.0)
    the_task.x0.set(dt(), 0.5)
    the_task.x0.set(gx(), 20.0)

    # fluent metadata
    the_task.declare_state_fluent(x(), 0.0)
    the_task.declare_state_fluent(t(), 0.0)
    the_task.declare_interm_fluent(v(), 1)
    the_task.declare_action_fluent(u(), 0.0)
    the_task.declare_non_fluent(dt(), 0.0)
    the_task.declare_non_fluent(gx(), 0.0)

    the_writer = rddl.Writer(the_task)
    rddl_filename = os.path.join(tempfile.gettempdir(), 'lqr_nav_1d_001.rddl')
    the_writer.write_model(rddl_filename)
    mr_reader = rddl.Reader(rddl_filename)
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'lqr_nav_1d'
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None


def test_rddl_model_with_random_vars():
    lang = tarski.language('lqg_nav_1d', [Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])
    the_task = Task(lang, 'lqg_nav_1d', 'instance_001')

    the_task.requirements = [rddl.Requirements.CONTINUOUS, rddl.Requirements.REWARD_DET]

    the_task.parameters.discount = 1.0
    the_task.parameters.horizon = 10
    the_task.parameters.max_nondef_actions = 1

    # variables
    x = lang.function('x', lang.Real)
    v = lang.function('v', lang.Real)
    u = lang.function('u', lang.Real)
    t = lang.function('t', lang.Real)

    # non fluents
    dt = lang.function('dt', lang.Real)
    gx = lang.function('gx', lang.Real)
    # Perturbation distribution parameters
    mu_w = lang.function('mu_w', lang.Real)
    sigma_w = lang.function('sigma_w', lang.Real)

    # cpfs
    the_task.add_cpfs(t(), t() + dt())
    the_task.add_cpfs(v(), v() + dt() * u() + normal(mu_w(), sigma_w()))
    the_task.add_cpfs(x(), x() + dt() * v())

    # constraints
    the_task.add_constraint((u() >= -1.0) & (u() <= 1.0), rddl.ConstraintType.ACTION)
    the_task.add_constraint((v() >= -5.0) & (v() <= 5.0), rddl.ConstraintType.STATE)
    the_task.add_constraint((x() >= -100.0) & (x() <= 100.0), rddl.ConstraintType.STATE)

    # cost function
    Q = (x() - gx()) * (x() - gx())
    # MRJ: RDDL does not support the abs() algebraic construct
    R = ite(abs(x() - gx()) > 0.0, u() * u() * 0.01, lang.constant(0.0, lang.Real))
    # R = u() * u() * 0.01
    the_task.reward = Q + R

    # definitions
    the_task.x0.set(x(), 0.0)
    the_task.x0.set(v(), 0.0)
    the_task.x0.set(u(), 0.0)
    the_task.x0.set(t(), 0.0)
    the_task.x0.set(dt(), 0.5)
    the_task.x0.set(gx(), 20.0)
    the_task.x0.set(mu_w(), 0.0)
    the_task.x0.set(sigma_w(), 0.05)

    # fluent metadata
    the_task.declare_state_fluent(x(), 0.0)
    the_task.declare_state_fluent(t(), 0.0)
    the_task.declare_interm_fluent(v(), 1)
    the_task.declare_action_fluent(u(), 0.0)
    the_task.declare_non_fluent(dt(), 0.0)
    the_task.declare_non_fluent(gx(), 0.0)
    the_task.declare_non_fluent(mu_w(), 0.0)
    the_task.declare_non_fluent(sigma_w(), 0.0)

    the_writer = rddl.Writer(the_task)
    rddl_filename = os.path.join(tempfile.gettempdir(), 'lqg_nav_1d_001.rddl')
    the_writer.write_model(rddl_filename)
    mr_reader = rddl.Reader(rddl_filename)
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'lqg_nav_1d'
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None


def test_parametrized_model_with_random_vars():
    lang = tarski.language('lqg_nav_2d_multi_unit', [Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])
    the_task = Task(lang, 'lqg_nav_2d_multi_unit', 'instance_001')

    the_task.requirements = [rddl.Requirements.CONTINUOUS, rddl.Requirements.REWARD_DET]

    the_task.parameters.discount = 1.0
    the_task.parameters.horizon = 10
    the_task.parameters.max_nondef_actions = 1

    vehicle = lang.sort('vehicle', lang.Object)

    # variables
    x = lang.function('x', vehicle, lang.Real)
    y = lang.function('y', vehicle, lang.Real)
    vx = lang.function('vx', vehicle, lang.Real)
    vy = lang.function('vy', vehicle, lang.Real)
    ux = lang.function('ux', vehicle, lang.Real)
    uy = lang.function('uy', vehicle, lang.Real)
    t = lang.function('t', lang.Real)

    # objects
    v001 = lang.constant('v001', vehicle)

    # non fluents
    dt = lang.function('dt', lang.Real)
    gx = lang.function('gx', lang.Real)
    gy = lang.function('gy', lang.Real)
    # Perturbation distribution parameters
    mu_w = lang.function('mu_w', lang.Real)
    sigma_w = lang.function('sigma_w', lang.Real)

    # logical variable
    v = lang.variable('v', vehicle)

    # cpfs
    the_task.add_cpfs(t(), t() + dt())
    the_task.add_cpfs(vx(v), vx(v) + dt() * ux(v) + normal(mu_w(), sigma_w()))
    the_task.add_cpfs(vy(v), vy(v) + dt() * uy(v) + normal(mu_w(), sigma_w()))
    the_task.add_cpfs(x(v), x(v) + dt() * vx(v))
    the_task.add_cpfs(y(v), y(v) + dt() * vy(v))

    # constraints
    the_task.add_constraint(forall(v, (ux(v) >= -1.0) & (ux(v) <= 1.0) & (uy(v) >= -1.0) & (uy(v) <= 1.0)),
                            rddl.ConstraintType.ACTION)
    the_task.add_constraint(forall(v, (sqrt(vx(v) * vx(v) + vy(v) * vy(v)) <= 5.0)), rddl.ConstraintType.STATE)
    the_task.add_constraint(forall(v, (x(v) >= -100.0) & (x(v) <= 100.0)), rddl.ConstraintType.STATE)
    the_task.add_constraint(forall(v, (y(v) >= -100.0) & (y(v) <= 100.0)), rddl.ConstraintType.STATE)

    # cost function
    Q = sumterm(v, ((x(v) - gx()) * (x(v) - gx())) + ((y(v) - gy()) * (y(v) * gy())))
    # MRJ: RDDL does not support the abs() algebraic construct
    R = sumterm(v, ite(sqrt(vx(v) * vx(v) + vy(v) * vy(v)) > 0.0, (ux(v) * ux(v) * 0.01) + (uy(v) * uy(v) * 0.01),
                       lang.constant(0.0, lang.Real)))
    # R = u() * u() * 0.01
    the_task.reward = Q + R

    # definitions
    the_task.x0.set(x(v001), 0.0)
    the_task.x0.set(y(v001), 0.0)
    the_task.x0.set(vx(v001), 0.0)
    the_task.x0.set(vy(v001), 0.0)
    the_task.x0.set(ux(v001), 0.0)
    the_task.x0.set(uy(v001), 0.0)
    the_task.x0.set(t(), 0.0)
    the_task.x0.set(dt(), 0.5)
    the_task.x0.set(gx(), 20.0)
    the_task.x0.set(gy(), 20.0)
    the_task.x0.set(mu_w(), 0.0)
    the_task.x0.set(sigma_w(), 0.05)

    # fluent metadata
    the_task.declare_state_fluent(x(v), 0.0)
    the_task.declare_state_fluent(y(v), 0.0)
    the_task.declare_state_fluent(t(), 0.0)
    the_task.declare_interm_fluent(vx(v), 1)
    the_task.declare_interm_fluent(vy(v), 1)
    the_task.declare_action_fluent(ux(v), 0.0)
    the_task.declare_action_fluent(uy(v), 0.0)
    the_task.declare_non_fluent(dt(), 0.0)
    the_task.declare_non_fluent(gx(), 0.0)
    the_task.declare_non_fluent(gy(), 0.0)
    the_task.declare_non_fluent(mu_w(), 0.0)
    the_task.declare_non_fluent(sigma_w(), 0.0)

    the_writer = rddl.Writer(the_task)
    rddl_filename = os.path.join(tempfile.gettempdir(), 'lqg_nav_2d_multi_unit_001.rddl')
    the_writer.write_model(rddl_filename)
    mr_reader = rddl.Reader(rddl_filename)
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'lqg_nav_2d_multi_unit'
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None


def test_parametrized_model_with_random_vars_and_waypoints():
    lang = tarski.language('lqg_nav_2d_multi_unit_waypoints',
                           [Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])
    the_task = Task(lang, 'lqg_nav_2d_multi_unit_waypoints', 'instance_001')

    the_task.requirements = [rddl.Requirements.CONTINUOUS, rddl.Requirements.REWARD_DET]

    the_task.parameters.discount = 1.0
    the_task.parameters.horizon = 40
    the_task.parameters.max_nondef_actions = 2

    vehicle = lang.sort('vehicle', lang.Object)
    waypoint = lang.sort('waypoint', lang.Object)

    # variables
    x = lang.function('x', vehicle, lang.Real)
    y = lang.function('y', vehicle, lang.Real)
    wx = lang.function('wx', waypoint, lang.Real)
    wy = lang.function('wy', waypoint, lang.Real)
    wv = lang.function('visited', waypoint, lang.Real)
    vx = lang.function('vx', vehicle, lang.Real)
    vy = lang.function('vy', vehicle, lang.Real)
    ux = lang.function('ux', vehicle, lang.Real)
    uy = lang.function('uy', vehicle, lang.Real)
    t = lang.function('t', lang.Real)

    # objects
    v001 = lang.constant('v001', vehicle)
    p1 = lang.constant('p1', waypoint)
    p2 = lang.constant('p2', waypoint)
    p3 = lang.constant('p3', waypoint)

    # non fluents
    dt = lang.function('dt', lang.Real)
    wr = lang.function('waypoint_radius', lang.Real)
    # Perturbation distribution parameters
    mu_w = lang.function('mu_w', lang.Real)
    sigma_w = lang.function('sigma_w', lang.Real)

    # logical variable
    v = lang.variable('v', vehicle)
    wpt = lang.variable('wpt', waypoint)

    # cpfs
    the_task.add_cpfs(t(), t() + dt())
    dist_vec_norm = ((x(v) - wx(wpt)) * (x(v) - wx(wpt))) + ((y(v) - wy(wpt)) * (y(v) - wy(wpt)))
    the_task.add_cpfs(wv(wpt), ite(sqrt(dist_vec_norm) <= wr(), lang.constant(1.0, lang.Real),
                                   max(lang.constant(0.0, lang.Real), wv(wpt))))
    the_task.add_cpfs(vx(v), vx(v) + dt() * ux(v) + normal(mu_w(), sigma_w()))
    the_task.add_cpfs(vy(v), vy(v) + dt() * uy(v) + normal(mu_w(), sigma_w()))
    the_task.add_cpfs(x(v), x(v) + dt() * vx(v))
    the_task.add_cpfs(y(v), y(v) + dt() * vy(v))

    # constraints
    the_task.add_constraint(forall(v, (ux(v) >= -1.0) & (ux(v) <= 1.0) & (uy(v) >= -1.0) & (uy(v) <= 1.0)),
                            rddl.ConstraintType.ACTION)
    the_task.add_constraint(forall(v, (sqrt(vx(v) * vx(v) + vy(v) * vy(v)) <= 5.0)), rddl.ConstraintType.STATE)
    the_task.add_constraint(forall(v, (x(v) >= -100.0) & (x(v) <= 100.0)), rddl.ConstraintType.STATE)
    the_task.add_constraint(forall(v, (y(v) >= -100.0) & (y(v) <= 100.0)), rddl.ConstraintType.STATE)

    # cost function
    WV = sumterm(wpt, wv(wpt))
    # MRJ: RDDL does not support the abs() algebraic construct
    R = sumterm(v, (ux(v) * ux(v) * 0.01) + (uy(v) * uy(v) * 0.01))
    # R = u() * u() * 0.01
    the_task.reward = WV - R

    # definitions
    the_task.x0.set(x(v001), 0.0)
    the_task.x0.set(y(v001), 0.0)
    the_task.x0.set(vx(v001), 0.0)
    the_task.x0.set(vy(v001), 0.0)
    the_task.x0.set(ux(v001), 0.0)
    the_task.x0.set(uy(v001), 0.0)

    the_task.x0.set(wx(p1), 1.0)
    the_task.x0.set(wy(p1), -1.0)
    the_task.x0.set(wv(p1), 0.0)

    the_task.x0.set(wx(p2), 1.0)
    the_task.x0.set(wy(p2), 1.0)
    the_task.x0.set(wv(p2), 0.0)

    the_task.x0.set(wx(p3), 2.0)
    the_task.x0.set(wy(p3), 1.0)
    the_task.x0.set(wv(p3), 0.0)

    the_task.x0.set(t(), 0.0)
    the_task.x0.set(dt(), 0.5)
    the_task.x0.set(mu_w(), 0.0)
    the_task.x0.set(sigma_w(), 0.05)
    the_task.x0.set(wr(), 2.0)

    # fluent metadata
    the_task.declare_state_fluent(x(v), 0.0)
    the_task.declare_state_fluent(y(v), 0.0)
    the_task.declare_state_fluent(t(), 0.0)
    the_task.declare_state_fluent(wv(wpt), 0.0)
    the_task.declare_interm_fluent(vx(v), 1)
    the_task.declare_interm_fluent(vy(v), 1)
    the_task.declare_action_fluent(ux(v), 0.0)
    the_task.declare_action_fluent(uy(v), 0.0)
    the_task.declare_non_fluent(dt(), 0.0)
    the_task.declare_non_fluent(mu_w(), 0.0)
    the_task.declare_non_fluent(sigma_w(), 0.0)
    the_task.declare_non_fluent(wx(wpt), 0.0)
    the_task.declare_non_fluent(wy(wpt), 0.0)
    the_task.declare_non_fluent(wr(), 0.0)

    the_writer = rddl.Writer(the_task)
    rddl_filename = os.path.join(tempfile.gettempdir(), 'lqg_nav_2d_multi_unit_waypoints.rddl')
    the_writer.write_model(rddl_filename)
    mr_reader = rddl.Reader(rddl_filename)
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'lqg_nav_2d_multi_unit_waypoints'
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None


def test_parametrized_model_with_random_vars_and_waypoints_boolean():
    lang = tarski.language('lqg_nav_2d_multi_unit_bool_waypoints',
                           [Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])
    the_task = Task(lang, 'lqg_nav_2d_multi_unit_bool_waypoints', 'instance_001')

    the_task.requirements = [rddl.Requirements.CONTINUOUS, rddl.Requirements.REWARD_DET]

    the_task.parameters.discount = 1.0
    the_task.parameters.horizon = 40
    the_task.parameters.max_nondef_actions = 2

    vehicle = lang.sort('vehicle', lang.Object)
    waypoint = lang.sort('waypoint', lang.Object)

    # variables
    x = lang.function('x', vehicle, lang.Real)
    y = lang.function('y', vehicle, lang.Real)
    wx = lang.function('wx', waypoint, lang.Real)
    wy = lang.function('wy', waypoint, lang.Real)
    vx = lang.function('vx', vehicle, lang.Real)
    vy = lang.function('vy', vehicle, lang.Real)
    ux = lang.function('ux', vehicle, lang.Real)
    uy = lang.function('uy', vehicle, lang.Real)
    t = lang.function('t', lang.Real)

    wv = lang.predicate('visited', waypoint)

    # objects
    v001 = lang.constant('v001', vehicle)
    p1 = lang.constant('p1', waypoint)
    p2 = lang.constant('p2', waypoint)
    p3 = lang.constant('p3', waypoint)

    # non fluents
    dt = lang.function('dt', lang.Real)
    wr = lang.function('waypoint_radius', lang.Real)
    # Perturbation distribution parameters
    mu_w = lang.function('mu_w', lang.Real)
    sigma_w = lang.function('sigma_w', lang.Real)

    # logical variable
    v = lang.variable('v', vehicle)
    wpt = lang.variable('wpt', waypoint)

    # cpfs
    the_task.add_cpfs(t(), t() + dt())
    dist_vec_norm = ((x(v) - wx(wpt)) * (x(v) - wx(wpt))) + ((y(v) - wy(wpt)) * (y(v) - wy(wpt)))
    the_task.add_cpfs(wv(wpt), (wv(wpt) | (sqrt(dist_vec_norm) <= wr())))
    the_task.add_cpfs(vx(v), vx(v) + dt() * ux(v) + normal(mu_w(), sigma_w()))
    the_task.add_cpfs(vy(v), vy(v) + dt() * uy(v) + normal(mu_w(), sigma_w()))
    the_task.add_cpfs(x(v), x(v) + dt() * vx(v))
    the_task.add_cpfs(y(v), y(v) + dt() * vy(v))

    # constraints
    the_task.add_constraint(forall(v, (ux(v) >= -1.0) & (ux(v) <= 1.0) & (uy(v) >= -1.0) & (uy(v) <= 1.0)),
                            rddl.ConstraintType.ACTION)
    the_task.add_constraint(forall(v, (sqrt(vx(v) * vx(v) + vy(v) * vy(v)) <= 5.0)), rddl.ConstraintType.STATE)
    the_task.add_constraint(forall(v, (x(v) >= -100.0) & (x(v) <= 100.0)), rddl.ConstraintType.STATE)
    the_task.add_constraint(forall(v, (y(v) >= -100.0) & (y(v) <= 100.0)), rddl.ConstraintType.STATE)

    # cost function
    WV = sumterm(wpt, ite(wv(wpt), lang.constant(1.0, lang.Real), lang.constant(0.0, lang.Real)))
    # MRJ: RDDL does not support the abs() algebraic construct
    R = sumterm(v, (ux(v) * ux(v) * 0.01) + (uy(v) * uy(v) * 0.01))
    # R = u() * u() * 0.01
    the_task.reward = WV - R

    # definitions
    the_task.x0.set(x(v001), 0.0)
    the_task.x0.set(y(v001), 0.0)
    the_task.x0.set(vx(v001), 0.0)
    the_task.x0.set(vy(v001), 0.0)
    the_task.x0.set(ux(v001), 0.0)
    the_task.x0.set(uy(v001), 0.0)

    the_task.x0.set(wx(p1), 1.0)
    the_task.x0.set(wy(p1), -1.0)

    the_task.x0.set(wx(p2), 1.0)
    the_task.x0.set(wy(p2), 1.0)

    the_task.x0.set(wx(p3), 2.0)
    the_task.x0.set(wy(p3), 1.0)

    the_task.x0.set(t(), 0.0)
    the_task.x0.set(dt(), 0.5)
    the_task.x0.set(mu_w(), 0.0)
    the_task.x0.set(sigma_w(), 0.05)
    the_task.x0.set(wr(), 2.0)

    # fluent metadata
    the_task.declare_state_fluent(x(v), 0.0)
    the_task.declare_state_fluent(y(v), 0.0)
    the_task.declare_state_fluent(t(), 0.0)
    the_task.declare_state_fluent(wv(wpt), False)
    the_task.declare_interm_fluent(vx(v), 1)
    the_task.declare_interm_fluent(vy(v), 1)
    the_task.declare_action_fluent(ux(v), 0.0)
    the_task.declare_action_fluent(uy(v), 0.0)
    the_task.declare_non_fluent(dt(), 0.0)
    the_task.declare_non_fluent(mu_w(), 0.0)
    the_task.declare_non_fluent(sigma_w(), 0.0)
    the_task.declare_non_fluent(wx(wpt), 0.0)
    the_task.declare_non_fluent(wy(wpt), 0.0)
    the_task.declare_non_fluent(wr(), 0.0)

    the_writer = rddl.Writer(the_task)
    rddl_filename = os.path.join(tempfile.gettempdir(), 'lqg_nav_2d_multi_unit_bool_waypoints.rddl')
    the_writer.write_model(rddl_filename)
    mr_reader = rddl.Reader(rddl_filename)
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'lqg_nav_2d_multi_unit_bool_waypoints'
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None

def test_rddl_integration_academic_advising_example_write():
    lang = tarski.language('standard', [Theory.EQUALITY, Theory.ARITHMETIC, Theory.RANDOM])
    the_task = Task(lang, 'academic_advising', 'instance_001')

    the_task.requirements = [rddl.Requirements.REWARD_DET, rddl.Requirements.PRECONDITIONS]

    the_task.parameters.discount = 1.0
    the_task.parameters.horizon = 20
    the_task.parameters.max_nondef_actions = 1

    #sorts
    course = lang.sort('course')

    # variables
    c = lang.variable('c', course)
    c2 = lang.variable('c2', course)

    # non fluents
    PREREQ = lang.predicate('PREREQ', course, course)
    PRIOR_PROB_PASS_NO_PREREQ = lang.function('PRIOR_PROB_PASS_NO_PREREQ', course, lang.Real)
    PRIOR_PROB_PASS = lang.function('PRIOR_PROB_PASS', course, lang.Real)
    PROGRAM_REQUIREMENT = lang.predicate('PROGRAM_REQUIREMENT', course)
    COURSE_COST = lang.function('COURSE_COST', lang.Real)
    COURSE_RETAKE_COST = lang.function('COURSE_RETAKE_COST', lang.Real)
    PROGRAM_INCOMPLETE_PENALTY = lang.function('PROGRAM_INCOMPLETE_PENALTY', lang.Real)
    COURSES_PER_SEMESTER = lang.function('COURSES_PER_SEMESTER', lang.Real)

    # state fluents
    passed = lang.predicate('passed', course)
    taken = lang.predicate('taken', course)

    # action fluents
    take_course = lang.predicate('take-course', course)

    one = lang.constant(1, lang.Real)
    # cpfs
    the_task.add_cpfs(passed(c), ite(take_course(c) & ~(exists(c2, PREREQ(c2, c))),
                                     bernoulli(PRIOR_PROB_PASS_NO_PREREQ(c)),
                                     ite(take_course(c),
                                         bernoulli((one - PRIOR_PROB_PASS(c))
                                                   * (sumterm(c2, (PREREQ(c2, c) & passed(c2))))
                                                   / (one + sumterm(c2, (PREREQ(c2, c))))),
                                         passed(c))))

    the_task.add_cpfs(taken(c), taken(c) | take_course(c))

    # cost function
    the_task.reward = ( sumterm(c, COURSE_COST() * (take_course(c) & ~taken(c)))
                        + sumterm(c, COURSE_RETAKE_COST() * (take_course(c) & taken(c)))
                        + (PROGRAM_INCOMPLETE_PENALTY() * ~(forall(c, PROGRAM_REQUIREMENT(c) > passed(c)))))

    # constraints
    the_task.add_constraint(forall(c, take_course(c) > ~passed(c)), rddl.ConstraintType.ACTION)
    the_task.add_constraint(sumterm(c, take_course(c)) <= COURSES_PER_SEMESTER(), rddl.ConstraintType.ACTION)

    # fluent metadata
    the_task.declare_state_fluent(passed(c), 'false')
    the_task.declare_state_fluent(taken(c), 'false')
    the_task.declare_action_fluent(take_course(c), 'false')
    the_task.declare_non_fluent(PREREQ(c, c2), 'false')
    the_task.declare_non_fluent(PRIOR_PROB_PASS_NO_PREREQ(c), 0.8)
    the_task.declare_non_fluent(PRIOR_PROB_PASS(c), 0.2)
    the_task.declare_non_fluent(PROGRAM_REQUIREMENT(c), 'false')
    the_task.declare_non_fluent(COURSE_COST(), -1)
    the_task.declare_non_fluent(COURSE_RETAKE_COST(), -2)
    the_task.declare_non_fluent(PROGRAM_INCOMPLETE_PENALTY(), -5)
    the_task.declare_non_fluent(COURSES_PER_SEMESTER(), 1)

    #constants
    c0000 = lang.constant('c0000', course)
    c0001 = lang.constant('c0001', course)
    c0002 = lang.constant('c0002', course)
    c0003 = lang.constant('c0003', course)
    c0004 = lang.constant('c0004', course)
    c0100 = lang.constant('c0100', course)
    c0101 = lang.constant('c0101', course)
    c0102 = lang.constant('c0102', course)
    c0103 = lang.constant('c0103', course)
    c0200 = lang.constant('c0200', course)
    c0201 = lang.constant('c0201', course)
    c0202 = lang.constant('c0202', course)
    c0300 = lang.constant('c0300', course)
    c0301 = lang.constant('c0301', course)
    c0302 = lang.constant('c0302', course)

    the_task.x0.set(PRIOR_PROB_PASS_NO_PREREQ(c0000), 0.80)
    the_task.x0.set(PRIOR_PROB_PASS_NO_PREREQ(c0001), 0.55)
    the_task.x0.set(PRIOR_PROB_PASS_NO_PREREQ(c0002), 0.67)
    the_task.x0.set(PRIOR_PROB_PASS_NO_PREREQ(c0003), 0.78)
    the_task.x0.set(PRIOR_PROB_PASS_NO_PREREQ(c0004), 0.75)
    the_task.x0.set(PRIOR_PROB_PASS(c0100), 0.22)
    the_task.x0.set(PRIOR_PROB_PASS(c0101), 0.45)
    the_task.x0.set(PRIOR_PROB_PASS(c0102), 0.41)
    the_task.x0.set(PRIOR_PROB_PASS(c0103), 0.44)
    the_task.x0.set(PRIOR_PROB_PASS(c0200), 0.14)
    the_task.x0.set(PRIOR_PROB_PASS(c0201), 0.07)
    the_task.x0.set(PRIOR_PROB_PASS(c0202), 0.24)
    the_task.x0.set(PRIOR_PROB_PASS(c0300), 0.23)
    the_task.x0.set(PRIOR_PROB_PASS(c0301), 0.08)
    the_task.x0.set(PRIOR_PROB_PASS(c0302), 0.16)


    the_task.x0.add(PREREQ(c0003, c0100), 'true')
    the_task.x0.add(PREREQ(c0000, c0100), 'true')
    the_task.x0.add(PREREQ(c0004, c0100), 'true')
    the_task.x0.add(PREREQ(c0001, c0101), 'true')
    the_task.x0.add(PREREQ(c0002, c0101), 'true')
    the_task.x0.add(PREREQ(c0000, c0102), 'true')
    the_task.x0.add(PREREQ(c0004, c0102), 'true')
    the_task.x0.add(PREREQ(c0001, c0103), 'true')
    the_task.x0.add(PREREQ(c0001, c0200), 'true')
    the_task.x0.add(PREREQ(c0101, c0200), 'true')
    the_task.x0.add(PREREQ(c0103, c0201), 'true')
    the_task.x0.add(PREREQ(c0002, c0202), 'true')
    the_task.x0.add(PREREQ(c0200, c0300), 'true')
    the_task.x0.add(PREREQ(c0201, c0301), 'true')
    the_task.x0.add(PREREQ(c0201, c0301), 'true')
    the_task.x0.add(PREREQ(c0200, c0302), 'true')

    the_task.x0.add(PROGRAM_REQUIREMENT(c0300), 'true')
    the_task.x0.add(PROGRAM_REQUIREMENT(c0202), 'true')
    the_task.x0.add(PROGRAM_REQUIREMENT(c0101), 'true')
    the_task.x0.add(PROGRAM_REQUIREMENT(c0002), 'true')
    the_task.x0.add(PROGRAM_REQUIREMENT(c0001), 'true')

    the_task.x0.add(passed(c0000), 'false')

    the_writer = rddl.Writer(the_task)
    rddl_filename = os.path.join(tempfile.gettempdir(), 'academic_advising_001.rddl')
    the_writer.write_model(rddl_filename)
    mr_reader = rddl.Reader(rddl_filename)
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'academic_advising'
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None
