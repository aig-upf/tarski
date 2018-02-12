# -*- coding: utf-8 -*-


class TarskiError(Exception):
    """ Common ancestor class to all of Tarski's exceptions """
    pass


class LanguageError(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'Unexplained Tarski language error'
        super().__init__(msg)


class MismatchingLanguage(LanguageError):
    def __init__(self, obj, l1, l2, msg=None):
        msg = msg or ('Language mismatch when operating on object {obj} of type {classname}.\n'
                      'Object\'s language: {l1}\n'
                      'Base language: : {l2}\n')\
            .format(obj=obj, classname=type(obj).__name__, l1=l1, l2=l2)
        super().__init__(msg)


class DuplicateDefinition(LanguageError):
    def __init__(self, name, other, msg=None):
        msg = msg or 'Duplicate definition of element "{}": "{}"'.format(name, other)
        super().__init__(msg)
        self.name = name
        self.other = other


class UndefinedElement(LanguageError):
    def __init__(self, name, msg=None):
        msg = msg or 'Undefined element "{}"'.format(name)
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
