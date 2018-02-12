# -*- coding: utf-8 -*-
from .errors import LanguageError
from ._sorts import Sort
import copy


class Term(object):
    """
        Term class

        NOTE: since we are overloading operators like __eq__, etc. these objects
        may invalidate the assumptions of standard Python containers like set()
        or break methods like find(). Any container for Term and subclasses
        will need to be implemented using the comparison the id() of the instances.
    """

    def __init__(self, sym, arguments, lang):
        self._f = sym
        self._lang = lang

        for a in arguments:
            if not isinstance(a, Term):
                raise LanguageError("Syntax error: argument {} is not a term".format(a))

        self._args = copy.copy(arguments)

    @property
    def symbol(self):
        return self._f

    @property
    def arguments(self):
        return self._args

    @property
    def is_constant(self):
        return isinstance(self, Constant)

    @property
    def type(self):
        return self.symbol.type

    @property
    def language(self):
        return self._lang

    def __str__(self):
        return '{}({})'.format(self.symbol.symbol, ','.join([str(t) for t in self.arguments]))

    def dump(self):
        return dict(symbol=self.f.dump(),
                    arguments=[t.dump() for t in self.arguments])

    def __add__(self, rhs):
        sym = self.language.resolve_function_symbol_2('+', self.type, rhs.type)
        return sym(self, rhs)

    def __sub__(self, rhs):
        sym = self.language.resolve_function_symbol_2('-', self.type, rhs.type)
        return sym(self, rhs)

    def __mul__(self, rhs):
        sym = self.language.resolve_function_symbol_2('*', self.type, rhs.type)
        return sym(self, rhs)

    def __matmul__(self, rhs):
        sym = self.language.resolve_function_symbol_2('@', self.type, rhs.type)
        return sym(self, rhs)

    def __truediv__(self, rhs):
        sym = self.language.resolve_function_symbol_2('/', self.type, rhs.type)
        return sym(self, rhs)

    def __floordiv__(self, rhs):
        sym = self.language.resolve_function_symbol_2('//', self.type, rhs.type)
        return sym(self, rhs)

    def __mod__(self, rhs):
        sym = self.language.resolve_function_symbol_2('%', self.type, rhs.type)
        return sym(self, rhs)

    def __divmod__(self, rhs):
        sym = self.language.resolve_function_symbol_2('divmod', self.type, rhs.type)
        return sym(self, rhs)

    def __pow__(self, rhs):
        sym = self.language.resolve_function_symbol_2('**', self.type, rhs.type)
        return sym(self, rhs)

    def __lshift__(self, rhs):
        sym = self.language.resolve_function_symbol_2('<<', self.type, rhs.type)
        return sym(self, rhs)

    def __rshift__(self, rhs):
        sym = self.language.resolve_function_symbol_2('>>', self.type, rhs.type)
        return sym(self, rhs)

    def __and__(self, rhs):
        sym = self.language.resolve_function_symbol_2('&', self.type, rhs.type)
        return sym(self, rhs)

    def __xor__(self, rhs):
        sym = self.language.resolve_function_symbol_2('^', self.type, rhs.type)
        return sym(self, rhs)

    def __or__(self, rhs):
        sym = self.language.resolve_function_symbol_2('|', self.type, rhs.type)
        return sym(self, rhs)

    def __eq__(self, rhs):
        sym = self.language.resolve_formula_symbol('=')
        return sym(self, rhs)

    def __ne__(self, rhs):
        sym = self.language.resolve_formula_symbol('!=')
        return sym(self, rhs)

    def __lt__(self, rhs):
        sym = self.language.resolve_formula_symbol('<')
        return sym(self, rhs)

    def __gt__(self, rhs):
        sym = self.language.resolve_formula_symbol('>')
        return sym(self, rhs)

    def __le__(self, rhs):
        sym = self.language.resolve_formula_symbol('<=')
        return sym(self, rhs)

    def __ge__(self, rhs):
        sym = self.language.resolve_formula_symbol('>=')
        return sym(self, rhs)

    def __enter__(self) :
        return self

    def __exit__(self, exc_type, exc_value, traceback) :
        if exc_type is None : return False
        return True


class Constant(Term):
    def __init__(self, name: str, sort: Sort, lang):
        self._name = name
        super(Constant, self).__init__(self, [], lang)
        self._sort = sort
        self._sort.extend(self)

    @property
    def symbol(self):
        return self._name

    @property
    def sort(self):
        return self._sort

    @property
    def type(self):
        return self._sort

    @property
    def language(self):
        return self._lang

    @classmethod
    def create(klass, name, sort: Sort, lang):
        return Constant(name, sort, lang)

    def dump(self):
        return dict(symbol=self.symbol, sort=self.sort.name)

    def __deepcopy__(self, memo):
        newone = type(self)(self._name, self._sort, self._lang)
        memo[id(self)] = newone
        for k, v in self.__dict__.items():
            setattr(newone, k, copy.deepcopy(v, memo))
        return newone

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return str(self.symbol)

    def __add__(self, rhs: Term):
        return super(Constant, self).__add__(rhs)

    def __sub__(self, rhs: Term):
        return super(Constant, self).__sub__(rhs)

    def __mul__(self, rhs: Term):
        return super(Constant, self).__mul__(rhs)

    def __matmul__(self, rhs: Term):
        return super(Constant, self).__matmul__(rhs)

    def __truediv__(self, rhs: Term):
        return super(Constant, self).__truediv__(rhs)

    def __floordiv__(self, rhs: Term):
        return super(Constant, self).__floordiv__(rhs)

    def __mod__(self, rhs: Term):
        return super(Constant, self).__mod__(rhs)

    def __divmod__(self, rhs: Term):
        return super(Constant, self).__divmod__(rhs)

    def __pow__(self, rhs: Term):
        return super(Constant, self).__pow__(rhs)

    def __lshift__(self, rhs: Term):
        return super(Constant, self).__lshift__(rhs)

    def __rshift__(self, rhs: Term):
        return super(Constant, self).__rshift__(rhs)

    def __and__(self, rhs: Term):
        return super(Constant, self).__and__(rhs)

    def __xor__(self, rhs: Term):
        return super(Constant, self).__xor__(rhs)

    def __or__(self, rhs: Term):
        return super(Constant, self).__or__(rhs)

    def __eq__(self, rhs):
        return super(Constant, self).__eq__(rhs)

    def __ne__(self, rhs):
        return super(Constant, self).__ne__(rhs)

    def __lt__(self, rhs):
        return super(Constant, self).__lt__(rhs)

    def __gt__(self, rhs):
        return super(Constant, self).__gt__(rhs)

    def __le__(self, rhs):
        return super(Constant, self).__le__(rhs)

    def __ge__(self, rhs):
        return super(Constant, self).__ge__(rhs)


class Variable(Term):
    def __init__(self, name: str, sort: Sort, lang):
        super().__init__(self, [], lang)
        self._name = name
        self._sort = sort

    def __deepcopy__(self, memo):
        newone = type(self)(self._name, self._sort, self._lang)
        memo[id(self)] = newone
        for k, v in self.__dict__.items():
            setattr(newone, k, copy.deepcopy(v, memo))
        return newone

    @property
    def symbol(self):
        return self._name

    @property
    def sort(self):
        return self._sort

    @property
    def type(self):
        return self._sort

    @property
    def language(self):
        return self._lang

    def __hash__(self):
        return hash((self._name, self._sort.name))

    def dump(self):
        return dict(symbol=self.symbol)

    def __str__(self):
        return '?{}'.format(str(self.symbol))

    def __add__(self, rhs: Term):
        return super(Variable, self).__add__(rhs)

    def __sub__(self, rhs: Term):
        return super(Variable, self).__sub__(rhs)

    def __mul__(self, rhs: Term):
        return super(Variable, self).__mul__(rhs)

    def __matmul__(self, rhs: Term):
        return super(Variable, self).__matmul__(rhs)

    def __truediv__(self, rhs: Term):
        return super(Variable, self).__truediv__(rhs)

    def __floordiv__(self, rhs: Term):
        return super(Variable, self).__floordiv__(rhs)

    def __mod__(self, rhs: Term):
        return super(Variable, self).__mod__(rhs)

    def __divmod__(self, rhs: Term):
        return super(Variable, self).__divmod__(rhs)

    def __pow__(self, rhs: Term):
        return super(Variable, self).__pow__(rhs)

    def __lshift__(self, rhs: Term):
        return super(Variable, self).__lshift__(rhs)

    def __rshift__(self, rhs: Term):
        return super(Variable, self).__rshift__(rhs)

    def __and__(self, rhs: Term):
        return super(Variable, self).__and__(rhs)

    def __xor__(self, rhs: Term):
        return super(Variable, self).__xor__(rhs)

    def __or__(self, rhs: Term):
        return super(Variable, self).__or__(rhs)

    def __eq__(self, rhs):
        return super(Variable, self).__eq__(rhs)

    def __ne__(self, rhs):
        return super(Variable, self).__ne__(rhs)

    def __lt__(self, rhs):
        return super(Variable, self).__lt__(rhs)

    def __gt__(self, rhs):
        return super(Variable, self).__gt__(rhs)

    def __le__(self, rhs):
        return super(Variable, self).__le__(rhs)

    def __ge__(self, rhs):
        return super(Variable, self).__ge__(rhs)


Var = Variable
