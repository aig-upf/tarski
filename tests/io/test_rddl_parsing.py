
import pytest
import tarski
from tarski.theories import Theory
from tarski.syntax import *
from tarski.io import rddl

def test_language_init_mars_rovers():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    assert mr_reader.rddl_model is not None
    assert mr_reader.rddl_model.domain.name == 'simple_mars_rover'
    # create sorts and initialize constants
    domain = mr_reader.rddl_model.domain
    non_fluents = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()
    assert mr_reader.language is not None

    # try to construct expression without triggering any exceptions
    snap_picture = mr_reader.language.get('snapPicture')
    delta_x = mr_reader.language.get('xMove')
    delta_y = mr_reader.language.get('yMove')
    phi = implies(snap_picture(), (delta_x() == 0.0) & (delta_y() == 0.0))

def test_language_init_navigation():
    import tarski.syntax.arithmetic as tm
    nav_reader = rddl.Reader('tests/data/rddl/Navigation.rddl')
    assert nav_reader.rddl_model is not None
    assert nav_reader.rddl_model.domain.name == 'Navigation'

    # create sorts and initialize constants
    domain = nav_reader.rddl_model.domain
    non_fluents = nav_reader.rddl_model.non_fluents
    nav_reader.translate_rddl_model()
    assert nav_reader.language is not None

    # try to construct expression without triggering any exceptions
    x = nav_reader.language.get('x')
    y = nav_reader.language.get('y')
    l = nav_reader.language.get('location')
    dzc = nav_reader.language.get('DECELERATION_ZONE_CENTER')
    z1 = nav_reader.language.get('z1')
    distance = nav_reader.language.get('distance')
    expr = distance(z1) == tm.sqrt(tm.pow( l(x) - dzc(z1, x), 2.0) + tm.pow(l(y) - dzc(z1, y), 2.0))

def test_language_init_reservoir():
    import tarski.syntax.arithmetic as tm
    import tarski.syntax.arithmetic.special as tms

    res_reader = rddl.Reader('tests/data/rddl/Reservoir.rddl')
    assert res_reader.rddl_model is not None
    assert res_reader.rddl_model.domain.name == 'reservoir'

    # create sorts and initialize constants
    domain = res_reader.rddl_model.domain
    non_fluents = res_reader.rddl_model.non_fluents
    res_reader.translate_rddl_model()
    assert res_reader.language is not None

    # try to construct expression without triggering any exceptions
    t1 = res_reader.language.get('t1')
    overflow = res_reader.language.get('overflow')
    rlevel = res_reader.language.get('rlevel')
    outflow = res_reader.language.get('outflow')
    max_reservoir_capacity = res_reader.language.get('MAX_RES_CAP')

    expr = overflow(t1) == tms.max(0.0, rlevel(t1) - outflow(t1) - max_reservoir_capacity(t1))

def test_language_mars_rovers_load_cpfs():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    # create sorts and initialize constants
    domain = mr_reader.rddl_model.domain
    non_fluents = mr_reader.rddl_model.non_fluents
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
    non_fluents = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()

    precs = []
    for prec in domain.preconds:
        precs += [ rddl.translate_expression(mr_reader.language, prec)]
    assert len(precs) == 1

    action_constraints = []
    for c in domain.constraints:
        action_constraints += [ rddl.translate_expression(mr_reader.language, c.expr)]
    assert len(action_constraints) == 0

    state_constraints = []
    for c in domain.invariants:
        state_constraints += [ rddl.translate_expression(mr_reader.language, c.expr)]
    assert len(state_constraints) == 0

def test_language_mars_rovers_load_reward():
    mr_reader = rddl.Reader('tests/data/rddl/Mars_Rover.rddl')
    # create sorts and initialize constants
    domain = mr_reader.rddl_model.domain
    non_fluents = mr_reader.rddl_model.non_fluents
    mr_reader.translate_rddl_model()
    reward_func = rddl.translate_expression(mr_reader.language, domain.reward)
    print(reward_func)
    assert  isinstance(reward_func, Term)
