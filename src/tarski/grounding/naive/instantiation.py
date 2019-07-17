
from ...fol import FirstOrderLanguage
from ...syntax.terms import Constant, Variable
from ..errors import UnableToGroundError


def enumerate_groundings(_: FirstOrderLanguage, symbols):
    """ """
    syms = []
    instantiations = []
    cardinality = 1
    for st in symbols:
        if isinstance(st, Constant):
            continue
        elif isinstance(st, Variable):
            if st.sort.builtin:
                raise UnableToGroundError(st,
                                          "Term is of built-in sort '{}', domain is too large!".format(st.sort.name))
            syms.append(st)
            instantiations.append(list(st.sort.domain()))
            cardinality *= len(instantiations[-1])
        else:
            raise UnableToGroundError(st, "Grounding of complex nested subterms is not implemented yet!")

    return cardinality, symbols, instantiations
