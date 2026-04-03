from ..errors import DuplicateDefinition, TarskiError, UndefinedElement


class IncompleteProblemError(TarskiError):
    def __init__(self, problem, msg=None):
        msg = msg or "specification is incomplete!"
        super().__init__(f'Problem "{problem.name}": {msg}')


class InvalidEffectError(TarskiError):
    def __init__(self, effect, msg=None):
        msg = msg or f'definition of effect "{effect.tostring()}" is invalid!'
        super().__init__(f"{msg}")


class DuplicateActionDefinition(DuplicateDefinition):
    pass


class DuplicateDerivedDefinition(DuplicateDefinition):
    pass


class UndefinedAction(UndefinedElement):
    pass


class InvalidDerivedPredicateError(TarskiError):
    def __init__(self, symbol, formula, msg=None):
        if msg is None:
            msg = " "

        msg = f'definition of derived predicate "{symbol} \\equiv {formula}" is invalid! {msg}'
        super().__init__(msg)
