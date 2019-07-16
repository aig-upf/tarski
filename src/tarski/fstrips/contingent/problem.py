
from collections import OrderedDict
from ..problem import Problem
from .sensor import Sensor
from . import errors as err


class ContingentProblem(Problem):
    """ A Functional STRIPS Contingent problem """

    def __init__(self):
        super().__init__()
        self.sensors = OrderedDict()

    def sensor(self, name, parameters, condition, obs):
        if name in self.sensors:
            raise err.DuplicateSensorDefinition(name, self.sensors[name])
        self.sensors[name] = Sensor(self.language, name, parameters, condition, obs)
        return self.sensors[name]

    def has_sensor(self, name):
        return name in self.sensors

    def get_sensor(self, name):
        if not self.has_sensor(name):
            raise err.UndefinedSensor(name)
        return self.sensors[name]

    def get_symbols(self, pv, ev, cv):
        super().get_symbols(pv, ev, cv)
        for _, sensor in self.sensors.items():
            pv.visit(sensor.condition)
            pv.visit(sensor.obs)

    def __str__(self):
        return 'FSTRIPS Contingent Problem "{}", domain "{}"'.format(self.name, self.domain_name)

    __repr__ = __str__
