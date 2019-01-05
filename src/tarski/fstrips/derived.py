from . import errors as err

class Derived:
    """ A derived predicate. """

    def __init__(self, language, name, parameters, formula):
        self.name = name
        self.language = language
        self.parameters = parameters
        self.formula = formula

    def __lt__(self, other):
        return self.name < other.name

    def dump(self):
        return dict(name=self.name,
                    params = [par.dump() for par in self.parameters],
                    formula = self.formula.dump())

    def ident(self):
        params = ', '.join([str(o) for o in self.parameters])
        return '{}({})'.format(self.name, params)

    def __str__(self):
        tokens = ['derived {} {}:'.format(self.name,
                                          ' '.join([str(o) for o in self.parameters])),
                  'formula=({})'.format(self.precondition)]
        return '\n'.join(tokens)
