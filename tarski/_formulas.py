# -*- coding: utf-8 -*-
from ._errors import LanguageError
from ._terms import Term, Variable, Constant

from enum import Enum

class RelationalFormulaSymbol(Enum) :
    EQ = "="
    NEQ = "!="
    LT = "<"
    LEQ = "<="
    GT = ">"
    GEQ = ">="



class Formula(object) :

    def __init__(self) :
        pass


    def is_tautology(self) :
        return False


    def is_contradiction(self) :
        return False

    def __str__(self) :
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
            setattr(newone, k, deepcopy(v, memo))
        return newone


class AtomicFormula(Formula) :

    def __init__(self, *args ) :
        self._subterms = []
        for a in args :
            if not isinstance(a,Term):
                raise LanguageError("Atomic formulae can only be defined over Terms, found argument of type '{}' ".format(type(a)))
            self._subterms.append(a)


class AxiomaticFormula(Formula) :

    def __init__(self, head, body) :
        if not isinstance(head,Formula) :
            raise LanguageError("The head of an axiomatic formulae can only be a Formula, was '{}'".format(type(head)))
        self._head = head
        if not isinstance(body, Formula) :
            raise LanguageError("The body of an axiomatic formulae can only be a Formula, was '{}'".format(type(body)))
        self._body = body

    def __str__(self) :
        return '{} :- {}'.format(self._head,self._body)

axiom = AxiomaticFormula

class ExternallyDefinedFormula(Formula) :

    def __init__(self, *args) :
        super(ExternallyDefinedFormula,self).__init__(*args)

    @property
    def name(self) :
        return self._name

    def __str__(self) :
        return '{}({})'.format(self.name, ','.join([str(t) for t in self._subterms]))

class Tautology(Formula) :

    def __init__(self) :
        pass

    def is_tautology(self) : return True

    def is_contradiction(self) : return False

top = Tautology()

class Contradiction(Formula) :

    def __init__(self) :
        pass

    def is_tautology(self) : return False

    def is_contradiction(self) : return True

bot = Contradiction()

class OpenFormula(Formula) :

    def __init__(self, *args ) :
        self._subformulae = []
        for f in args :
            if not isinstance(a,Formula):
                raise LanguageError("Open formulae can only be defined over Formulas, found argument of type '{}' ".format(type(a)))
            self._subformulae.append(f)

    @property
    def name(self) :
        self._name

    @property
    def subformulae(self) :
        for f in self._subformulae :
            yield f

    def __str__(self) :
        return '{}({})'.format(self.name, ','.join([str(f) for f in self.subformulae]))

class Conjunction(OpenFormula) :

    def __init(self, *args) :
        if len(args) < 2:
            raise LanguageError('Formula is not well formed: Conjunction requires at least two subformulas')
        super(Conjunction,self).__init__(*args)
        self._name = 'and'

def and( *args ) :
    if len(args) < 2:
        raise LanguageError('Conjunction requires at least two subformulas')
    rhs = args.pop()
    lhs = args.pop()
    rhs = Conjunction(lhs,rhs)
    while len(args) > 0 :
        lhs = args.pop()
        rhs = Conjunction(lhs,rhs)

    return rhs

class Disjunction(OpenFormula) :

    def __init(self, *args) :
        if len(args) < 2:
            raise LanguageError('Formula is not well formed: Disjunction requires at least two subformulas')
        super(Disjunction,self).__init__(*args)
        self._name = 'or'

def or( *args ) :
    if len(args) < 2:
        raise LanguageError('Conjunction requires at least two subformulas')
    rhs = args.pop()
    lhs = args.pop()
    rhs = Disjunction(lhs,rhs)
    while len(args) > 0 :
        lhs = args.pop()
        rhs = Disjunction(lhs,rhs)
    return rhs

class Negation(OpenFormula) :

    def __init__(self, *args) :
        if len(args) != 1 :
            raise LanguageError("Formula is not well formed: Negation admits only one subformula")
        super(Negation,self).__init__(*args)
