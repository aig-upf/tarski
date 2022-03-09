from collections import OrderedDict
from enum import Enum
from typing import List

from .. import errors as err
from .builtins import BuiltinPredicateSymbol
from .terms import Variable, Term
from .util import termlists_are_equal, termlist_hash
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


def negate_quantifier(q: Quantifier):
    return Quantifier.Exists if q == Quantifier.Forall else Quantifier.Forall


class Formula:
    """ A first-order logical formula. """

    def __str__(self):
        raise NotImplementedError()  # To be subclassed

    def __and__(self, rhs):
        return land(self, rhs)

    def __or__(self, rhs):
        return lor(self, rhs)

    def __invert__(self):
        return neg(self)

    def __gt__(self, rhs):
        return implies(self, rhs)

    def __eq__(self, other):
        raise NotImplementedError()  # To be subclassed

    def __hash__(self):
        raise NotImplementedError()  # To be subclassed

    def hash(self):
        # Define a shortcut for uniformity with the Term class
        return self.__hash__()

    def is_syntactically_equal(self, other):
        """ Return true if this formula and other are strictly syntactically equivalent.
        This is equivalent to self == other, but is provided for reasons of uniformity with the Term class.
        """
        return self.__eq__(other)


class Tautology(Formula):
    def __str__(self):
        return "T"

    __repr__ = __str__

    def __eq__(self, other):
        return self.__class__ is other.__class__

    def __hash__(self):
        return hash(self.__class__)


class Contradiction(Formula):
    def __str__(self):
        return "F"

    __repr__ = __str__

    def __eq__(self, other):
        return self.__class__ is other.__class__

    def __hash__(self):
        return hash(self.__class__)


class CompoundFormula(Formula):
    """ A set of formulas combined through some logical connective """

    def __init__(self, connective, subformulas):
        super().__init__()
        self.connective = connective
        self.subformulas = subformulas
        self._check_well_formed()

    def _check_well_formed(self):
        if any(not isinstance(f, Formula) for f in self.subformulas):
            raise err.LanguageError(f"Wrong argument types for compound formula: '{self.subformulas}' ")

        if self.connective == Connective.Not:
            if len(self.subformulas) != 1:
                raise err.LanguageError("Negation admits only one subformula")
        elif len(self.subformulas) < 2:
            raise err.LanguageError("Conjunction and disjunction require at least two subformulas")

    def __str__(self):
        if self.connective == Connective.Not:
            assert len(self.subformulas) == 1
            return f"({self.connective} {str(self.subformulas[0])})"

        inner = f" {self.connective} ".join(str(f) for f in self.subformulas)
        return f"({inner})"

    __repr__ = __str__

    def __eq__(self, other):
        return (self.__class__ is other.__class__
                and self.connective == other.connective
                and self.subformulas == other.subformulas)

    def __hash__(self):
        element_hashes = [self.__class__, self.connective]
        # TODO: formulas need to be flattened if we want to hash them,
        # it would be good to check if there is a better way of flattening
        # than this
        for phi in self.subformulas:
            element_hashes.append(hash(phi))
        return hash(tuple(element_hashes))


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
        return f'{self.quantifier} {vars_} : ({self.formula})'

    __repr__ = __str__

    def __eq__(self, other):
        return (self.__class__ is other.__class__
                and self.quantifier == other.quantifier
                and termlists_are_equal(self.variables, other.variables)
                and self.formula == other.formula)

    def __hash__(self):
        return hash((self.__class__, self.quantifier, termlist_hash(self.variables), self.formula))


top = Tautology()
bot = Contradiction()


def _to_binary_tree(args, connective):
    assert len(args) > 1
    phi = CompoundFormula(connective, (args[-2], args[-1]))
    for arg in reversed(args[:-2]):
        phi = CompoundFormula(connective, (arg, phi))
    return phi


def _create_compound(args, connective, flat):
    if len(args) == 1:  # Handle gracefully the case of a single-atom compound formula
        return args[0]
    if flat:
        return CompoundFormula(connective, args)
    return _to_binary_tree(args, connective)


def land(*args, flat=False):
    """ Create an and-formula with the given subformulas. If binary is true, the and-formula will be shaped as a binary
     tree (e.g. (...((p1 and p2) and p3) and ...))), otherwise it will have a flat structure. This is an implementation
     detail, but might be relevant performance-wise when dealing with large structures """
    if not args:
        return top
    return _create_compound(args, Connective.And, flat)


def lor(*args, flat=False):
    """ Create an or-formula with the given subformulas. If binary is true, the or-formula will be shaped as a binary
    tree (e.g. (...((p1 or p2) or p3) or ...))), otherwise it will have a flat structure. This is an implementation
    detail, but might be relevant performance-wise when dealing with large structures """
    if not args:
        return bot
    return _create_compound(args, Connective.Or, flat)


def neg(phi):
    return CompoundFormula(Connective.Not, [phi])


def implies(phi, psi):
    """ Create the implication phi -> psi """
    return lor(neg(phi), psi)


def equiv(phi, psi):
    """ Create the bi-implication phi <-> psi """
    return land(implies(phi, psi), implies(psi, phi))  # pylint: disable=arguments-out-of-order


def forall(*args):
    """ Create a universally-quantified formula. The argument list needs to be of the form (v1, v2, ..., vn, f),
    where v_i are the variables and f is the quantified formula. To represent the formula "forall x, y x < y",
    we would use:
    >>> forall(x, y, x<y)
    """
    return quantified(Quantifier.Forall, *args)


def exists(*args):
    """ Create an existentially-quantified formula. The argument list needs to be of the form (v1, v2, ..., vn, f),
    where v_i are the variables and f is the quantified formula. To represent the formula "exists x, y such that x < y",
    we would use:
    >>> exists(x, y, x<y)
    """
    return quantified(Quantifier.Exists, *args)


def quantified(quantifier, *args):
    """ Create a quantified formula.

        'args' is expected to be of the form [v1, ..., vn, f], where v_i are the variables
        and f is the quantified formula.
    """
    if len(args) < 2:
        raise err.LanguageError('Quantified formula needs at least two arguments')

    variables, formula = args[:-1], args[-1]

    if not isinstance(formula, Formula):
        raise err.LanguageError(f'Illformed arguments for quantified formula: {args}')

    if not all(isinstance(x, Variable) for x in variables):
        raise err.LanguageError(f'Illformed arguments for quantified formula: {args}')

    return QuantifiedFormula(quantifier, variables, args[-1])


def is_and(phi: Formula):
    """ Return whether the given formula is a conjunction """
    return isinstance(phi, CompoundFormula) and phi.connective == Connective.And


def is_or(phi: Formula):
    """ Return whether the given formula is a disjunction """
    return isinstance(phi, CompoundFormula) and phi.connective == Connective.Or


def is_neg(phi: Formula):
    """ Return whether the given formula is a negation """
    return isinstance(phi, CompoundFormula) and phi.connective == Connective.Not


def is_atom(phi: Formula):
    """ Return whether the given formula is an atom """
    return isinstance(phi, Atom)


def is_eq_atom(phi: Formula):
    """ Return whether the given formula is an equality """
    return isinstance(phi, Atom) and phi.predicate.symbol == BuiltinPredicateSymbol.EQ


def is_ne_atom(phi: Formula):
    """ Return whether the given formula is an inequality """
    return isinstance(phi, Atom) and phi.predicate.symbol == BuiltinPredicateSymbol.NE


def unwrap_conjunction_or_atom(phi):
    """ """
    if is_atom(phi):
        return [phi]
    if is_and(phi):
        return phi.subformulas
    return []


class Atom(Formula):
    """ A first-order atom. """

    def __init__(self, predicate, arguments):
        super().__init__()
        self.predicate = predicate
        self.subterms = arguments
        self._check_well_formed()

    @property
    def symbol(self):
        return self.predicate  # For uniformity with CompoundTerms

    def _check_well_formed(self):
        head = self.predicate

        if not isinstance(head, Predicate):
            raise err.LanguageError(f"Incorrect atom head: '{head}' ")

        # Check arities match
        if len(self.subterms) != self.predicate.arity:
            raise err.ArityMismatch(head, self.subterms)

        language = head.language

        # Check arguments are all terms of the appropriate type and matching language
        for arg, expected_sort in zip(self.subterms, head.sort):
            if not isinstance(arg, Term):
                raise err.LanguageError(f"Wrong argument for atomic formula: '{arg}' ")

            if arg.language != language:
                raise err.LanguageMismatch(arg, arg.language, language)

            if not language.is_subtype(arg.sort, expected_sort):
                raise err.SortMismatch(arg, arg.sort, expected_sort)

    def __str__(self):
        return '{}({})'.format(self.predicate.symbol, ','.join(str(t) for t in self.subterms))

    __repr__ = __str__

    def __eq__(self, other):
        return (self.__class__ is other.__class__
                and self.predicate == other.predicate
                and termlists_are_equal(self.subterms, other.subterms))

    def __hash__(self):
        return hash((self.__class__, self.predicate, termlist_hash(self.subterms)))


class VariableBinding:
    """ A VariableBinding contains a set of logical variables which are _bound_ in some formula or term """

    def __init__(self, variables=None):
        variables = variables or []
        # An (ordered) map between variable name and the variable itself:
        self.variables = OrderedDict((v.symbol, v) for v in variables)
        self._v_values = variables[:]
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
        yield from self.variables.values()

    def __str__(self):
        return f"Variables({','.join(map(str, self._v_values))})"

    __repr__ = __str__
