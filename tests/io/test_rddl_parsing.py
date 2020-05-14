import os

from tarski.syntax import *
from tarski.io import rddl
from .. import TEST_DIR


def test_language_init_mars_rovers():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Mars_Rover.rddl"))
    assert reader.rddl_model is not None
    assert reader.rddl_model.domain.name == 'simple_mars_rover'
    # create sorts and initialize constants
    _ = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()
    assert reader.language is not None

    # try to construct expression without triggering any exceptions
    snap_picture = reader.language.get('snapPicture')
    delta_x = reader.language.get('xMove')
    delta_y = reader.language.get('yMove')
    _ = implies(snap_picture(), (delta_x() == 0.0) & (delta_y() == 0.0))


def test_language_init_navigation():
    import tarski.syntax.arithmetic as tm
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Navigation.rddl"))
    assert reader.rddl_model is not None
    assert reader.rddl_model.domain.name == 'Navigation'

    # create sorts and initialize constants
    _ = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()
    assert reader.language is not None

    # try to construct expression without triggering any exceptions
    x = reader.language.get('x')
    y = reader.language.get('y')
    loc = reader.language.get('location')
    dzc = reader.language.get('DECELERATION_ZONE_CENTER')
    z1 = reader.language.get('z1')
    distance = reader.language.get('distance')
    _ = distance(z1) == tm.sqrt(tm.pow(loc(x) - dzc(z1, x), 2.0) + tm.pow(loc(y) - dzc(z1, y), 2.0))


def test_language_init_reservoir():
    import tarski.syntax.arithmetic.special as tms

    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Reservoir.rddl"))
    assert reader.rddl_model is not None
    assert reader.rddl_model.domain.name == 'reservoir'

    # create sorts and initialize constants
    _ = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()
    assert reader.language is not None

    # try to construct expression without triggering any exceptions
    t1 = reader.language.get('t1')
    overflow = reader.language.get('overflow')
    rlevel = reader.language.get('rlevel')
    outflow = reader.language.get('outflow')
    max_reservoir_capacity = reader.language.get('MAX_RES_CAP')

    _ = overflow(t1) == tms.max(0.0, rlevel(t1) - outflow(t1) - max_reservoir_capacity(t1))


def test_language_mars_rovers_load_cpfs():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Mars_Rover.rddl"))
    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    # collect state cpfs
    state_cpfs = []
    for f in domain.state_cpfs:
        state_cpfs += [rddl.translate_expression(reader.language, f.expr)]
    # collect intermediate cpfs
    intermediate_cpfs = []
    for f in domain.intermediate_cpfs:
        intermediate_cpfs += [rddl.translate_expression(reader.language, f.expr)]

    assert len(state_cpfs) + len(intermediate_cpfs) == 4


def test_language_mars_rovers_load_constraints():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Mars_Rover.rddl"))
    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    precs = []
    for prec in domain.preconds:
        precs += [rddl.translate_expression(reader.language, prec)]
    assert len(precs) == 1

    action_constraints = []
    for c in domain.constraints:
        action_constraints += [rddl.translate_expression(reader.language, c.expr)]
    assert len(action_constraints) == 0

    state_constraints = []
    for c in domain.invariants:
        state_constraints += [rddl.translate_expression(reader.language, c.expr)]
    assert len(state_constraints) == 0


def test_language_mars_rovers_load_reward():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Mars_Rover.rddl"))
    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()
    reward_func = rddl.translate_expression(reader.language, domain.reward)
    assert isinstance(reward_func, Term)


def test_language_navigation_load_cpfs():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Navigation.rddl"))

    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    # collect state cpfs
    state_cpfs = []
    for f in domain.state_cpfs:
        state_cpfs += [rddl.translate_expression(reader.language, f.expr)]
    intermediate_cpfs = []
    for f in domain.intermediate_cpfs:
        intermediate_cpfs += [rddl.translate_expression(reader.language, f.expr)]

    assert len(state_cpfs) + len(intermediate_cpfs) == 3


def test_language_navigation_load_constraints():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Navigation.rddl"))

    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    reader.translate_rddl_model()

    precs = []
    for prec in domain.preconds:
        precs += [rddl.translate_expression(reader.language, prec)]
    assert len(precs) == 2

    action_constraints = []
    for c in domain.constraints:
        action_constraints += [rddl.translate_expression(reader.language, c.expr)]
    assert len(action_constraints) == 0

    state_constraints = []
    for c in domain.invariants:
        state_constraints += [rddl.translate_expression(reader.language, c.expr)]
    assert len(state_constraints) == 0


def test_language_navigation_load_reward():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Navigation.rddl"))

    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    reader.translate_rddl_model()
    reward_func = rddl.translate_expression(reader.language, domain.reward)
    assert isinstance(reward_func, Term)
    assert reader.parameters.horizon == 20
    assert reader.parameters.discount == 1.0
    assert reader.parameters.max_actions == 2


def test_language_reservoir_load_cpfs():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Reservoir.rddl"))

    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    # collect state cpfs
    state_cpfs = []
    for f in domain.state_cpfs:
        state_cpfs += [rddl.translate_expression(reader.language, f.expr)]
    intermediate_cpfs = []
    for f in domain.intermediate_cpfs:
        intermediate_cpfs += [rddl.translate_expression(reader.language, f.expr)]

    assert len(state_cpfs) + len(intermediate_cpfs) == 5


def test_language_reservoir_load_constraints():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Reservoir.rddl"))

    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    precs = []
    for prec in domain.preconds:
        precs += [rddl.translate_expression(reader.language, prec)]
    assert len(precs) == 2

    action_constraints = []
    for c in domain.constraints:
        action_constraints += [rddl.translate_expression(reader.language, c.expr)]
    assert len(action_constraints) == 0

    state_constraints = []
    for c in domain.invariants:
        state_constraints += [rddl.translate_expression(reader.language, c)]
    assert len(state_constraints) == 2


def test_language_reservoir_load_reward():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Reservoir.rddl"))

    # create sorts and initialize constants
    domain = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    assert reader.parameters.horizon == 40
    assert reader.parameters.discount == 1.0
    assert reader.parameters.max_actions is None

    reward_func = rddl.translate_expression(reader.language, domain.reward)
    assert isinstance(reward_func, Term)


def test_mars_rovers_load_parameters():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Mars_Rover.rddl"))

    # create sorts and initialize constants
    _ = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    assert reader.parameters.horizon == 40
    assert reader.parameters.discount == 1.0
    assert reader.parameters.max_actions is None


def test_mars_rovers_load_initial_state():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Mars_Rover.rddl"))
    # create sorts and initialize constants
    _ = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()
    xPos = reader.language.get('xPos')
    yPos = reader.language.get('yPos')
    time = reader.language.get('time')
    assert reader.x0[xPos()].symbol == 0.0
    assert reader.x0[yPos()].symbol == 0.0
    assert reader.x0[time()].symbol == 0.0


def test_language_navigation_load_initial_state():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Navigation.rddl"))

    # create sorts and initialize constants
    _ = reader.rddl_model.domain
    reader.translate_rddl_model()
    x = reader.language.get('x')
    y = reader.language.get('y')
    location = reader.language.get('location')

    assert reader.x0[location(x)].symbol == 0.0
    assert reader.x0[location(y)].symbol == 0.0


def test_language_reservoir_load_initial_state():
    reader = rddl.Reader(os.path.join(TEST_DIR, "data/rddl/Reservoir.rddl"))

    # create sorts and initialize constants
    _ = reader.rddl_model.domain
    _ = reader.rddl_model.non_fluents
    reader.translate_rddl_model()

    t1 = reader.language.get('t1')
    rlevel = reader.language.get('rlevel')

    assert reader.x0[rlevel(t1)].symbol == 75.0
