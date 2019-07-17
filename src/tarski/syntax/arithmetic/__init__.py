import itertools
import copy
import numpy as np

from ...syntax import Term, AggregateCompoundTerm, CompoundTerm, Constant, Variable, IfThenElse, create_substitution, \
    term_substitution
from ...syntax.algebra import Matrix
from ... import errors as err
from ... grounding.naive import instantiation
from ..builtins import BuiltinFunctionSymbol, get_arithmetic_binary_functions


def sumterm(*args):
    variables = args[:-1]
    expr = args[-1]
    if len(variables) < 1:
        raise err.SyntacticError(msg='sumterm(x0,x1,...,xn,expr) requires at least one\
        bound variable, arguments: {}'.format(args))
    for x in variables:
        if not isinstance(x, Variable):
            raise err.SyntacticError(msg='sum(x0,...,xn,expr) require each\
            argument xi to be an instance of Variable')
    if not isinstance(expr, Term):
        raise err.SyntacticError(msg='sum(x0,x1,...,xn,expr) requires last \
        argument "expr" to be an instance of Term, got "{}"'.format(expr))
    return AggregateCompoundTerm(BuiltinFunctionSymbol.ADD, variables, expr)


def prodterm(*args):
    variables = args[:-1]
    expr = args[-1]
    if len(variables) < 1:
        raise err.SyntacticError(msg='sumterm(x0,x1,...,xn,expr) requires at least one\
        bound variable, arguments: {}'.format(args))
    for x in variables:
        if not isinstance(x, Variable):
            raise err.SyntacticError(msg='sum(x0,...,xn,expr) require each\
            argument xi to be an instance of Variable')
    if not isinstance(expr, Term):
        raise err.SyntacticError(msg='sum(x0,x1,...,xn,expr) requires last \
        argument "expr" to be an instance of Term, got "{}"'.format(expr))
    return AggregateCompoundTerm(BuiltinFunctionSymbol.MUL, variables, expr)


def summation(*args):
    """
        Summation of a (nested) sequence of expressions defined over one or more
        variables.
    """
    expr = args[-1]
    if not isinstance(expr, Term):
        raise err.SyntacticError(msg='sum(x0,x1,...,xn,expr) requires last \
        argument "expr" to be an instance of Term, got "{}"'.format(expr))
    variables = []
    for x in args[:-1]:
        if not isinstance(x, Variable):
            raise err.SyntacticError(msg='sum(x0,...,xn,expr) require each\
            argument xi to be an instance of Variable')
        variables.append(x)

    L = expr.language
    _, syms, substs = instantiation.enumerate_groundings(L, list(variables))
    processed_expr = []
    for values in itertools.product(*substs):
        subst = create_substitution(syms, values)
        processed_expr.append(term_substitution(L, expr, subst))

    lhs = processed_expr[0]
    for k in range(1, len(processed_expr)):
        lhs = L.dispatch_operator(BuiltinFunctionSymbol.ADD, Term, Term, lhs, processed_expr[k])

    return lhs


def product(*args):
    """
        Product of a (nested) sequence of expressions defined over one or
        more variables.
    """
    expr = args[-1]
    if not isinstance(expr, Term):
        raise err.SyntacticError(msg='prod(x0,x1,...,xn,expr) requires last \
        argument "expr" to be an instance of Term')
    variables = []
    for x in args[:-1]:
        if not isinstance(x, Variable):
            raise err.SyntacticError(msg='prod(x0,...,xn,expr) require each\
            argument xi to be an instance of Variable')
        variables.append(x)

    L = expr.language
    _, syms, substs = instantiation.enumerate_groundings(L, list(variables))
    processed_expr = []
    for values in itertools.product(*substs):
        subst = create_substitution(syms, values)
        processed_expr.append(term_substitution(L, expr, subst))

    lhs = processed_expr[0]
    for k in range(1, len(processed_expr)):
        lhs = L.dispatch_operator(BuiltinFunctionSymbol.MUL, Term, Term, lhs, processed_expr[k])

    return lhs


def pow(x, y):
    pow_func = x.language.get_function(BuiltinFunctionSymbol.POW)
    return pow_func(x, y)


def sqrt(x):
    sqrt_func = x.language.get_function(BuiltinFunctionSymbol.SQRT)
    return sqrt_func(x)


def transpose(m: Term):
    if isinstance(m, Matrix):
        m_t = copy.copy(m)
        m_t.matrix = m_t.matrix.T
        return m_t
    elif isinstance(m, CompoundTerm):
        if m.symbol.symbol in get_arithmetic_binary_functions():
            # handle as an operator
            if m.symbol.symbol == BuiltinFunctionSymbol.ADD:
                m.subterms = (transpose(m.subterms[0]), transpose(m.subterms[1]))
                return m
            if m.symbol.symbol == BuiltinFunctionSymbol.SUB:
                m.subterms = (transpose(m.subterms[0]), transpose(m.subterms[1]))
                return m
            elif m.symbol.symbol == BuiltinFunctionSymbol.MUL:
                m.subterms = (transpose(m.subterms[1]), transpose(m.subterms[0]))
                return m
        raise err.SyntacticError("transpose() only applicable on scalars (constants, variables), "
                                 "matrices and basic arithmetic operations.")
    elif isinstance(m, Constant):
        return Matrix([m], m.sort)
    elif isinstance(m, Variable):
        return Matrix([m], m.sort)
    raise err.SyntacticError(
        "transpose(): can only be applied on scalars (constants, variables), matrices and basic arithmetic operations.")


def zero(sort):
    assert sort.name in ('Real', 'Integer', 'Natural')
    return sort.language.constant(0, sort)


def one(sort):
    assert sort.name in ('Real', 'Integer', 'Natural')
    return sort.language.constant(1, sort)


def simplify(expr: Term):
    if isinstance(expr, Constant):
        return expr
    elif isinstance(expr, Variable):
        return expr
    elif isinstance(expr, CompoundTerm):
        if not expr.symbol.builtin:
            return expr
        if expr.symbol.symbol == BuiltinFunctionSymbol.ADD:
            simp_st = (simplify(expr.subterms[0]), simplify(expr.subterms[1]))
            if simp_st[0].is_syntactically_equal(zero(expr.sort)):
                return simp_st[1]
            if simp_st[1].is_syntactically_equal(zero(expr.sort)):
                return simp_st[0]
            expr.subterms = simp_st
            return expr
        if expr.symbol.symbol == BuiltinFunctionSymbol.SUB:
            simp_st = (simplify(expr.subterms[0]), simplify(expr.subterms[1]))
            if simp_st[0].is_syntactically_equal(zero(expr.sort)):
                return -1 * simp_st[1]
            if simp_st[1].is_syntactically_equal(zero(expr.sort)):
                return simp_st[0]
            expr.subterms = simp_st
            return expr
        if expr.symbol.symbol == BuiltinFunctionSymbol.MUL:
            simp_st = (simplify(expr.subterms[0]), simplify(expr.subterms[1]))
            if simp_st[0].is_syntactically_equal(zero(expr.sort)):
                return zero(expr.sort)
            if simp_st[1].is_syntactically_equal(zero(expr.sort)):
                return zero(expr.sort)
            if simp_st[0].is_syntactically_equal(one(expr.sort)):
                return simp_st[1]
            if simp_st[1].is_syntactically_equal(one(expr.sort)):
                return simp_st[0]
            expr.subterms = simp_st
            return expr
        if expr.symbol.symbol == BuiltinFunctionSymbol.DIV:
            simp_st = (simplify(expr.subterms[0]), simplify(expr.subterms[1]))
            if simp_st[0].is_syntactically_equal(zero(expr.sort)):
                return zero(expr.sort)
            if simp_st[1].is_syntactically_equal(zero(expr.sort)):
                raise err.SemanticError("Division by Zero detected when \
            simplifying expression '{}' in division '{}'".format(expr.subterms[1], expr))
            if simp_st[1].is_syntactically_equal(one(expr.sort)):
                return simp_st[0]
            expr.subterms = simp_st
            return expr
        if expr.symbol.symbol == BuiltinFunctionSymbol.EXP:
            simp_st = simplify(expr.subterms[0])
            if simp_st.is_syntactically_equal(zero(expr.sort)):
                return one(expr.sort)
            expr.subterms = (simp_st,)
            return expr
    elif isinstance(expr, (Matrix, np.ndarray)):
        N, M = expr.shape
        for i in range(N):
            for j in range(M):
                expr[i, j] = simplify(expr[i, j])
        return expr
    elif isinstance(expr, AggregateCompoundTerm):
        expr.subterm = simplify(expr.subterm)
        return expr
    elif isinstance(expr, IfThenElse):
        expr.subterms = (simplify(expr.subterms[0]), simplify(expr.subterms[1]))
        return expr

    raise NotImplementedError("Can't handle expression {} yet".format(expr))
