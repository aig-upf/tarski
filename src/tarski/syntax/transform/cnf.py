"""
    CNF Transformation
"""
from ..formulas import CompoundFormula, Connective, QuantifiedFormula
from ..transform import to_negation_normal_form

from .errors import TransformationError


class CNFTransformation:
    """ Rewrite an input quantifier-free formula into an equivalent CNF formula. """

    def __init__(self, lang, phi, do_copy=True):
        self.L = lang
        self.blueprint = to_negation_normal_form(phi, do_copy)
        self.cnf = None
        self.clauses = []
        self.current_clause = []

    def distribute(self, n1, n2):
        """ Distribute w.r.t. disjunction, see Huth & Ryan, pp. 60-62 """
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
                psi0, psi1 = self._convert(phi.subformulas[0]), self._convert(phi.subformulas[1])
                result = CompoundFormula(Connective.And, (psi0, psi1))
                for k in range(2, len(phi.subformulas)):
                    psi_k = self._convert(phi.subformulas[k])
                    result = CompoundFormula(Connective.And, (result, psi_k))
                return result
            else:
                assert phi.connective == Connective.Or
                psi0, psi1 = self._convert(phi.subformulas[0]), self._convert(phi.subformulas[1])
                result = self.distribute(psi0, psi1)
                for k in range(2, len(phi.subformulas)):
                    psi_k = self._convert(phi.subformulas[k])
                    result = self.distribute(result, psi_k)
                return result

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
        return self.cnf

    def convert_to_clause_list(self):
        self.cnf = self._convert(self.blueprint)
        self.collect_clauses(self.cnf)
        return self.clauses

    @staticmethod
    def rewrite(lang, phi, do_copy=True):
        trans = CNFTransformation(lang, phi, do_copy)
        trans.convert()
        return trans


def to_conjunctive_normal_form(lang, phi, do_copy=True):
    trans = CNFTransformation(lang, phi, do_copy)
    return trans.convert()


def to_conjunctive_normal_form_clauses(lang, phi, do_copy=True):
    trans = CNFTransformation(lang, phi, do_copy)
    return trans.convert_to_clause_list()

