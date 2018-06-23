# -*- coding: utf-8 -*-
from ..errors import TarskiError, DuplicateDefinition, UndefinedElement


class IncompleteProblemError(TarskiError):
    def __init__(self, problem, msg=None):
        msg = msg or 'specification is incomplete!'
        super().__init__('Problem "{}": {}'.format(problem.name, msg))


class DuplicateActionDefinition(DuplicateDefinition):
    pass


class UndefinedAction(UndefinedElement):
    pass
