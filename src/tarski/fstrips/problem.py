# -*- coding: utf-8 -*-
from collections import OrderedDict
from . action import Action
from . import errors as err

class Problem(object):
    """ A Functional STRIPS problem """

    def __init__(self, name = None, language = None, **kwargs):
        """
        A FSTRIPS Problem description. Constructor parameters are:

         - name: the name of the problem
         - language: FOL associated with the planning problem
         - init: initial state of the problem (required)
         - goal: formula specifying the set of goal states
         - constraints: the set of constraints that valid plans need to comply with
         before reaching a goal state
        """
        self.name = name
        self.language = language
        self.init = kwargs.get('init', None)
        self.goal = kwargs.get('goal', None)
        self.constraints = kwargs.get('constraints',[])
        actions = [ ( (a.name,tuple(a.parameters)) , a) for a in kwargs.get('actions',[])]
        self.actions = OrderedDict(actions) if actions is not None else OrderedDict()

        # TODO Add axioms, state constraints, etc.

    def __str__(self):
        return 'FSTRIPS Problem "{}", domain "{}"'.format(self.name, self.domain_name)

    __repr__ = __str__

    def action(self, name, parameters, precondition, effects):
        if name in self.actions:
            # @TODO: MRJ: check action signature, rather than just the name
            raise err.DuplicateActionDefinition(name, self.actions[name])

        self.actions[(name,tuple(parameters))] = Action(self.language, name, parameters, precondition, effects)
        return self.actions[(name,tuple(parameters))]

    def has_action(self, name):
        return name in self.actions

    def get_action(self, name):
        if not self.has_action(name):
            raise err.UndefinedAction(name)
        return self.actions[name]
