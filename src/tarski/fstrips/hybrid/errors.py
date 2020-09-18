
from ... errors import DuplicateDefinition, UndefinedElement, SyntacticError


class DuplicateReactionDefinition(DuplicateDefinition):
    pass


class UndefinedReaction(UndefinedElement):
    pass


class DuplicateDifferentialConstraintDefinition(DuplicateDefinition):
    pass


class UndefinedDifferentialConstraint(UndefinedElement):
    pass


class InvalidDifferentialConstraintDefinition(SyntacticError):

    def __init__(self, culprit, msg):
        super().__init__(msg=f"Invalid Differential Constraint\n'{culprit}' {msg}")
