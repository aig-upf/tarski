
from ..errors import LanguageError, LanguageMismatch
from .sorts import Sort


class Predicate:
    def __init__(self, name, language, *args):
        self.name = name
        self.language = language
        self.sort = []
        self.builtin = False

        # Validate the arguments
        for k, a in enumerate(args):
            if not isinstance(a, Sort):
                raise LanguageError(f"Predicate arg #{k} ('{a}') is a '{type(a)}' instead of a Sort")
            if self.language != a.language:
                raise LanguageMismatch(a, a.language, self.language)
            self.sort.append(a)

    @property
    def symbol(self):
        return self.name

    @property
    def signature(self):
        return tuple([self.symbol] + [a.name for a in self.sort])

    @property
    def arity(self):
        return len(self.sort)

    def uniform_arity(self):
        return len(self.sort)

    @property
    def domain(self):
        return self.sort

    def __hash__(self):
        return hash(self.signature)

    def __eq__(self, other):
        return self.signature == other.signature

    def __str__(self):
        # return "{}/{}".format(self.symbol, self.arity)
        return "{}/{}".format(self.name, self.arity)

    __repr__ = __str__

    def dump(self):
        return dict(symbol=self.name, sort=[a.name for a in self.sort])

    def __call__(self, *args):
        from .formulas import Atom
        return Atom(self, args)
