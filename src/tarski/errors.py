
class TarskiError(Exception):
    """ Common ancestor class to all of Tarski's exceptions """


class LanguageError(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'Unexplained Tarski language error'
        super().__init__(msg)


class SyntacticError(LanguageError):
    def __init__(self, msg=None):
        msg = msg or 'Unexplained Tarski syntactic error'
        super().__init__(msg)


class SemanticError(LanguageError):
    def __init__(self, msg=None):
        msg = msg or 'Unexplained Tarski semantic error'
        super().__init__(msg)


class LanguageMismatch(SyntacticError):
    def __init__(self, obj, l1, l2, msg=None):
        msg = msg or ('Language mismatch when operating on object {obj} of type {classname}.\n'
                      'Expected language: {l2}\n'
                      'Actual language: : {l1}\n') \
            .format(obj=obj, classname=type(obj).__name__, l1=l1, l2=l2)
        super().__init__(msg)


class ArityMismatch(SyntacticError):
    def __init__(self, head, arguments, msg=None):
        msg = msg or 'Arity mismatch applying element {} with arity {} to arguments {}'. \
            format(head, head.arity, arguments)
        super().__init__(msg)


class SortMismatch(SyntacticError):
    def __init__(self, element, type_, expected_type, msg=None):
        msg = msg or 'Sort mismatch on element {}. Expected sort was "{}", element has sort "{}"'.format(
            element, expected_type, type_)
        super().__init__(msg)


class DuplicateDefinition(SyntacticError):
    def __init__(self, name, other, msg=None):
        msg = msg or 'Duplicate definition of element "{}": "{}"'.format(name, other)
        super().__init__(msg)
        self.name = name
        self.other = other


class UndefinedElement(SyntacticError):
    def __init__(self, name, msg=None):
        if msg is not None:
            msg = 'Undefined element {}, {}'.format(name, msg)
        else:
            msg = 'Undefined element: {}'.format(name)
        super().__init__(msg)


class DuplicateSortDefinition(DuplicateDefinition):
    pass


class DuplicatePredicateDefinition(DuplicateDefinition):
    pass


class DuplicateFunctionDefinition(DuplicateDefinition):
    pass


class DuplicateConstantDefinition(DuplicateDefinition):
    pass


class DuplicateActionDefinition(DuplicateDefinition):
    pass


class DuplicateVariableDefinition(DuplicateDefinition):
    def __init__(self, variable, other, msg=None):
        msg = msg or "Variable with name '{}' already defined in binding: {}".format(variable.symbol, other)
        super().__init__(variable, other, msg)


class UndefinedTerm(UndefinedElement):
    pass


class UndefinedSort(UndefinedElement):
    pass


class UndefinedPredicate(UndefinedElement):
    pass


class UndefinedFunction(UndefinedElement):
    pass


class UndefinedConstant(UndefinedElement):
    pass


class UndefinedAction(UndefinedElement):
    pass


class UndefinedVariable(UndefinedElement):
    pass


class UnboundVariable(SemanticError):
    def __init__(self, var, msg=None):
        msg = msg or 'Attempted to evaluate open formula with free variable {}'.format(var)
        super().__init__(msg)


class IncorrectExtensionDefinition(SemanticError):
    def __init__(self, element, point, value, msg=None):
        msg = msg or 'Incorrect definition of extension of symbol "{}". Cannot assign value "{}" to point "{}"'.format(
            element, value, point)
        super().__init__(msg)


class UnknownTheory(LanguageError):
    def __init__(self, theory):
        super().__init__('Unknown first-order theory "{}"'.format(theory))


class CommandNotFoundError(TarskiError):
    def __init__(self, name, msg=None):
        msg = msg or 'Necessary command "{}" could not be found'.format(name)
        super().__init__(msg)


class ExternalCommandError(TarskiError):
    pass


# class WrongTermUsageError(TarskiError):
#     def __init__(self):
#         super().__init__("""Tarski terms overload the equality operator `__eq__` to allow the
#         construction of FOL atoms such as "loc(b1)==table". A side-effect of this is that Term objects cannot be
#         inserted as such into associative containers such as dictionaries or sets. In order to use those, you will
#         need to wrap the Term object with a call to `symref`, as e.g. in counter[symref(c)] = 2
#         """)
