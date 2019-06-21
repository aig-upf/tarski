import operator
from .. import funcsym
from .. import errors as err
from ..syntax import ops, Connective, Atom, Formula, CompoundFormula, QuantifiedFormula, builtins, Variable, \
    Constant, CompoundTerm, Tautology, Contradiction, IfThenElse, AggregateCompoundTerm
from ..syntax.algebra import Matrix
from ..model import Model


# TODO We will need to extend this so that the interpretation depends on a certain, given sigma of values to
# TODO the free variables in the given termn / sentence, as is standard in textbook-FOL
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

    raise RuntimeError("Unknown logical element type: {}, {}".format(element, type(element)))


_compound_evaluators = {
    Connective.Not: lambda f, m, s: not evaluate(f.subformulas[0], m, s),
    Connective.And: lambda f, m, s: all(evaluate(sub, m, s) for sub in f.subformulas),
    Connective.Or: lambda f, m, s: any(evaluate(sub, m, s) for sub in f.subformulas)
}


def evaluate_atom(atom: Atom, m: Model, sigma):
    if builtins.is_builtin_predicate(atom.predicate):
        return evaluate_builtin_predicate(atom, m, sigma)

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
        return evaluate_builtin_function(term, m, sigma)
    # MRJ: Coerce float and int Python literals into constants
    if isinstance(term, float):
        term = Constant(term, m.language.Real)
    if isinstance(term, int):
        term = Constant(term, m.language.Integer)
    assert isinstance(term, (Constant, CompoundTerm))  # TODO Add support for variables
    arguments = []

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
        arguments = tuple(evaluate(a, m, sigma) for a in term.subterms)

    try:
        return m.value(term.symbol, arguments)
    except KeyError:
        raise err.UndefinedTerm(term)


def evaluate_builtin_predicate(atom, model, sigma):
    bip = builtins.BuiltinPredicateSymbol
    _evaluators = {
        bip.EQ: lambda f, m, s: evaluate(f.subterms[0], m, s).symbol == evaluate(f.subterms[1], m, s).symbol,
        bip.NE: lambda f, m, s: evaluate(f.subterms[0], m, s).symbol != evaluate(f.subterms[1], m, s).symbol,
        bip.LT: lambda f, m, s: evaluate(f.subterms[0], m, s).symbol < evaluate(f.subterms[1], m, s).symbol,
        bip.LE: lambda f, m, s: evaluate(f.subterms[0], m, s).symbol <= evaluate(f.subterms[1], m, s).symbol,
        bip.GT: lambda f, m, s: evaluate(f.subterms[0], m, s).symbol > evaluate(f.subterms[1], m, s).symbol,
        bip.GE: lambda f, m, s: evaluate(f.subterms[0], m, s).symbol >= evaluate(f.subterms[1], m, s).symbol,
    }

    return _evaluators[atom.predicate.symbol](atom, model, sigma)


def symbolic_matrix_multiplication(lhs: Matrix, rhs: Matrix):
    A, B = lhs.shape
    C, D = rhs.shape

    if B != C:
        raise TypeError('matrices {}x{} and {}x{} cannot be multiplied together'.format(A, B, C, D))

    zip_b = zip(*rhs.matrix)
    zip_b = list(zip_b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in lhs.matrix]


def evaluate_builtin_function(term, model, sigma):
    bif = builtins.BuiltinFunctionSymbol
    ae1 = _arithmetic_evaluator_1
    ae2 = _arithmetic_evaluator_2
    _evaluators = {
        bif.ADD: lambda f, m, s: ae2(operator.add, f.subterms[0], f.subterms[1], m, s),
        bif.SUB: lambda f, m, s: ae2(operator.sub, f.subterms[0], f.subterms[1], m, s),
        bif.MUL: lambda f, m, s: ae2(operator.mul, f.subterms[0], f.subterms[1], m, s),
        bif.MATMUL: lambda f, m, s: ae2(symbolic_matrix_multiplication, f.subterms[0], f.subterms[1], m, s),
        bif.DIV: lambda f, m, s: ae2(operator.truediv, f.subterms[0], f.subterms[1], m, s),
        bif.POW: lambda f, m, s: ae2(operator.pow, f.subterms[0], f.subterms[1], m, s),
        bif.MOD: lambda f, m, s: ae2(operator.mod, f.subterms[0], f.subterms[1], model, s),
        bif.MIN: lambda f, m, s: ae2(funcsym.impl[bif.MIN.value], f.subterms[0], f.subterms[1], m, s),
        bif.MAX: lambda f, m, s: ae2(funcsym.impl[bif.MAX.value], f.subterms[0], f.subterms[1], m, s),
        bif.ABS: lambda f, m, s: ae1(funcsym.impl[bif.ABS.value], f.subterms[0], m, s),
        bif.SIN: lambda f, m, s: ae1(funcsym.impl[bif.SIN.value], f.subterms[0], m, s),
        bif.COS: lambda f, m, s: ae1(funcsym.impl[bif.COS.value], f.subterms[0], m, s),
        bif.TAN: lambda f, m, s: ae1(funcsym.impl[bif.TAN.value], f.subterms[0], m, s),
        bif.ATAN: lambda f, m, s: ae1(funcsym.impl[bif.ATAN.value], f.subterms[0], m, s),
        bif.ASIN: lambda f, m, s: ae1(funcsym.impl[bif.ASIN.value], f.subterms[0], m, s),
        bif.EXP: lambda f, m, s: ae1(funcsym.impl[bif.EXP.value], f.subterms[0], m, s),
        bif.LOG: lambda f, m, s: ae1(funcsym.impl[bif.LOG.value], f.subterms[0], m, s),
        bif.ERF: lambda f, m, s: ae1(funcsym.impl[bif.ERF.value], f.subterms[0], m, s),
        bif.ERFC: lambda f, m, s: ae1(funcsym.impl[bif.ERFC.value], f.subterms[0], m, s),
        bif.SGN: lambda f, m, s: ae1(funcsym.impl[bif.SGN.value], f.subterms[0], m, s),
        bif.SQRT: lambda f, m, s: ae1(funcsym.impl[bif.SQRT.value], f.subterms[0], m, s),
        bif.NORMAL: lambda f, m, s: ae2(funcsym.impl[bif.NORMAL.value], f.subterms[0], f.subterms[1], m, s),
        bif.GAMMA: lambda f, m, s: ae2(funcsym.impl[bif.GAMMA.value], f.subterms[0], f.subterms[1], m, s),
    }

    return _evaluators[term.symbol.symbol](term, model, sigma)


def _arithmetic_evaluator_1(operation, expr, model, sigma):
    # _lhs = args[0].symbol
    # _rhs = args[1].symbol
    # assert self.domain[0].contains(_lhs)
    # assert self.domain[1].contains(_rhs)
    expr = evaluate_term(expr, model, sigma)
    value = operation(ops.cast_to_number(expr))
    sort = ops.infer_numeric_sort(value, expr.language)
    return Constant(value, sort)


def _arithmetic_evaluator_2(operation, lhs, rhs, model, sigma):
    # _lhs = args[0].symbol
    # _rhs = args[1].symbol
    # assert self.domain[0].contains(_lhs)
    # assert self.domain[1].contains(_rhs)
    lhs = evaluate_term(lhs, model, sigma)
    rhs = evaluate_term(rhs, model, sigma)
    if isinstance(lhs, Matrix) and isinstance(rhs, Matrix):
        # print("Matrix op Matrix")
        value = operation(lhs, rhs)
        # print('Result : {}'.format(value))
        return evaluate_term(Matrix(value, lhs.sort), model, sigma)
    elif isinstance(lhs, Matrix) and not isinstance(rhs, Matrix):
        value = operation(lhs.matrix, ops.cast_to_number(rhs))
        return evaluate_term(Matrix(value, lhs.sort), model, sigma)
    elif isinstance(rhs, Matrix) and not isinstance(lhs, Matrix):
        value = operation(ops.cast_to_number(lhs), rhs.matrix)
        return evaluate_term(Matrix(value, rhs.sort), model, sigma)

    value = operation(ops.cast_to_number(lhs), ops.cast_to_number(rhs))
    sort = ops.infer_numeric_sort(value, lhs.language)
    return Constant(value, sort)
