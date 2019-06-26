from tarski.syntax import *
from tarski.io import rddl


def test_language_init_mars_rovers():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'simple_mars_rover'
    # create sorts and initialize constants
    _ = mr_reader.rddl_model.domain
    _ = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None

    # try to construct expression without triggering any exceptions
    snap_picture = mr_reader.language.get('snapPicture')
    delta_x = mr_reader.language.get('xMove')
    delta_y = mr_reader.language.get('yMove')
    _ = implies(snap_picture(), (delta_x() == 0.0) & (delta_y() == 0.0))


def test_language_init_navigation():
    import tarski.syntax.arithmetic as tm
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')
    assert nav_reader.rddl_model is not None
    assert nav_reader.rddl_model.domain.name == 'Navigation'

    # create sorts and initialize constants
    _ = nav_reader.rddl_model.domain
    _ = nav_reader.rddl_model.non_fluents
    nav_reader.translate_rddl_model()
    assert nav_reader.language is not None

    # try to construct expression without triggering any exceptions
    x = nav_reader.language.get('x')
    y = nav_reader.language.get('y')
    loc = nav_reader.language.get('location')
    dzc = nav_reader.language.get('DECELERATION_ZONE_CENTER')
    z1 = nav_reader.language.get('z1')
    distance = nav_reader.language.get('distance')
    _ = distance(z1) == tm.sqrt(tm.pow(loc(x) - dzc(z1, x), 2.0) + tm.pow(loc(y) - dzc(z1, y), 2.0))


def test_language_init_reservoir():
    import tarski.syntax.arithmetic.special as tms

    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')
    assert res_reader.rddl_model is not None
    assert res_reader.rddl_model.domain.name == 'reservoir'

    # create sorts and initialize constants
    _ = res_reader.rddl_model.domain
    _ = res_reader.rddl_model.non_fluents
    res_reader.translate_rddl_model()
    assert res_reader.language is not None

    # try to construct expression without triggering any exceptions
    t1 = res_reader.language.get('t1')
    overflow = res_reader.language.get('overflow')
    rlevel = res_reader.language.get('rlevel')
    outflow = res_reader.language.get('outflow')
    max_reservoir_capacity = res_reader.language.get('MAX_RES_CAP')

    _ = overflow(t1) == tms.max(0.0, rlevel(t1) - outflow(t1) - max_reservoir_capacity(t1))


def test_language_mars_rovers_load_cpfs():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    # create sorts and initialize constants
    domain = mr_reader.rddl_model.domain
    _ = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()

    # collect state cpfs
    state_cpfs = []
    for f in domain.state_cpfs:
        state_cpfs += [rddl.translate_expression(mr_reader.language, f.expr)]
    # collect intermediate cpfs
    intermediate_cpfs = []
    for f in domain.intermediate_cpfs:
        intermediate_cpfs += [rddl.translate_expression(mr_reader.language, f.expr)]

    assert len(state_cpfs) + len(intermediate_cpfs) == 4


def test_language_mars_rovers_load_constraints():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    # create sorts and initialize constants
    domain = mr_reader.rddl_model.domain
    _ = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()

    precs = []
    for prec in domain.preconds:
        precs += [rddl.translate_expression(mr_reader.language, prec)]
    assert len(precs) == 1

    action_constraints = []
    for c in domain.constraints:
        action_constraints += [rddl.translate_expression(mr_reader.language, c.expr)]
    assert len(action_constraints) == 0

    state_constraints = []
    for c in domain.invariants:
        state_constraints += [rddl.translate_expression(mr_reader.language, c.expr)]
    assert len(state_constraints) == 0


def test_language_mars_rovers_load_reward():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    # create sorts and initialize constants
    domain = mr_reader.rddl_model.domain
    _ = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()
    reward_func = rddl.translate_expression(mr_reader.language, domain.reward)
    assert isinstance(reward_func, Term)


def test_language_navigation_load_cpfs():
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')

    # create sorts and initialize constants
    domain = nav_reader.rddl_model.domain
    _ = nav_reader.rddl_model.non_fluents
    nav_reader.translate_rddl_model()

    # collect state cpfs
    state_cpfs = []
    for f in domain.state_cpfs:
        state_cpfs += [rddl.translate_expression(nav_reader.language, f.expr)]
    intermediate_cpfs = []
    for f in domain.intermediate_cpfs:
        intermediate_cpfs += [rddl.translate_expression(nav_reader.language, f.expr)]

    assert len(state_cpfs) + len(intermediate_cpfs) == 3


def test_language_navigation_load_constraints():
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')

    # create sorts and initialize constants
    domain = nav_reader.rddl_model.domain
    nav_reader.translate_rddl_model()

    precs = []
    for prec in domain.preconds:
        precs += [rddl.translate_expression(nav_reader.language, prec)]
    assert len(precs) == 2

    action_constraints = []
    for c in domain.constraints:
        action_constraints += [rddl.translate_expression(nav_reader.language, c.expr)]
    assert len(action_constraints) == 0

    state_constraints = []
    for c in domain.invariants:
        state_constraints += [rddl.translate_expression(nav_reader.language, c.expr)]
    assert len(state_constraints) == 0


def test_language_navigation_load_reward():
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')

    # create sorts and initialize constants
    domain = nav_reader.rddl_model.domain
    nav_reader.translate_rddl_model()
    reward_func = rddl.translate_expression(nav_reader.language, domain.reward)
    assert isinstance(reward_func, Term)
    assert nav_reader.parameters.horizon == 20
    assert nav_reader.parameters.discount == 1.0
    assert nav_reader.parameters.max_actions == 2


def test_language_reservoir_load_cpfs():
    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')

    # create sorts and initialize constants
    domain = res_reader.rddl_model.domain
    _ = res_reader.rddl_model.non_fluents
    res_reader.translate_rddl_model()

    # collect state cpfs
    state_cpfs = []
    for f in domain.state_cpfs:
        state_cpfs += [rddl.translate_expression(res_reader.language, f.expr)]
    intermediate_cpfs = []
    for f in domain.intermediate_cpfs:
        intermediate_cpfs += [rddl.translate_expression(res_reader.language, f.expr)]

    assert len(state_cpfs) + len(intermediate_cpfs) == 5


def test_language_reservoir_load_constraints():
    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')

    # create sorts and initialize constants
    domain = res_reader.rddl_model.domain
    _ = res_reader.rddl_model.non_fluents
    res_reader.translate_rddl_model()

    precs = []
    for prec in domain.preconds:
        precs += [rddl.translate_expression(res_reader.language, prec)]
    assert len(precs) == 2

    action_constraints = []
    for c in domain.constraints:
        action_constraints += [rddl.translate_expression(res_reader.language, c.expr)]
    assert len(action_constraints) == 0

    state_constraints = []
    for c in domain.invariants:
        state_constraints += [rddl.translate_expression(res_reader.language, c)]
    assert len(state_constraints) == 2


def test_language_reservoir_load_reward():
    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')

    # create sorts and initialize constants
    domain = res_reader.rddl_model.domain
    _ = res_reader.rddl_model.non_fluents
    res_reader.translate_rddl_model()

    assert res_reader.parameters.horizon == 40
    assert res_reader.parameters.discount == 1.0
    assert res_reader.parameters.max_actions is None

    reward_func = rddl.translate_expression(res_reader.language, domain.reward)
    assert isinstance(reward_func, Term)


def test_mars_rovers_load_parameters():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    # create sorts and initialize constants
    _ = mr_reader.rddl_model.domain
    _ = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()

    assert mr_reader.parameters.horizon == 40
    assert mr_reader.parameters.discount == 1.0
    assert mr_reader.parameters.max_actions is None


def test_mars_rovers_load_initial_state():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    # create sorts and initialize constants
    _ = mr_reader.rddl_model.domain
    _ = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()
    xPos = mr_reader.language.get('xPos')
    yPos = mr_reader.language.get('yPos')
    time = mr_reader.language.get('time')
    assert mr_reader.x0[xPos()].symbol == 0.0
    assert mr_reader.x0[yPos()].symbol == 0.0
    assert mr_reader.x0[time()].symbol == 0.0


def test_language_navigation_load_initial_state():
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')

    # create sorts and initialize constants
    _ = nav_reader.rddl_model.domain
    nav_reader.translate_rddl_model()
    x = nav_reader.language.get('x')
    y = nav_reader.language.get('y')
    location = nav_reader.language.get('location')

    assert nav_reader.x0[location(x)].symbol == 0.0
    assert nav_reader.x0[location(y)].symbol == 0.0


def test_language_reservoir_load_initial_state():
    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')

    # create sorts and initialize constants
    _ = res_reader.rddl_model.domain
    _ = res_reader.rddl_model.non_fluents
    res_reader.translate_rddl_model()

    t1 = res_reader.language.get('t1')
    rlevel = res_reader.language.get('rlevel')

    assert res_reader.x0[rlevel(t1)].symbol == 75.0
