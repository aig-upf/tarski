# -*- coding: utf-8 -*-
from tarski import FOL, \
    Formula, \
    Variable, \
    LanguageError

import abc


class Action(abc.ABC):
    def __init__(self, lang, name, parameters, precondition, effects):
        self._name = name
        self.lang = lang
        self._params = parameters
        self._pre = precondition
        self._effs = effects

    @property
    def name(self) :
        return self._name

    @property
    def precondition(self) :
        return self._pre

    @property
    def effects(self) :
        return self._effs

    @property
    def parameters(self) :
        return self._params

    def dump(self) :
        return dict(name=self.name,\
            params=[par.dump() for par in self.parameters],\
            precondition=self.precondition.dump(),
            effects=[eff.dump() for eff in self.effects.dump() ])

def action( L : FOL, **kwargs ) :
    # let's pick up each argument from kwargs and
    # process it
    argnames = kwargs.keys()
    name = None
    parameters = None
    precondition = None
    effects = None

    for arg in argnames :
        if arg == 'name' :
            name = kwargs[arg]
        elif arg in ('parameters','params') :
            parameters = kwargs[arg]
        elif arg in ('precondition','pre') :
            precondition = kwargs[arg]
        elif arg in ('effects','eff') :
            effects = kwargs[arg]
        kwargs.pop(arg)

    if len(kwargs) > 0 :
        raise LanguageError('Unknown arguments were passed: {}'.format(','.join(kwargs.keys())))

    return Action(name, parameters, precondition, effects)
