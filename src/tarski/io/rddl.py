"""
    RDDL model acquisition module
"""
import tarski
from tarski.syntax import *
import tarski.syntax.arithmetic as tm
import tarski.syntax.arithmetic.special as tmsp
import tarski.syntax.arithmetic.random as tmr
import tarski.syntax.temporal.ltl as tt

from tarski.errors import LanguageError
from tarski.theories import Theory
import pyrddl

logic_rddl_to_tarski = {
    '=>' : implies,
    '^' : land,
    '|' : lor,
    '~' : neg}

relational_rddl_to_tarski = {
    '==': BuiltinPredicateSymbol.EQ,
    '<=': BuiltinPredicateSymbol.LE,
    '>=': BuiltinPredicateSymbol.GE
}

arithmetic_rddl_to_tarski = {
    '-': lambda L, x, y : L.dispatch_operator(BuiltinFunctionSymbol.SUB, Term, Term, x, y),
    '+': lambda L, x, y : L.dispatch_operator(BuiltinFunctionSymbol.ADD, Term, Term, x, y),
    '*': lambda L, x, y : L.dispatch_operator(BuiltinFunctionSymbol.MUL, Term, Term, x, y),
    '/': lambda L, x, y : L.dispatch_operator(BuiltinFunctionSymbol.DIV, Term, Term, x, y)
}

func_rddl_to_tarski = {
    'abs': BuiltinFunctionSymbol.ABS,
    'Normal': BuiltinFunctionSymbol.NORMAL,
    'sqrt': BuiltinFunctionSymbol.SQRT,
    'pow': BuiltinFunctionSymbol.POW,
    'exp': BuiltinFunctionSymbol.EXP
}

def translate_expression(L, rddl_expr):
    try:
        expr_type, expr_sym = rddl_expr.etype
    except AttributeError:
        expr_type, expr_sym = rddl_expr

    if expr_type == 'number':
        if 'float' in expr_sym:
            return Constant(rddl_expr.args, L.Real)
        elif 'int' in expr_sym:
            return Constant(rddl_expr.args, L.Integer)
    elif expr_type == 'pvar':
        # MRJ: this is a next state fluent
        prima_fluent = False
        if "'" in rddl_expr.args[0]:
            prima_fluent = True
        tsym = L.get(rddl_expr.args[0].replace("'", ""))
        if len(rddl_expr.args) == 2 and rddl_expr.args[1] is None:
            if prima_fluent:
                if not isinstance(tsym, Predicate):
                    raise LanguageError("Temporal operator X only defined for predicates!")
                return tt.X(tsym())
            return tsym() # 0-ary
        targs = []
        for k, arg in enumerate(rddl_expr.args[1]):
            if arg[0] == '?':
                if isinstance(tsym, Function):
                    targs += [Variable(arg, tsym.domain[k])]
                elif isinstance(tsym, Predicate):
                    targs += [Variable(arg, tsym.sort[k])]
                else:
                    assert False
            elif isinstance(arg, float):
                targs += [Constant(arg, L.Real)]
            elif isinstance(arg, int):
                targs += [Constant(arg, L.Integer)]
            else:
                print(arg)
                targs += [L.get(arg)] # named constant?
        if prima_fluent:
            if not isinstance(tsym, Predicate):
                raise LanguageError("Temporal operator X only defined for predicates!")
            return tt.X(tsym(*targs))

        return tsym(*targs)
    elif expr_type == 'typed_var':
        var_name, var_type = expr_sym
        return Variable(var_name, L.get(var_type))
    elif expr_type == 'control':
        assert expr_sym == 'if'
        targs = [translate_expression(L, arg) for arg in rddl_expr.args]
        return ite(*targs)
    elif expr_type == 'relational':
        tsym = relational_rddl_to_tarski[expr_sym]
        targs = [translate_expression(L, arg) for arg in rddl_expr.args]
        return builtins.create_atom(L, tsym, targs[0], targs[1])
    elif expr_type == 'aggregation':
        if expr_sym == 'sum':
            var = translate_expression(L, rddl_expr.args[0])
            sum_expr = translate_expression(L, rddl_expr.args[1])
            return tm.summation(var, sum_expr)
        elif expr_sym == 'prod':
            var = translate_expression(L, rddl_expr.args[0])
            prod_expr = translate_expression(L, rddl_expr.args[1])
            return tm.product(var, prod_expr)
    elif expr_type == 'arithmetic':
        op = arithmetic_rddl_to_tarski[expr_sym]
        targs = [L] + [translate_expression(L, arg) for arg in rddl_expr.args]
        # MRJ: in some domains (e.g. Mars Rovers) there's stuff like a boolean multiplying an
        # expression
        if expr_sym == '*':
            if isinstance(targs[1], Formula):
                return ite(targs[1], targs[2], Constant(0, targs[2].sort))
            if isinstance(targs[2], Formula):
                return ite(targs[2], targs[1], Constant(0, targs[1].sort))
        #print(expr_sym, targs)
        if len(targs) == 2: # unary operator
            if expr_sym == '-':
                # replace -x by -1 * x
                actual_op = arithmetic_rddl_to_tarski['*']
                targs = [targs[0]] + [Constant(-1.0, L.Real)] + [targs[1]]
                return actual_op(*targs)
        return op(*targs)
    elif expr_type == 'func':
        func = func_rddl_to_tarski[expr_sym]
        targs = [translate_expression(L, arg) for arg in rddl_expr.args]
        return L.get(func)(*targs)
    elif expr_type == 'randomvar':
        func = func_rddl_to_tarski[expr_sym]
        targs = [translate_expression(L, arg) for arg in rddl_expr.args]
        return L.get(func)(*targs)
    elif expr_type == 'boolean':
        connective = logic_rddl_to_tarski[expr_sym]
        targs = [translate_expression(L, arg) for arg in rddl_expr.args]
        return connective(*targs)
    print(rddl_expr)
    assert False

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
            theories=[Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])

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
