
from ..syntax import symref, CompoundFormula, QuantifiedFormula, Atom, CompoundTerm, Variable


class MatchExpression:
    """
        This Visitor traverses a formula/expression stopping when
        finding an exact syntactic match for the target
    """

    def __init__(self, target):
        self.psi = target
        self.target = symref(target)
        self.hits = 0

    def _check_match(self, phi):
        if symref(phi) == self.target:
            self.hits += 1
            return True
        return False

    def visit(self, phi):
        if isinstance(phi, CompoundFormula):
            if self._check_match(phi):
                return
            _ = [self.visit(f) for f in phi.subformulas]

        elif isinstance(phi, QuantifiedFormula):
            if self._check_match(phi):
                return
            self.visit(phi.formula)

        elif isinstance(phi, (Atom, CompoundTerm)):
            if self._check_match(phi):
                return
            _ = [self.visit(f) for f in phi.subterms]


class CollectVariables:
    """ Collect all variables in a given formula or term """

    def __init__(self):
        self.variables = set()

    def visit(self, phi):
        if isinstance(phi, Variable):
            self.variables.add(phi)

        elif isinstance(phi, CompoundFormula):
            _ = [self.visit(f) for f in phi.subformulas]

        elif isinstance(phi, QuantifiedFormula):
            self.visit(phi.formula)

        elif isinstance(phi, (Atom, CompoundTerm)):
            _ = [self.visit(f) for f in phi.subterms]


class CollectFreeVariables:
    """ Collect all free variables in a given formula or term """
    def __init__(self):
        self.quantified_vars = set()
        self._free_variables = set()

    @property
    def free_variables(self):
        for ref in self._free_variables:
            yield ref.expr

    def visit(self, phi):
        if isinstance(phi, Variable):
            t_ref = symref(phi)
            if t_ref not in self.quantified_vars:
                self._free_variables.add(t_ref)
        elif isinstance(phi, CompoundFormula):
            _ = [self.visit(f) for f in phi.subformulas]

        elif isinstance(phi, QuantifiedFormula):
            _ = [self.quantified_vars.add(symref(x)) for x in phi.variables]
            self.visit(phi.formula)
            _ = [self.quantified_vars.remove(symref(x)) for x in phi.variables]

        elif isinstance(phi, (Atom, CompoundTerm)):
            _ = [self.visit(f) for f in phi.subterms]
