# -*- coding: utf-8 -*-
import itertools, copy

from . import instantiation
from tarski import fstrips as fs
from tarski.fstrips.contingent import Sensor
from tarski.syntax.transform import TermSubstitution
from tarski.syntax.visitors import CollectVariables
from tarski.util import IndexDictionary
from tarski.syntax import *

class SensorGrounder(object):

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
            K, syms, substs = instantiation.enumerate(self.L, act_schema.parameters )
            for values in itertools.product(*substs):
                subst = { syms[k] : v for k,v in enumerate(values) }
                g_prec = copy.deepcopy(act_schema.condition)
                op = TermSubstitution(self.L,subst)
                g_prec.accept(op)
                var_collector = CollectVariables(self.L)
                g_prec.accept(var_collector)
                assert len(var_collector.variables) == 0

                g_obs = copy.deepcopy(act_schema.obs)
                g_obs.accept(op)

                # MRJ: invariant
                var_collector = CollectVariables(self.L)
                g_obs.accept(var_collector)
                assert len(var_collector.variables) == 0
                self.problem.ground_sensors.add(Sensor(self.L, act_schema.name, [], g_prec, g_obs))
            self.sensors_generated += K
