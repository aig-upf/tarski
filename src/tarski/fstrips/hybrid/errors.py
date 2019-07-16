
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
        error_msg = "Invalid Differential Constraint\n'{}' {}".format(str(culprit), msg)
        super().__init__(self, msg=error_msg)
