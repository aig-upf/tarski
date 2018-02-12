# -*- coding: utf-8 -*-
from .errors import LanguageError
from ._sorts import Sort
from ._terms import Constant


class Predicate(object):
    def __init__(self, name, language, *args):

        self._symbol = name  # name, a string
        self.language = language  # fol the symbol belongs to
        self.type = []

        # we validate the arguments now
        for k, a in enumerate(args):
            if not isinstance(a, Sort):
                raise LanguageError("Predicate.__init__() : arguments need \
                to be of type 'Sort', {}-th argument '{}' is of type '{}''".format(k + 1, a, type(a)))
            if self.language != a.language:
                raise LanguageError("Predicate.__init__(): {}-th argument \
                belongs to a different language".format(k + 1))
            self.type.append(a)

    @property
    def symbol(self):
        return self._symbol

    @property
    def signature(self):
        return tuple([self.symbol] + [a.name for a in self.type])

    @property
    def arity(self):
        return len(self.type)

    def __str__(self):
        return '{}({})'.format(self.symbol, ','.join([a.name for a in self.type]))

    def dump(self):
        return dict(symbol=self.symbol, type=[a.name for a in self.type])

    def __call__(self, *args):
        from ._formulas import Atom
        return Atom(self, args)

    def check_arguments(self, *args):
        if len(args) != self.arity:
            raise LanguageError('Error setting predicate  extension: arity of {} is {}, {} arguments given'.
                                format(self.symbol, self.arity, len(args)))

        for k, arg in enumerate(args):
            if not isinstance(arg, Constant):
                raise LanguageError('Error setting predicate extension: {}-th argument is not a constant'.format(k + 1))
            if arg.type.name != self.type[k].name:
                raise LanguageError('Error setting predicate extension: {}-th argument type mismatch, type is {}, '
                                    'was expected to be {}'.format(k + 1, arg.type.name, self.type[k].name))

    def satisfied(self, *args):
        raise ValueError("Extensionally defined")
