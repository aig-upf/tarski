
import copy

from ... import fstrips as fs
from ...syntax import Variable, symref
from ...syntax.visitors import CollectVariables
from ...syntax.ops import all_variables


def process_expression(language, schema, op, copy_schema=True):
    # pylint: disable=unused-argument
    if copy_schema:
        g_expr = copy.deepcopy(schema)
    else:
        g_expr = schema
    op.visit(g_expr)
    assert len(all_variables(g_expr)) == 0
    return g_expr


def process_effect(language, eff_schema, op):
    # pylint: disable=unused-argument
    if isinstance(eff_schema, (fs.AddEffect, fs.DelEffect)):
        op.visit(eff_schema.atom)
    elif isinstance(eff_schema, fs.LiteralEffect):
        op.visit(eff_schema.lit)
    elif isinstance(eff_schema, fs.FunctionalEffect):
        op.visit(eff_schema.lhs)
        if isinstance(eff_schema.rhs, Variable):
            eff_schema.rhs = op.subst.get(symref(eff_schema.rhs), None)
        else:
            op.visit(eff_schema.rhs)
    elif isinstance(eff_schema, fs.ChoiceEffect):
        op.visit(eff_schema.obj)
        _ = [op.visit(x) for x in eff_schema.variables]

    # MRJ: invariant
    var_collector = CollectVariables()
    if isinstance(eff_schema, (fs.AddEffect, fs.DelEffect)):
        var_collector.visit(eff_schema.atom)
    elif isinstance(eff_schema, fs.FunctionalEffect):
        var_collector.visit(eff_schema.lhs)
        var_collector.visit(eff_schema.rhs)
    elif isinstance(eff_schema, fs.LiteralEffect):
        var_collector.visit(eff_schema.lit)
    elif isinstance(eff_schema, fs.ChoiceEffect):
        var_collector.visit(eff_schema.obj)
        _ = [var_collector.visit(x) for x in eff_schema.variables]
    assert len(var_collector.variables) == 0
    return eff_schema
