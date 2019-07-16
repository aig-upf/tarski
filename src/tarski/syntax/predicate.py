
from ..errors import LanguageError
from .sorts import Sort
from .terms import Constant


class Predicate:
    def __init__(self, name, language, *args):

        self._symbol = name  # name, a string
        self.language = language  # fol the symbol belongs to
        self.sort = []
        self.builtin = False

        # we validate the arguments now
        for k, a in enumerate(args):
            if not isinstance(a, Sort):
                raise LanguageError("Predicate.__init__() : arguments need \
                to be of type 'Sort', {}-th argument '{}' is of type '{}''".format(k + 1, a, type(a)))
            if self.language != a.language:
                raise LanguageError("Predicate.__init__(): {}-th argument \
                belongs to a different language".format(k + 1))
            self.sort.append(a)

    @property
    def symbol(self):
        return self._symbol

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

    # def __str__(self):
    #     return '{}({})'.format(self.symbol, ','.join([a.name for a in self.sort]))

    def __hash__(self):
        return hash(self.signature)

    def __eq__(self, other):
        return self.signature == other.signature

    def __str__(self):
        return "{}/{}".format(self.symbol, self.arity)

    __repr__ = __str__

    def dump(self):
        return dict(symbol=self.symbol, sort=[a.name for a in self.sort])

    def __call__(self, *args):
        from .formulas import Atom
        return Atom(self, args)

    def check_arguments(self, *args):
        if len(args) != self.arity:
            raise LanguageError('Error setting predicate  extension: arity of {} is {}, {} arguments given'.
                                format(self.symbol, self.arity, len(args)))

        for k, arg in enumerate(args):
            if not isinstance(arg, Constant):
                raise LanguageError('Error setting predicate extension: {}-th argument is not a constant'.format(k + 1))
            if arg.sort.name != self.sort[k].name:
                raise LanguageError('Error setting predicate extension: {}-th argument type mismatch, type is {}, '
                                    'was expected to be {}'.format(k + 1, arg.sort.name, self.sort[k].name))

    def satisfied(self, *args):
        # pylint: disable=unused-argument
        raise ValueError("Extensionally defined")
