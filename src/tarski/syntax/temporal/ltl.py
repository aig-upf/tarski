
from enum import Enum
from ... import errors as err
from ..formulas import Formula, Connective, CompoundFormula, lor


class TemporalConnective(Enum):
    X, F, G, U, R = range(5)

    def __str__(self):
        return self.name


class TemporalCompoundFormula(CompoundFormula):

    def __init(self, conn, sub):
        super().__init__(conn, sub)

    def _check_well_formed(self):
        if any(not isinstance(f, Formula) for f in self.subformulas):
            raise err.LanguageError("Wrong argument types for compound formula: '{}' ".format(self.subformulas))

        if self.connective == Connective.Not or \
                self.connective in (TemporalConnective.X, TemporalConnective.F, TemporalConnective.G):
            if len(self.subformulas) != 1:
                raise err.LanguageError("{} admits only one subformula".format(str(self.connective)))
        elif len(self.subformulas) < 2:
            raise err.LanguageError("{} requires at least two subformulas".format(str(self.connective)))

    def __str__(self):
        if self.connective == Connective.Not or \
                self.connective in (TemporalConnective.X, TemporalConnective.F, TemporalConnective.G):
            assert len(self.subformulas) == 1
            return "{} ({})".format(self.connective, str(self.subformulas[0]))

        inner = " {} ".format(self.connective).join(str(f) for f in self.subformulas)
        return "({})".format(inner)


def X(arg):
    return TemporalCompoundFormula(TemporalConnective.X, [arg])


def F(arg):
    return TemporalCompoundFormula(TemporalConnective.F, [arg])


def G(arg):
    return TemporalCompoundFormula(TemporalConnective.G, [arg])


def U(*args):
    return TemporalCompoundFormula(TemporalConnective.U, args)


def R(*args):
    return TemporalCompoundFormula(TemporalConnective.R, args)


def W(*args):
    return lor(U(args), G(args[0]))
    # return CompoundFormula(TemporalConnective.W, args)
