# -*- coding: utf-8 -*-
from collections import OrderedDict

from . import errors as err

# class Action(abc.ABC):
class Action(object):
    """ A (possibly lifted) planning action """
    def __init__(self, language, name, parameters, precondition, effects):
        self.name = name
        self.language = language
        self.parameters = parameters
        self.precondition = precondition
        self.effects = effects

    def dump(self):
        return dict(name=self.name,
                    params=[par.dump() for par in self.parameters],
                    precondition=self.precondition.dump(),
                    effects=[eff.dump() for eff in self.effects.dump()])


    def __str__(self):
        tokens = [ 'action {}:'.format(self.name),\
                    'pre=({})'.format(self.precondition),\
                    'eff=({})'.format(' & '.join( str(eff) for eff in self.effects))]
        return  '\n'.join(tokens)

class Problem(object):
    """ A Functional STRIPS problem """

    def __init__(self, name, language, **kwargs):
        """
        A FSTRIPS Problem description. Constructor parameters are:

         - name: the name of the problem
         - language: FOL associated with the planning problem
         - init: initial state of the problem (required)
         - goal: formula specifying the set of goal states
         - constraints: the set of constraints that valid plans need to comply with
         before reaching a goal state
        """
        self._name = name
        self.language = language
        try :
            self.init = kwargs['init']
            if self.init is None :
                raise err.IncompleteProblemError(self,msg="No initial state was given")    
        except KeyError:
            raise err.IncompleteProblemError(self,msg="No initial state was given")
        try :
            self.goal = kwargs['goal']
        except KeyError:
            raise err.IncompleteProblemError(self,msg="Goal was not specified")

        self.constraints = kwargs.get('constraints',None)
        actions = [ ( (a.name,tuple(a.parameters)) , a) for a in kwargs.get('actions',[])]
        self.actions = OrderedDict(actions) if actions is not None else OrderedDict()

        # TODO Add axioms, state constraints, etc.

    @property
    def name(self):
        return self._name

    def action(self, name, parameters, precondition, effects):
        if name in self.actions:
            # @TODO: MRJ: check action signature, rather than just the name
            raise err.DuplicateActionDefinition(name, self.actions[name])

        self.actions[(name,tuple(parameters))] = Action(self.language, name, parameters, precondition, effects)
        return self.actions[name]

    def has_action(self, name):
        return name in self.actions

    def get_action(self, name):
        if not self.has_action(name):
            raise err.UndefinedAction(name)
        return self.actions[name]
