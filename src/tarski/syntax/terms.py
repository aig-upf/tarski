
from typing import Tuple

from .util import termlists_are_equal, termlist_hash
from .sorts import Sort, parent, Interval
from .. import errors as err
from .builtins import BuiltinPredicateSymbol, BuiltinFunctionSymbol
#from .formulas import Formula, FormulaTerm


class Term:
    """ A first-order logical term.

        Important note: Term objects overload the equality operator `__eq__` to provide syntactic sugar and allow the
        construction of FOL atoms such as "loc(b1)==table". A side-effect of this is that Term objects cannot be
        inserted as such into associative containers such as dictionaries or sets. In order to use those, you will
        need to wrap the Term object with a call to `symref`, as e.g. in:
        >>> from tarski.fstrips import language
        >>> from tarski.syntax import symref
        >>> lang = language("test")
        >>> counter = dict()
        >>> c = lang.constant('c', 'object')
        >>> counter[c] = 2  # ERROR: will not work correctly
        >>> counter[symref(c)] = 2  # This is the correct way of doing it

        To prevent usage in such containers, Term objects are not hashable. If you need to hash them for other purposes,
        use the `t.hash()` method.
    """

    @property
    def language(self):
        raise NotImplementedError()  # Let the subclasses implement this

    @property
    def sort(self):
        raise NotImplementedError()  # Let the subclasses implement this

    def __enter__(self):
        """ This is useful to support scoped declaration of variables, e.g.:
                >>> bw = lang('blocksworld')
                >>> with bw.variable('x', block) as x, bw.variable('y', block) as y:
                >>>     _ = exists(x, clear(x))
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return exc_type is not None

    def __lshift__(self, rhs):
        return self.language.dispatch_operator('<<', Term, Term, self, rhs)

    def __rshift__(self, rhs):
        return self.language.dispatch_operator('>>', Term, Term, self, rhs)

    def __eq__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.EQ, Term, Term, self, rhs)

    def __ne__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.NE, Term, Term, self, rhs)

    def __lt__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.LT, Term, Term, self, rhs)

    def __gt__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.GT, Term, Term, self, rhs)

    def __le__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.LE, Term, Term, self, rhs)

    def __ge__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.GE, Term, Term, self, rhs)

    def __add__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.ADD, Term, Term, self, rhs)

    def __sub__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.SUB, Term, Term, self, rhs)

    def __mul__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.MUL, Term, Term, self, rhs)

    def __matmul__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.MATMUL, Term, Term, self, rhs)

    def __truediv__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.DIV, Term, Term, self, rhs)

    def __radd__(self, lhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.ADD, Term, Term, lhs, self)

    def __rsub__(self, lhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.SUB, Term, Term, lhs, self)

    def __rmul__(self, lhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.MUL, Term, Term, lhs, self)

    def __rtruediv__(self, lhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.DIV, Term, Term, lhs, self)

    def __pow__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.POW, Term, Term, self, rhs)

    def __mod__(self, rhs):
        return self.language.dispatch_operator(BuiltinFunctionSymbol.MOD, Term, Term, self, rhs)

    def __floordiv__(self, rhs):
        return self.language.dispatch_operator('//', Term, Term, self, rhs)

    def __divmod__(self, rhs):
        return self.language.dispatch_operator('divmod', Term, Term, self, rhs)

    def __and__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.AND, Term, Term, self, rhs)

    def __xor__(self, rhs):
        return self.language.dispatch_operator('^', Term, Term, self, rhs)

    def __or__(self, rhs):
        return self.language.dispatch_operator(BuiltinPredicateSymbol.OR, Term, Term, self, rhs)

    def is_syntactically_equal(self, other):
        """ Return true if this term and other are strictly syntactically equivalent.
        This would tipically be in the magic method `__eq__`, but we use `__eq__` for a different purpose,
        namely, to be able to use Python expressions such as "loc(b1)==table" in order to construct a FOL atom. """
        raise NotImplementedError()  # To be subclassed

    # def __hash__(self):
    #     Raise an informative exception to prevent wrong usage of terms in associative containers
        # raise err.WrongTermUsageError()
    # @see https://docs.python.org/3/reference/datamodel.html#object.__hash__
    __hash__ = None  # type: ignore

    def hash(self):
        """ Return a hash of the current object. Meant to be used by TermReference objects to wrap Terms appropriately
        for use within associative containers. """
        raise NotImplementedError()  # To be subclassed


class Variable(Term):

    def __init__(self, symbol: str, sort: Sort):
        self.symbol = symbol
        self._sort = sort

    @property
    def language(self):
        return self.sort.language

    @property
    def sort(self):
        return self._sort

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return '{} ({})'.format(self.symbol, self.sort.name)

    def hash(self):
        return hash((self.symbol, self.sort.name))

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ and self.symbol == other.symbol and self.sort.name == other.sort.name


class CompoundTerm(Term):
    """ A first order compound term such as "f(c, d)", where f is a function symbol of arity 2, and c and d are both
    constant symbols. More generally, a compound term is a function symbol of a certain arity n paired with an n-tuple
    of terms, sorts matching.
    """

    def __init__(self, symbol, subterms: Tuple[Term]):

        self.symbol = symbol

        if len(subterms) != self.symbol.arity:
            raise err.ArityMismatch(symbol, subterms)
        argument_sorts = list(self.symbol.sort)[:-1]
        processed_st = []
        for k, s in enumerate(argument_sorts):
            # @TODO Implement upcasting for non built-in compound terms
            try:
                if subterms[k].sort.name != s.name and not self.symbol.language.is_subtype(subterms[k].sort, s):
                    raise err.SortMismatch(self.symbol, subterms[k].sort, s)
                processed_st.append(subterms[k])
            except AttributeError:
                s_k = s.cast(subterms[k])
                if s_k is None:
                    raise err.SortMismatch(self.symbol, subterms[k], s) from None
                processed_st.append(s_k)
        self.subterms = tuple(processed_st)

    @property
    def language(self):
        return self.symbol.language

    @property
    def sort(self):
        return self.symbol.codomain

    def __str__(self):
        return '{}({})'.format(self.symbol.symbol, ', '.join(str(t) for t in self.subterms))

    __repr__ = __str__

    def hash(self):
        return hash((self.symbol.symbol, termlist_hash(self.subterms)))

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ and \
               self.symbol == other.symbol and \
               termlists_are_equal(self.subterms, other.subterms)


class AggregateCompoundTerm(Term):
    """
        Combinations of a functional symbol, a set of bound variables and a sequence of terms.
        Examples of such terms include summations, products and other operations over sequences.

        Argument symbol needs to be an instance of Function or have Function-like interface.
    """

    def __init__(self, operator, bound_vars, subterm: Term):
        self.symbol = operator
        self.bound_vars = bound_vars
        if not isinstance(subterm, Term):
            subterm = subterm.build_formulaterm()
        self.subterm = subterm  # TODO: type checking?

    @property
    def language(self):
        return self.subterm.language

    @property
    def sort(self):
        return self.subterm.sort

    def __str__(self):
        return '{}_{{{}}}({})'.format(self.symbol, ','.join([str(x) for x in self.bound_vars]), str(self.subterm))

    __repr__ = __str__

    def hash(self):
        raise NotImplementedError()

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ and \
               self.symbol == other.symbol and \
               termlists_are_equal(self.bound_vars, other.bound_vars) and \
               self.subterm.is_syntactically_equal(other.subterm)


class IfThenElse(Term):
    """
        Combination of a formula C and two terms, t1 and t2.

        This term evaluates to t1 if C is true, and t2 otherwise. t1 and t2
        are restricted to have the same codomain.
    """

    def __init__(self, condition, subterms: Tuple[Term, Term]):
        if len(subterms) != 2:
            raise err.ArityMismatch('IfThenElse', subterms, msg='IfThenElse term needs exactly two sub terms')

        self.symbol = subterms[0].language.get('ite')
        self.condition = condition
       #if either of the subterms are boolean Formulae, wrap them as Terms
        if not isinstance(subterms[0], Term): #todo: [John Peterson] It's gross that we can't directly compare against Formula (because of circular import concerns). This needs to be fixed eventually (likely with the full Formula/Term refactor)
            subterms = (subterms[0].build_formulaterm(), subterms[1])
        if not isinstance(subterms[1], Term):
            subterms = (subterms[0], subterms[1].build_formulaterm())#todo:[John Peterson] I'm not sure if I like this build_formulaterm name. Consider renaming.

        # Our implementation of ite requires both branches to have equal sort
        if subterms[0].sort != subterms[1].sort:
            if parent(subterms[0].sort) == subterms[1].sort:
                self._sort = subterms[1].sort
            elif parent(subterms[1].sort) == subterms[0].sort:
                self._sort = subterms[0].sort
            else:
                raise err.SyntacticError(
                    msg='IfThenElse: both subterms need to be of the same sort! lhs: "{}"({}), rhs: "{}"({})'.format(
                        subterms[0], subterms[0].sort, subterms[1], subterms[1].sort))
        else:
            self._sort = subterms[0].sort

        self.subterms = tuple(subterms)

    @property
    def language(self):
        return self.symbol.language

    @property
    def sort(self):
        return self._sort

    def __str__(self):
        return '{}({})'.format(self.symbol, ', '.join([str(self.condition)] + [str(t) for t in self.subterms]))

    __repr__ = __str__

    def hash(self):
        return hash(('ite', self.condition.hash(), termlist_hash(self.subterms)))

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ and \
               self.symbol == other.symbol and \
               self.condition.is_syntactically_equal(other.condition) and \
               termlists_are_equal(self.subterms, other.subterms)


def ite(c, t1: Term, t2: Term):
    return IfThenElse(c, (t1, t2))

class Constant(Term):
    def __init__(self, name, sort: Sort):
        self.name = name
        self._sort = sort

        if isinstance(sort, Interval):
            self.name = sort.cast(self.name)
        else:
            # If the sort is an enumerated type, constructing a new constant extends its domain
            sort.extend(self)

    @property
    def symbol(self):
        return self.name

    @property
    def language(self):
        return self.sort.language

    @property
    def sort(self):
        return self._sort

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return '{} ({})'.format(self.name, self.sort.name)

    def hash(self):
        return hash((self.name, self.sort))

    def is_syntactically_equal(self, other):
        return self.__class__ is other.__class__ and self.name == other.name and self.sort == other.sort
