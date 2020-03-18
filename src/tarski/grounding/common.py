from ..errors import TarskiError
from ..syntax import Predicate, Function, Constant, termlists_are_equal, termlist_hash


class StateVariableLite:
    """ A state variable is a ground CompoundTerm or Atom which can possibly change its value along the execution of a
    plan. The set of all state variables of a problem makes up all information necessary to represent a state.
    State variables are different to static atoms, whose truth value can be proven to remain the same.
    This proof can be based on simple techniques such as looking at the effects of actions, or on more sophisticated
    reachability analyses.

    Note that we could use the CompoundTerm or Atom classes to represent the same concept represented by a
    StateVariableLite, but currently we prefer to use a single class, hence the existence of StateVariableLite.
    Note: This is a lightweight version of the StateVariable class above, hoping that it can eventually replace it.
    """

    def __init__(self, symbol, binding):
        if not isinstance(symbol, (Predicate, Function)) or not all(isinstance(c, Constant) for c in binding):
            raise TarskiError(f"Cannot build state variable from {symbol} and {binding}")
        self.symbol = symbol
        self.binding = binding

    def __hash__(self):
        return hash((self.symbol, termlist_hash(self.binding)))

    def __eq__(self, other):
        return self.symbol == other.symbol and termlists_are_equal(self.binding, other.binding)

    def __str__(self):
        return '{}({})'.format(self.symbol.symbol, ','.join(map(str, self.binding)))

    __repr__ = __str__

    @staticmethod
    def from_atom(atom):
        return StateVariableLite(atom.predicate, atom.subterms)

    def to_atom(self):
        return self.symbol(*self.binding)
