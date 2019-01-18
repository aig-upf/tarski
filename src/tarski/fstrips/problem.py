# -*- coding: utf-8 -*-
from collections import OrderedDict

from .. import model
from .action import Action
from . import errors as err


class Problem:
    """ A Functional STRIPS problem """

    def __init__(self, problem_name=None, domain_name=None):
        self.name = problem_name
        self.domain_name = domain_name
        self.language = None
        self.init = None
        self.goal = None
        self.constraints = []
        self.actions = OrderedDict()
        self.metric = None

        # TODO Add axioms, state constraints, etc.

    def action(self, name, parameters, precondition, effects):
        if name in self.actions:
            raise err.DuplicateActionDefinition(name, self.actions[name])

        self.actions[name] = Action(self.language, name, parameters, precondition, effects)
        return self.actions[name]

    def has_action(self, name):
        return name in self.actions

    def get_action(self, name):
        if not self.has_action(name):
            raise err.UndefinedAction(name)
        return self.actions[name]

    def __str__(self):
        return 'FSTRIPS Problem "{}", domain "{}"'.format(self.name, self.domain_name)

    __repr__ = __str__


def create_fstrips_problem(language, problem_name=None, domain_name=None):
    """ Creates an FSTRIPS problem with empty initial state and with no assigned goal """
    problem_name = problem_name or "Unnamed FSTRIPS problem"
    domain_name = domain_name or "Unnamed FSTRIPS domain"
    problem = Problem(problem_name=problem_name, domain_name=domain_name)
    problem.language = language
    problem.init = model.create(language)
    return problem
