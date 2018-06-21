# -*- coding: utf-8 -*-
from ..errors import TarskiError


class UnableToGroundError(TarskiError):

    def __init__(self, sym, msg=None):
        msg = msg or 'Reason unspecified'
        super().__init__('Unable to ground Term/Atom "{}": {}'.format(str(sym), msg))
