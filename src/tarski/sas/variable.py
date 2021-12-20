"""
    SAS+ Variables - lean implementation
"""
from tarski.syntax import Term, symref
from tarski.sas.helper import make_domain


class Variable(object):

    def __init__(self, **kwargs):
        self._id = kwargs.get('id', 0)
        self._symbol = kwargs.get('symbol', None)
        self._domain = kwargs.get('domain', [])
        self.needs_closure = kwargs.get('needs_closure', False)
        self.derived = kwargs.get('derived', False)

        self._domain = make_domain(self._domain, self.needs_closure)

    @property
    def id(self):
        return self._id

    @property
    def symbol(self):
        return self._symbol

    @property
    def domain(self):
        return self._domain

    def add_value(self, v: Term):
        """
        Adds a value to the variable domain
        :param v:
        :return:
        """
        if self.needs_closure:
            raise RuntimeError("Variable domain is requires closure under negation, needs to be rebuilt")
        self._domain += [symref(v)]
