"""
    Rewrite formulas into prenex normal form
"""
from ..symrefs import symref
from ..formulas import CompoundFormula, QuantifiedFormula, Connective, Quantifier, lor
from ..transform.nnf import NNFTransformation
from ..transform import term_substitution

from .errors import TransformationError


class PrenexTransformation:
    """
        This class rewrites the input formula phi into an equivalent formula
        in Prenex NNF

    """

    def __init__(self, lang, phi, do_copy=True):
        self.L = lang
        self.blueprint = NNFTransformation.rewrite(phi, do_copy).nnf
        self.prenex = None

    def _merge_quantified_subformulas(self, lhs, rhs, renaming=True):
        assert isinstance(lhs, QuantifiedFormula)
        assert isinstance(rhs, QuantifiedFormula)
        new_variables = {(x.symbol, x.sort.name): x for x in lhs.variables}
        subst = {}
        for y in rhs.variables:
            key_y = (y.symbol, y.sort.name)
            if key_y not in new_variables:
                new_variables[key_y] = y
            else:
                if renaming:
                    y2 = self.L.variable("{}'".format(y.symbol), y.sort)
                    subst[y] = y2
                    new_variables[(y2.symbol, y2.sort.name)] = y2
        if len(subst) > 0:
            rhs.formula = term_substitution(self.L, rhs.formula, subst, inplace=True)
        new_phi = QuantifiedFormula(lhs.quantifier, list(new_variables.values()), lor(lhs.formula, rhs.formula))
        return new_phi

    def _nest_quantifiers(self, out_q, out_vars, out_phi, inner_q, inner_vars, conn, lhs, rhs):
        """
            Note that out_phi is either lhs or rhs, we have the parameter duplicated so we
            can preserve the ordering of subformulas
        """
        in_vars_dict = {(x.symbol, x.sort.name): x for x in inner_vars}
        new_out_vars = []
        subst = {}
        for y in out_vars:
            key_y = (y.symbol, y.sort.name)
            if key_y not in in_vars_dict:
                new_out_vars.append(y)
            else:
                y2 = self.L.variable("{}'".format(y.symbol), y.sort)
                subst[symref(y)] = y2
                new_out_vars.append(y2)
        if len(subst) > 0:
            term_substitution(self.L, out_phi, subst, inplace=True)
        phi = CompoundFormula(conn, tuple([lhs, rhs]))
        inner = QuantifiedFormula(inner_q, inner_vars, phi)
        return QuantifiedFormula(out_q, new_out_vars, inner)

    def _convert(self, phi):
        if isinstance(phi, CompoundFormula):
            return self.convert_compound(phi)

        elif isinstance(phi, QuantifiedFormula):
            return self.convert_quantified(phi)

        else:
            return phi

    def convert_compound(self, phi):
        assert isinstance(phi, CompoundFormula)
        if phi.connective == Connective.Not:
            if isinstance(phi.subformulas[0], QuantifiedFormula):
                raise TransformationError('prenex', phi, 'Subformula is not in NNF!')

            if isinstance(phi.subformulas[0], CompoundFormula):
                raise TransformationError('prenex', phi, 'Subformula is not in NNF!')

            return phi
        else:
            # and/or
            return self.convert_and_or(phi)

    def convert_and_or(self, phi):
        lhs, rhs = self._convert(phi.subformulas[0]), self._convert(phi.subformulas[1])
        is_quant_lhs = isinstance(lhs, QuantifiedFormula)
        is_quant_rhs = isinstance(rhs, QuantifiedFormula)
        if not is_quant_lhs and not is_quant_rhs:
            return phi
        elif is_quant_lhs and is_quant_rhs:
            # both parts of the formula are quantified
            if lhs.quantifier == rhs.quantifier:
                return self._merge_quantified_subformulas(lhs, rhs)
                # GFM: Code below commented out, as it is unreachable!
                # if lhs.quantifier == Quantifier.Exist:
                #     if phi.connective == Connective.And:
                #         return self._merge_quantified_subformulas(lhs, rhs)
                #     assert phi.connective == Connective.Or
                #     return self._merge_quantified_subformulas(lhs, rhs, False)  # no renaming
                # assert lhs.quantifier == Quantifier.Forall
                # if phi.connective == Connective.Or:
                #     return self._merge_quantified_subformuls(lhs, rhs)
                # return self._merge_quantified_subformulas(lhs, rhs, False)
            # we have different quantifiers, we apply the null quantifier
            # equivalence

            if rhs.quantifier == Quantifier.Exists and lhs.quantifier == Quantifier.Forall:
                return self._nest_quantifiers(Quantifier.Exists, rhs.variables, rhs.formula,
                                              Quantifier.Forall, lhs.variables,
                                              phi.connective, lhs.formula, rhs.formula)
            return self._nest_quantifiers(Quantifier.Exists, lhs.variables, lhs.formula,
                                          Quantifier.Forall, rhs.variables,
                                          phi.connective, lhs.formula, rhs.formula)
        # \forall ( P \lor Q(x)) \equiv P \lor \forall x Q(x)
        # \exists (P \land Q(x)) \equiv P \land \exists x Q(x)
        elif is_quant_rhs:
            return _merge_mixed_subformulas(rhs.quantifier, rhs.variables, lhs, phi.connective, rhs.formula)
        else:  # is_quant_lhs
            assert is_quant_lhs
            return _merge_mixed_subformulas(lhs.quantifier, lhs.variables, lhs.formula, phi.connective, rhs)

    def convert_quantified(self, phi):
        assert isinstance(phi, QuantifiedFormula)
        phi.formula = self._convert(phi.formula)
        if isinstance(phi.formula, QuantifiedFormula):
            if phi.formula.quantifier == phi.quantifier:  # absorb
                new_variables = [x for x in phi.variables]
                for x in phi.formula.variables:
                    new_variables.append(x)
                phi.formula.variables = tuple(new_variables)
                return phi.formula
            if phi.formula.quantifier == Quantifier.Exists:  # push up existential
                phi.quantifier, phi.formula.quantifier = phi.formula.quantifier, phi.quantifier
                phi.variables, phi.formula.variables = phi.formula.variables, phi.variables
                phi.formula = self._convert(
                    phi.formula)  # reordering the quantifiers may trigger further quantifier reordering
            return phi
        else:
            return phi

    def convert(self):
        self.prenex = self._convert(self.blueprint)

    @staticmethod
    def rewrite(lang, phi, do_copy=True):
        trans = PrenexTransformation(lang, phi, do_copy)
        trans.convert()
        return trans


def _merge_mixed_subformulas(quant, variables, lhs, conn, rhs):
    new_phi = QuantifiedFormula(quant, variables, CompoundFormula(conn, tuple([lhs, rhs])))
    return new_phi
