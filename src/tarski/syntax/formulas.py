# * coding: utf8 *
from collections import OrderedDict
from enum import Enum
from typing import List

from .. import errors as err
from .terms import Variable, Term
from .predicate import Predicate


class Connective(Enum):
    """" A logical connective """
    And, Or, Not = range(3)

    def __str__(self):
        return self.name.lower()


class Quantifier(Enum):
    """" A logical quantifier """
    Exists, Forall = range(2)
    to_string = ["exists", "forall"]

    def __str__(self):
        return self.name.lower()


class Formula:

    def __str__(self):
        raise RuntimeError("Abstract Method Formula.__str__ was called!")

    def __and__(self, rhs):
        return land(self, rhs)

    def __or__(self, rhs):
        return lor(self, rhs)

    def __invert__(self):
        return neg(self)

    def __gt__(self, rhs):
        return implies(self, rhs)

    def is_syntactically_equal(self, other):
        """ Strict syntactic equivalence, which would tipically be in `__eq__`,
        but here we use `__eq__` for a different purpose """
        raise NotImplementedError()  # To be subclassed


class Tautology(Formula):
    def __str__(self):
        return "T"

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__


class Contradiction(Formula):
    def __str__(self):
        return "F"

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__


class CompoundFormula(Formula):
    """ A set of formulas combined through some logical connective """

    def __init__(self, connective, subformulas):
        super().__init__()
        self.connective = connective
        self.subformulas = subformulas
        self._check_well_formed()

    def _check_well_formed(self):
        if any(not isinstance(f, Formula) for f in self.subformulas):
            raise err.LanguageError("Wrong argument types for compound formula: '{}' ".format(self.subformulas))

        if self.connective == Connective.Not:
            if len(self.subformulas) != 1:
                raise err.LanguageError("Negation admits only one subformula")
        elif len(self.subformulas) < 2:
            raise err.LanguageError("Conjunction and disjunction require at least two subformulas")

    def __str__(self):
        if self.connective == Connective.Not:
            assert len(self.subformulas) == 1
            return "{} ({})".format(self.connective, str(self.subformulas[0]))

        inner = " {} ".format(self.connective).join(str(f) for f in self.subformulas)
        return "({})".format(inner)

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ \
               and self.connective == other.connective \
               and all(x.is_syntactically_equal(y) for x, y in zip(self.subformulas, other.subformulas))


class QuantifiedFormula(Formula):
    def __init__(self, quantifier: Quantifier, variables: List[Variable], formula: Formula):
        self.quantifier = quantifier
        self.variables = variables
        self.formula = formula
        self._check_well_formed()

    def _check_well_formed(self):
        if len(self.variables) == 0:
            raise err.LanguageError("Quantified formula with no variable")

    def __str__(self):
        vars_ = ', '.join(str(x) for x in self.variables)
        return '{} {} : ({})'.format(self.quantifier, vars_, self.formula)

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ \
               and self.quantifier == other.quantifier \
               and all(x.is_syntactically_equal(y) for x, y in zip(self.variables, other.variables)) \
               and self.formula.is_syntactically_equal(other.formula)


top = Tautology()
bot = Contradiction()


def _to_binary_tree(args, connective):
    assert len(args) > 1
    phi = CompoundFormula(connective, (args[-2], args[-1]))
    for arg in reversed(args[:-2]):
        phi = CompoundFormula(connective, (arg, phi))
    return phi


def _create_compound(args, connective, binary):
    if binary:
        return _to_binary_tree(args, connective)
    return CompoundFormula(connective, args)


def land(*args, binary=True):
    """ Create an and-formula with the given subformulas. If binary is true, the and-formula will be shaped as a binary
     tree (e.g. (...((p1 and p2) and p3) and ...))), otherwise it will have a flat structure. This is an implementation
     detail, but might be relevant performance-wise when dealing with large structures """
    return _create_compound(args, Connective.And, binary)


def lor(*args, binary=True):
    """ Create an or-formula with the given subformulas. If binary is true, the or-formula will be shaped as a binary
    tree (e.g. (...((p1 or p2) or p3) or ...))), otherwise it will have a flat structure. This is an implementation
    detail, but might be relevant performance-wise when dealing with large structures """
    return _create_compound(args, Connective.Or, binary)


def neg(phi):
    return CompoundFormula(Connective.Not, [phi])


def implies(phi, psi):
    return lor(neg(phi), psi)


def equiv(phi, psi):
    # MRJ: I choose the form below in the code over
    #
    # lor(land(phi,psi), land(neg(psi),neg(phi)))
    #
    # as I find it easier to transform into a
    # given normal form.
    return land(implies(phi, psi), implies(psi, phi))


def forall(*args):
    return _quantified(Quantifier.Forall, *args)


def exists(*args):
    return _quantified(Quantifier.Exists, *args)


def _quantified(quantifier, *args):
    """ Create a quantified formula.

        'args' is expected to be of the form [v1, ..., vn, f], where v_i are the variables
        and f is the quantified formula.
    """
    if len(args) < 2:
        raise err.LanguageError('Quantified formula needs at least two arguments')

    variables, formula = args[:-1], args[-1]

    if not isinstance(formula, Formula):
        raise err.LanguageError('Illformed arguments for quantified formula: {}'.format(args))

    if not all(isinstance(x, Variable) for x in variables):
        raise err.LanguageError('Illformed arguments for quantified formula: {}'.format(args))

    return QuantifiedFormula(quantifier, variables, args[-1])


class Atom(Formula):
    """ A first-order atom """

    def __init__(self, predicate, arguments):
        super().__init__()
        self.predicate = predicate
        self.subterms = arguments
        self._check_well_formed()

    def _check_well_formed(self):
        head = self.predicate

        if not isinstance(head, Predicate):
            raise err.LanguageError("Incorrect atom head: '{}' ".format(head))

        # Check arities match
        if len(self.subterms) != self.predicate.arity:
            raise err.ArityMismatch(head, self.subterms)

        language = head.language

        # Check arguments are all terms of the appropriate type and matching language
        for arg, expected_sort in zip(self.subterms, head.sort):
            if not isinstance(arg, Term):
                raise err.LanguageError("Wrong argument for atomic formula: '{}' ".format(arg))

            if arg.language != language:
                raise err.LanguageMismatch(arg, arg.language, language)

            if not language.is_subtype(arg.sort, expected_sort):
                raise err.SortMismatch(arg, arg.sort, expected_sort)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return '{}({})'.format(self.predicate.symbol, ','.join([str(t) for t in self.subterms]))

    def is_syntactically_equal(self, other):
        if (self.__class__ is not other.__class__ or
                self.predicate != other.predicate or len(self.subterms) != len(other.subterms)):
            return False

        # Else we just need to recursively check if all subterms are syntactically equal
        return all(x.is_syntactically_equal(y) for x, y in zip(self.subterms, other.subterms))

    __repr__ = __str__


class VariableBinding:
    """ A VariableBinding contains a set of logical variables which are _bound_ in some formula or term """

    def __init__(self, variables=None):
        variables = variables or []
        # An (ordered) map between variable name and the variable itself:
        self.variables = OrderedDict((v.symbol, v) for v in variables)
        self._idx = 0
        self._v_values = list(self.variables.values())
        self.index_ = {v.symbol: i for i, v in enumerate(variables)}

    def __len__(self):
        return len(self.variables)

    def __getitem__(self, index):
        return self._v_values[index]

    def add(self, variable: Variable):
        other = self.variables.get(variable.symbol, None)
        if other is not None:
            raise err.DuplicateVariableDefinition(variable, other)
        self.variables[variable.symbol] = variable
        self._v_values += [variable]
        self.index_[variable.symbol] = len(self.index_)

    def get(self, name):
        var = self.variables.get(name, None)
        if var is None:
            raise err.UndefinedVariable(name)
        return var

    def index(self, name):
        idx = self.index_.get(name, None)
        if idx is None:
            raise err.UndefinedVariable(name)
        return idx

    def merge(self, binding):
        """ Merge the given binding into the current binding, inplace """
        raise NotImplementedError()

    @staticmethod
    def empty():
        return VariableBinding()

    def vars(self):
        return list(self.variables.values())

    def __iter__(self):
        self._v_values = [v for _, v in self.variables.items()]
        self._idx = 0
        return self

    def __next__(self):
        if self._idx == len(self._v_values):
            raise StopIteration()
        self._idx += 1
        return self._v_values[self._idx - 1]
