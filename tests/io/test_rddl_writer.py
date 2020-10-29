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
