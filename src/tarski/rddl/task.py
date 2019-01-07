import tarski
from tarski.io import rddl
from tarski.model import Model
from tarski.evaluators.simple import evaluate

class Task(object):

    def __init__(self, L: tarski.FirstOrderLanguage, domain_name: str, instance_name: str):
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