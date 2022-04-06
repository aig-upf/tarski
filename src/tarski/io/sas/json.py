# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# tarski/io/sas/json.py
#
# Planner-agnostic SAS serialization into JSON streams
# ----------------------------------------------------------------------------------------------------------------------
import json

from tarski.syntax import symref
from tarski.util import SymbolIndex


def dump(lang, actions, initial, goal, objects, domains, name, fp):
    """
    Serializes instance elements (domain theory, actions, initial state and goal condition) into a JSON
    formatted stream.

    :param lang: Domain theory
    :param actions: List of ground actions
    :param initial: Initial state, a list of equality literals, given as pairs of terms
    (symbol of the form $x(\bar{a})$) and values v (constant symbols)
    :param goal: Goal state, a list of equality literals, given as pairs of term (as above) and values v (as above)
    :param name: instance name
    :param fp:
    :return:
    """

    # `SymbolIndex` is a container class that allows to define a set of objects, where each element is indexed
    X = SymbolIndex()

    # We identify the set of terms by inspecting 1) action transition constraints, 2) the definition of the
    # initial state, and 3) the structure of the (conjunctive) goal formula.
    for act in actions:
        for x, _, _ in act.transitions:
            if symref(x) in X:
                continue
            X.add(symref(x))

    for x, _ in initial:
        if symref(x) in X:
            continue
        X.add(symref(x))

    for x, _ in goal:
        if symref(x) in X:
            continue
        X.add(symref(x))

    # We aggregate all "named" constants in a set (domain) D
    D = SymbolIndex()
    for obj in objects:
        if obj.sort == lang.Integer:
            continue  # do not encode integers as objects
        if symref(obj) in D:
            continue
        D.add(symref(obj))

    # Depending on the planner, it may be convenient to have definitions of "types" subsets of D, the naturals,
    # integers or the reals even
    types_data = [
        {"name": "object",
         "domain": [str(o) for o in objects]}
    ]

    # Here we setup an index that defines the variables of the SAS instance. For each variable we give its
    # symbolic representation (a string of characters like "on(A)"), and a reference to its domain (set of
    # objects). Note that a domain does not need to be "tight" and may include many values that never appear
    # in the set of solutions of transition constraints.

    vars_data = []

    for x in X.objects:
        if x.expr.symbol.codomain == lang.Object:
            vars_data += [
                {"name": str(x.expr), "type": "object"}
            ]
        elif x.expr.symbol.codomain == lang.Integer:
            # we need the bounds
            vars_data += [
                {"name": str(x.expr), "type": "int", "domain": [domains[x][0], domains[x][-1]]}
            ]

    vars_data = [
        {"name": str(x.expr),
         "type": "object"} for x in X.objects
    ]

    # Now we provide the list of symbolic representations for each of the actions in the instance
    action_names = [
        "{}({})".format(a.name, ",".join([str(arg) for arg in a.arguments])) for a in actions
    ]

    # The transition function is factored as table constraints $Tr(a,x)$, and for each constraint
    # - indexed by action and variable - we give the pairs of values v and w s.t. for any tuple
    # (s,a,s') \in Tr, s \models v, s' \models w.
    trans_data = []

    for k, a in enumerate(actions):
        for x, v, w in a.transitions:
            if x.symbol.codomain == lang.Object:
                trans_data += [
                    {"a": k,
                     "x": X.get_index(symref(x)),
                     "v": D.get_index(symref(v)),
                     "w": D.get_index(symref(w))}
                ]
            elif x.symbol.codomain == lang.Integer:
                trans_data += [
                    {"a": k,
                     "x": X.get_index(symref(x)),
                     "v": v.symbol,
                     "w": w.symbol}
                ]
    # We provide the definitions of initial and goal states as lists of pairs of indices into the
    # set of variables and values in the domain D.
    init_data = []

    for x, v in initial:
        if isinstance(v, int):
            init_data += [[X.get_index(symref(x)), v]]
        else:
            init_data += [[X.get_index(symref(x)), D.get_index(symref(v))]]

    goal_data = []
    for x, v in goal:
        if isinstance(v, int):
            goal_data += [[X.get_index(symref(x)), v]]
        else:
            goal_data += [[X.get_index(symref(x)), D.get_index(symref(v))]]

    # Now we put all the instance data together and build the JSON document
    doc = {
        "metadata": {
            "domain": lang.name,
            "instance": name
        },
        "types": types_data,
        "vars": vars_data,
        "actions": action_names,
        "trans": trans_data,
        "init": init_data,
        "goal": goal_data
    }

    json.dump(doc, fp, indent=4)
