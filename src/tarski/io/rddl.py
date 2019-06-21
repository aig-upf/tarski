"""
    RDDL model acquisition module
"""
from enum import Enum

from pyrddl.parser import RDDLParser

from .common import load_tpl
from ..fol import FirstOrderLanguage
from ..syntax import implies, land, lor, neg, Connective, Quantifier, CompoundTerm, Interval, Atom, IfThenElse, \
    Contradiction, Tautology, CompoundFormula, forall, ite, AggregateCompoundTerm, QuantifiedFormula, Term, Function, \
    Variable, Predicate, Constant, Formula, builtins
from ..syntax import arithmetic as tm
from ..syntax.temporal import ltl as tt
from ..syntax.builtins import create_atom, BuiltinPredicateSymbol as BPS, BuiltinFunctionSymbol as BFS
from ..model import Model
from ..evaluators.simple import evaluate
from ..errors import LanguageError
from ..theories import Theory, language


class TranslationError(Exception):
    pass


logic_rddl_to_tarski = {
    '=>': implies,
    '^': land,
    '|': lor,
    '~': neg}

relational_rddl_to_tarski = {
    '==': BPS.EQ,
    '<=': BPS.LE,
    '>=': BPS.GE
}

arithmetic_rddl_to_tarski = {
    '-': lambda lang, x, y: lang.dispatch_operator(BFS.SUB, Term, Term, x, y),
    '+': lambda lang, x, y: lang.dispatch_operator(BFS.ADD, Term, Term, x, y),
    '*': lambda lang, x, y: lang.dispatch_operator(BFS.MUL, Term, Term, x, y),
    '/': lambda lang, x, y: lang.dispatch_operator(BFS.DIV, Term, Term, x, y)
}

func_rddl_to_tarski = {
    'abs': BFS.ABS,
    'Normal': BFS.NORMAL,
    'sqrt': BFS.SQRT,
    'pow': BFS.POW,
    'exp': BFS.EXP,
    'max': BFS.MAX,
    'Gamma': BFS.GAMMA
}


def translate_expression(lang, rddl_expr):
    try:
        expr_type, expr_sym = rddl_expr.etype
    except AttributeError:
        expr_type, expr_sym = rddl_expr

    if expr_type == 'number':
        if 'float' in expr_sym:
            return Constant(rddl_expr.args, lang.Real)
        elif 'int' in expr_sym:
            return Constant(rddl_expr.args, lang.Integer)
    elif expr_type == 'pvar_expr':
        # MRJ: this is a next state fluent
        # prima_fluent = False
        pvar_name = expr_sym[0]
        # if "'" in pvar_name:
        #     prima_fluent = True
        tsym = lang.get(pvar_name.replace("'", ""))
        args = expr_sym[1]
        targs = []
        if args is not None:
            for k, arg in enumerate(args):
                if arg[0] == '?':
                    if isinstance(tsym, Function):
                        targs += [Variable(arg, tsym.domain[k])]
                    elif isinstance(tsym, Predicate):
                        targs += [Variable(arg, tsym.sort[k])]
                    else:
                        assert False
                elif isinstance(arg, float):
                    targs += [Constant(arg, lang.Real)]
                elif isinstance(arg, int):
                    targs += [Constant(arg, lang.Integer)]
                else:
                    # print(arg)
                    targs += [lang.get(arg)]  # named constant?
        return tsym(*targs)

    elif expr_type == 'pvar':
        # MRJ: this is a next state fluent
        prima_fluent = False
        if "'" in rddl_expr.args[0]:
            prima_fluent = True
        tsym = lang.get(rddl_expr.args[0].replace("'", ""))
        if len(rddl_expr.args) == 2 and rddl_expr.args[1] is None:
            if prima_fluent:
                if not isinstance(tsym, Predicate):
                    raise LanguageError("Temporal operator X only defined for predicates!")
                return tt.X(tsym())
            return tsym()  # 0-ary
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
                targs += [Constant(arg, lang.Real)]
            elif isinstance(arg, int):
                targs += [Constant(arg, lang.Integer)]
            else:
                # print(arg)
                targs += [lang.get(arg)]  # named constant?
        if prima_fluent:
            if not isinstance(tsym, Predicate):
                raise LanguageError("Temporal operator X only defined for predicates!")
            return tt.X(tsym(*targs))

        return tsym(*targs)
    elif expr_type == 'typed_var':
        var_name, var_type = expr_sym
        return Variable(var_name, lang.get(var_type))
    elif expr_type == 'control':
        assert expr_sym == 'if'
        targs = [translate_expression(lang, arg) for arg in rddl_expr.args]
        return ite(*targs)
    elif expr_type == 'relational':
        tsym = relational_rddl_to_tarski[expr_sym]
        targs = [translate_expression(lang, arg) for arg in rddl_expr.args]
        return create_atom(lang, tsym, targs[0], targs[1])
    elif expr_type == 'aggregation':
        if expr_sym == 'sum':
            var = translate_expression(lang, rddl_expr.args[0])
            sum_expr = translate_expression(lang, rddl_expr.args[1])
            if isinstance(sum_expr, Formula):
                sum_expr = ite(sum_expr, Constant(1, lang.Integer), Constant(0, lang.Integer))
            return tm.summation(var, sum_expr)
        elif expr_sym == 'prod':
            var = translate_expression(lang, rddl_expr.args[0])
            prod_expr = translate_expression(lang, rddl_expr.args[1])
            if isinstance(prod_expr, Formula):
                prod_expr = ite(prod_expr, Constant(1, lang.Integer), Constant(0, lang.Integer))
            return tm.product(var, prod_expr)
        elif expr_sym == 'forall':
            var = translate_expression(lang, rddl_expr.args[0])
            forall_expr = translate_expression(lang, rddl_expr.args[1])
            return forall(var, forall_expr)
    elif expr_type == 'arithmetic':
        op = arithmetic_rddl_to_tarski[expr_sym]
        targs = [lang] + [translate_expression(lang, arg) for arg in rddl_expr.args]
        # MRJ: in some domains (e.g. Mars Rovers) there's stuff like a boolean multiplying an
        # expression
        if expr_sym == '*':
            if isinstance(targs[1], Formula):
                return ite(targs[1], targs[2], Constant(0, targs[2].sort))
            if isinstance(targs[2], Formula):
                return ite(targs[2], targs[1], Constant(0, targs[1].sort))
        # print(expr_sym, targs)
        if len(targs) == 2:  # unary operator
            if expr_sym == '-':
                # replace -x by -1 * x
                actual_op = arithmetic_rddl_to_tarski['*']
                targs = [targs[0]] + [Constant(-1.0, lang.Real)] + [targs[1]]
                return actual_op(*targs)
        return op(*targs)
    elif expr_type == 'func':
        func = func_rddl_to_tarski[expr_sym]
        targs = [translate_expression(lang, arg) for arg in rddl_expr.args]
        return lang.get(func)(*targs)
    elif expr_type == 'randomvar':
        func = func_rddl_to_tarski[expr_sym]
        targs = [translate_expression(lang, arg) for arg in rddl_expr.args]
        return lang.get(func)(*targs)
    elif expr_type == 'boolean':
        connective = logic_rddl_to_tarski[expr_sym]
        targs = [translate_expression(lang, arg) for arg in rddl_expr.args]
        return connective(*targs)
    elif expr_type == 'constant':
        if "class 'float'" in expr_sym:
            k = Constant(rddl_expr.args, lang.Real)
            return k
        if "class 'int'" in expr_sym:
            k = Constant(rddl_expr.args, lang.Real)
            return k

    # print(rddl_expr, expr_type, type(expr_sym))
    assert False


class Parameters:
    """
        RDDL instance parameters
    """

    def __init__(self):
        self.horizon = None
        self.discount = None
        self.max_actions = None


class Reader:
    """
        Reader creates a FOL and several language components
        that specify a RDDL task
    """

    def __init__(self, filename):
        self.language = None
        self.rddl_model = self._load_rddl_model(filename)
        self.parameters = Parameters()
        self.x0 = None

    def _load_rddl_model(self, filename):
        with open(filename, 'r') as input_file:
            rddl = input_file.read()
        parser = RDDLParser()
        parser.build()
        # parse RDDL
        return parser.parse(rddl)

    def _translate_types(self):
        for typename, parent_type in self.rddl_model.domain.types:
            assert parent_type == 'object'
            self.language.sort(typename, self.language.Object)
        non_fluents = self.rddl_model.non_fluents
        if not hasattr(non_fluents, 'objects') or not non_fluents.objects or non_fluents.objects[0] is None:
            return
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
        self.language = language(self.rddl_model.domain.name,
                                 theories=[Theory.EQUALITY, Theory.ARITHMETIC, Theory.SPECIAL, Theory.RANDOM])

        # 1. create types
        self._translate_types()

        # 2. create functions (or predicates) for all variable types
        self._translate_variables()

        # 3. acquire instance parameters
        self.parameters.horizon = self.rddl_model.instance.horizon
        self.parameters.discount = self.rddl_model.instance.discount
        if self.rddl_model.instance.max_nondef_actions != 'pos-inf':
            self.parameters.max_actions = self.rddl_model.instance.max_nondef_actions

        # 4. recover initial state, interpretation of fluents
        self.x0 = Model(self.language)
        self.x0.evaluator = evaluate

        for fluent, value in self.rddl_model.instance.init_state:
            expr = translate_expression(self.language, ('pvar_expr', fluent))
            if isinstance(expr, Term):
                self.x0.setx(expr, value)
            if isinstance(expr, Atom) and value is True:
                self.x0.add(expr.predicate, *expr.subterms)
        for fluent, value in self.rddl_model.non_fluents.init_non_fluent:
            expr = translate_expression(self.language, ('pvar_expr', fluent))
            if isinstance(expr, Term):
                self.x0.setx(expr, value)
            if isinstance(expr, Atom) and value is True:
                self.x0.add(expr.predicate, *expr.subterms)


built_in_type_map = {'object': 'Object', 'real': 'Real', 'int': 'Integer'}
reverse_built_in_type_map = {'Object': 'object', 'Real': 'real', 'Integer': 'int'}


def translate_builtin_type(lang: FirstOrderLanguage, name):
    return lang.get(built_in_type_map[name])


def translate_variable(lang: FirstOrderLanguage, name, term):
    name = name.split('/')[0]  # forget about the arity of the symbol
    params = []
    if term.param_types is not None:
        params = term.param_types
    if term.range in ('bool', 'boolean'):
        signature = tuple(params)
    else:
        signature = tuple(params + [term.range])
    # translate signature to sorts
    t_signature = []
    for s in signature:
        try:
            t_s = lang.get(s)
        except LanguageError:
            t_s = translate_builtin_type(lang, s)
        t_signature += [t_s]
    if term.range in ('bool', 'boolean'):
        return lang.predicate(name, *t_signature)
    return lang.function(name, *t_signature)


class Requirements(Enum):
    CONTINUOUS = "continuous"
    MULTIVALUED = "multivalued"
    REWARD_DET = "reward-deterministic"
    INTERMEDIATE_NODES = "intermediate-nodes"
    PARTIALLY_OBS = "partially-observed"
    CONCURRENT = "concurrent"
    INTEGER_VALUED = "integer-valued"
    CPF_DETERMINISTIC = "cpf-deterministic"

    def __str__(self):
        return self.value.lower()


class PVarTypes(Enum):
    NON_FLUENT = "non-fluent"
    STATE_FLUENT = "state-fluent"
    INTERM_FLUENT = "interm-fluent"
    OBSERV_FLUENT = "observ-fluent"

    def __str__(self):
        return self.value.lower()


class PVarDomains(Enum):
    BOOL = "bool"
    INT = "int"
    REAL = "real"
    OBJECT = "object"
    ENUMERATED = "enumerated"

    def __str__(self):
        return self.value.lower()


class ConstraintType(Enum):
    ACTION = "action"
    STATE = "state"
    INVARIANT = "invariant"

    def __str__(self):
        return self.value.lower()


symbol_map = {
    BPS.EQ: "==",
    BPS.NE: "~=",
    BPS.LT: "<",
    BPS.LE: "<=",
    BPS.GT: ">",
    BPS.GE: ">=",
    Connective.And: "^",
    Connective.Or: "|",
    Connective.Not: "~",
    Quantifier.Exists: "exists",
    Quantifier.Forall: "forall",
    BFS.ADD: "+",
    BFS.SUB: "-",
    BFS.MUL: "*",
    BFS.DIV: "/",
    BFS.POW: "**",
    BFS.MOD: "%"
}

function_map = {
    BFS.MIN: "min",
    BFS.MAX: "max",
    BFS.ABS: "abs",
    BFS.SIN: "sin",
    BFS.COS: "cos",
    BFS.TAN: "tan",
    BFS.ATAN: "atan",
    BFS.ASIN: "asin",
    BFS.EXP: "exp",
    BFS.LOG: "log",
    BFS.ERF: "erf",
    BFS.ERFC: "erfc",
    BFS.SGN: "sgn",
    BFS.SQRT: "sqrt",
    BFS.NORMAL: "Normal",
    BFS.GAMMA: "Gamma",
    BFS.KRON: "KronDelta",
    BFS.DIRAC: "DiracDelta",
    BFS.BERNOULLI: "Bernoulli",
    BFS.DISCRETE: "Discrete",
    BFS.POISSON: "Poisson"
}


class Writer:
    """
        Writer compiles the specification of a planning task
        into RDDL
    """

    def __init__(self, task):
        self.task = task
        self.need_constraints = {}
        self.need_obj_decl = []
        self.non_fluent_signatures = set()
        self.interm_signatures = set()

    def write_model(self, filename):
        tpl = load_tpl("rddl_model.tpl")
        content = tpl.format(
            domain_name=self.task.domain_name,
            req_list=self.get_requirements(),
            type_list=self.get_types(),
            pvar_list=self.get_pvars(),
            cpfs_list=self.get_cpfs(),
            reward_expr=self.get_reward(),
            action_precondition_list=self.get_preconditions(),
            state_invariant_list=self.get_state_invariants(),
            domain_non_fluents='{}_non_fluents'.format(self.task.instance_name),
            object_list=self.get_objects(),
            non_fluent_expr=self.get_non_fluent_init(),
            instance_name=self.task.instance_name,
            init_state_fluent_expr=self.get_state_fluent_init(),
            non_fluents_ref='{}_non_fluents'.format(self.task.instance_name),
            max_nondef_actions=self.get_max_nondef_actions(),
            horizon=self.get_horizon(),
            discount=self.get_discount()
        )
        with open(filename, 'w') as file:
            file.write(content)

    def get_requirements(self):
        return ', '.join([str(r) for r in self.task.requirements])

    def get_types(self):
        from tarski.syntax.sorts import parent
        type_decl_list = []
        for S in self.task.L.sorts:
            if S.builtin or S.name == 'object':
                continue
            if isinstance(S, Interval):
                self.need_constraints[S.name] = S
                continue
            type_decl_list += ['{} : {};'.format(S.name, parent(S).name)]
            self.need_obj_decl += [S]
        return '\n'.join(type_decl_list)

    def get_type(self, fl):
        if isinstance(fl, Atom):
            return 'bool'
        try:
            return reverse_built_in_type_map[fl.symbol.codomain.name]
        except KeyError:
            return fl.symbol.codomain.name

    def get_signature(self, fl):
        if isinstance(fl, CompoundTerm):
            sig = fl.symbol.signature
            head = sig[0]
            domain = sig[1:-1]
        elif isinstance(fl, Atom):
            sig = fl.predicate.signature
            head = sig[0]
            domain = sig[1:]
        else:
            assert False
        if len(domain) == 0:
            return '{}'.format(head)
        return '{}({})'.format(head, ','.join(domain))

    def get_pvars(self):
        pvar_decl_list = []
        # state fluents
        for fl, v in self.task.state_fluents:
            rsig = self.get_signature(fl)
            pvar_decl_list += ['\t{} : {{state-fluent, {}, default = {}}};'.format(rsig, self.get_type(fl), str(v))]
        for fl, level in self.task.interm_fluents:
            rsig = self.get_signature(fl)
            try:
                self.interm_signatures.add(fl.symbol.signature)
            except AttributeError:
                self.interm_signatures.add(fl.predicate.signature)
            pvar_decl_list += ['\t{} : {{interm-fluent, {}, level = {}}};'.format(rsig, self.get_type(fl), str(level))]
        for fl, v in self.task.action_fluents:
            rsig = self.get_signature(fl)
            pvar_decl_list += ['\t{} : {{action-fluent, {}, default = {}}};'.format(rsig, self.get_type(fl), str(v))]
        for fl, v in self.task.non_fluents:
            rsig = self.get_signature(fl)
            try:
                self.non_fluent_signatures.add(fl.symbol.signature)
            except AttributeError:
                self.non_fluent_signatures.add(fl.predicate.signature)
            pvar_decl_list += ['\t{} : {{non-fluent, {}, default = {}}};'.format(rsig, self.get_type(fl), str(v))]
        return '\n'.join(pvar_decl_list)

    def get_cpfs(self):
        cpfs_decl_list = []
        for lhs, rhs in self.task.cpfs:
            cpfs_decl_list += ['\t{} = {};'.format(self.get_fluent(lhs, True), self.rewrite(rhs))]
        return '\n'.join(cpfs_decl_list)

    def get_reward(self):
        return self.rewrite(self.task.reward)

    def get_preconditions(self):
        act_prec_list = []
        for expr, ctype in self.task.constraints:
            if ctype == ConstraintType.ACTION:
                act_prec_list += ['\t{};'.format(self.rewrite(expr))]
        return '\n'.join(act_prec_list)

    def get_state_invariants(self):
        state_inv_list = []
        for expr, ctype in self.task.constraints:
            if ctype == ConstraintType.STATE:
                state_inv_list += ['\t{};'.format(self.rewrite(expr))]
        return '\n'.join(state_inv_list)

    def get_objects(self):
        obj_decl_blocks = []

        if len(self.need_obj_decl) == 0:
            return ''

        # initialize
        for S in self.need_obj_decl:
            domain_str = ','.join([str(c.symbol) for c in S.domain()])
            obj_decl_blocks += ['\t{} : {{{}}};'.format(S.name, domain_str)]

        return 'objects {{{}}};'.format('\n'.join(obj_decl_blocks))

    def get_non_fluent_init(self):
        non_fluent_init_list = []
        for signature, defs in self.task.x0.function_extensions.items():
            if signature not in self.non_fluent_signatures:
                continue
            for st_refs, value in defs.data.items():
                subterms = [r.expr for r in st_refs]
                if len(subterms) == 0:
                    term_str = signature[0]
                else:
                    term_str = str(self.task.L.get(signature[0])(*subterms))
                non_fluent_init_list += ['\t{} = {};'.format(term_str, value)]
        for signature, defs in self.task.x0.predicate_extensions.items():
            if signature not in self.non_fluent_signatures:
                continue
            for st_refs in defs:
                subterms = [r.expr for r in st_refs]
                if len(subterms) == 0:
                    atom_str = signature[0]
                else:
                    atom_str = str(self.task.L.get(signature[0])(*subterms))
                non_fluent_init_list += ['\t{} = true;'.format(atom_str)]

        if len(non_fluent_init_list) == 0:
            return ''

        return 'non-fluents {{{}}};'.format('\n'.join(non_fluent_init_list))

    def get_state_fluent_init(self):
        init_list = []
        for signature, defs in self.task.x0.function_extensions.items():
            if signature in self.non_fluent_signatures \
                    or signature in self.interm_signatures:
                continue
            for st_refs, value in defs.data.items():
                subterms = [r.expr for r in st_refs]
                if len(subterms) == 0:
                    term_str = signature[0]
                else:
                    term_str = str(self.task.L.get(signature[0])(*subterms))
                init_list += ['\t{} = {};'.format(term_str, value)]
        for signature, defs in self.task.x0.predicate_extensions.items():
            if signature in self.non_fluent_signatures \
                    or signature in self.interm_signatures:
                continue
            for st_refs in defs:
                subterms = [r.expr for r in st_refs]
                if len(subterms) == 0:
                    atom_str = signature[0]
                else:
                    atom_str = str(self.task.L.get(signature[0])(*subterms))
                init_list += ['\t{} = true;'.format(atom_str)]

        return '\n'.join(init_list)

    def rewrite(self, expr):
        if expr is None:
            return '0.0'
        if isinstance(expr, CompoundTerm):
            re_st = [self.rewrite(st) for st in expr.subterms]
            if expr.symbol.builtin:
                if expr.symbol.symbol in symbol_map.keys():
                    return '({} {} {})'.format(re_st[0], symbol_map[expr.symbol.symbol], re_st[1])
            st_str = ''
            if expr.symbol.builtin:
                if expr.symbol.symbol in function_map.keys():
                    if len(re_st) > 0:
                        # MRJ: Random variables need parenthesis, other functions need
                        # brackets...
                        if expr.symbol.symbol in builtins.get_random_binary_functions():
                            st_str = '({})'.format(','.join(re_st))
                        else:
                            st_str = '[{}]'.format(','.join(re_st))
                    return '{}{}'.format(function_map[expr.symbol.symbol], st_str)
            if len(re_st) > 0:
                st_str = '({})'.format(','.join(re_st))
            return '{}{}'.format(expr.symbol.signature[0], st_str)
        elif isinstance(expr, Atom):
            re_st = [self.rewrite(st) for st in expr.subterms]
            if expr.predicate.builtin:
                if expr.predicate.symbol in symbol_map.keys():
                    return '({} {} {})'.format(re_st[0], symbol_map[expr.predicate.symbol], re_st[1])
            st_str = ''
            if len(re_st) > 0:
                st_str = '({})'.format(','.join(re_st))
            return '{}{}'.format(expr.predicate.signature[0], st_str)
        elif isinstance(expr, Variable):
            # remove ? just in case
            return '?{}'.format(expr.symbol.replace('?', ''))
        elif isinstance(expr, Constant):
            return str(expr)
        elif isinstance(expr, IfThenElse):
            cond = self.rewrite(expr.condition)
            expr1 = self.rewrite(expr.subterms[0])
            expr2 = self.rewrite(expr.subterms[1])
            return 'if ({}) then ({}) else ({})'.format(cond, expr1, expr2)
        elif isinstance(expr, Tautology):
            return 'true'
        elif isinstance(expr, Contradiction):
            return 'false'
        elif isinstance(expr, CompoundFormula):
            re_sf = [self.rewrite(st) for st in expr.subformulas]
            re_sym = symbol_map[expr.connective]
            if len(re_sf) == 1:
                return '{}{}'.format(re_sym, re_sf)
            return '({} {} {})'.format(re_sf[0], re_sym, re_sf[1])
        elif isinstance(expr, QuantifiedFormula):
            re_f = self.rewrite(expr.formula)
            re_vars = ['?{} : {}'.format(x.symbol, x.sort.name) for x in expr.variables]
            re_sym = symbol_map[expr.quantifier]
            return '{}_{{{}}} ({})'.format(re_sym, ','.join(re_vars), re_f)
        elif isinstance(expr, AggregateCompoundTerm):
            re_expr = self.rewrite(expr.subterm)
            re_vars = ['?{} : {}'.format(x.symbol, x.sort.name) for x in expr.bound_vars]
            if expr.symbol == BFS.ADD:
                re_sym = 'sum'
            elif expr.symbol == BFS.MUL:
                re_sym = 'prod'
            return '{}_{{{}}} ({})'.format(re_sym, ','.join(re_vars), re_expr)

    def get_fluent(self, fl, next_state=False):
        try:
            head = fl.symbol.signature[0]
        except AttributeError:
            head = fl.predicate.signature[0]
        subterms_str = ''
        if len(fl.subterms) > 0:
            subterms_str = []
            for st in fl.subterms:
                if isinstance(st, Variable):
                    # remove any ? from symbol just in case
                    subterms_str += ['?{}'.format(st.symbol.replace('?', ''))]
                else:
                    subterms_str += [str(st)]
            subterms_str = '({})'.format(','.join(subterms_str))
        prima = ''
        if next_state:
            prima = "'"
        return "{}{}{}".format(head, prima, subterms_str)

    def get_max_nondef_actions(self):
        return str(self.task.parameters.max_nondef_actions)

    def get_horizon(self):
        return str(self.task.parameters.horizon)

    def get_discount(self):
        return str(self.task.parameters.discount)
