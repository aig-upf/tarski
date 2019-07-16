"""
    CNF Transformation
"""
from ..formulas import CompoundFormula, Connective, QuantifiedFormula
from ..transform import NNFTransformation

from .errors import TransformationError


class CNFTransformation:
    """
        This class rewrites an input quantifier free formula phi into an equivalent formula
        in CNF

    """

    def __init__(self, lang, phi, do_copy=True):
        """ Distribute w.r.t. disjunction, see Huth & Ryan, pp. 60-62 """
        self.L = lang
        self.blueprint = NNFTransformation.rewrite(phi, do_copy).nnf
        self.cnf = None
        self.clauses = []
        self.current_clause = []

    def distribute(self, n1, n2):
        if isinstance(n1, CompoundFormula) and n1.connective == Connective.And:
            lhs = self.distribute(n1.subformulas[0], n2)
            rhs = self.distribute(n1.subformulas[1], n2)
            return CompoundFormula(Connective.And, (lhs, rhs))
        elif isinstance(n2, CompoundFormula) and n2.connective == Connective.And:
            lhs = self.distribute(n1, n2.subformulas[0])
            rhs = self.distribute(n1, n2.subformulas[1])
            return CompoundFormula(Connective.And, (lhs, rhs))
        else:
            return CompoundFormula(Connective.Or, (n1, n2))

    def _convert(self, phi):

        if isinstance(phi, QuantifiedFormula):
            raise TransformationError("cnf transformation", phi, "Formula is not quantifier free!")

        if isinstance(phi, CompoundFormula):
            if phi.connective == Connective.Not:
                return phi  # already CNF
            elif phi.connective == Connective.And:
                lhs, rhs = self._convert(phi.subformulas[0]), self._convert(phi.subformulas[1])
                return CompoundFormula(Connective.And, (lhs, rhs))
            else:
                assert phi.connective == Connective.Or
                lhs, rhs = self._convert(phi.subformulas[0]), self._convert(phi.subformulas[1])
                return self.distribute(lhs, rhs)

        return phi

    def collect_clauses(self, phi):
        if isinstance(phi, QuantifiedFormula):
            raise TransformationError("cnf transformation", phi, "Formula is not quantifier free!")

        if isinstance(phi, CompoundFormula):
            if phi.connective == Connective.Not:
                self.current_clause.append(phi)
                return None
            elif phi.connective == Connective.And:
                self.current_clause = []
                self.collect_clauses(phi.subformulas[0])
                self.clauses.append(self.current_clause)
                self.current_clause = []
                self.collect_clauses(phi.subformulas[1])
                self.clauses.append(self.current_clause)
                return None
            else:
                self.collect_clauses(phi.subformulas[0])
                self.collect_clauses(phi.subformulas[1])
                return None
        self.current_clause.append(phi)
        return phi

    def convert(self):
        self.cnf = self._convert(self.blueprint)
        self.collect_clauses(self.cnf)

    @staticmethod
    def rewrite(lang, phi, do_copy=True):
        trans = CNFTransformation(lang, phi, do_copy)
        trans.convert()
        return trans
