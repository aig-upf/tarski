# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez (miquel.ramirez@pm.me)
# ----------------------------------------------------------------------------------------------------------------------
# io/pddl/parser.py
#
# PDDL parser
# ----------------------------------------------------------------------------------------------------------------------

import logging

from ply import yacc  # type: ignore

from tarski.syntax import CompoundTerm, Term, land, lor, neg, QuantifiedFormula, Quantifier
from tarski.io.pddl import Features, supported_features
from tarski.io.pddl.lexer import PDDLlex
from tarski.io.pddl.instance import *
from tarski.io.pddl.errors import *


class PDDLparser:
    """
    The PDDL parser class
    """
    def __init__(self, lexer=None, verbose=False, debug=False):
        if lexer is None:
            self.lexer = PDDLlex()
            # Lexer debugging isn't particularly helpful, change
            # line below if this assessment ever changes
            self.lexer.build(debug=False)
        else:
            self.lexer = lexer

        self.logfile = None
        self.verbose = verbose
        self.tokens = self.lexer.tokens

        self.domain_name = None
        self.problem_name = None
        self.required_features = set()

        self.precedence = (
            ('left', 'rwIMPLY'),
            ('left', 'rwOR'),
            ('left', 'rwAND'),
            ('nonassoc', 'rwNOT'),
            ('nonassoc', 'LT', 'GT', 'LEQ', 'GEQ', 'EQUA', 'NEQUA'),
            ('left', 'MINUS', 'PLUS'),
            ('left', 'TIMES', 'DIV')
        )

        self.debug = debug
        self.instance = None
        self.var_dict = None
        self._parser = None

    def build(self, **kwargs):
        # self.logfile = os.path.join(tempfile.gettempdir(), 'pddl_parse.log')
        self.logfile = kwargs.get('logfile', 'pddl_parse.log')
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.FileHandler(self.logfile, mode='w'))
        self._parser = yacc.yacc(module=self, start='begin', debug=self.debug)
        self.instance = InstanceModel(debug=self.debug)
        self.var_dict = OrderedDict()

    def parse(self, input_data):
        return self._parser.parse(input=input_data, lexer=self.lexer, debug=self.log)

    def _print_verbose(self, p_name):
        if self.verbose:
            print('>> Parsed `{}` ...'.format(p_name))

    def p_begin(self, p):
        '''begin    : domain
                    | domain problem
                    | problem'''
        pass

    def p_domain(self, p):
        '''domain   : LPAREN rwDEFINE domain_name domain_require_def domain_body_def RPAREN'''
        print("Domain Parsed")
        pass

    # Rules like A : B C D
    # where B C and D are like: X : Y | empty
    # can't work because of parser disambiguation skipping possible productions
    # excellent explanation of the issue here: https://stackoverflow.com/a/61966032/338107
    def p_domain_body_def(self, p):
        '''domain_body_def  : types_def domain_body_def
                            | constants_def domain_body_def
                            | predicates_def domain_body_def
                            | functions_def domain_body_def
                            | domain_constraints_def domain_body_def
                            | structure_def_list'''
        pass

    def p_domain_name(self, p):
        '''domain_name : LPAREN rwDOMAIN  ID RPAREN'''
        self.domain_name = p[3]

    def p_problem(self, p):
        '''problem  : LPAREN rwDEFINE problem_name domain_ref problem_body_def RPAREN'''
        pass

    def p_problem_body_def(self, p):
        '''
        problem_body_def    :  problem_require_def problem_body_def
                            | object_declaration problem_body_def
                            | init problem_body_def
                            | goal problem_body_def
                            | problem_constraints_def problem_body_def
                            | metric_spec
                            | empty
        '''
        pass

    def p_problem_name(self, p):
        '''problem_name    : LPAREN rwPROBLEM ID RPAREN'''
        self.problem_name = p[3]

    def p_domain_ref(self, p):
        '''domain_ref  : LPAREN rwDOMAIN_REF ID RPAREN'''
        expected_domain = p[3]
        if expected_domain != self.domain_name:
            msg = "Domain and problem mismatch: expected domain name is '{}', provided domain is '{}'".format(expected_domain, self.domain_name)
            raise SemanticError(self.lexer.lineno(), msg)

    def p_domain_require_def(self, p):
        '''domain_require_def  :  LPAREN rwREQUIREMENTS requirement_key_list RPAREN'''
        self.check_requirements_support()

    def check_requirements_support(self):
        """
        Checks if requirements are supported
        :return:
        """
        unsupported = self.required_features - supported_features
        if len(unsupported) > 0:
            msg = "The following UNSUPPORTED features are required: {}".format(" ".join([f.name for f in unsupported]))
            raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_requirement_key_list(self, p):
        '''requirement_key_list : rwSTRIPS requirement_key_list
                                | rwTYPING requirement_key_list
                                | rwNEGATIVE_PRECONDITIONS requirement_key_list
                                | rwDISJUNCTIVE_PRECONDITIONS requirement_key_list
                                | rwEQUALITY requirement_key_list
                                | rwEXISTENTIAL_PRECONDITIONS requirement_key_list
                                | rwUNIVERSAL_PRECONDITIONS requirement_key_list
                                | rwQUANTIFIED_PRECONDITIONS requirement_key_list
                                | rwCONDITIONAL_EFFECTS requirement_key_list
                                | rwFLUENTS requirement_key_list
                                | rwNUMERIC_FLUENTS requirement_key_list
                                | rwADL requirement_key_list
                                | rwDURATIVE_ACTIONS requirement_key_list
                                | rwDURATION_INEQUALITIES requirement_key_list
                                | rwCONTINUOUS_EFFECTS requirement_key_list
                                | rwDERIVED_PREDICATES requirement_key_list
                                | rwTIMED_INITIAL_LITERALS requirement_key_list
                                | rwPREFERENCES requirement_key_list
                                | rwCONSTRAINTS requirement_key_list
                                | rwACTION_COSTS requirement_key_list
                                | empty'''
        # If token 1 is null, we have hit the end of the list
        if p[1] is None:
            return
        if p[1] == self.lexer.symbols.rwSTRIPS:
            self.required_features.add(Features.STRIPS)
        elif p[1] == self.lexer.symbols.rwTYPING:
            self.required_features.add(Features.TYPING)
        elif p[1] == self.lexer.symbols.rwNEGATIVE_PRECONDITIONS:
            self.required_features.add(Features.NEGATIVE_PRECONDITIONS)
        elif p[1] == self.lexer.symbols.rwDISJUNCTIVE_PRECONDITIONS:
            self.required_features.add(Features.DISJUNCTIVE_PRECONDITIONS)
        elif p[1] == self.lexer.symbols.rwEQUALITY:
            self.required_features.add(Features.EQUALITY)
        elif p[1] == self.lexer.symbols.rwEXISTENTIAL_PRECONDITIONS:
            self.required_features.add(Features.EXISTENTIAL_PRECONDITIONS)
        elif p[1] == self.lexer.symbols.rwUNIVERSAL_PRECONDITIONS:
            self.required_features.add(Features.UNIVERSAL_PRECONDITIONS)
        elif p[1] == self.lexer.symbols.rwQUANTIFIED_PRECONDITIONS:
            self.required_features.add(Features.UNIVERSAL_PRECONDITIONS)
            self.required_features.add(Features.EXISTENTIAL_PRECONDITIONS)
        elif p[1] == self.lexer.symbols.rwCONDITIONAL_EFFECTS:
            self.required_features.add(Features.CONDITIONAL_EFFECTS)
        elif p[1] == self.lexer.symbols.rwOBJECT_FLUENTS:
            self.required_features.add(Features.OBJECT_FLUENTS)
        elif p[1] == self.lexer.symbols.rwNUMERIC_FLUENTS:
            self.required_features.add(Features.NUMERIC_FLUENTS)
        elif p[1] == self.lexer.symbols.rwFLUENTS:
            self.required_features.add(Features.OBJECT_FLUENTS)
            self.required_features.add(Features.NUMERIC_FLUENTS)
        elif p[1] == self.lexer.symbols.rwADL:
            self.required_features.add(Features.STRIPS)
            self.required_features.add(Features.TYPING)
            self.required_features.add(Features.NEGATIVE_PRECONDITIONS)
            self.required_features.add(Features.DISJUNCTIVE_PRECONDITIONS)
            self.required_features.add(Features.EQUALITY)
            self.required_features.add(Features.UNIVERSAL_PRECONDITIONS)
            self.required_features.add(Features.EXISTENTIAL_PRECONDITIONS)
            self.required_features.add(Features.CONDITIONAL_EFFECTS)
        elif p[1] == self.lexer.symbols.rwDURATIVE_ACTIONS:
            self.required_features.add(Features.DURATIVE_ACTIONS)
        elif p[1] == self.lexer.symbols.rwDERIVED_PREDICATES:
            self.required_features.add(Features.DERIVED_PREDICATES)
        elif p[1] == self.lexer.symbols.rwTIMED_INITAL_LITERALS:
            self.required_features.add(Features.TIMED_INITIAL_LITERALS)
        elif p[1] == self.lexer.symbols.rwPREFERENCES:
            self.required_features.add(Features.PREFERENCES)
        elif p[1] == self.lexer.symbols.rwCONSTRAINTS:
            self.required_features.add(Features.CONSTRAINTS)
        elif p[1] == self.lexer.symbols.rwACTION_COSTS:
            self.required_features.add(Features.ACTION_COSTS)
        elif p[1] == self.lexer.symbols.rwCONTINUOUS_EFFECTS:
            self.required_features.add(Features.CONTINUOUS_EFFECTS)
        elif p[1] == self.lexer.symbols.rwTIMED_INITAL_LITERALS:
            self.required_features.add(Features.DURATIVE_ACTIONS)
            self.required_features.add(Features.TIMED_INITIAL_LITERALS)
        elif p[1] == self.lexer.symbols.rwDURATION_INEQUALITIES:
            self.required_features.add(Features.DURATIVE_ACTIONS)
            self.required_features.add(Features.DURATION_INEQUALITIES)
        else:
            raise RuntimeError("Handling of requirements should be exhaustive!")

    def p_types_def(self, p):
        '''types_def    : LPAREN rwTYPES typed_list_of_names RPAREN'''
        if p[1] is None:
            return
        if self.debug:
            print("Defined types:", p[3])
        for type_entry in p[3]:
            if isinstance(type_entry, tuple):
                supertype, subtypes = type_entry
                self.instance.process_supertype_definition(supertype, subtypes, self.lexer.lineno())
            else:
                self.instance.process_type_definition(type_entry)

    def p_typed_list_of_names(self, p):
        '''typed_list_of_names  : ID list_of_names typed_list_of_names
                                | ID list_of_names MINUS type typed_list_of_names
                                | type typed_list_of_names
                                | empty'''
        if p[1] is None:
            p[0] = []
            return
        if len(p) == 4:
            # 1st production rule
            new_name = p[1]
            p[0] = [new_name] + p[2]
            return
        if len(p) == 6:
            sub_types = [p[1]] + p[2]
            super_type = p[4]
            p[0] = [(super_type, sub_types)] + p[5]
            return
        p[0] = [p[1]] + p[2]

    def p_list_of_names(self, p):
        '''list_of_names    : ID list_of_names
                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_type(self, p):
        '''type : LPAREN rwEITHER primitive_type_list RPAREN
                | primitive_type'''
        if len(p) > 2:
            assert p[2] == self.lexer.symbols.rwEITHER
            msg = "Unsupported PDDL feature: (either <list of type names>)"
            raise SemanticError(self.lexer.lineno(), msg)
        p[0] = p[1]

    def p_primitive_type_list(self, p):
        '''primitive_type_list  : primitive_type primitive_type_list
                                | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_primitive_type(self, p):
        '''primitive_type   : rwOBJECT
                            | rwNUMBER
                            | ID'''
        if p[1] == self.lexer.symbols.rwOBJECT:
            p[0] = 'Object'
            return
        if p[1] == self.lexer.symbols.rwNUMBER:
            p[0] = 'Real'
            return
        p[0] = p[1]

    def p_constants_def(self, p):
        '''constants_def    :  LPAREN rwCONSTANTS typed_list_of_names RPAREN'''
        if p[1] is None:
            if self.debug:
                print("No constants defined")
            return
        def_list = p[3]
        total_constants = 0
        for entry in def_list:
            if isinstance(entry, tuple):
                typename, constant_list = entry
                if typename not in self.instance.types:
                    msg = "Error parsing (:constants ) section: type '{}' was not defined".format(typename)
                    raise SemanticError(self.lexer.lineno(), msg)

                self.instance.process_constant_definition(entry)

                total_constants += len(constant_list)
            else:
                msg = "Error processing (:constants ) section: constant '{}' has no type attached".format(entry)
                raise SemanticError(self.lexer.lineno(), msg)
        if self.debug:
            print("Total constants defined:", total_constants)


    def p_predicates_def(self, p):
        '''predicates_def   : LPAREN rwPREDICATES list_of_atomic_formula_skeleton RPAREN
                            | LPAREN rwPREDICATES RPAREN'''
        if p[1] is None:
            return
        if len(p) == 4:
            return
        def_pred_list = p[3]
        if self.debug:
            print("Number of predicates defined:", len(def_pred_list))
        for _, name, args in def_pred_list:
            self.instance.process_predicate_definition((name, args))
        if self.debug:
            for k, f in self.instance.predicates.items():
                print("\t", f)


    def p_list_of_atomic_formula_skeleton(self, p):
        '''list_of_atomic_formula_skeleton  : atomic_formula_skeleton list_of_atomic_formula_skeleton
                                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def normalize_typed_variable_list(self, unnorm_args):
        """
        Normalizes a list of typed variables
        """
        unnorm_args += [('type', 'object')]
        args = []
        last_index = -1
        for i, token in enumerate(unnorm_args):
            token_type, token_value = token
            if token_type == 'type':
                var_type = token_value
                if var_type not in self.instance.types:
                    msg = "Error parsing list of typed variables: type '{}' is not defined".format(var_type)
                    raise SemanticError(self.lexer.lineno(), msg)
                for t2 in unnorm_args[last_index+1:i]:
                    var_term, var_sort = self.instance.get_variable(t2[1], var_type)
                    args += [{'var': t2[1], 'term': var_term, 'type': var_sort}]
                last_index = i
        return args

    def p_atomic_formula_skeleton(self, p):
        '''atomic_formula_skeleton  : LPAREN predicate list_of_typed_variables RPAREN'''
        # MRJ: rule #2 is for untyped PDDL, where object is the assumed type

        if self.debug:
            print("Defined predicate:", p[2])
        # Normalize arguments
        p[0] = ('atomic_formula_skeleton', p[2], self.normalize_typed_variable_list(p[3]))

    def p_atomic_formula_skeleton_vars(self, p):
        '''atomic_formula_skeleton_vars  : LPAREN predicate list_of_typed_variables RPAREN'''
        # Normalize arguments
        var_list =  self.normalize_typed_variable_list(p[3])
        p[0] = ('atomic_formula_skeleton', p[2], var_list)
        if self.debug:
            print("Defined predicate:", p[2])
            print("\t and variables:")
            for entry in var_list:
                print("var: {} term: {}".format(entry['var'], entry['term']))
                print("var: {} term: {}".format(entry['var'], entry['term']))
        # declare variables
        for entry in var_list:
            self.var_dict[entry['var']] = entry['term']

    def p_predicate(self, p):
        '''predicate    :   ID
                        | rwAT'''
        p[0] = p[1]

    def p_list_of_typed_variables(self, p):
        '''
        list_of_typed_variables : VAR list_of_typed_variables
                                | VAR MINUS type list_of_typed_variables
                                | empty'''
        if p[1] is None:
            p[0] = []
            return
        if len(p) == 3:
            p[0] = [('var', p[1])] + p[2]
            return
        p[0] = [('var', p[1]), ('type', p[3])] + p[4]

    def p_quantifier_scope(self, p):
        '''
        quantifier_scope : LPAREN VAR quantifier_scope
                        | LPAREN VAR MINUS type quantifier_scope
                        | VAR MINUS type quantifier_scope
                        | VAR quantifier_scope
                        | RPAREN'''
        # production: quantifier_scope -> RPAREN
        if p[1] == ')':
            p[0] = []
            return

        if p[1] == '(':
            # all variables captured
            if len(p) == 4:
                var_token_list = [('var', p[2])] + p[3]
            else:
                var_token_list = [('var', p[2]), ('type', p[4])] + p[5]

            var_list = self.normalize_typed_variable_list(var_token_list)
            # register all variables into scope
            for entry in var_list:
                self.var_dict[entry['var']] = entry['term']
            p[0] = var_list
            return

        # production: quantifier_scope -> VAR quantifier_scope
        if len(p) == 3:
            p[0] = [('var', p[1])] + p[2]
            return

        # production: quantifier_scope -> VAR MINUS type quantifier_scope
        p[0] = [('var', p[1]), ('type', p[3])] + p[4]


    def p_functions_def(self, p):
        '''
        functions_def   : LPAREN rwFUNCTIONS function_typed_list RPAREN
                        | LPAREN rwFUNCTIONS RPAREN'''
        if len(p) == 4:
            return
        func_spec_list = p[3]
        if self.debug:
            print("Number of functions defined:", len(func_spec_list))
        for func_spec in func_spec_list:
            self.instance.process_function_skeleton(func_spec)
        if self.debug:
            for name, func_obj in self.instance.functions.items():
                print("\t", func_obj)

    def p_function_typed_list(self, p):
        '''
        function_typed_list : atomic_function_skeleton MINUS type function_typed_list
                            | atomic_function_skeleton function_typed_list
                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        if len(p) == 3:
            p[0] = [p[1]] + p[2]
            return
        func_data = p[1]
        func_data['codomain'] = p[3]
        p[0] = [func_data] + p[4]

    # def p_list_of_atomic_function_skeleton(self, p):
    #     '''
    #     list_of_atomic_function_skeleton    :  list_of_atomic_function_skeleton
    #                                         | atomic_function_skeleton
    #                                         | empty'''
    #     pass

    def p_atomic_function_skeleton(self, p):
        '''
        atomic_function_skeleton    : LPAREN function list_of_typed_variables RPAREN'''
        p[0] = {
            'type': 'atomic_function_skeleton',
            'name': p[2],
            'domain': self.normalize_typed_variable_list(p[3])
        }

    def p_function(self, p):
        '''
        function    : ID
                    | rwAT'''
        p[0] = p[1]

    def p_domain_constraints_def(self, p):
        '''domain_constraints_def   : LPAREN rwCONSTRAINTS con_GD RPAREN'''
        pass

    def p_con_GD(self, p):
        '''
        con_GD  : LPAREN rwAND con_GD_list RPAREN
                | LPAREN rwFORALL LPAREN list_of_typed_variables RPAREN con_GD RPAREN
                | LPAREN rwAT rwEND GD RPAREN
                | LPAREN rwALWAYS GD RPAREN
                | LPAREN rwSOMETIME GD RPAREN
                | LPAREN rwWITHIN GD RPAREN
                | LPAREN rwAT_MOST_ONCE GD RPAREN
                | LPAREN rwSOMETIME_AFTER GD GD RPAREN
                | LPAREN rwSOMETIME_BEFORE GD GD RPAREN
                | LPAREN rwALWAYS_WITHIN NAT GD GD RPAREN
                | LPAREN rwHOLD_DURING NAT NAT GD RPAREN
                | LPAREN rwHOLD_AFTER NAT GD RPAREN'''
        pass

    def p_con_GD_list(self, p):
        '''
        con_GD_list : con_GD con_GD_list
                    | empty'''
        pass

    def p_structure_def_list(self, p):
        '''
        structure_def_list  : structure_def structure_def_list
                            | empty'''
        pass

    def p_structure_def(self, p):
        '''
        structure_def   : action_def
                        | durative_action_def
                        | derived_def'''
        pass

    def p_action_def(self, p):
        '''
        action_def  : LPAREN rwACTION action_symbol action_parameters action_def_body RPAREN'''
        name = p[3]
        parameters = p[4]
        action_body = p[5]
        if 'duration' in action_body and action_body['duration'] is None:
            msg = "Error processing durative action: durative actions with unbounded duration are not supported"
            raise SemanticError(self.lexer.lineno(), msg)
        self.instance.process_action_skeleton(name, parameters, action_body)
        # clear up scope
        for entry in parameters:
            del self.var_dict[entry['var']]

    def p_action_parameters(self, p):
        '''
        action_parameters   : rwPARAMETERS LPAREN list_of_typed_variables RPAREN
        '''
        var_list = self.normalize_typed_variable_list(p[3])
        for entry in var_list:
            self.var_dict[entry['var']] = entry['term']
        p[0] = var_list

    def p_action_symbol(self, p):
        '''
        action_symbol   : ID'''
        p[0] = p[1]

    def p_action_def_body(self, p):
        '''
        action_def_body : rwPRECONDITION empty_or_pre_GD rwEFFECT empty_or_effect
                        | rwEFFECT empty_or_effect'''
        if len(p) == 5:
            p[0] = {
                'precondition': p[2],
                'effect': p[4]
            }
            return
        p[0] = {
            'precondition': None,
            'effect': p[2]
        }

    def p_empty_or_pre_GD(self, p):
        '''
        empty_or_pre_GD : pre_GD
                        | LPAREN RPAREN'''
        if len(p) == 3:
            p[0] = None
            return
        p[0] = p[1]

    def p_empty_or_effect(self, p):
        '''
        empty_or_effect : effect
                        | LPAREN RPAREN'''
        if len(p) == 3:
            p[0] = None
            return
        p[0] = p[1]

    # MRJ: preferences grammar is not compatible with LALR parsers...
    # def p_list_of_pre_GD(self, p):
    #     '''
    #     list_of_pre_GD  : pre_GD list_of_pre_GD
    #                     | empty'''
    #     pass

    # def p_pre_GD(self, p):
    #     '''
    #     pre_GD  : pref_GD
    #             | LPAREN rwAND list_of_pre_GD RPAREN
    #             | LPAREN rwFORALL LPAREN list_of_typed_variables RPAREN pre_GD RPAREN'''
    #     pass

    # def p_pref_GD(self, p):
    #     '''
    #     pref_GD : LPAREN rwPREFERENCE GD RPAREN
    #             | LPAREN rwPREFERENCE pref_name GD RPAREN
    #             | GD'''
    #     pass

    def p_pre_GD(self, p):
        '''pre_GD   : GD'''
        p[0] = p[1]

    def p_pref_name(self, p):
        '''pref_name   : ID'''
        p[0] = p[1]

    def p_list_of_GD(self, p):
        '''
        list_of_GD  : GD list_of_GD
                    | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_GD(self, p):
        '''
        GD  : literal_of_term
            | LPAREN rwAND list_of_GD RPAREN
            | LPAREN rwOR list_of_GD RPAREN
            | LPAREN rwNOT GD RPAREN
            | LPAREN rwIMPLY GD GD RPAREN
            | LPAREN rwEXISTS quantifier_scope GD RPAREN
            | LPAREN rwFORALL quantifier_scope GD RPAREN
            | f_comp'''
        if len(p) == 2:
            # processes literal of atom or arithmetic atom
            p[0] = p[1]
            return
        if p[2] == self.lexer.symbols.rwAND:
            p[0] = land(*p[3])
        elif p[2] == self.lexer.symbols.rwOR:
            p[0] = lor(*p[3])
        elif p[2] == self.lexer.symbols.rwNOT:
            p[0] = neg(p[3])
        elif p[2] == self.lexer.symbols.rwIMPLY:
            p[0] = lor(neg(p[3]), p[4])
        elif p[2] == self.lexer.symbols.rwEXISTS:
            if self.debug:
                print('existential quantifier, scope tokens: {} formula: {}'.format(p[3], p[4]))
            vars = p[3]
            phi = p[4]
            p[0] = QuantifiedFormula(Quantifier.Exists, [entry['term'] for entry in vars], phi)
            # clear vars from scope
            for entry in vars:
                del self.var_dict[entry['var']]
        elif p[2] == self.lexer.symbols.rwFORALL:
            vars = p[3]
            phi = p[4]
            p[0] = QuantifiedFormula(Quantifier.Forall,  [entry['term'] for entry in vars], phi)
            # clear vars from scope
            for entry in vars:
                del self.var_dict[entry['var']]
        else:
            assert False


    def p_literal_of_term(self, p):
        '''
        literal_of_term : atomic_formula_of_term
                        | LPAREN rwNOT atomic_formula_of_term RPAREN'''
        if len(p) == 2:
            if p[1]['boolean']:
                p[0] = p[1]['lhs'] == 1
            else:
                p[0] = p[1]['lhs'] == p[1]['rhs']
        else:
            if p[3]['boolean']:
                p[0] = p[3]['lhs'] == 0
            else:
                p[0] = neg(p[3]['lhs'] == p[3]['rhs'])

    def p_atomic_formula_of_term(self, p):
        '''
        atomic_formula_of_term  : LPAREN predicate list_of_term RPAREN
                                | LPAREN EQUA term term RPAREN'''
        if len(p) == 5:
            lhs_func = self.instance.get(p[2])
            sub_terms = p[3]
            lhs = lhs_func(*sub_terms)
            p[0] = {
                'boolean': True,
                'lhs': lhs,
                'rhs': 1
            }
        else:
            p[0] = {
                'boolean': False,
                'lhs': p[3],
                'rhs': p[4]
            }


    def p_list_of_term(self, p):
        '''
        list_of_term    : term list_of_term
                        | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_term(self, p):
        '''
        term    : ID
                | VAR
                | LPAREN function list_of_term RPAREN'''

        if len(p) > 2:
            try:
                func_name = self.instance.get(p[2])
            except tsk.LanguageError as e:
                msg = "Error parsing term in formula, function '{}' is not declared".format(p[2])
                raise SemanticError(self.lexer.lineno(), msg)
            sub_terms = p[3]
            p[0] = func_name(*sub_terms)
            return
        if self.lexer.is_identifier(p[1]):
            try:
                constant_ref = self.instance.get(p[1])
                p[0] = constant_ref
            except tsk.LanguageError as e:
                msg = "Error parsing term in formula, constant '{}' is not declared".format(p[1])
                raise SemanticError(self.lexer.lineno(), msg)
        elif self.lexer.is_variable(p[1]):
            try:
                var_ref = self.var_dict[p[1]]
                p[0] = var_ref
            except KeyError as e:
                msg = "Error parsing term in formula, variable '{}' is not declared in the current scope".format(p[1])
                raise SemanticError(self.lexer.lineno(), msg)

    def p_function_term(self, p):
        '''function_term   : LPAREN function list_of_term RPAREN'''
        try:
            func_name = self.instance.get(p[2])
            sub_terms = p[3]
            p[0] = func_name(*sub_terms)
        except tsk.LanguageError as e:
            msg = "Error parsing function term, function '{}' is not declared".format(p[2])
            raise SemanticError(self.lexer.lineno(), msg)

    def p_list_of_expression(self, p):
        '''
        list_of_expression  : f_exp list_of_expression
                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_f_exp(self, p):
        '''
        f_exp   : NAT
                | REAL
                | VAR
                | LPAREN binary_op f_exp f_exp RPAREN
                | LPAREN multi_op f_exp f_exp list_of_expression RPAREN
                | LPAREN MINUS f_exp RPAREN
                | f_head'''
        if len(p) == 2:
            if isinstance(p[1], int):
                p[0] = self.instance.int_const(p[1])
                return
            elif isinstance(p[1], float):
                p[0] = self.instance.real_const(p[1])
                return
            elif isinstance(p[1], CompoundTerm):
                p[0] = p[1]
                return
            elif self.lexer.is_variable(p[1]):
                # check if variable in scope
                try:
                    var_ref = self.var_dict[p[1]]
                    p[0] = var_ref
                    return
                except KeyError as e:
                    msg = "Error parsing expression, variable '{}' is not declared in the current scope".format(
                        p[1])
                    raise SemanticError(self.lexer.lineno(), msg)
            elif self.lexer.is_identifier(p[1]):
                # check if it is a constant
                try:
                    constant_ref = self.instance.get(p[1])
                    p[0] = constant_ref
                    return
                except tsk.LanguageError as e:
                    msg = "Error parsing expression, constant '{}' is not declared".format(p[1])
                    raise SemanticError(self.lexer.lineno(), msg)
            else:
                # raise error
                msg = "Error parsing expression: '{}' is not a constant or variable symbol"
                raise SemanticError(self.lexer.lineno(), msg)
            p[0] = p[1]
            return
        if len(p) == 5:
            p[0] = -p[3]
            return
        if len(p) == 6:
            if p[2] == '-':
                p[0] = p[3] - p[4]
            elif p[2] == '/':
                p[0] = p[3] / p[4]
            return
        expr_list = [p[3], p[4]] + p[5]
        sym_expr = expr_list[0]
        for i in range(1, len(expr_list)):
            if p[2] == '+':
                sym_expr = sym_expr + expr_list[i]
            elif p[2] == '*':
                sym_expr = sym_expr * expr_list[i]
        p[0] = sym_expr


    def p_f_head(self, p):
        '''
        f_head  : LPAREN function list_of_term RPAREN
                | ID'''
        if len(p) == 2:
            try:
                func_name = self.instance.get(p[1])
                p[0] = func_name()
            except tsk.LanguageError as e:
                msg = "Error parsing expression, function '{}' is not declared".format(p[1])
                raise SemanticError(self.lexer.lineno(), msg)
            return

        try:
            func_name = self.instance.get(p[2])
            sub_terms = p[3]
            p[0] = func_name(*sub_terms)
        except tsk.LanguageError as e:
            msg = "Error parsing expression, function '{}' is not declared".format(p[1])
            raise SemanticError(self.lexer.lineno(), msg)

    def p_binary_op(self, p):
        '''
        binary_op   : multi_op
                    | MINUS
                    | DIV'''
        p[0] = p[1]

    def p_multi_op(self, p):
        '''
        multi_op    : PLUS
                    | TIMES'''
        p[0] = p[1]

    def p_f_comp(self, p):
        '''f_comp  : LPAREN binary_comp f_exp f_exp RPAREN'''
        if p[2] == '<':
            p[0] = p[3] < p[4]
        elif p[2] == '<=':
            p[0] = p[3] <= p[4]
        elif p[2] == '>':
            p[0] = p[3] > p[4]
        elif p[2] == '>=':
            p[0] = p[3] >= p[4]
        elif p[2] == '=':
            #print('equality: =({}/{}, {}/{})'.format(p[3], type(p[3]), p[4], type(p[4])))
            p[0] = p[3] == p[4]
        else:
            assert False

    def p_binary_comp(self, p):
        '''
        binary_comp :  GT
                    | LT
                    | EQUA
                    | GEQ
                    | LEQ'''
        p[0] = p[1]

    def p_effect(self, p):
        '''
        effect  : LPAREN rwAND list_of_c_effect RPAREN
                | c_effect
        '''
        if len(p) == 2:
            p[0] = [p[1]]
            return
        p[0] = p[3]

    def p_list_of_c_effect(self, p):
        '''
        list_of_c_effect    : c_effect list_of_c_effect
                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_c_effect(self, p):
        '''
        c_effect    : LPAREN rwFORALL LPAREN list_of_typed_variables RPAREN effect RPAREN
                    | LPAREN rwWHEN GD cond_effect RPAREN
                    | p_effect'''
        if len(p) == 2:
            p[0] = p[1]
            return
        if p[2] == self.lexer.symbols.rwFORALL:
            msg = "Error parsing effect: universally quantified effects are not supported at the moment"
            raise UnsupportedFeature(self.lexer.lineno(), msg)
        if p[2] == self.lexer.symbols.rwWHEN:
            msg = "Error parsing effect: conditional effects are not supported at the moment"
            raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_p_effect(self, p):
        '''
        p_effect    : LPAREN rwNOT atomic_formula_of_term RPAREN
                    | atomic_formula_of_term
                    | LPAREN assign_op f_head f_exp RPAREN
                    | LPAREN rwASSIGN function_term term RPAREN
                    | LPAREN rwASSIGN function_term rwUNDEFINED RPAREN'''
        if len(p) == 2:
            atomic_formula = p[1]
            p[0] = AssignmentEffectData(lhs=atomic_formula['lhs'], rhs=atomic_formula['rhs'])
            return
        if p[2] == self.lexer.symbols.rwNOT:
            atomic_formula = p[3]
            if atomic_formula['boolean'] == False:
                msg = "Error parsing action effect: negated literals over non-Boolean functions are not supported"
                raise SemanticError(self.lexer.lineno(), msg)
            p[0] = AssignmentEffectData(lhs=atomic_formula['lhs'], rhs=0)
            return
        if p[2] == self.lexer.symbols.rwASSIGN:
            if isinstance(p[4], Term):
                p[0] = AssignmentEffectData(lhs=p[3], rhs=p[4])
                return
            if p[4] == self.lexer.symbols.rwUNDEFINED:
                msg = "Error parsing action effect: 'undefined' special constant is not supported at the moment"
                raise UnsupportedFeature(self.lexer.lineno(), msg)
            return
        if p[2] == self.lexer.symbols.rwSCALE_UP:
            lhs = p[3]
            rhs = p[4]
            p[0] = AssignmentEffectData(lhs=lhs, rhs=lhs * rhs)
            return
        elif p[2] == self.lexer.symbols.rwSCALE_DOWN:
            lhs = p[3]
            rhs = p[4]
            p[0] = AssignmentEffectData(lhs=lhs, rhs=lhs * rhs)
            return
        elif p[2] == self.lexer.symbols.rwINCREASE:
            lhs = p[3]
            rhs = p[4]
            p[0] = AssignmentEffectData(lhs=lhs, rhs=lhs + rhs)
            return
        elif p[2] == self.lexer.symbols.rwDECREASE:
            lhs = p[3]
            rhs = p[4]
            p[0] = AssignmentEffectData(lhs=lhs, rhs=lhs - rhs)
            return
        msg = "Error parsing action effect: special assignment operator {} is not supported at the moment".format(p[2])
        raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_cond_effect(self, p):
        '''
        cond_effect : LPAREN rwAND list_of_p_effect RPAREN
                    | p_effect'''
        if len(p) == 2:
            p[0] = [p[1]]
            return
        p[0] = p[3]

    def p_list_of_p_effect(self, p):
        '''
        list_of_p_effect    : p_effect list_of_p_effect
                            | empty'''
        if p[1] is None:
            p[0] = []
        p[0] = [p[1]] + p[2]

    def p_assign_op(self, p):
        '''
        assign_op   : rwASSIGN
                    | rwSCALE_UP
                    | rwSCALE_DOWN
                    | rwINCREASE
                    | rwDECREASE'''
        p[0] = p[1]

    def p_durative_action_def(self, p):
        '''durative_action_def  : LPAREN rwDURATIVE_ACTION da_symbol action_parameters da_def_body RPAREN'''
        name = p[3]
        parameters = p[4]
        body_data = p[5]
        self.instance.process_action_skeleton(name, parameters, body_data)
        # clear up scope
        for entry in parameters:
            del self.var_dict[entry['var']]

    def p_da_symbol(self, p):
        '''da_symbol   : ID'''
        p[0] = p[1]

    def p_da_def_body(self, p):
        '''da_def_body : rwDURATION duration_constraint rwCONDITION empty_or_da_GD rwEFFECT empty_or_da_effect'''
        p[0] = {
            'duration': p[2],
            'precondition': p[4],
            'effect': p[6]
        }

    def p_empty_or_da_GD(self, p):
        '''
        empty_or_da_GD  : da_GD
                        | LPAREN RPAREN'''
        if len(p) == 3:
            p[0] = None
            return
        if not isinstance(p[1], list):
            # MRJ: we do this in order to capture singleton conditions
            p[0] = [p[1]]
        else:
            p[0] = p[1]

    def p_empty_or_da_effect(self, p):
        '''
        empty_or_da_effect  : da_effect
                            | LPAREN RPAREN'''
        if len(p) == 3:
            p[0] = None
            return
        if not isinstance(p[1], list):
            # MRJ: we do this in order to capture singleton effects
            p[0] = [p[1]]
        else:
            p[0] = p[1]

    def p_list_of_da_GD(self, p):
        '''
        list_of_da_GD   : da_GD list_of_da_GD
                        | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_da_GD(self, p):
        '''
        da_GD   : pref_timed_GD
                | LPAREN rwAND list_of_da_GD RPAREN
                | LPAREN rwFORALL LPAREN list_of_typed_variables RPAREN da_GD RPAREN'''
        if len(p) == 2:
            p[0] = p[1]
            return
        if p[2] == self.lexer.symbols.rwAND:
            # MRJ: Note that we do not attempt to convert the preconditions of durative actions into a
            # conjunctive formula just yet
            p[0] = p[3]
            return
        msg = "Error parsing precondition of durative action: universally quantified preconditions are not supported at the moment"
        raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_pref_timed_GD(self, p):
        '''
        pref_timed_GD   : timed_GD
                        | LPAREN rwPREFERENCE timed_GD RPAREN
                        | LPAREN rwPREFERENCE pref_name timed_GD RPAREN'''
        if len(p) > 2:
            assert p[2] == self.lexer.symbols.rwPREFERENCES
            msg = "Error parsing precondition of durative action: preferences are not supported"
            raise UnsupportedFeature(self.lexer.lineno(), msg)
        p[0] = p[1]

    def p_timed_GD(self, p):
        '''
        timed_GD    : LPAREN rwAT time_specifier GD RPAREN
                    | LPAREN rwOVER interval GD RPAREN'''
        if p[2] == self.lexer.symbols.rwAT:
            p[0] = {
                'type': 'instant',
                'offset': p[3],
                'formula': p[4]
            }
            return
        p[0] = {
            'type': 'interval',
            'offset': None,
            'formula': p[4]
        }

    def p_time_specifier(self, p):
        '''
        time_specifier  : rwSTART
                        | rwEND'''
        p[0] = p[1]

    def p_interval(self, p):
        '''interval    : rwALL'''
        p[0] = p[1]

    def p_duration_constraint(self, p):
        '''
        duration_constraint : LPAREN rwAND list_of_simple_duration_constraint RPAREN
                            | LPAREN RPAREN
                            | simple_duration_constraint'''
        if len(p) == 2:
            p[0] = p[1]
            return
        if len(p) == 3:
            return
        msg = "Error parsing durative action: complex duration constraints are not supported"
        raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_list_of_simple_duration_constraint(self, p):
        '''
        list_of_simple_duration_constraint  : simple_duration_constraint list_of_simple_duration_constraint
                                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_simple_duration_constraint(self, p):
        '''
        simple_duration_constraint  : LPAREN d_op VAR d_value RPAREN
                                    | LPAREN rwAT time_specifier simple_duration_constraint RPAREN'''
        # Note that the VAR in the first rule needs to be ?duration
        if len(p) > 6:
            msg = "Error parsing duration of durative action: instant-specific duration constraints are not supported"
            raise UnsupportedFeature(self.lexer.lineno(), msg)
        if p[2] != '=':
            msg = "Error parsing duration of durative action: inequality expressions in duration constraints are not supported"
            raise UnsupportedFeature(self.lexer.lineno(), msg)
        variable = p[3]
        if variable != '?duration':
            msg = "Error parsing duration of durative action: found variable '{}' rather than '?duration'".format(variable)
            raise ParseError(self.lexer.lineno(), msg)
        p[0] = p[4]

    def p_d_op(self, p):
        '''
        d_op    : LEQ
                | GEQ
                | EQUA'''
        p[0] = p[1]

    def p_d_value(self, p):
        '''
        d_value : f_exp'''
        p[0] = p[1]

    def p_da_effect(self, p):
        '''
        da_effect   : LPAREN rwAND list_of_da_effect RPAREN
                    | timed_effect
                    | LPAREN rwFORALL LPAREN list_of_typed_variables RPAREN da_effect RPAREN
                    | LPAREN rwWHEN da_GD timed_effect RPAREN'''
        if len(p) == 2:
            p[0] = p[1]
            return
        if p[2] == self.lexer.symbols.rwAND:
            p[0] = p[3]
            return
        if p[2] == self.lexer.symbols.rwFORALL:
            msg = "Error parsing effect of durative action: universally quantified effects are not supported at the moment"
            raise UnsupportedFeature(self.lexer.lineno(), msg)
        if p[2] == self.lexer.symbols.rwWHEN:
            msg = "Error parsing effect of durative action: conditional effects are not supported at the moment"
            raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_list_of_da_effect(self, p):
        '''
        list_of_da_effect   : da_effect list_of_da_effect
                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_timed_effect(self, p):
        '''
        timed_effect    : LPAREN rwAT time_specifier cond_effect RPAREN
                        | LPAREN rwAT time_specifier f_assign_da RPAREN
                        | LPAREN assign_op_t f_head f_exp_t RPAREN'''
        if p[2] == self.lexer.symbols.rwAT:
            p[0] = {
                'type': 'timed_effect',
                'instant': p[3],
                'effect': p[4]
            }
            return
        msg = "Error parsing effects of durative actions: extended assignment operators are not supported"
        raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_f_assign_da(self, p):
        '''f_assign_da : LPAREN assign_op f_head f_exp_da RPAREN'''
        if p[2] != self.lexer.symbols.rwASSIGN:
            msg = "Error parsing effects of durative actions: assignment operators other than 'assign' are not supported at the moment"
            raise UnsupportedFeature(self.lexer.lineno(), msg)
        p[0] = AssignmentEffectData(lhs=p[3], rhs=p[4])

    def p_f_exp_da(self, p):
        '''
        f_exp_da    : LPAREN assign_op  f_head f_exp_da RPAREN
                    | LPAREN binary_op f_exp_da f_exp_da RPAREN
                    | LPAREN multi_op f_exp_da list_of_f_exp_da RPAREN
                    | LPAREN MINUS f_exp_da RPAREN
                    | VAR
                    | f_exp'''
        # NOTE: the VAR above must be ?duration
        msg = "Error parsing effects of durative actions: arithmetic expressions are not supported at the moment"
        raise SemanticError(self.lexer.lineno(), msg)

    def p_list_of_exp_da(self, p):
        '''
        list_of_f_exp_da    : f_exp_da list_of_f_exp_da
                            | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_assign_op_t(self, p):
        '''
        assign_op_t : rwINCREASE
                    | rwDECREASE'''
        p[0] = p[1]

    def p_f_exp_t(self, p):
        '''
        f_exp_t : LPAREN TIMES f_exp rwDT RPAREN
                | LPAREN TIMES rwDT f_exp RPAREN
                | rwDT'''
        msg = "Error parsing effect of action: continuous time effects are not supported at the moment"
        raise UnsupportedFeature(self.lexer.lineno(), msg)

    def p_derived_def(self, p):
        '''derived_def : LPAREN rwDERIVED atomic_formula_skeleton_vars GD RPAREN'''
        description, symbol, var_list = p[3]
        if self.debug:
            print("Derived predicate head:", symbol)
        # Check that the predicate is defined and there's no variable renaming
        try:
            head_pred = self.instance.predicates.get(symbol)
        except ValueError as e:
            msg = "Error parsing derived predicate, head symbol '{}' is not declared".format(symbol)
            raise SemanticError(self.lexer.lineno(), msg)
        for k, arg in enumerate(head_pred.domain):
            if self.debug:
                print('signature: {} provided: {}'.format(head_pred.domain[k], var_list[k]['type']))
            if not head_pred.domain[k] == var_list[k]['type']:
                msg = "Error parsing derived predicate, head predicate '{}' type mismatch, check definition in (:predicates ...)".format(symbol)
                raise SemanticError(self.lexer.lineno(), msg)
        dpred_body = p[4]
        if self.debug:
            print("Body: {} type: {}".format(dpred_body, type(dpred_body)))
        self.instance.process_derived_predicate_skeleton(head_pred, var_list, dpred_body)
        # clear up scope
        for entry in var_list:
            del self.var_dict[entry['var']]

    def p_problem_require_def(self, p):
        '''problem_require_def  : LPAREN rwREQUIREMENTS requirement_key_list RPAREN'''
        self.check_requirements_support()

    def p_object_declaration(self, p):
        '''object_declaration   : LPAREN rwOBJECTS typed_list_of_names RPAREN'''
        if p[1] is None:
            if self.debug:
                print("No objects defined")
            return
        def_list = p[3]

        for entry in def_list:
            if isinstance(entry, tuple):
                typename, constant_list = entry
                if typename not in self.instance.types:
                    msg = "Error parsing (:objects ) section: type '{}' was not defined".format(typename)
                    raise SemanticError(self.lexer.lineno(), msg)
                self.instance.process_constant_definition(entry)
            else:
                msg = "Error processing (:objects ) section: constant '{}' has no type attached".format(entry)
                raise SemanticError(self.lexer.lineno(), msg)
        if self.debug:
            total_constants = 0
            for typename, constant_list in self.instance.domains.items():
                total_constants += len(constant_list)
            print("Total constants defined:", total_constants)

    def p_init(self, p):
        '''init    : LPAREN rwINIT list_of_init_el RPAREN'''
        self.instance.init = p[3]

    def p_list_of_init_el(self, p):
        '''
        list_of_init_el : init_el list_of_init_el
                        | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_init_el(self, p):
        '''
        init_el : literal_of_name
                | LPAREN rwAT REAL literal_of_name RPAREN
                | LPAREN EQUA term REAL RPAREN
                | LPAREN EQUA term NAT RPAREN
                | LPAREN EQUA term ID RPAREN'''
        # Need to check that terms have no variables!
        if len(p) == 2:
            p[0] = (p[1]['lhs'], p[1]['rhs'])
            return
        if p[2] == self.lexer.symbols.rwAT:
            msg = "Error parsing initial state: temporal literals are not supported at the moment"
            raise UnsupportedFeature(self.lexer.lineno(), msg)
        if isinstance(p[4], float):
            p[0] = (p[3], p[4])
        elif isinstance(p[4], int):
            p[0] = (p[3], p[4])
        else:
            try:
                constant_term = self.instance.get(p[4])
                p[0] = (p[3], constant_term)
            except tsk.LanguageError as e:
                msg = "Error processing initial state: object '{}' was not defined".format(p[4])
                raise SemanticError(self.lexer.lineno(), msg)

    def p_literal_of_name(self, p):
        '''
        literal_of_name : atomic_formula_of_name
                        | LPAREN rwNOT atomic_formula_of_name RPAREN'''
        if len(p) == 2:
            p[0] = p[1]
            return
        else:
            if p[3]['boolean']:
                p[3]['rhs'] = 1 - p[3]['rhs']
            else:
                msg = "Error parsing literal of ground atom: Negation of atoms of non-boolean functions is not supported"
                raise SemanticError(self.lexer.lineno(), msg)

    def p_atomic_formula_of_name(self, p):
        '''
        atomic_formula_of_name  : LPAREN predicate list_of_term RPAREN
                                | LPAREN EQUA term term RPAREN'''
        if len(p) == 5:
            try:
                func_symbol = self.instance.get(p[2])
            except tsk.LanguageError as e:
                msg = "Error parsing ground atomic formula: function '{}' is not defined".format(p[2])
                raise SemanticError(self.lexer.lineno(), msg)
            sub_terms = p[3]
            p[0] = {
                'boolean': True,
                'lhs': func_symbol(*sub_terms),
                'rhs': 1
            }
            return
        p[0] = {
            'boolean': False,
            'lhs': p[3],
            'rhs': p[4]
        }

    def p_list_of_name(self, p):
        '''
        list_of_name    : ID list_of_name
                        | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_goal(self, p):
        '''goal    : LPAREN rwGOAL pre_GD RPAREN'''
        self.instance.goal = p[3]

    def p_problem_constraints_def(self, p):
        '''problem_constraints_def  : LPAREN rwCONSTRAINTS con_GD RPAREN'''
        pass

    def p_metric_spec(self, p):
        '''metric_spec  : LPAREN rwMETRIC optimization metric_f_exp RPAREN'''
        self.instance.process_objective_definition(dict(mode=p[3], definition=p[4]))

    def p_optimization(self, p):
        '''
        optimization    : rwMINIMIZE
                        | rwMAXIMIZE'''
        if p[1] == self.lexer.symbols.rwMINIMIZE:
            p[0] = ObjectiveMode.MINIMIZE
            return
        p[0] = ObjectiveMode.MAXIMIZE

    def p_metric_f_exp(self, p):
        '''
        metric_f_exp    : LPAREN binary_op metric_f_exp metric_f_exp RPAREN
                        | LPAREN multi_op metric_f_exp list_of_metric_f_exp RPAREN
                        | LPAREN MINUS metric_f_exp RPAREN
                        | REAL
                        | LPAREN ID list_of_name RPAREN
                        | ID
                        | LPAREN rwTOTAL_TIME RPAREN
                        | LPAREN rwTOTAL_COST RPAREN
                        | LPAREN rwIS_VIOLATED pref_name RPAREN'''
        if p[2] == self.lexer.symbols.rwTOTAL_TIME:
            p[0] = dict(type=ObjectiveType.TOTAL_TIME, expr=None)
            return
        if p[2] == self.lexer.symbols.rwTOTAL_COST:
            p[0] = dict(type=ObjectiveType.TOTAL_COST, expr=None)
            return
        print("Warning: implementation of `metric` section still work in progress, objective is ignored")
        p[0] = dict(type=ObjectiveType.UNSPECIFIED, expr=None)

    def p_list_of_metric_f_exp(self, p):
        '''
        list_of_metric_f_exp    : metric_f_exp list_of_metric_f_exp
                                | empty'''
        if p[1] is None:
            p[0] = []
            return
        p[0] = [p[1]] + p[2]

    def p_empty(self, p):
        '''empty    :'''
        pass

    def p_error(self, p):
        if not p:
            # reached End of File
            return
        if self.debug:
            print('Syntax error in input! See log file: {}'.format(self.logfile))

        print('Syntax error in input! Line: {} failed token: {} next: {}'.format(p.lineno, p, self._parser.token()))

        while True:
            tok = self._parser.token()
            if not tok or tok.type == 'LPAREN':
                break
        self._parser.errok()

        return tok
