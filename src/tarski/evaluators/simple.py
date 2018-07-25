import operator

from ..syntax import ops, Connective, Atom, Formula, CompoundFormula, QuantifiedFormula, builtins, Variable, \
    Constant, CompoundTerm
from ..model import Model


# TODO We will need to extend this so that the interpretation depends on a certain, given sigma of values to
# TODO the free variables in the given termn / sentence, as is standard in textbook-FOL
def evaluate(element, m: Model, sigma=None):
    """ Evaluate the denotation of a given formula or term over a given model """
    sigma = sigma if sigma is not None else {}

    # Formulas
    if isinstance(element, Atom):
        return evaluate_atom(element, m, sigma)

    if isinstance(element, CompoundFormula):
        return _compound_evaluators[element.connective](element, m, sigma)

    if isinstance(element, QuantifiedFormula):
        return evaluate_quantified(element, m, sigma)

    # Terms
    if isinstance(element, Variable):
        return sigma[element]  # TODO Finish this, ATM it will raise a runtime error

    if isinstance(element, (Constant, CompoundTerm)):
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
    if isinstance(term, CompoundTerm) and builtins.is_builtin_function(term.symbol):
        return evaluate_builtin_function(term, m, sigma)

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

    return m.value(term.symbol, arguments)


def evaluate_builtin_predicate(atom, model, sigma):
    bip = builtins.BuiltinPredicateSymbol
    _evaluators = {
        bip.EQ: lambda f, m, s: evaluate(f.subterms[0], m, s) == evaluate(f.subterms[1], m, s),
        bip.NE: lambda f, m, s: evaluate(f.subterms[0], m, s) != evaluate(f.subterms[1], m, s),
        bip.LT: lambda f, m, s: evaluate(f.subterms[0], m, s) < evaluate(f.subterms[1], m, s),
        bip.LE: lambda f, m, s: evaluate(f.subterms[0], m, s) <= evaluate(f.subterms[1], m, s),
        bip.GT: lambda f, m, s: evaluate(f.subterms[0], m, s) > evaluate(f.subterms[1], m, s),
        bip.GE: lambda f, m, s: evaluate(f.subterms[0], m, s) >= evaluate(f.subterms[1], m, s),
    }

    return _evaluators[atom.predicate.symbol](atom, model, sigma)


def evaluate_builtin_function(term, model, sigma):
    bif = builtins.BuiltinFunctionSymbol
    _evaluators = {
        bif.ADD: lambda f, m, s: _arithmetic_evaluator(operator.add, f.subterms[0], f.subterms[1], model, sigma),
        bif.SUB: lambda f, m, s: _arithmetic_evaluator(operator.sub, f.subterms[0], f.subterms[1], model, sigma),
        bif.MUL: lambda f, m, s: _arithmetic_evaluator(operator.mul, f.subterms[0], f.subterms[1], model, sigma),
        bif.DIV: lambda f, m, s: _arithmetic_evaluator(operator.truediv, f.subterms[0], f.subterms[1], model, sigma),
    }

    return _evaluators[term.symbol.symbol](term, model, sigma)


def _arithmetic_evaluator(operation, lhs, rhs, model, sigma):
    # _lhs = args[0].symbol
    # _rhs = args[1].symbol
    # assert self.domain[0].contains(_lhs)
    # assert self.domain[1].contains(_rhs)
    lhs = evaluate_term(lhs, model, sigma)
    rhs = evaluate_term(rhs, model, sigma)
    value = operation(ops.cast_to_number(lhs), ops.cast_to_number(rhs))
    sort = ops.infer_numeric_sort(value, lhs.language)
    return Constant(value, sort)
