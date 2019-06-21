from ...syntax import CompoundFormula, Atom, Connective
from . import errors as err


class Sensor:
    """ A (possibly lifted) sensing action """

    def __init__(self, language, name, parameters, condition, obs):
        self.name = name
        self.language = language
        self.parameters = parameters
        self.condition = condition
        self.obs = obs
        self._check_well_formed()

    def _check_well_formed(self):
        if isinstance(self.obs, Atom):
            return True
        if isinstance(self.obs, CompoundFormula):
            if self.obs.connective == Connective.Not:
                if isinstance(self.obs.subformulas[0], Atom):
                    return True
        # We do not support anything other than literals
        raise err.ObservationExpressivenessMismatch(self)

    def ident(self):
        params = ', '.join([str(o) for o in self.parameters])
        return '{}({})'.format(self.name, params)

    def dump(self):
        return dict(name=self.name,
                    params=[par.dump() for par in self.parameters],
                    condition=self.condition.dump(),
                    obs=[eff.dump() for eff in self.effects.dump()])

    def __str__(self):
        tokens = ['action {}:'.format(self.name),
                  'C=({})'.format(self.condition),
                  'L=({})'.format(str(self.obs))]
        return '\n'.join(tokens)
