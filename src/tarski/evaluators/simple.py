import operator
from typing import List

from ..theories import arithmetic
from ..theories.sets import set_semantics_evaluation
from .. import errors as err
from ..syntax import ops, Connective, Atom, Formula, CompoundFormula, QuantifiedFormula, builtins, Variable, \
    Constant, CompoundTerm, Tautology, Contradiction, IfThenElse, AggregateCompoundTerm, Term
from ..syntax.algebra import Matrix
from ..model import Model


# TODO We will need to extend this so that the interpretation depends on a certain, given sigma of values to
# TODO the free variables in the given term / sentence, as is standard in textbook-FOL
def evaluate(element, m: Model, sigma=None):
    """ Evaluate the denotation of a given formula or term over a given model """
    sigma = sigma if sigma is not None else {}

    # Formulas
    if isinstance(element, Tautology):
        return True

    if isinstance(element, Contradiction):
        return False

    if isinstance(element, Atom):
        return evaluate_atom(element, m, sigma)

    if isinstance(element, CompoundFormula):
        return _compound_evaluators[element.connective](element, m, sigma)

    if isinstance(element, QuantifiedFormula):
        return evaluate_quantified(element, m, sigma)

    # Terms
    if isinstance(element, Variable):
        return sigma[element]  # TODO Finish this, ATM it will raise a runtime error

    if isinstance(element, (Constant, CompoundTerm, IfThenElse, Matrix, AggregateCompoundTerm)):
        return evaluate_term(element, m, sigma)

    raise err.UnexpectedElementType(element)


_compound_evaluators = {
    Connective.Not: lambda f, m, s: not evaluate(f.subformulas[0], m, s),
    Connective.And: lambda f, m, s: all(evaluate(sub, m, s) for sub in f.subformulas),
    Connective.Or: lambda f, m, s: any(evaluate(sub, m, s) for sub in f.subformulas)
}


def evaluate_atom(atom: Atom, m: Model, sigma):
    if builtins.is_builtin_predicate(atom.predicate):
        subterms = tuple(evaluate_term(x, m, sigma) for x in atom.subterms)
        return evaluate_builtin_predicate(atom.language, atom.symbol.symbol, subterms)

    # Otherwise, the extension is given by the model
    point = tuple(evaluate(t, m, sigma) for t in atom.subterms)
    return m.holds(atom.predicate, point)


def evaluate_quantified(formula: Formula, m: Model, sigma):
    # pylint: disable=unused-argument
    raise NotImplementedError()


def evaluate_term(term, m: Model, sigma):
    if isinstance(term, IfThenElse):
        if evaluate(term.condition, m, sigma):  # condition is true
            term = term.subterms[0]
        else:
            term = term.subterms[1]

    if isinstance(term, Matrix):
        N, M = term.shape
        result = []
        for i in range(N):
            row = [evaluate_term(term.matrix[i, j], m, sigma) for j in range(M)]
            result.append(row)
        return Matrix(result, term.sort)

    if isinstance(term, CompoundTerm) and builtins.is_builtin_function(term.symbol):
        subterms = tuple(evaluate_term(x, m, sigma) for x in term.subterms)
        return _evaluate_builtin_function(term.language, term.symbol.symbol, term.sort, subterms, m, sigma)

    # MRJ: Coerce float and int Python literals into constants
    if isinstance(term, float):
        term = Constant(term, m.language.Real)
    if isinstance(term, int):
        term = Constant(term, m.language.Integer)
    assert isinstance(term, (Constant, CompoundTerm))  # TODO Add support for variables
    arguments = []  # type: List[Term]

    # TODO This is technically not correct - a constant still depends on the actual model on which is evaluated.
    # TODO A constant is simply a nullary compound term. E.g. an integer variable is still a logical constant.
    # TODO "Constant" does NOT mean "fixed denotation", although we can assume for convenience that there is one
    # TODO constant for each element in the universe, and the other way round
    # TODO How does Z3 deal with this distinction?
    # TODO We'll need to fix this eventually
    if isinstance(term, Constant):
        return term

    if isinstance(term, CompoundTerm):
        # evaluate each of the arguments
        arguments = [evaluate(a, m, sigma) for a in term.subterms]

    try:
        return m.value(term.symbol, arguments)
    except KeyError:
        raise err.UndefinedTerm(term)


def evaluate_builtin_predicate(lang, symbol, subterms):
    bip = builtins.BuiltinPredicateSymbol

    if symbol in builtins.get_set_symbols():
        return set_semantics_evaluation(lang, symbol, subterms, sort=None)

    _evaluators = {
        bip.EQ: lambda: subterms[0].symbol == subterms[1].symbol,
        bip.NE: lambda: subterms[0].symbol != subterms[1].symbol,
        bip.LT: lambda: subterms[0].symbol < subterms[1].symbol,
        bip.LE: lambda: subterms[0].symbol <= subterms[1].symbol,
        bip.GT: lambda: subterms[0].symbol > subterms[1].symbol,
        bip.GE: lambda: subterms[0].symbol >= subterms[1].symbol,
    }

    evaluator = _evaluators.get(symbol)
    return evaluator()


def symbolic_matrix_multiplication(lhs: Matrix, rhs: Matrix):
    A, B = lhs.shape
    C, D = rhs.shape

    if B != C:
        raise TypeError('matrices {}x{} and {}x{} cannot be multiplied together'.format(A, B, C, D))

    zip_b = list(zip(*rhs.matrix))
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in lhs.matrix]


def _evaluate_builtin_function(lang, symbol, sort, subterms, model, sigma):
    bif = builtins.BuiltinFunctionSymbol
    ae1 = _arithmetic_evaluator_1
    ae2 = _arithmetic_evaluator_2

    if symbol in builtins.get_set_symbols():
        return set_semantics_evaluation(lang, symbol, subterms, sort)

    if symbol == bif.MATMUL:
        return ae2(symbolic_matrix_multiplication, subterms, model, sigma)

    _evaluators = {
        bif.ADD: lambda: ae2(operator.add, subterms, model, sigma),
        bif.SUB: lambda: ae2(operator.sub, subterms, model, sigma),
        bif.MUL: lambda: ae2(operator.mul, subterms, model, sigma),
        bif.DIV: lambda: ae2(operator.truediv, subterms, model, sigma),
        bif.POW: lambda: ae2(operator.pow, subterms, model, sigma),
        bif.MOD: lambda: ae2(operator.mod, subterms, model, sigma),
        bif.MIN: lambda: ae2(arithmetic.impl(bif.MIN.value), subterms, model, sigma),
        bif.MAX: lambda: ae2(arithmetic.impl(bif.MAX.value), subterms, model, sigma),
        bif.ABS: lambda: ae1(arithmetic.impl(bif.ABS.value), subterms, model, sigma),
        bif.SIN: lambda: ae1(arithmetic.impl(bif.SIN.value), subterms, model, sigma),
        bif.COS: lambda: ae1(arithmetic.impl(bif.COS.value), subterms, model, sigma),
        bif.TAN: lambda: ae1(arithmetic.impl(bif.TAN.value), subterms, model, sigma),
        bif.ATAN: lambda: ae1(arithmetic.impl(bif.ATAN.value), subterms, model, sigma),
        bif.ASIN: lambda: ae1(arithmetic.impl(bif.ASIN.value), subterms, model, sigma),
        bif.EXP: lambda: ae1(arithmetic.impl(bif.EXP.value), subterms, model, sigma),
        bif.LOG: lambda: ae1(arithmetic.impl(bif.LOG.value), subterms, model, sigma),
        bif.ERF: lambda: ae1(arithmetic.impl(bif.ERF.value), subterms, model, sigma),
        bif.ERFC: lambda: ae1(arithmetic.impl(bif.ERFC.value), subterms, model, sigma),
        bif.SGN: lambda: ae1(arithmetic.impl(bif.SGN.value), subterms, model, sigma),
        bif.SQRT: lambda: ae1(arithmetic.impl(bif.SQRT.value), subterms, model, sigma),
        bif.NORMAL: lambda: ae2(arithmetic.impl(bif.NORMAL.value), subterms, model, sigma),
        bif.GAMMA: lambda: ae2(arithmetic.impl(bif.GAMMA.value), subterms, model, sigma),
    }
    evaluator = _evaluators.get(symbol)
    return evaluator()


def _arithmetic_evaluator_1(operation, subterms, model, sigma):
    expr = subterms[0]
    value = operation(expr.sort.literal(expr))
    sort = ops.infer_numeric_sort(value, expr.language)
    return Constant(value, sort)


def _arithmetic_evaluator_2(operation, subterms, model, sigma):
    lhs, rhs = subterms

    if isinstance(lhs, Matrix) and isinstance(rhs, Matrix):
        value = operation(lhs, rhs)
        return evaluate_term(Matrix(value, lhs.sort), model, sigma)
    elif isinstance(lhs, Matrix) and not isinstance(rhs, Matrix):
        value = operation(lhs.matrix, rhs.sort.literal(rhs))
        return evaluate_term(Matrix(value, lhs.sort), model, sigma)
    elif isinstance(rhs, Matrix) and not isinstance(lhs, Matrix):
        value = operation(lhs.sort.literal(lhs), rhs.matrix)
        return evaluate_term(Matrix(value, rhs.sort), model, sigma)

    value = operation(lhs.sort.literal(lhs), rhs.sort.literal(rhs))
    sort = ops.infer_numeric_sort(value, lhs.language)
    return Constant(value, sort)
