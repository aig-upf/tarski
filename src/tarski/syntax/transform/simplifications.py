
from tarski.syntax import Atom, CompoundFormula, Connective, Constant
from .errors import TransformationError


def unpack_atom(atom):
    assert isinstance(atom, Atom)
    # if atom.predicate.symbol == BuiltinPredicateSymbol.EQ:
    if atom.predicate.builtin:
        raise NotImplemented("Yet to be implemented")

    elems = [atom.predicate.symbol]
    for c in atom.subterms:
        if not isinstance(c, Constant):
            raise TransformationError("transform-to-ground-atoms", atom, "Cannot unpack non-ground atom")
        elems.append(c.symbol)
    return tuple(elems)


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
