# -*- coding: utf-8 -*-
from ._errors import LanguageError
from ._sorts import *
from ._terms import Term, Constant, Variable
from ._predicate import Predicate, Equality
from ._function import Function
from ._model import Model

from ._relational import EQFormula, LTFormula, GTFormula, LEQFormula, GEQFormula, NEQFormula

import tarski.funcsym

class FOL :

    formula_symbols = {
        '=' : EQFormula,
        '!=' : NEQFormula,
        '<' : LTFormula,
        '>' : GTFormula,
        '<=' : LEQFormula,
        '>=' : GEQFormula
    }

    def __init__(self) :
        self._sorts = {}
        # MRJ: let's represent this temporally as pairs of names of sorts,
        # lhs \sqsubseteq rhs, lhs is a subset of rhs
        self._sort_hierarchy = set()
        # MRJ: this contains a table where we record possible promotions
        # between sorts (i.e. bottom up along the hierarchy)
        self._possible_promotions = {}
        self._functions = {}
        self._predicates = {}
        self._variables = set()

        # MRJ: let's allow default equality predicates to be enabled/disabled
        # dynamically
        self._default_equality = True
        self._symbol_table = {}
        self._build_builtin_sorts()
        tarski.funcsym.initialize(self)

    def _inclusion_closure( self, s: Sort ) -> Set[Sort] :
        """
            Calculates the inclusion closure over given sort s
        """
        closure = set()
        frontier = { s }
        while len(frontier) > 0 :
            s = frontier.pop()
            closure.add(s)
            for p in parents(s) :
                frontier.add(p)
        return closure

    @property
    def variables(self) :
        for x in self._variables :
            yield x

    @property
    def sort_hierarchy(self) :
        return self._sort_hierarchy

    @property
    def sorts(self) :
        for s in self.sorts :
            yield s

    @property
    def predicates(self) :
        for _, p in self._predicates.items() :
            yield p

    @property
    def functions(self) :
        for f in self._functions.items() :
            yield f

    def _build_builtin_sorts(self) :
        self._build_the_reals()
        self._build_the_integers()
        self._build_the_naturals()

    def _build_the_reals(self) :
        the_reals = Interval( -3.40282e+38, 3.40282e+38, lambda x : float(x), 'Real', self )
        the_reals.built_in = True
        the_reals.pi = scipy.constants.pi
        self._sorts['Real'] = the_reals
        sort_eq = Equality(self,the_reals,the_reals)
        self._predicates[sort_eq.signature] = sort_eq

    @property
    def Real(self) :
        return self._sorts['Real']

    def _build_the_integers(self) :
        the_ints = Interval( -(2**31-1), 2**31-1, lambda x : int(x), 'Integer', self )
        the_ints.built_in = True
        self._sorts['Integer'] = the_ints
        self.set_parent( the_ints, self.sort('Real'))
        sort_eq = Equality(self,the_ints,the_ints)
        self._predicates[sort_eq.signature] = sort_eq

    @property
    def Integer(self) :
        return self._sorts['Integer']

    def _build_the_naturals(self) :
        the_nats = Interval( 0, 2**32-1, lambda x : int(x), 'Natural', self )
        the_nats.built_in = True
        self._sorts['Natural'] = the_nats
        self.set_parent( the_nats, self.sort('Integer'))
        sort_eq = Equality(self,the_nats,the_nats)
        self._predicates[sort_eq.signature] = sort_eq

    @property
    def Natural(self) :
        return self._sorts['Natural']

    def sort( self, name : str, super_list : List[Sort] = []) :
        """
            Creates instance of Sort object, adds it to the table of
            sorts
        """
        other = self._sorts.get(name,None)
        if other :
            return other
        sort_obj = Sort(name, self)
        self._sorts[name] = sort_obj
        if super is None :
            self._possible_promotions[name] = set() # no possible promotions
            return sort_obj
        # MRJ: list of objects or names?
        for parent in super_list :
            self.set_parent(sort_obj, parent)
        # MRJ: create equality
        if self._default_equality :
            sort_eq = Equality(self,sort_obj,sort_obj)
            self._predicates[sort_eq.signature] = sort_eq
        return sort_obj

    def var( self, name : str, type : Sort ) :
        return Variable(name, type, self)

    def set_parent(self, lhs : Sort, rhs : Sort ) :
        if rhs.language is not self :
            raise LanguageError("FOL.sort(): tried to set as parent a sort from a different language")
        self._sort_hierarchy.add( (lhs.name, rhs.name))
        self._possible_promotions[lhs.name] = self._inclusion_closure(rhs)

    def const( self, namelist, sort ) :
        """
            Creates constant symbol of a given sort
        """
        if isinstance(sort, str) :
            try :
                sort = self._sorts[sort]
            except KeyError :
                raise LanguageError("FOL.const() : unknown sort '{}'".format(sort))
        elif isinstance(sort, Sort) :
            if sort._language != self :
                raise LanguageError("FOL.const() : sort '{}' has not been declared for this language!".format(sort.name))
        else :
            raise LanguageError("FOL.const() : the specified 'sort' argument needs to be a string or a Sort instance, not {}".format(type(sort)))

        if namelist is None :
            raise LanguageError("'None' cannot be a constant symbol!")

        if not sort.built_in :

            if isinstance(namelist, types.GeneratorType) :
                return tuple(list(Constant(n,sort,self) for n in namelist ))

            const_sym = Constant(namelist, sort, self)
            return const_sym

        if isinstance(namelist, types.GeneratorType) :
            return tuple(list(sort.cast(n) for n in namelist))
        return sort.cast(namelist)

    def predicate(self, symbol : str, *args ) :
        pred = Predicate(symbol, self, *args)
        try :
            return self._predicates[pred.signature]
        except KeyError :
            self._predicates[ pred.signature ] = pred
        return pred

    def function(self, symbol : str, *args) :
        func = Function(symbol, self, *args)
        try :
            return self._functions[ func.signature ]
        except KeyError :
            self._functions[ func.signature ] = func
        return func

    def model( self ) :
        return Model( self )

    def dump(self) :
        return dict(\
                sorts = [s.dump() for _, s in self._sorts.items() ],\
                predicates = [p.dump() for _, p in self._predicates.items()],\
                functions = [f.dump() for _, f in self._functions.items()]
                )


    def is_well_formed(self) :
        for _, s in self._sorts.items() :
            s.check_empty()

    def register_symbol(self, key, func_obj ) :
        self._symbol_table[key] = func_obj

    def resolve_function_symbol_2( self, sym : str, lhs : Sort, rhs : Sort ) :
        try :
            return self._symbol_table[(sym,lhs,rhs)]
        except KeyError :
            raise LanguageError("FOL.resolve_function_symbol_2(): function symbol '{}' is not defined for domain ({},{})"\
                .format(sym,lhs,rhs))
        return None

    def resolve_formula_symbol(self, symbol) :
        return FOL.formula_symbols[symbol]
