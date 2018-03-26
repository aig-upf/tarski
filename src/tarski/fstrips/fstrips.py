# -*- coding: utf-8 -*-
from collections import OrderedDict

from .. import fol
from ..syntax import Formula, Tautology

from ..errors import DuplicateActionDefinition, UndefinedAction

class Effect(object):
    pass


class UniversalEffect(Effect):
    """ A forall-effect """
    def __init__(self, variables, effects):
        self.variables = variables
        self.effects = effects

    def __str__(self):
        return "forall ({}) : ({})".format(self.variables, ', '.join(self.effects))

    __repr__ = __str__


class SingleEffect(Effect):
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return "({} -> {})".format(self.condition, self.tostring())

    __repr__ = __str__

    def tostring(self):
        raise NotImplementedError("To be subclassed")


class AddEffect(SingleEffect):
    def __init__(self, atom, condition=Tautology):
        super().__init__(condition)
        self.atom = atom

    def tostring(self):
        return "ADD({})".format(self.atom)


class DelEffect(SingleEffect):
    def __init__(self, atom, condition=Tautology):
        super().__init__(condition)
        self.atom = atom

    def tostring(self):
        return "DEL({})".format(self.atom)


class FunctionalEffect(SingleEffect):
    def __init__(self, lhs, rhs, condition=Tautology):
        super().__init__(condition)
        self.lhs = lhs
        self.rhs = rhs

    def tostring(self):
        return "{} := {}".format(self.lhs, self.rhs)


def language(name="L"):
    """ Create an FSTRIPS-oriented First-Order Language.
        This is a standard FOL with a few convenient add-ons.
    """
    lang = fol.language(name)
    lang.register_operator_handler("<<", fol.Term, fol.Term, lambda lhs, rhs: FunctionalEffect(lhs, rhs))
    return lang
