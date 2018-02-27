"""
    A module to deal with the instantiation of state variables.
"""

import itertools

from .util import IndexDictionary
from tarski import Function, Predicate

class StateVariable(object):
    """
    A state variable, a CompoundTerm of note along with a particular instantiation
    of its subterms.
    """
    def __init__(self, term, instantiation):
        self.term = term
        try :
            self.head = term.symbol.symbol
        except AttributeError:
            self.head = term.predicate.symbol
        self.instantiation = instantiation

    def __hash__(self):
        return hash((self.term.symbol, self.instantiation))

    def __eq__(self, other):
        return self.term.symbol == other.term.symbol\
            and all(repr(lhs)==repr(rhs) for lhs, rhs in zip(self.instantiation,other.instantiation))

    def __str__(self):
        return '{}({})'.format(self.head, ','.join([str(a) for a in self.instantiation]))

    __repr__ = __str__

def create_all_possible_state_variables(fluent_symbols):
    """ Creates an index with all possible state variables by brute-force
        enumeration.
    """
    variables = IndexDictionary()

    for expr in fluent_symbols:
        # @TODO: Work in Progress and we will need to iterate over this a bit
        instantiations = [ list(t.sort.domain()) for t in expr.e.subterms]
        for instantiation in itertools.product(*instantiations):
            variables.add( StateVariable(expr.e,instantiation) )
    return variables


# @TODO: review and refactor this method, most definitely we don't want the groundings of the symbols
# to come as part of the predicates or functions
def create_all_possible_state_variables_from_groundings(predicates, functions, object_idx, static_symbols):
    variables = IndexDictionary()

    for pred in predicates:
        raise NotImplementedError("state_variables.create_all_possible_state_variables_from_groundings() not implemented yet!")
        # MRJ: @TODO: I am leaving the code below commented for future reference
        #name = pred.name
        #if is_external(name) or name in static_symbols:
        #    continue

        #grounding_ids = []  # A list with the (integer index of) each grounding
        #for grounding in pred.groundings:
        #    grounding_ids.append(tuple(object_idx.get_index(obj_name) for obj_name in grounding))

        #for grounding in sorted(grounding_ids):  # IMPORTANT to output the groundings in lexicographical order
        #    variables.add(Variable(name, [object_idx.get_object(obj_id) for obj_id in grounding]))

    if functions:
        raise NotImplementedError("Gringo grounder not yet prepared for functions")

    return variables
