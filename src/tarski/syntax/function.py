# -*- coding: utf-8 -*-

from tarski.errors import LanguageError
from .sorts import Sort
from tarski import errors as err


class Function(object):
    def __init__(self, symbol, language, *args):
        self.symbol = symbol
        self.language = language
        self.domain = tuple(args[:-1])
        self.codomain = args[-1]

        self._check_well_formed()

    def _check_well_formed(self):

        for k, a in enumerate(self.domain):
            if not isinstance(a, Sort):
                raise LanguageError("Function.__init__() : arguments need \
                to be of type 'Sort', {}-th argument '{}' is of type '{}''".format(k + 1, a, type(a)))

            if self.language != a.language:
                raise err.LanguageMismatch(a, a.language, self.language)

    @property
    def signature(self):
        return tuple([self.symbol] + [a.name for a in self.domain] + [self.codomain.name])

    @property
    def arity(self):
        return len(self.domain)

    @property
    def sort(self):
        return self.domain + (self.codomain, )

    def __str__(self):
        return '{}({})'.format(self.symbol, ','.join([a.name for a in self.domain]))

    def dump(self):
        return dict(symbol=self.symbol,
                    domain=[a.name for a in self.domain],
                    codomain=self.codomain.name)

    def __call__(self, *args):
        from .terms import CompoundTerm
        return CompoundTerm(self, args)
