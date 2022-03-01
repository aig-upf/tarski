"""
    SAS+ Actions - lean implementation

    Key characteristics:
        - No difference is made between causal laws describing change of values or their persistence
        - Representation of action costs is not baked into the class
"""
from typing import Union
from tarski.syntax import Term, symref


class InvalidEffectDefinition(Exception):
    pass


def wrap_term(t: Union[Term, None]):
    if t is None:
        return t
    return symref(t)


class Effect:

    def __init__(self, **kwargs):
        self._var = kwargs['var']
        self._pre = wrap_term(kwargs['pre'])
        self._post = wrap_term(kwargs['post'])
        self.tuple = (self.var.id, self.var.index(self._pre), self.var.index(self._post))

    @property
    def var(self):
        return self._var

    @property
    def pre(self):
        return self._pre

    @property
    def post(self):
        return self._post

    def __eq__(self, other):
        return self.var.id == other.var.id and self.pre == other.pre and self.post == other.post

    def __hash__(self):
        return hash(self.tuple)


class Action:

    def __init__(self, **kwargs):
        self._name = kwargs.get('name', None)
        self._effects = kwargs.get('effects', [])
        for eff in self._effects:
            if not isinstance(eff, Effect):
                raise RuntimeError("Action effect has invalid type: got: {} expected: Effect".format(type(eff)))

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

