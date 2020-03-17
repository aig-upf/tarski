
from ...syntax.terms import Constant, Variable
from ..errors import UnableToGroundError


def enumerate_groundings(symbols):
    """ """
    syms = []
    instantiations = []
    cardinality = 1
    for st in symbols:
        if isinstance(st, Constant):
            continue
        elif isinstance(st, Variable):
            if st.sort.builtin:
                # TODO This restriction could be lifted?
                raise UnableToGroundError(st, "Cannot ground variables of built-in sorts")
            syms.append(st)
            instantiations.append(list(st.sort.domain()))
            cardinality *= len(instantiations[-1])
        else:
            raise UnableToGroundError(st, "Grounding of complex nested subterms is not implemented yet!")

    return cardinality, symbols, instantiations
