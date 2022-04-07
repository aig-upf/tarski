# tarski
#
# Author: Miquel Ramirez (miquel.ramirez@pm.me)
# ----------------------------------------------------------------------------------------------------------------------
# io/pddl/lexer.py
#
# PDDL tokenizer
# ----------------------------------------------------------------------------------------------------------------------

import ply.lex as lex  # type: ignore
import re

# helper definitions
alpha = r'[A-Za-z]'
num = r'[0-9]'
alpnum = r'[0-9A-Za-z_\']'
identifier = r'(' + alpha + r')((' + alpha + r'|' + num + r'|\-|\_)*(' + alpha + r'|' + num + r'))?'
variable = r'\?' + identifier
directive = r':' + identifier
section = r':\(' + identifier
nat = num + r'+'
real = num + r'*\.' + num + r'+'
ws = ' \t'


class LexSymbols:

    def __init__(self):
        # PDDL Requirements

        self.rwSTRIPS = ':strips'
        self.rwTYPING = ':typing'
        self.rwNEGATIVE_PRECONDITIONS = ':negative-preconditions'
        self.rwDISJUNCTIVE_PRECONDITIONS = ':disjunctive-preconditions'
        self.rwEQUALITY = ':equality'
        self.rwEXISTENTIAL_PRECONDITIONS = ':existential-preconditions'
        self.rwUNIVERSAL_PRECONDITIONS = ':universal-preconditions'
        self.rwQUANTIFIED_PRECONDITIONS = ':quantified-preconditions'
        self.rwCONDITIONAL_EFFECTS = ':conditional-effects'
        self.rwOBJECT_FLUENTS = ':object-fluents'
        self.rwNUMERIC_FLUENTS = ':numeric-fluents'
        self.rwFLUENTS = ':fluents'
        self.rwADL = ':adl'
        self.rwDURATIVE_ACTIONS = ':durative-actions'
        self.rwDERIVED_PREDICATES = ':derived-predicates'
        self.rwTIMED_INITAL_LITERALS = ':timed-initial-literals'
        self.rwPREFERENCES = ':preferences'
        self.rwACTION_COSTS = ':action-costs'
        self.rwCONSTRAINTS = ':constraints'
        self.rwCONTINUOUS_EFFECTS = ':continuous-effects'
        self.rwDURATION_INEQUALITIES = ':duration-inequalities'
        self.rwTIMED_INITIAL_LITERALS = ':timed-initial-literals'

        # PDDL section tags

        self.rwREQUIREMENTS = ':requirements'
        self.rwINIT = ':init'
        self.rwGOAL = ':goal'
        self.rwACTION = ':action'
        self.rwDOMAIN_REF = ':domain'
        self.rwCONSTANTS = ':constants'
        self.rwPREDICATES = ':predicates'
        self.rwFUNCTIONS = ':functions'
        self.rwCONSTRAINTS = ':constraints'
        self.rwDERIVED = ':derived'
        self.rwOBJECTS = ':objects'
        self.rwMETRIC = ':metric'
        self.rwDURATIVE_ACTION = ':durative-action'
        self.rwTYPES = ':types'
        self.rwDERIVED = ':derived'


        # PDDL fields
        self.rwPRECONDITION = ':precondition'
        self.rwEFFECT = ':effect'
        self.rwPARAMETERS = ':parameters'
        self.rwCONDITION = ':condition'
        self.rwDURATION = ':duration'


        # PDDL keywords and operators
        self.rwAND = 'and'
        self.rwNOT = 'not'
        self.rwOR = 'or'
        self.rwIMPLY = 'imply'
        self.rwEXISTS = 'exists'
        self.rwFORALL = 'forall'
        self.rwWHEN = 'when'
        self.rwDOMAIN = 'domain'
        self.rwPROBLEM = 'problem'
        self.rwAT = 'at'
        self.rwOVER = 'over'
        self.rwSTART = 'start'
        self.rwEND = 'end'
        self.rwOVERALL = 'overall'
        self.rwASSIGN = 'assign'
        self.rwDEFINE = 'define'
        self.rwINCREASE = 'increase'
        self.rwDECREASE = 'decrease'
        self.rwSCALE_UP = 'scale-up'
        self.rwSCALE_DOWN = 'scale-down'
        self.rwINT = 'int'
        self.rwFLOAT = 'float'
        self.rwOBJECT = 'object'
        self.rwNUMBER = 'number'
        self.rwEITHER = 'either'
        self.rwALWAYS = 'always'
        self.rwSOMETIME = 'sometime'
        self.rwWITHIN = 'within'
        self.rwAT_MOST_ONCE = 'at-most-once'
        self.rwSOMETIME_AFTER = 'sometime-after'
        self.rwSOMETIME_BEFORE = 'sometime-before'
        self.rwALWAYS_WITHIN = 'always-within'
        self.rwHOLD_DURING = 'hold-during'
        self.rwHOLD_AFTER = 'hold-after'
        self.rwPREFERENCE = 'preference'
        self.rwUNDEFINED = 'undefined'
        self.rwMINIMIZE = 'minimize'
        self.rwMAXIMIZE = 'maximize'
        self.rwDT = '#t'
        self.rwTOTAL_TIME = 'total-time'
        self.rwTOTAL_COST = 'total-cost'
        self.rwIS_VIOLATED = 'is-violated'
        self.rwALL = 'all'


class PDDLlex:
    """
    Lexical analyser for PDDL
    """

    def __init__(self):
        self._lexer = None
        self.symbols = LexSymbols()

        self.reserved = {getattr(self.symbols, attr): attr for attr in self.symbols.__dict__.keys() if 'rw' in attr}

        self.tokens = [
            'LPAREN',
            'RPAREN',
            'LBRACE',
            'RBRACE',
            'LBRACKET',
            'RBRACKET',
            'DOUBLEDOT',
            'COMMA',
            'ASSIGN',
            'SEMICOLON',
            'ARROW',
            'EQUA',
            'NEQUA',
            'LT',
            'GT',
            'LEQ',
            'GEQ',
            'PLUS',
            'MINUS',
            'TIMES',
            'DIV',
            'ID',
            'VAR',
            'NAT',
            'REAL',
            'QUESTION',
            'UNKNOWN_DIRECTIVE',
            'UNKNOWN_SECTION'
        ]
        self.tokens += list(self.reserved.values())

        self.regexp = {
            'ID': re.compile(identifier),
            'VAR': re.compile(variable),
            'NAT': re.compile(nat),
            'REAL': re.compile(real)
        }

    t_ignore = ws

    t_QUESTION = r'\?'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    #t_LBRACE = r'\{'
    #t_RBRACE = r'\}'
    #t_LBRACKET = r'\['
    #t_RBRACKET = r'\]'
    t_DOUBLEDOT = r'\.\.'
    #t_COMMA = r','
    #t_ASSIGN = r':='
    #t_SEMICOLON = r';'
    t_EQUA = r'='
    #t_NEQUA = r'!='
    t_LT = r'<'
    t_GT = r'>'
    t_LEQ = r'<='
    t_GEQ = r'>='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIV = r'/'

    def t_newline(self, t):
        r'\n+'
        self._lexer.lineno += len(t.value)

    def t_ignore_COMMENT(self, t):
        r';.*'

    @lex.TOKEN(identifier)
    def t_ID(self, t):
        t.type = self.reserved.get(t.value, 'ID')
        t.value = t.value.lower()
        return t

    @lex.TOKEN(variable)
    def t_VAR(self, t):
        t.type = self.reserved.get(t.value, 'VAR')
        return t

    @lex.TOKEN(directive)
    def t_DIRECTIVE(self, t):
        t.type = self.reserved.get(t.value, 'UNKNOWN_DIRECTIVE')
        return t

    @lex.TOKEN(section)
    def t_SECTION(self, t):
        t.type = self.reserved.get(t.value, 'UNKNOWN_SECTION')

    @lex.TOKEN(real)
    def t_REAL(self, t):
        t.value = float(t.value)
        return t

    @lex.TOKEN(nat)
    def t_NAT(self, t):
        t.value = int(t.value)
        return t

    def t_error(self, t):
        print("Illegal character: {} at line: {}".format(repr(t.value[0]), self._lexer.lineno))
        t.lexer.skip(1)

    def lineno(self):
        return self._lexer.lineno

    def build(self, **kwargs):
        self._lexer = lex.lex(object=self, **kwargs)

    def token(self):
        return self._lexer.token()

    def input(self, data):
        if self._lexer is None:
            self.build()
        self._lexer.input(data)

    def is_identifier(self, v):
        return self.regexp['ID'].match(v) is not None

    def is_variable(self, v: str):
        #print("is variable:", v, type(v))
        return self.regexp['VAR'].match(v) is not None

    def __call__(self):
        while True:
            tok = self.token()
            if not tok:
                break
            yield tok