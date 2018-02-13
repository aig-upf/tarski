
from tarski.syntax.terms import Variable, Constant, CompoundTerm

from . import builtins
from ..syntax import Connective, Atom, Formula, CompoundFormula, QuantifiedFormula
from ..model import Model


# TODO We will need to extend this so that the interpretation depends on a certain, given sigma of values to
# TODO the free variables in the given termn / sentence, as is standard in textbook-FOL
def evaluate(element, m: Model, sigma={}):
    """ Evaluate the denotation of a given formula or term over a given model """

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

    raise RuntimeError("Unknown logical element type: {}".format(element))


_compound_evaluators = {
    Connective.Not: lambda f, m, s: not evaluate(f.subformulas[0], m, s),
    Connective.And: lambda f, m, s: all(evaluate(sub, m, s) for sub in f.subformulas),
    Connective.Or: lambda f, m, s: any(evaluate(sub, m, s) for sub in f.subformulas)
}


def evaluate_atom(atom: Atom, m: Model, sigma):
    if builtins.is_builtin_predicate(atom.predicate):
        return builtins.evaluate(atom, m, sigma)

    else:  # the extension is given by the model
        point = [evaluate(t, m, sigma) for t in atom.subterms]
        return m.holds(atom.predicate, point)


def evaluate_quantified(formula: Formula, m: Model, sigma):
    raise NotImplementedError()


def evaluate_term(term, m: Model, sigma):
    assert isinstance(term, (Constant, CompoundTerm))
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
