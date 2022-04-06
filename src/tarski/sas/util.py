# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# tarski/sas/utility.py
#
# Utility method to process SAS
# ----------------------------------------------------------------------------------------------------------------------
from itertools import product
import tarski.model
from tarski.evaluators.simple import evaluate
from tarski.syntax import symref
from tarski.theories import Theory
from tarski.syntax.transform.substitutions import substitute_expression, create_substitution

from tarski.sas import Action
from tarski.sas.temporal import TemporalAction


def check_constraints(C, s, subst):
    r"""
    Returns true if s \models C[x/subst(x)], that is, the result of replacing every variable symbol x by
    subst(x) in C is satisfiable under s.
    :param C: A constraint (predicate)
    :param s: A semantic structure (model) object
    :param subst: A mapping of variable symbols in C to constants
    :return:
    """
    return all([s[substitute_expression(c, subst)] for c in C])


def ground_action_schemas(lang, schemas, domains=None, sem_struct=None):
    """
    Straightforward grounding by enumeration
    :param lang: domain theory
    :param schemas: action schemas to be enumerated
    :param domains: table with variable symbols domains, or None if domains provided inline
    :param sem_struct: semantic structure to check the satisfiability of schema constraints, or None if all
    predicates in constraints are built-ins (e.g. relational operators, equality)
    :return:
    """

    actions = []
    if sem_struct is None:
        s = tarski.model.create(lang)
        s.evaluator = evaluate
    else:
        s = sem_struct

    for sch in schemas:
        sch_x = [entry[0] for entry in sch.variables]
        if domains is None:
            sch_D = [entry[1] for entry in sch.variables]
        else:
            sch_D = [domains[entry[1]] for entry in sch.variables]

        for a in product(*sch_D):
            subst = create_substitution(sch_x, a)
            if not check_constraints(sch.constraints, s, subst):
                continue

            action_a = Action(name=sch.name,
                              arguments=a,
                              transitions=[(substitute_expression(x, subst),
                                            substitute_expression(pre, subst),
                                            substitute_expression(post, subst)) for x, pre, post in sch.transitions])
            actions += [action_a]
            # print(action_a.name, a)

    return actions


def ground_temporal_action(lang, s, schema, domains=None):
    """
    Grounds temporal actions events
    :param lang:
    :param schema:
    :return:
    """
    # 1. consolidate schema variables and constraints
    X = set()
    D = {}
    for evt in schema.events:
        for x_e, D_x_e in evt.variables:
            if symref(x_e) in X:
                continue
            X.add(symref(x_e))
            D[symref(x_e)] = D_x_e

    sch_x = [x.expr for x in X]
    sch_D = [D[symref(x_k)] for x_k in sch_x]

    actions = []

    for a in product(*sch_D):
        subst = create_substitution(sch_x, a)
        ground_events = []
        for evt in schema.events:
            if not check_constraints(evt.constraints, s, subst):
                break
            ground_events += [
                Action(name=evt.name,
                       arguments=a,
                       transitions=[
                           (substitute_expression(x, subst),
                            substitute_expression(pre, subst),
                            substitute_expression(post, subst)) for x, pre, post in evt.transitions
                       ])
            ]
        if len(ground_events) != len(schema.events):
            # one event grounding failed due to constraints
            continue
        actions += [TemporalAction(
            name='{}({})'.format(schema.name, ','.join([str(c) for c in a])),
            events=[(schema.deltas[k], gnd_evt) for k, gnd_evt in enumerate(ground_events)])]

    return actions
