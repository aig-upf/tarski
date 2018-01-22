import types
import scipy.constants

from typing import List, Set, Union


class Sort :

    def __init__(self, name, lang) :
        self._name = name
        self._language = lang
        self._domain = {}
        self._built_in = False

    def __str__(self) :
        return 'Sort({})'.format(self.name)

    def __repr__(self) :
        return self.name

    @property
    def name(self) :
        return self._name

    @property
    def language(self) :
        return self._language
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

def parents( s : Sort ) -> List[Sort] :
    """ Returns direct parent sorts in the sort hierarchy associated with
        the language
    """
    parents = []
    for lhs, rhs in s.language.sort_hierarchy :
        if lhs == s.name :
            parents.append( s.language.sort(rhs) )
    return parents

def children( s : Sort ) -> List[Sort] :
    """ Return direct child sorts in the sort hierarchy associated with
        the language
    """
    children = []
    for lhs, rhs in s.language.sort_hierarchy :
        if rhs == sort :
            children.append( s.language.sort(lhs))
    return children



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
