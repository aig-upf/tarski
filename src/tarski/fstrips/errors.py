
from ..errors import TarskiError, DuplicateDefinition, UndefinedElement


class IncompleteProblemError(TarskiError):
    def __init__(self, problem, msg=None):
        msg = msg or 'specification is incomplete!'
        super().__init__('Problem "{}": {}'.format(problem.name, msg))


class InvalidEffectError(TarskiError):
    def __init__(self, effect, msg=None):
        msg = msg or 'definition of effect "{}" is invalid!'.format(effect.tostring())
        super().__init__('{}'.format(msg))


class DuplicateActionDefinition(DuplicateDefinition):
    pass


class DuplicateDerivedDefinition(DuplicateDefinition):
    pass


class UndefinedAction(UndefinedElement):
    pass


class InvalidDerivedPredicateError(TarskiError):
    def __init__(self, symbol, formula, msg=None):
        if msg is None:
            msg = ' '

        msg = 'definition of derived predicate "{} \\equiv {}" is invalid! {}'.format(symbol, formula, msg)
        super().__init__(msg)
