"""
 Classes and methods related to the naive grounding strategy of planning problems.
"""
import itertools
from typing import List

from ..grounding.ops import approximate_symbol_fluency
from ..syntax import Constant, Variable, CompoundTerm, Atom, create_substitution, termlists_are_equal, termlist_hash
from ..errors import DuplicateDefinition
from .errors import UnableToGroundError
from .common import StateVariableLite
from ..syntax.transform.substitutions import substitute_expression
from ..util import SymbolIndex
from ..fstrips.visitors import FluentSymbolCollector, FluentHeuristic


class ProblemGrounding:
    """ A ProblemGrounding contains information about the grounding of a lifted Tarski problem, possibly including
    information about ground state variables and ground actions.
    """
    def __init__(self, problem):
        self.problem = problem
        self.static_terms = None
        self.fluent_terms = None
        self.state_variables = None

    def _check_static_not_fluents(self):
        """
            Sorts fluent and static sets, so that the only
            static expressions are those which haven't been flagged
            as fluent by at least one of our heuristics.
        """
        self.static_terms = {x for x in self.static_terms if x not in self.fluent_terms}
        assert all(x not in self.static_terms for x in self.fluent_terms)

    def process_symbols(self, problem):
        lang = problem.language
        self.fluent_terms = set()
        self.static_terms = set()

        prec_visitor = FluentSymbolCollector(lang, self.fluent_terms, self.static_terms, FluentHeuristic.precondition)
        eff_visitor = FluentSymbolCollector(lang, self.fluent_terms, self.static_terms, FluentHeuristic.action_effects)
        constr_visitor = FluentSymbolCollector(lang, self.fluent_terms, self.static_terms, FluentHeuristic.constraint)

        o_f = len(self.fluent_terms)
        o_s = len(self.static_terms)
        while True:
            problem.get_symbols(prec_visitor, eff_visitor, constr_visitor)
            self._check_static_not_fluents()
            if len(self.fluent_terms) == o_f and len(self.static_terms) == o_s:
                break
            o_f = len(self.fluent_terms)
            o_s = len(self.static_terms)


def create_all_possible_state_variables(fluent_terms):
    """ Creates an index with all possible state variables by brute-force
        enumeration.
    """
    variables = SymbolIndex()

    for ref in fluent_terms:
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
            try:
                variables.add(StateVariable(ref.expr, instantiation))
            except DuplicateDefinition:
                pass
    return variables


class StateVariable:
    """ A state variable is nothing else than a CompoundTerm or Atom which is expected to change its
    value, along with a particular instantiation of its subterms.
    """

    def __init__(self, term, instantiation):
        assert isinstance(term, (CompoundTerm, Atom))
        self.term = term
        self.head = term.predicate if isinstance(term, Atom) else term.symbol
        self.instantiation = instantiation

    def __hash__(self):
        return hash((self.head.symbol, termlist_hash(self.instantiation)))

    def __eq__(self, other):
        return self.head.symbol == other.head.symbol and termlists_are_equal(self.instantiation, other.instantiation)

    def __str__(self):
        return '{}({})'.format(self.head.symbol, ','.join(str(a) for a in self.instantiation))

    __repr__ = __str__

    @property
    def ground(self):
        subst = create_substitution(self.term.subterms, self.instantiation)
        return substitute_expression(self.term, subst)


class NaiveGroundingStrategy:
    """ A naive problem grounding grounds actions and state variables of a lifted Tarski problem by (type-informed)
    exhaustive enumeration of all possible subsitutions of the representation variables.
    TODO / Note: This is a lightweight version of the ProblemGrounding class above, hoping that it can eventually
                 replace it.
    """
    def __init__(self, problem, ignore_symbols=None):
        self.problem = problem
        self.fluent_symbols, self.static_symbols = approximate_symbol_fluency(problem)
        if ignore_symbols:  # Remove undesired symbols if necessary
            self.fluent_symbols = {s for s in self.fluent_symbols if s.name not in ignore_symbols}
            self.static_symbols = {s for s in self.static_symbols if s.name not in ignore_symbols}

    def ground_state_variables(self):
        """ Create and index all state variables of the problem by exhaustively grounding all predicate and function
        symbols that are considered to be fluent with respect to the problem constants. Thus, if the problem has one
        fluent predicate "p" and one static predicate "q", and constants "a", "b", "c", the result of this operation
        will be the state variables "p(a)", "p(b)" and "p(c)".
        """
        return ground_symbols_exhaustively(self.fluent_symbols)

    def ground_actions(self):
        """  Return a dictionary mapping each action schema of the problem to the set of parameter groundings that
        make that schema a possible ground action. """
        groundings = {}
        for aname, action in self.problem.actions.items():
            domains = [p.sort.domain() for p in action.parameters]
            groundings[aname] = list(itertools.product(*domains))
        return groundings

    def __str__(self):
        return f'NaiveGroundingStrategy["{self.problem.name}"]'

    __repr__ = __str__


def ground_symbols_exhaustively(symbols):
    """ Creates an index with all possible groundings of the given predicate and function symbols
    in the given language """
    variables = SymbolIndex()

    for symbol in symbols:
        # We need to consider full sort for predicates, domain only for functions
        domains = [s.domain() for s in symbol.domain]

        for binding in itertools.product(*domains):
            variables.add(StateVariableLite(symbol, binding))

    return variables


def ground_partially_grounded_terms_exhaustively(terms: List[CompoundTerm]) -> SymbolIndex:
    """
    Creates an index with all possible groundings for the given terms, taking into account arguments which have
    been set to a constant
    :param terms:
    :return:
    """
    variables = SymbolIndex()

    for term in terms:
        domains = [s.domain() for s in term.symbol.domain]
        for i in range(len(domains)):
            if isinstance(term.subterms[i], Constant):
                domains[i] = [term.subterms[i]]
        for binding in itertools.product(*domains):
            variables.add(StateVariableLite(term.symbol, binding))

    return variables
