# -*- coding: utf-8 -*-
from collections import OrderedDict

from .. import fol
from ..syntax import Formula, Tautology

from ..errors import DuplicateActionDefinition, UndefinedAction


class Action(object):
    """ A (possibly lifted) planning action """

    def __init__(self, language, name, parameters, precondition, effects):
        self.name = name
        self.language = language
        self.parameters = parameters
        self.precondition = precondition
        self.effects = effects

    def dump(self):
        return dict(name=self.name,
                    params=[par.dump() for par in self.parameters],
                    precondition=self.precondition.dump(),
                    effects=[eff.dump() for eff in self.effects.dump()])

    def __str__(self):
        tokens = ['action {}:'.format(self.name),
                  'pre=({})'.format(self.precondition),
                  'eff=({})'.format(' & '.join(str(eff) for eff in self.effects))]
        return '\n'.join(tokens)


class Problem(object):
    """ A Functional STRIPS problem """

    def __init__(self):
        self.name = None
        self.domain_name = None
        self.language = None
        self.init = None
        self.goal = None
        self.actions = OrderedDict()

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
        return 'FSTRIPS Problem "{}", domain "{}"'.format(self.name, self.domain_name)

    __repr__ = __str__


class UniversalEffect(object):
    """ A forall-effect """
    def __init__(self, variables, effects):
        self.variables = variables
        self.effects = effects

    def __str__(self):
        return "forall ({}) : ({})".format(self.variables, ', '.join(self.effects))

    __repr__ = __str__


class SingleEffect(object):
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
    lang.register_operator_handler("<<", fol.Term, fol.Term, lambda lhs, rhs: FunctionalEffect(rhs, lhs))  # Inverted
    return lang
