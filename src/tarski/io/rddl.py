"""
    RDDL model acquisition module
"""
import tarski
from tarski.syntax import *
from tarski.errors import LanguageError
from tarski.theories import Theory
import pyrddl


class Reader(object):
    """
        Reader creates a FOL and several language components
        that specify a RDDL task
    """
    def __init__(self, filename):
        self.language = None
        self.rddl_model = self._load_rddl_model(filename)

    def _load_rddl_model(self, filename):
        with open(filename, 'r') as input_file:
            rddl = input_file.read()
        parser = pyrddl.Parser()
        parser.build()
        # parse RDDL
        return parser.parse(rddl)

    def _translate_types(self):
        for typename, parent_type in self.rddl_model.domain.types:
            assert parent_type == 'object'
            self.language.sort(typename, self.language.Object)
        for typename, dom in self.rddl_model.non_fluents.objects:
            for o in dom:
                self.language.constant(o, self.language.get(typename))

    def _translate_variables(self):
        non_fluent_terms = self.rddl_model.domain.non_fluents
        for name, term in non_fluent_terms.items():
            translate_variable(self.language, name, term)
        for name, term in self.rddl_model.domain.state_fluents.items():
            translate_variable(self.language, name, term)
        for name, term in self.rddl_model.domain.intermediate_fluents.items():
            translate_variable(self.language, name, term)
        for name, term in self.rddl_model.domain.action_fluents.items():
            translate_variable(self.language, name, term)

    def translate_rddl_model(self):
        # 0. create language
        self.language = tarski.language(self.rddl_model.domain.name,
            theories=[Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL])

        # 1. create types
        self._translate_types()

        # 2. create functions (or predicates) for all variable types
        self._translate_variables()

built_in_type_map = { 'object': 'Object', 'real': 'Real', 'integer': 'Integer'}

def translate_builtin_type(L: tarski.FirstOrderLanguage, name):
    return L.get(built_in_type_map[name])

def translate_variable(L : tarski.FirstOrderLanguage, name, term):
    name = name.split('/')[0] # forget about the arity of the symbol
    params = []
    if term.param_types is not None:
        params = term.param_types
    if term.range == 'bool':
        signature = tuple(params)
    else:
        signature = tuple(params + [term.range])
    # translate signature to sorts
    t_signature = []
    for s in signature:
        try:
            t_s = L.get(s)
        except LanguageError:
            t_s = translate_builtin_type(L, s)
        t_signature += [t_s]
    if term.range == 'bool':
        return L.predicate(name, *t_signature)
    return L.function(name, *t_signature)


class Writer(object):
    """
        Writer compiles the specification of a planning task
        into RDDL
    """
    def __init__(self, task):
        pass
