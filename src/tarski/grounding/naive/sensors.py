
import itertools

from ...fstrips.contingent import Sensor
from ...syntax import create_substitution, TermSubstitution
from ...util import IndexDictionary
from .elements import process_expression
from . import instantiation


class SensorGrounder:

    def __init__(self, prob, index):
        self.problem = prob
        self.L = self.problem.language
        self.index = index
        self.problem.ground_sensors = IndexDictionary()
        self.schemas = list(self.problem.sensors.values())
        self.sensors_generated = 0

    def __str__(self):
        return 'Sensors generated: {}'.format(self.sensors_generated)

    def calculate_sensors(self):
        # @TODO: this is pretty much the same code as that of grounding actions
        # this NEEDS to be refactored, so we ground action elements in a more
        # moudular and component oriented fashion
        for act_schema in self.schemas:
            K, syms, substs = instantiation.enumerate_groundings(self.L, act_schema.parameters)
            for values in itertools.product(*substs):
                subst = create_substitution(syms, values)

                op = TermSubstitution(self.L, subst)
                g_prec = process_expression(self.L, act_schema.condition, op)
                g_obs = process_expression(self.L, act_schema.obs, op)
                self.problem.ground_sensors.add(Sensor(self.L, act_schema.name, [], g_prec, g_obs))
            self.sensors_generated += K
