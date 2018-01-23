# -*- coding: utf-8 -*-
from ._errors import LanguageError
from ._sorts import Sort
from ._terms import Term

class Function(object) :

    def __init__(self, name, lang, *args ) :
        self._symbol = name # name, a string
        self._lang = lang # fol the symbol belongs to
        self._domain = []
        self._codomain = None

        # we validate the arguments now
        for k, a in enumerate(args) :
            if isinstance(type(a),Sort) :
                raise LanguageError("Function.__init__() : arguments need \
                to be of type 'Sort', {}-th argument '{}' is of type '{}''".format(k+1,a, type(a)))
            if self._lang != a.language  :
                raise LanguageError("Function.__init__(): {}-th argument \
                belongs to a different language".format(k+1))
            if k < len(args) - 1 :
                self._domain.append(a)
            else :
                self._codomain = a

    @property
    def symbol(self) :
        return self._symbol

    @property
    def signature(self) :
        return tuple([self.symbol] + [a.name for a in self.domain] + [self.codomain.name] )

    @property
    def arity(self) :
        return len(self._domain)

    @property
    def domain(self) :
        return tuple(self._domain)

    @property
    def codomain(self) :
        return self._codomain

    @property
    def type(self) :
        return self._codomain


    def __str__(self) :
        return '{}({})'.format(self.symbol, ','.join([ a.name for a in self._domain ]))

    def dump(self) :
        return dict(symbol=self.symbol, \
                    domain = [a.name for a in self.domain],\
                    codomain = self.codomain.name)

    def __call__(self, *args) :
        return Term(self, args)
