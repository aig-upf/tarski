
from ..syntax import Predicate, Function, Constant, termlists_are_equal, termlist_hash


class StateVariableLite:
    """ A state variable is nothing else than a CompoundTerm or Atom which is expected to change its
    value, along with a particular instantiation of its subterms.
    Note: This is a lightweight version of the StateVariable class above, hoping that it can eventually replace it.
    """

    def __init__(self, symbol, binding):
        assert isinstance(symbol, (Predicate, Function))
        assert all(isinstance(c, Constant) for c in binding)
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
