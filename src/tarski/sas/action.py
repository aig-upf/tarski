"""
    SAS+ Actions - lean implementation

    Key characteristics:
        - No difference is made between causal laws describing change of values or their persistence
        - Representation of action costs is not baked into the class
"""
import typing
from tarski.syntax import Term


class Action(object):

    def __init__(self, **kwargs):
        self._name = kwargs.get('name', None)
        self._effects = kwargs.get('effects', [])

    @property
    def name(self):
        return self.name

    @property
    def effects(self):
        return self._effects

    def add_effect(self, variable: Term, v0: Term, v1: Term):
        """
        Adds a new causal law (effect) to the action. It is not checked whether this law is already
        considered in the action description
        :param variable: A `Term` instance that models the state variable/parameter relevant to this law
        :param v0: A `Term` instance that corresponds to the value of `variable` required during the execution of
        the action
        :param v1: A `Term` instance that corresponds to the value of `variable` when the execution of the action
        has finished
        :return:
        """
        self._effects += [(variable, v0, v1)]

