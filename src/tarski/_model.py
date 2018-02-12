# -*- coding: utf-8 -*-
from .errors import LanguageError
from ._terms import Term, Variable, Constant
from ._formulas import Formula
from ._function import Function
from ._predicate import Predicate


class Model(object):
    """
        A First Order Language Model
    """

    def __init__(self, lang):
        self._lang = lang
        self._func_ext = {}
        self._pred_ext = {}

    def L(self):
        return self._lang

    def __getitem__(self, obj):
        if isinstance(obj, Term):
            return self.evaluate(obj)
        if isinstance(obj, Formula):
            return self.check_satisfiability(obj)

    def set(self, symbol: Function, tup):
        try:
            symbol.check_arguments(*tup)
            interpreted_args = tuple(a.symbol for a in tup[:-1])
            value = Constant.create(symbol.codomain.cast(tup[-1]), symbol.codomain, self.L)

        except TypeError:
            interpreted_args = ()
            value = Constant.create(symbol.codomain.cast(tup), symbol.codomain, self.L)
        # print('{} : {} -> {}'.format(symbol.signature,interpreted_args,value.symbol))
        try:
            self._func_ext[symbol.signature][interpreted_args] = value
        except KeyError:
            self._func_ext[symbol.signature] = {interpreted_args: value}

    def add(self, symbol: Predicate, tup=None):
        try:
            entry = frozenset([a.symbol for a in tup])
        except TypeError:
            if tup is None :
                entry = frozenset()
            elif isinstance(tup, Constant):
                entry = frozenset([tup.symbol])
            else:
                raise LanguageError('Model.add() : arguments need to be tuple of constants, constants')
        try:
            self._pred_ext[symbol.signature].add(entry)
        except KeyError:
            self._pred_ext[symbol.signature] = set()
            self._pred_ext[symbol.signature].add(entry)

    def remove(self, symbol: Predicate, tup=None):
        try :
            entry = frozenset([a.symbol for a in tup])
        except TypeError :
            if tup is None :
                entry = frozenset()
            elif isinstance(tup, Constant) :
                entry = frozenset([tup.symbol])
            else :
                raise LanguageError('Model.remove() : arguments of tuple to add for predicate needs to be a tuple of constants or a constant')
        self._pred_ext[symbol.signature].remove(entry)

    def evaluate(self, t):
        if isinstance(t, Variable):
            raise LanguageError("eval(): Found free variable {}".format(t))
        elif isinstance(t, Constant):
            return t
        elif isinstance(t, Term):
            # evaluate each of the arguments
            interpreted = [self.evaluate(a) for a in t.arguments]
            symbols = tuple(i.symbol for i in interpreted)
            try:
                return t.symbol.__getitem__(*symbols)
            except ValueError:
                # check extension
                # print("[f({})]^s = {}".format(symbols, self._func_ext[t.symbol.signature][symbols]))
                return self._func_ext[t.symbol.signature][symbols]
        elif isinstance(t, tuple):
            pred_sym, terms = t
            interpreted = [self.evaluate(a) for a in terms]
            symbols = frozenset(tuple(i.symbol for i in interpreted))
            # print('P({}) : {}'.format(symbols, symbols in self._pred_ext[pred_sym.signature]))
            return symbols in self._pred_ext[pred_sym.signature]

        raise LanguageError("Model.evaluate() : Could not interpret: {}".format(t))

    def check_satisfiability(self, phi):
        return phi.satisfiable(self)
