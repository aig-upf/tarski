# -*- coding: utf-8 -*-

import types
import scipy.constants

class LanguageError(Exception) :
    pass

class Sort :

    def __init__(self, name, lang) :
        self._name = name
        self._language = lang
        self._domain = {}
        self._built_in = False

    @property
    def name(self) :
        return self._name

    @property
    def built_in(self) :
        return self._built_in
    @built_in.setter
    def built_in(self,v) :
        self._built_in = v
        assert self._built_in == True or self._built_in == False

    def contains( self, x ) :
        try :
            return self._domain[x] != None # this should always return True
        except KeyError :
            return False

    def check_empty(self) :
        if len(self._domain) == 0 :
            raise LanguageError("Sort '{}' is empty!".format(self._name))

    def dump(self) :
        return dict( name = self._name,\
                     domain = [n for n, _ in self._domain.items()] )


class Interval(Sort) :

    def __init__(self, lb, ub, encode_fn, name, lang ) :
        super(Interval, self).__init__(name,lang)
        self._lb = lb
        self._ub = ub
        self._encode = encode_fn
        self._domain = lambda x : x >= self._lb and x <= self._ub

    def cast( self, x ) :
        if isinstance(x,str) :
            try :
                return getattr(self,x)
            except AttributeError :
                pass
        y = self._encode(x) # can raise ValueError
        if not self._domain(y) :
            raise ValueError("Interval.cast() : symbol '{}', encoded as '{}' does not belong to the domain!".format(x,y))
        return y

    def contains(self, x ) :
        try :
            y = self._encode(x)
        except ValueError :
            return False
        return self._domain(y)

    def dump(self) :
        return dict( name = self.name,\
                    domain = [ self._lb, self._ub ] )

class Constant :

    def __init__(self, name, sort, lang ) :

        self._name = name
        self._sort = sort
        self._sort._domain[name] = self
        self._lang = lang

    @property
    def name(self) :
        return self._name


class FOL :

    def __init__(self) :
        self._sorts = {}
        # MRJ: let's represent this temporally as pairs of names of sorts,
        # lhs \sqsubseteq rhs
        self._sort_hierarchy = set()
        self._functions = {}
        self._predicates = {}
        self._variables = {}

        self._build_builtin_sorts()

    def _build_builtin_sorts(self) :
        self._build_the_reals()
        self._build_the_integers()
        self._build_the_naturals()

    def _build_the_reals(self) :
        the_reals = Interval( -3.40282e+38, 3.40282e+38, lambda x : float(x), 'Real', self )
        the_reals.built_in = True
        the_reals.pi = scipy.constants.pi
        self._sorts['Real'] = the_reals

    def _build_the_integers(self) :
        the_ints = Interval( -(2**31-1), 2**31-1, lambda x : int(x), 'Integer', self )
        the_ints.built_in = True
        self._sorts['Integer'] = the_ints

    def _build_the_naturals(self) :
        the_nats = Interval( 0, 2**32-1, lambda x : int(x), 'Natural', self )
        the_nats.built_in = True
        self._sorts['Natural'] = the_nats

    def sort( self, name, super = None ) :
        """
            Creates instance of Sort object, adds it to the table of
            sorts
        """
        if self._sorts.get(name, None) :
            # there is a sort already declared with the same names
            raise LanguageError("FOL.sort() : sort '{}' already declared".format(name))
        sort_obj = Sort(name, self)
        self._sorts[name] = sort_obj
        return sort_obj

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

    def dump(self) :
        return dict(\
                sorts = [s.dump() for _, s in self._sorts.items() ]\
                )


    def is_well_formed(self) :
        for _, s in self._sorts.items() :
            s.check_empty()
