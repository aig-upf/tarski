
from ..syntax import Connective, Atom, Formula, CompoundFormula, QuantifiedFormula, builtins, Variable, \
    Constant, CompoundTerm
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
    if isinstance(element, m.language.Variable):
        return sigma[element]  # TODO Finish this, ATM it will raise a runtime error

    if isinstance(element, (m.language.Constant, m.language.CompoundTerm)):
        return evaluate_term(element, m, sigma)

    raise RuntimeError("Unknown logical element type: {}, {}".format(element,type(element)))


_compound_evaluators = {
    Connective.Not: lambda f, m, s: not evaluate(f.subformulas[0], m, s),
    Connective.And: lambda f, m, s: all(evaluate(sub, m, s) for sub in f.subformulas),
    Connective.Or: lambda f, m, s: any(evaluate(sub, m, s) for sub in f.subformulas)
}


def evaluate_atom(atom: Atom, m: Model, sigma):
    if builtins.is_builtin_predicate(atom.predicate):
        return evaluate_builtin(atom, m, sigma)

    else:  # the extension is given by the model
        point = [evaluate(t, m, sigma) for t in atom.subterms]
        return m.holds(atom.predicate, point)


def evaluate_quantified(formula: Formula, m: Model, sigma):
    raise NotImplementedError()


def evaluate_term(term, m: Model, sigma):
    assert isinstance(term, (m.language.Constant, m.language.CompoundTerm))
    arguments = []

    # TODO This is technically not correct - a constant still depends on the actual model on which is evaluated.
    # TODO A constant is simply a nullary compound term. E.g. an integer variable is still a logical constant.
    # TODO "Constant" does NOT mean "fixed denotation", although we can assume for convenience that there is one
    # TODO constant for each element in the universe, and the other way round
    # TODO How does Z3 deal with this distinction?
    # TODO We'll need to fix this eventually
    if isinstance(term, m.language.Constant):
        return term

    if isinstance(term, m.language.CompoundTerm):
        # evaluate each of the arguments
        arguments = tuple(evaluate(a, m, sigma) for a in term.subterms)

    return m.value(term.symbol, arguments)


def evaluate_builtin(atom, model, sigma):
    bip = builtins.BuiltinPredicate
    _evaluators = {
        bip.EQ: lambda f, m, s: evaluate(f.subterms[0], m, s) == evaluate(f.subterms[1], m, s),
        bip.NE: lambda f, m, s: evaluate(f.subterms[0], m, s) != evaluate(f.subterms[1], m, s),
        bip.LT: lambda f, m, s: evaluate(f.subterms[0], m, s) < evaluate(f.subterms[1], m, s),
        bip.LE: lambda f, m, s: evaluate(f.subterms[0], m, s) <= evaluate(f.subterms[1], m, s),
        bip.GT: lambda f, m, s: evaluate(f.subterms[0], m, s) > evaluate(f.subterms[1], m, s),
        bip.GE: lambda f, m, s: evaluate(f.subterms[0], m, s) >= evaluate(f.subterms[1], m, s),
    }

    return _evaluators[atom.predicate.symbol](atom, model, sigma)
