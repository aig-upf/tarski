from ..syntax.ops import flatten
from .fstrips import AddEffect, DelEffect


class Action:
    """ A (possibly lifted) planning action """

    def __init__(self, language, name, parameters, precondition, effects, cost=None):
        self.name = name
        self.language = language
        self.parameters = parameters
        self.precondition = precondition
        self.effects = effects
        self.cost = cost

    def __lt__(self, other):
        return self.name < other.name

    def ident(self):
        paramlist = "{}".format(','.join("{}: {}".format(p.symbol, p.sort.name) for p in self.parameters))
        return f'{self.name}({paramlist})'

    def __str__(self):
        return self.ident()
    __repr__ = __str__

    def print(self):
        tokens = ['{}:'.format(self.ident()),
                  'pre=({})'.format(self.precondition),
                  'eff=({})'.format(' & '.join(str(eff) for eff in self.effects))]
        return '\n'.join(tokens)


class GroundOperator:
    """ A planning operator, i.e. a parameter-free action """
    def __init__(self, language, name):
        self.name = name  # The action name is assumed to contain parameter bindings, if any!
        self.language = language

    def ident(self):
        return self.name

    def __str__(self):
        return self.ident()
    __repr__ = __str__


class PlainOperator(GroundOperator):
    """ A ground STRIPS operator possibly extended with negated preconditions
    and conditional effects. """
    def __init__(self, language, name, precondition, effects):
        super().__init__(language, name)
        self.precondition = flatten(precondition)
        self.effects = effects
        # self.validate(self)


class AdditiveActionCost(object):
    def __init__(self, addend):
        self.addend = addend

    def __str__(self):
        return str(self.addend)
    __repr__ = __str__


def generate_zero_action_cost(lang):
    return AdditiveActionCost(lang.constant(0, lang.get_sort('Integer')))
