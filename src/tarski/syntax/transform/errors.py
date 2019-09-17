from ...errors import TarskiError


class SubstitutionError(TarskiError):
    def __init__(self, phi, subst, msg=None):
        msg = msg or 'unspecified error'
        super().__init__(f'Error applying substitution "{subst}" to formula "{phi}": {msg}')


class TransformationError(TarskiError):
    def __init__(self, name, phi, msg=None):
        msg = msg or 'unspecified error'
        super().__init__(f'Error applying transformation "{name}" to formula "{phi}": {msg}')
