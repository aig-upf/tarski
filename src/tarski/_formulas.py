# -*- coding: utf-8 -*-
from ._errors import LanguageError
from ._terms import Term, Variable

from typing import List
import copy
from abc import *


class Formula(ABC):
    def __init__(self):
        pass

    def is_tautology(self):
        return False

    def is_contradiction(self):
        return False

    def __str__(self):
        raise RuntimeError("Abstract Method Formula.__str__ was called!")

    # MRJ: shallow and deep copy are implemented to cover all subclasses
    def __copy__(self):
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        return newone

    def __deepcopy__(self, memo):
        cls = self.__class__
        newone = type(self)()
        memo[id(self)] = newone
        for k, v in self.__dict__.items():
            setattr(newone, k, copy.deepcopy(v, memo))
        return newone

    def __and__(self, rhs):
        return Conjunction(self, rhs)

    def __or__(self, rhs):
        return Disjunction(self, rhs)

    def __invert__(self):
        return Negation(self)

    def __gt__(self, rhs):
        return implies(self, rhs)

    @abstractmethod
    def satisfiable(self, s):
        pass


class AtomicFormula(Formula):
    def __init__(self, *args):
        self._subterms = []
        for a in args:
            if not isinstance(a, Term):
                raise LanguageError(
                    "Atomic formulae can only be defined over Terms, found argument of type '{}' ".format(type(a)))
            self._subterms.append(a)

    @property
    def subterms(self):
        return self._subterms

    @abstractmethod
    def satisfiable(self, s):
        pass


class RelationalFormula(AtomicFormula):
    def __init__(self, *args):
        terms = args[1:]
        super(RelationalFormula, self).__init__(*terms)
        self._symbol = args[0]

    @property
    def symbol(self):
        return self._symbol

    def __str__(self):
        return '{}({})'.format(self.symbol, ','.join([str(t) for t in self.subterms]))

    def satisfiable(self, s):
        return s.evaluate((self.symbol, self.subterms))


class AxiomaticFormula(Formula):
    def __init__(self, head, body):
        if not isinstance(head, Formula):
            raise LanguageError("The head of an axiomatic formulae can only be a Formula, was '{}'".format(type(head)))
        self._head = head
        if not isinstance(body, Formula):
            raise LanguageError("The body of an axiomatic formulae can only be a Formula, was '{}'".format(type(body)))
        self._body = body

    def __str__(self):
        return '{} :- {}'.format(self._head, self._body)

    def satisfiable(self, s):
        return s.check_satisfiability(implies(self._head, self._body)) and \
               s.check_satisfiability(implies(self._body, self._head))


axiom = AxiomaticFormula


class ExternallyDefinedFormula(Formula):
    def __init__(self, *args):
        super(ExternallyDefinedFormula, self).__init__(*args)

    @property
    def name(self):
        return self._name

    def __str__(self):
        return '{}({})'.format(self.name, ','.join([str(t) for t in self._subterms]))


def satisfiable(self, s):
    raise RuntimeError("AxiomaticFormula.satisfiable() : not implemented yet")


class Tautology(Formula):
    def __init__(self):
        pass

    def is_tautology(self): return True

    def is_contradiction(self): return False

    def satisfiable(self, s): return True


top = Tautology()


class Contradiction(Formula):
    def __init__(self):
        pass

    def is_tautology(self): return False

    def is_contradiction(self): return True

    def satisfiable(self, s): return False


bot = Contradiction()


class OpenFormula(Formula):
    def __init__(self, *args):
        self._subformulae = []
        for f in args:
            if not isinstance(f, Formula):
                raise LanguageError(
                    "Open formulae can only be defined over Formulas, found argument of type '{}' ".format(type(f)))
            self._subformulae.append(f)

    @property
    def name(self):
        return self._name

    @property
    def subformulae(self):
        for f in self._subformulae:
            yield f

    @property
    def subformula(self):
        return self._subformulae

    def __str__(self):
        return '{}({})'.format(self.name, ','.join([str(f) for f in self.subformulae]))


class Conjunction(OpenFormula):
    def __init(self, *args):
        if len(args) < 2:
            raise LanguageError('Formula is not well formed: Conjunction requires at least two subformulas')
        super(Conjunction, self).__init__(*args)
        self._name = 'and'

    def satisfiable(self, s):
        return s.check_satisfiability(self.subformula[0]) and \
               s.check_satisfiability(self.subformula[1])


def land(*args):
    if len(args) < 2:
        raise LanguageError('Conjunction requires at least two subformulas')
    args = list(args)
    rhs = args.pop()
    lhs = args.pop()
    rhs = Conjunction(lhs, rhs)
    while len(args) > 0:
        lhs = args.pop()
        rhs = Conjunction(lhs, rhs)

    return rhs


class Disjunction(OpenFormula):
    def __init__(self, *args):
        if len(args) < 2:
            raise LanguageError('Formula is not well formed: Disjunction requires at least two subformulas')
        super(Disjunction, self).__init__(*args)
        self._name = 'or'

    def satisfiable(self, s):
        return s.check_satisfiability(self.subformula[0]) or \
               s.check_satisfiability(self.subformula[1])


def lor(*args):
    if len(args) < 2:
        raise LanguageError('Conjunction requires at least two subformulas')
    args = list(args)
    rhs = args.pop()
    lhs = args.pop()
    rhs = Disjunction(lhs, rhs)
    while len(args) > 0:
        lhs = args.pop()
        rhs = Disjunction(lhs, rhs)
    return rhs


class Negation(OpenFormula):
    def __init__(self, *args):
        if len(args) != 1:
            raise LanguageError("Formula is not well formed: Negation admits only one subformula")
        super(Negation, self).__init__(*args)
        self._name = 'neg'

    def satisfiable(self, s):
        return ~s.check_satisfiability(self.subformula[0])


def neg(phi):
    return Negation(phi)


def implies(phi, psi):
    return Disjunction(Negation(phi), psi)


class QuantifiedFormula(Formula):
    def __init__(self, varset: List[Variable], phi: Formula):
        self._vars = varset
        self._phi = phi

    @property
    def subformula(self):
        return self._phi

    @property
    def vars(self):
        return self._vars


class ExistentiallyQuantifiedFormula(QuantifiedFormula):
    def __init__(self, varset: List[Variable], phi: Formula):
        super(ExistentiallyQuantifiedFormula, self).__init__(varset, phi)

    def __str__(self):
        return 'Exists {} : {}'.format(' '.join([str(x) for x in self.vars]), str(self.subformula))

    def satisfiable(self, s):
        raise RuntimeError("ExistentiallyQuantifiedFormula.satisifed() : not implemented yet")


def exists(*args):
    if len(args) < 2:
        raise LanguageError('Existential quantification needs at least two arguments')
    phi = args[-1]
    if not isinstance(phi, Formula):
        raise LanguageError('Last argument to exist(...) needs to be a formula')
    vars = args[:-1]
    for x in vars:
        if not isinstance(x, Variable):
            raise LanguageError('Every other argument of exist(...) but the last needs to be a variable')
    return ExistentiallyQuantifiedFormula(vars, phi)


class UniversallyQuantifiedFormula(QuantifiedFormula):
    def __init__(self, varset: List[Variable], phi: Formula):
        super(UniversallyQuantifiedFormula, self).__init__(varset, phi)

    def __str__(self):
        return 'Forall {} : {}'.format(' '.join([str(x) for x in self.vars]), str(self.subformula))

    def satisfiable(self, s):
        return not s.check_satisfiability(exists(x for x in self._vars + [self._phi]))


def forall(*args):
    if len(args) < 2:
        raise LanguageError('Universal quantification needs at least two arguments')
    phi = args[-1]
    if not isinstance(phi, Formula):
        raise LanguageError('Last argument to forall(...) needs to be a formula')
    vars = args[:-1]
    for x in vars:
        if not isinstance(x, Variable):
            raise LanguageError('Every other argument of exist(...) but the last needs to be a variable')
    return UniversallyQuantifiedFormula(vars, phi)
