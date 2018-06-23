from ...errors import TarskiError


class SubstitutionError(TarskiError):
    def __init__(self, phi, subst, msg=None):
        msg = msg or 'unspecified error'
        super().__init__('Error applying substitution "{}" to formula "{}": {}'.format(str(subst), str(phi), msg))


class TransformationError(TarskiError):
    def __init__(self, name, phi, msg=None):
        msg = msg or 'unspecified error'
        super().__init__('Error applying transformation "{}" to formula "{}": {}'.format(name, str(phi), msg))
