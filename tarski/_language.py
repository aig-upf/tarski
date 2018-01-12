# -*- coding: utf-8 -*-

class Sort :

    def __init__(self, name, lang) :
        self._name = name
        self._language = lang
        self._domain = {}

    @property
    def name(self) :
        return self._name

class Constant :

    def __init__(self, name, sort, lang ) :

        self._name = name
        self._sort = sort
        self._sort._domain[name] = self
        self._lang = lang

    @property
    def name(self) :
        return self._name


class FOL :

    def __init__(self) :
        self._sorts = {}
        self._constants = {}
        pass

    def sort( self, name ) :
        """
            Creates instance of Sort object, adds it to the table of
            sorts
        """
        sort_obj = Sort(name, self)
        self._sorts[name] = sort_obj
        return sort_obj

    def const( self, name, sort ) :
        """
            Creates constant symbol of a given sort
        """
        const_sym = Constant(name, sort)
        return const_sym
