
from ...syntax import BuiltinFunctionSymbol, CompoundTerm
from . import errors as err


class DifferentialConstraint:
    """ A (possibly lifted) reaction """

    def __init__(self, language, name, parameters, condition, variate, ode):
        self.name = name
        self.language = language
        self.parameters = parameters
        self.condition = condition
        self.variate = variate
        self.ode = ode
        self._check_well_formed()

    def _check_well_formed(self):
        if not isinstance(self.variate, CompoundTerm):
            raise err.InvalidDifferentialConstraintDefinition(self.variate, "Needs to be a compound term")
        if isinstance(self.variate, BuiltinFunctionSymbol):
            raise err.InvalidDifferentialConstraintDefinition(self.variate, "Cannot be a built-in function")
        # ....

    def ident(self):
        params = ', '.join([str(o) for o in self.parameters])
        return '{}({})'.format(self.name, params)

    def dump(self):
        return dict(name=self.name,
                    params=[par.dump() for par in self.parameters],
                    condition=self.condition.dump(),
                    variate=self.variate.dump(),
                    ode=self.ode.dump())

    def __str__(self):
        tokens = ['reaction {}:'.format(self.name),
                  'cond: ({})'.format(self.condition),
                  'variate: {}'.format(self.variate),
                  'ode: {}'.format(self.ode)]
        return '\n'.join(tokens)
