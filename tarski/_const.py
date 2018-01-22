# -*- coding: utf-8 -*-

from ._sorts import Sort

class Constant :

    def __init__(self, name : str , sort : Sort , lang ) :

        self._name = name
        self._sort = sort
        self._sort._domain[name] = self
        self._lang = lang

    @property
    def name(self) :
        return self._name

    @property
    def sort(self) :
        return self._sort
