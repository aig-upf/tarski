
from ...syntax import Atom, CompoundFormula, Connective, Constant, CompoundTerm
from ...syntax.builtins import BuiltinPredicateSymbol

from .errors import TransformationError


def unpack_element_subterms(element):
    elems = []
    for c in element.subterms:
        if not isinstance(c, Constant):
            raise TransformationError("transform-to-ground-atoms", element, "Cannot unpack non-ground atom")
        elems.append(c.symbol)
    return elems


def unpack_atom(atom):
    assert isinstance(atom, Atom)

    if atom.predicate.builtin:
        if not atom.predicate.symbol == BuiltinPredicateSymbol.EQ:
            raise TransformationError("transform-to-ground-atoms", atom, "Cannot unpack non-equality atom")
        x = [x for x in atom.subterms if isinstance(x, CompoundTerm)]
        c = [c for c in atom.subterms if isinstance(c, Constant)]
        if len(x) != 1 or len(c) != 1:
            raise TransformationError("transform-to-ground-atoms", atom,
                                      "Can only use functional atoms of the form f(c) = d, where c and d are constants")
        x, c = x[0], c[0]
        return tuple([x.symbol.symbol] + unpack_element_subterms(x) + [c.symbol])

    else:
        return tuple([atom.predicate.symbol] + unpack_element_subterms(atom))


def transform_to_ground_atoms(phi):
    """ Take a formula expected to be a conjunction of ground atoms and return the list of ground atoms,
    each of them as a tuple of the form (on, a, b).
    Raise an exception if the formula is not a conjunction of ground atoms. """
    if not isinstance(phi, Atom) and not (isinstance(phi, CompoundFormula) and phi.connective == Connective.And):
        raise TransformationError("transform-to-ground-atoms", phi,
                                  "Only conjunctions of ground atoms can be transformed")

    if isinstance(phi, Atom):  # Base case of the recursion
        return [unpack_atom(phi)]

    atoms = []
    for sub in phi.subformulas:
        atoms += transform_to_ground_atoms(sub)
    return atoms
