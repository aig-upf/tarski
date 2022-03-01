"""
    SAS+ Variables - lean implementation
"""
from tarski.syntax import Term, symref
from tarski.syntax.symrefs import TermReference
from tarski.sas.helper import make_domain
from typing import List, Union

class InvalidValue(Exception):
    pass


class Variable:

    def __init__(self, **kwargs):
        self._id = kwargs.get('id', 0)
        self._symbol = kwargs.get('symbol', None)
        self._domain = kwargs.get('domain', [])
        self.needs_closure = kwargs.get('needs_closure', False)
        self.derived = kwargs.get('derived', False)

        self._domain = make_domain(self._domain, self.needs_closure)

    @property
    def id(self) -> int:
        return self._id

    @property
    def symbol(self) -> Term:
        return self._symbol

    @property
    def domain(self) -> List[TermReference]:
        return self._domain

    def add_value(self, v: Term) -> None:
        """
        Adds a value to the variable domain
        :param v:
        :return:
        """
        if self.needs_closure:
            raise RuntimeError("Variable domain is requires closure under negation, needs to be rebuilt")
        self._domain += [symref(v)]

    def index(self, t: Union[TermReference, None]) -> int:
        """
        Returns index in domain, if t is None, then it is checked whether the
        domain required closure.
        :param t:
        :return:
        """
        if t is None:
            if not self.needs_closure:
                raise RuntimeError("Variable domain does not have a <none true> value")
            return -1
        return self._domain.index(t)