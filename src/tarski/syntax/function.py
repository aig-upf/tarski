
import itertools

from .. import errors as err
from .terms import CompoundTerm
from .sorts import Sort


class Function:
    def __init__(self, name, language, *args):
        self.name = name
        self.language = language
        self.domain = tuple(args[:-1])
        self.codomain = args[-1]
        self.builtin = False
        self._check_well_formed()

    def _check_well_formed(self):
        for k, a in enumerate(itertools.chain(self.domain, [self.codomain])):
            if not isinstance(a, Sort):
                raise err.LanguageError(f"Function arg #{k} ('{a}') is a '{type(a)}' instead of a Sort")

            if self.language != a.language:
                raise err.LanguageMismatch(a, a.language, self.language)

    @property
    def symbol(self):
        return self.name

    @property
    def signature(self):
        return tuple([self.name] + [a.name for a in self.domain] + [self.codomain.name])

    @property
    def arity(self):
        return len(self.domain)

    @property
    def sort(self):
        return self.domain + (self.codomain, )

    def __hash__(self):
        return hash(self.signature)

    def dump(self):
        return dict(symbol=self.name,
                    domain=[a.name for a in self.domain],
                    codomain=self.codomain.name)

    def uniform_arity(self):
        return len(self.domain) + 1

    def __eq__(self, other):
        return self.signature == other.signature

    def __call__(self, *args):
        return CompoundTerm(self, args)

    def __str__(self):
        return "{}".format(self.name)
        # return "{}/{}".format(self.name, self.arity)

    __repr__ = __str__
