from . problem import Problem
from .. action import Action

# -*- coding: utf-8 -*-
from collections import OrderedDict
from . action import Action
from . import errors as err

class Problem(object):
    """ A Functional STRIPS Contingent problem """

    def __init__(self):
        self.name = None
        self.domain_name = None
        self.language = None
        self.init = None
        self.sensors = OrderedDict()
        self.goal = None
        self.actions = OrderedDict()
        self.metric = None

        # TODO Add axioms, state constraints, etc.

    def action(self, name, parameters, precondition, effects):
        if name in self.actions:
            raise DuplicateActionDefinition(name, self.actions[name])

        self.actions[name] = Action(self.language, name, parameters, precondition, effects)
        return self.actions[name]

    def has_action(self, name):
        return name in self.actions

    def get_action(self, name):
        if not self.has_action(name):
            raise UndefinedAction(name)
        return self.actions[name]

    def __str__(self):
        return 'FSTRIPS Contingent Problem "{}", domain "{}"'.format(self.name, self.domain_name)

    __repr__ = __str__
