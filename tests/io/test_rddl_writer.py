import pytest
import os
import tempfile

import tarski
from tarski.theories import Theory
from tarski.syntax import *
from tarski.io import rddl
from tarski.model import Model
from tarski.evaluators.simple import evaluate
from tarski.syntax.arithmetic import *
from tarski.syntax.arithmetic.special import *
from tarski.syntax.arithmetic.random import *

class Task(object):

    def __init__(self, L, domain_name, instance_name):
        self.L = L
        self.state_fluents = []
        self.interm_fluents = []
        self.action_fluents = []
        self.non_fluents = []
        self.cpfs = []
        self.constraints = []
        self.reward = None
        self.parameters = rddl.Parameters()
        self.domain_name = domain_name
        self.instance_name = instance_name
        self.x0 = Model(self.L)
        self.x0.evaluator = evaluate
        self.requirements = []


    def declare_state_fluent(self, symbol, value):
        self.state_fluents += [(symbol,value)]

    def declare_interm_fluent(self, symbol, level):
        self.interm_fluents += [(symbol, level)]

    def declare_action_fluent(self, symbol, value):
        self.action_fluents += [(symbol, value)]

    def declare_non_fluent(self, symbol, value):
        self.non_fluents += [(symbol, value)]

    def add_constraint(self, expr, ctype):
        self.constraints += [(expr, ctype)]

    def add_cpfs(self, lhs, rhs):
        self.cpfs += [(lhs, rhs)]

def test_simple_rddl_model():

    lang = tarski.language('lqr_nav_1d', [Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL])
    the_task = Task( lang, 'lqr_nav_1d', 'instance_001')

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
    the_task.add_constraint( (u() >= -1.0) & (u() <= 1.0), rddl.ConstraintType.ACTION)
    the_task.add_constraint( (v() >= -5.0) & (v() <= 5.0), rddl.ConstraintType.STATE)
    the_task.add_constraint( (x() >= -100.0) & (x() <= 100.0), rddl.ConstraintType.STATE)

    # cost function
    Q = (x()-gx()) * (x()-gx())
    R = ite(abs(x()-gx()) > 0.0, u() * u() * 0.01, lang.constant(0.0, lang.Real))
    the_task.reward = Q + R

    # definitions
    the_task.x0.setx(x(), 0.0)
    the_task.x0.setx(v(), 0.0)
    the_task.x0.setx(u(), 0.0)
    the_task.x0.setx(t(), 0.0)
    the_task.x0.setx(dt(), 0.5)
    the_task.x0.setx(gx(), 20.0)

    # fluent metadata
    the_task.declare_state_fluent(x(), 0.0)
    the_task.declare_state_fluent(t(), 0.0)
    the_task.declare_interm_fluent(v(), 1)
    the_task.declare_action_fluent(u(), 0.0)
    the_task.declare_non_fluent(dt(), 0.0)
    the_task.declare_non_fluent(gx(), 0.0)

    the_writer = rddl.Writer(the_task)
    rddl_filename = os.path.join(tempfile.gettempdir(), 'monga.rddl')
    the_writer.write_model(rddl_filename)
