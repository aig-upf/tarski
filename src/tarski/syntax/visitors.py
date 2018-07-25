# -*- coding: utf-8 -*-
from .formulas import QuantifiedFormula, Variable, CompoundFormula, Atom
from .sorts import inclusion_closure
from .terms import Constant, CompoundTerm


def emvr(self, other):
    """
        Checks if two terms or atoms are equivalent modulo variable renaming
    """

    # @TODO: the variable renaming should be maintained across the
    # whole sub-expression
    if self.head.symbol != other.head.symbol:
        return False

    for lhs, rhs in zip(self.subterms, other.subterms):
        if isinstance(lhs, Variable) and \
                isinstance(rhs, Variable):
            if lhs.sort.name != rhs.sort.name:
                if rhs.sort not in inclusion_closure(lhs.sort):
                    return False
        elif isinstance(lhs, Constant) and \
                isinstance(rhs, Constant):
            if lhs.symbol != rhs.symbol:
                return False
        elif isinstance(lhs, CompoundTerm) and \
                isinstance(rhs, CompoundTerm):
            if not emvr(SymbolReference(lhs), SymbolReference(rhs)):
                return False
        else:
            return False
    return True


def esm(self, other):
    """
        Checks if two terms or atoms are exact syntactic matches
    """
    lhs = self.expr
    rhs = other.expr
    if isinstance(lhs, Variable):
        if not isinstance(rhs, Variable):
            return False
        if lhs.symbol != rhs.symbol:
            return False
        if lhs.sort.name != rhs.sort.name:
            if rhs.sort not in inclusion_closure(lhs.sort):
                return False
        return True
    if isinstance(lhs, Constant):
        if not isinstance(rhs, Constant):
            return False
        return lhs.symbol == rhs.symbol
    raise NotImplementedError()


class SymbolReference:

    def __init__(self, component, eq_fn=emvr):
        self.expr = component
        self.equality_fn = eq_fn
        try:
            self.head = self.expr.predicate
        except AttributeError:
            self.head = self.expr

    @property
    def language(self):
        return self.head.language

    @property
    def subterms(self):
        return self.expr.subterms

    def __hash__(self):
        return hash(self.head.symbol)

    def __eq__(self, other):
        return self.equality_fn(self, other)

    __cmp__ = __eq__

    def __str__(self):
        return str(self.expr)


class CollectVariables:
    """
        This Visitor collects all Variables in a given formula
    """

    def __init__(self, lang):
        self.L = lang
        self.variables = set()

    def visit(self, phi):

        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            phi.formula.accept(self)
        elif isinstance(phi, Atom):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    self.variables.add(t)
                else:
                    t.accept(self)
        elif isinstance(phi, CompoundTerm):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    self.variables.add(t)
                else:
                    t.accept(self)


class CollectFreeVariables:
    def __init__(self, lang):
        self.L = lang
        self.quantified_vars = set()
        self._free_variables = set()

    @property
    def free_variables(self):
        for ref in self._free_variables:
            yield ref.expr

    def visit(self, phi):
        if isinstance(phi, CompoundFormula):
            for f in phi.subformulas:
                f.accept(self)
        elif isinstance(phi, QuantifiedFormula):
            for x in phi.variables:
                x_ref = SymbolReference(x, esm)
                self.quantified_vars.add(x_ref)
            phi.formula.accept(self)
            for x in phi.variables:
                x_ref = SymbolReference(x, esm)
                self.quantified_vars.remove(x_ref)

        elif isinstance(phi, Atom):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    t_ref = SymbolReference(t, esm)
                    if t_ref not in self.quantified_vars:
                        self._free_variables.add(t_ref)
                else:
                    t.accept(self)
        elif isinstance(phi, CompoundTerm):
            for _, t in enumerate(phi.subterms):
                if isinstance(t, Variable):
                    t_ref = SymbolReference(t, esm)
                    if t_ref not in self.quantified_vars:
                        self._free_variables.add(t_ref)
                else:
                    t.accept(self)
