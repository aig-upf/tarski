from . import errors as err


class Derived:
    """ A derived predicate. """

    def __init__(self, language, name, parameters, formula):
        # MRJ: note this will raise an exception if the predicate
        # has not been defined
        self.predicate = language.get_predicate(name)
        self.language = language
        # Check arity and type
        if len(parameters) != self.predicate.arity:
            raise err.InvalidDerivedPredicateError(name, formula,
                                                   "Arity of predicate does not match length of parameter list")
        for k, param in enumerate(parameters):
            if self.predicate.sort[k] != param.sort:
                raise err.InvalidDerivedPredicateError(name, formula, "Type mismatch of parameter \
            #{}, should be: {} provided: {}".format(k, self.predicate.sort.name, param.sort.name))
        self.parameters = parameters
        self.formula = formula

    def __lt__(self, other):
        return self.name < other.name

    def dump(self):
        return dict(name=self.predicate.symbol,
                    params=[par.dump() for par in self.parameters],
                    formula=self.formula.dump())

    def ident(self):
        params = ', '.join([str(o) for o in self.parameters])
        return '{}({})'.format(self.predicate.symbol, params)

    def __str__(self):
        tokens = ['derived {} {}:'.format(self.predicate.symbol,
                                          ' '.join([str(o) for o in self.parameters])),
                  'formula=({})'.format(self.precondition)]
        return '\n'.join(tokens)
