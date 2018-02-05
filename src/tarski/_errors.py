# -*- coding: utf-8 -*-


class LanguageError(Exception):
    pass

class SortAlreadyDefined(LanguageError) :
    pass

class UndefinedSort(LanguageError) :
    pass
