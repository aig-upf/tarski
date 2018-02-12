# -*- coding: utf-8 -*-
from collections import OrderedDict

from ..errors import DuplicateActionDefinition, UndefinedAction
from . import Action


class Problem(object):
    """ A Functional STRIPS problem """

    def __init__(self, name, language, init, goal, actions=None):
        self._name = name
        self.language = language
        self.init = init
        self.goal = goal

        self.actions = OrderedDict(actions) if actions is not None else OrderedDict()

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
