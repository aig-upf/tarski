
from ..errors import TarskiError


class UnableToGroundError(TarskiError):
    def __init__(self, sym, msg=None):
        msg = msg or 'Reason unspecified'
        super().__init__('Unable to ground Term/Atom "{}": {}'.format(sym, msg))


class ReachabilityLPUnsolvable(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'The relaxed-reachabilty logic program is not solvable'
        super().__init__(msg)
