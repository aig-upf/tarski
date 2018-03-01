from ... errors import TarskiError

class SubstitutionError(TarskiError):
    def __init__(self, phi, subst, msg=None):
        msg = msg or 'unspecified error'
        super().__init__('Error applying substitution "{}" to formula "{}": {}'.format(str(subst),str(phi),msg))
