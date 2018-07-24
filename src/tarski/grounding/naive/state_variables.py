# -*- coding: utf-8 -*-
"""
    A module to deal with the instantiation of state variables.
"""

import itertools
import copy

from ...util import IndexDictionary
from ... import Variable, Constant
from ...syntax.transform.subst import TermSubstitution

from ..errors import UnableToGroundError


class StateVariable:
    """
    A state variable, a CompoundTerm or Atom which is expected to change its
    value, along with a particular instantiation of its subterms.
    """

    def __init__(self, term, instantiation):
        self.term = term
        try:
            self.head = term.predicate
        except AttributeError:
            self.head = term.symbol
        self.instantiation = instantiation

    def __hash__(self):
        if len(self.instantiation) == 0:
            return hash(self.head.symbol)
        accum = hash(self.instantiation[0])
        for k in range(1, len(self.instantiation)):
            accum = accum ^ hash(self.instantiation[k])
        return hash(self.head.symbol) ^ accum

    def __eq__(self, other):
        return self.head.symbol == other.head.symbol \
               and all(lhs.symbol == rhs.symbol for lhs, rhs, in zip(self.instantiation, other.instantiation))

    def __str__(self):
        return '{}({})'.format(self.head.symbol, ','.join([str(a) for a in self.instantiation]))

    @property
    def ground(self):
        subst = {k: v for k, v in zip(self.term.subterms, self.instantiation)}
        g = copy.deepcopy(self.term)
        v = TermSubstitution(self.head.language, subst)
        g.accept(v)
        return g

    __repr__ = __str__


def create_all_possible_state_variables(fluent_symbols):
    """ Creates an index with all possible state variables by brute-force
        enumeration.
    """
    variables = IndexDictionary()

    for ref in fluent_symbols:
        # @TODO: Work in Progress and we will need to iterate over this a bit
        # @TODO: Sort fluent symbols according to the number of variable subterms
        # L = ref.language
        instantiations = []
        for st in ref.expr.subterms:
            if isinstance(st, Constant):
                instantiations.append([st])
            elif isinstance(st, Variable):
                if st.sort.builtin:
                    raise UnableToGroundError(st, "Term is of built-in sort '{}', domain is too large!".format(
                        st.sort.name))
                instantiations.append(list(st.sort.domain()))
            else:
                raise UnableToGroundError(st, "Grounding of complex nested subterms is not implemented yet!")
        for instantiation in itertools.product(*instantiations):
            variables.add(StateVariable(ref.expr, instantiation))
    return variables


# @TODO: review and refactor this method, most definitely we don't want the groundings of the symbols
# @TODO: to come as part of the predicates or functions
def create_all_possible_state_variables_from_groundings(predicates, functions, object_idx, static_symbols):
    # pylint: disable=unused-argument
    raise NotImplementedError(
        "state_variables.create_all_possible_state_variables_from_groundings() not implemented yet!")
    # variables = IndexDictionary()
    # for pred in predicates:
    #     # MRJ: @TODO: I am leaving the code below commented for future reference
    #     name = pred.name
    #     if is_external(name) or name in static_symbols:
    #        continue
    #
    #     grounding_ids = []  # A list with the (integer index of) each grounding
    #     for grounding in pred.groundings:
    #        grounding_ids.append(tuple(object_idx.get_index(obj_name) for obj_name in grounding))
    #
    #     for grounding in sorted(grounding_ids):  # IMPORTANT to output the groundings in lexicographical order
    #        variables.add(Variable(name, [object_idx.get_object(obj_id) for obj_id in grounding]))

    # if functions:
    #     raise NotImplementedError("Gringo grounder not yet prepared for functions")

    # return variables
