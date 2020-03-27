
from ..errors import LanguageError, LanguageMismatch
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
        for k, a in enumerate(self.domain + (self.codomain, )):
            if not isinstance(a, Sort):
                raise LanguageError(f"Function arg #{k} ('{a}') is a '{type(a)}' instead of a Sort")

            if self.language != a.language:
                raise LanguageMismatch(a, a.language, self.language)

    @property
    def symbol(self):
        return self.name

    @property
    def signature(self):
        return (self.name,) + tuple(a.name for a in self.sort)

    @property
    def arity(self):
        return len(self.domain)

    def uniform_arity(self):
        return len(self.domain) + 1

    @property
    def sort(self):
        return self.domain + (self.codomain, )

    def dump(self):
        return dict(symbol=self.name,
                    domain=[a.name for a in self.domain],
                    codomain=self.codomain.name)

    def __hash__(self):
        return hash(self.signature)

    def __eq__(self, other):
        return self.signature == other.signature

    def __str__(self):
        return f"{self.name}/{self.arity}"
    __repr__ = __str__

    def __call__(self, *args):
        from .terms import CompoundTerm
        return CompoundTerm(self, args)