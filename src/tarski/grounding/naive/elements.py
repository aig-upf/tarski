# -*- coding: utf-8 -*-
import copy

from ... import fstrips as fs
from ...syntax import Variable
from ...syntax.visitors import CollectVariables


def process_expression(language, schema, op, copy_schema=True):
    if copy_schema:
        g_expr = copy.deepcopy(schema)
    else:
        g_expr = schema
    g_expr.accept(op)
    var_collector = CollectVariables()
    g_expr.accept(var_collector)
    assert len(var_collector.variables) == 0
    return g_expr


def process_effect(language, eff_schema, op):
    if isinstance(eff_schema, (fs.AddEffect, fs.DelEffect)):
        eff_schema.atom.accept(op)
    elif isinstance(eff_schema, fs.FunctionalEffect):
        eff_schema.lhs.accept(op)
        if isinstance(eff_schema.rhs, Variable):
            eff_schema.rhs = op.subst.get(eff_schema.rhs, None)
        else:
            eff_schema.rhs.accept(op)
    elif isinstance(eff_schema, fs.ChoiceEffect):
        eff_schema.obj.accept(op)
        for x in eff_schema.variables:
            x.accept(op)

    # MRJ: invariant
    var_collector = CollectVariables()
    if isinstance(eff_schema, (fs.AddEffect, fs.DelEffect)):
        eff_schema.atom.accept(var_collector)
    elif isinstance(eff_schema, fs.FunctionalEffect):
        eff_schema.lhs.accept(var_collector)
        eff_schema.rhs.accept(var_collector)
    elif isinstance(eff_schema, fs.ChoiceEffect):
        eff_schema.obj.accept(var_collector)
        for x in eff_schema.variables:
            x.accept(var_collector)
    assert len(var_collector.variables) == 0
    return eff_schema
