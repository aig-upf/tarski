
class Reaction:
    """ A (possibly lifted) reaction """

    def __init__(self, language, name, parameters, condition, effect):
        self.name = name
        self.language = language
        self.parameters = parameters
        self.condition = condition
        self.effect = effect
        self._check_well_formed()

    def _check_well_formed(self):
        pass

    def ident(self):
        params = ', '.join([str(o) for o in self.parameters])
        return '{}({})'.format(self.name, params)

    def dump(self):
        return dict(name=self.name,
                    params=[par.dump() for par in self.parameters],
                    condition=self.condition.dump(),
                    effect=[eff.dump() for eff in self.effect.dump()])

    def __str__(self):
        tokens = ['reaction {}:'.format(self.name),
                  'cond: ({})'.format(self.condition),
                  'eff: ({})'.format(self.effect)]
        return '\n'.join(tokens)
