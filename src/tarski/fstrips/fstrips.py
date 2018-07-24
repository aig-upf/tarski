# -*- coding: utf-8 -*-
from .. import theories as tsk_theories
from ..syntax import Tautology, Term


class UniversalEffect:
    """ A forall-effect """

    def __init__(self, variables, effects):
        self.variables = variables
        self.effects = effects

    def __str__(self):
        return "forall ({}) : ({})".format(self.variables, ', '.join(self.effects))

    __repr__ = __str__


class SingleEffect:
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return "({} -> {})".format(self.condition, self.tostring())

    __repr__ = __str__

    def tostring(self):
        raise NotImplementedError("To be subclassed")


class AddEffect(SingleEffect):
    def __init__(self, atom, condition=Tautology()):
        super().__init__(condition)
        self.atom = atom

    def tostring(self):
        return "ADD({})".format(self.atom)


class DelEffect(SingleEffect):
    def __init__(self, atom, condition=Tautology()):
        super().__init__(condition)
        self.atom = atom

    def tostring(self):
        return "DEL({})".format(self.atom)


class FunctionalEffect(SingleEffect):
    def __init__(self, lhs, rhs, condition=Tautology()):
        super().__init__(condition)
        self.lhs = lhs
        self.rhs = rhs

    def tostring(self):
        return "{} := {}".format(self.lhs, self.rhs)


class LogicalEffect(SingleEffect):
    def __init__(self, phi, condition=Tautology()):
        super().__init__(condition)
        self.formula = phi

    def tostring(self):
        return "{}".format(self.formula)


class OptimizationMetric:
    def __init__(self, opt_expression, opt_type):
        self.opt_expression = opt_expression
        self.opt_type = opt_type


def language(name="Unnamed FOL Language", theories=None):
    """ Create an FSTRIPS-oriented First-Order Language.
        This is a standard FOL with a few convenient add-ons.
    """
    # By default, when defining a FSTRIPS problem we use a FOL with equality
    theories = theories or [tsk_theories.Theory.EQUALITY]
    lang = tsk_theories.language(name, theories)
    lang.register_operator_handler("<<", Term, Term, FunctionalEffect)
    lang.register_operator_handler(">>", Term, Term, lambda lhs, rhs: FunctionalEffect(rhs, lhs))  # Inverted
    return lang
