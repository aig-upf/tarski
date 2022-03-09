# ----------------------------------------------------------------------------------------------------------------------
# examples/sas_without_pddl/__main__.py
#
# In this example we construct a sas instance programmatically and write it in a JSON document which can then be
# transformed or loaded by a backend planner.
#
# Extensive inline comments explain the code as we go.
# ----------------------------------------------------------------------------------------------------------------------

import os
from argparse import ArgumentParser, Namespace
from collections import namedtuple
from itertools import product
from tarski.evaluators.simple import evaluate

import tarski
import tarski.model

from tarski.syntax import symref
from tarski.theories import Theory
from tarski.syntax.transform.substitutions import substitute_expression, create_substitution
from tarski.util import SymbolIndex

Schema = namedtuple('Schema', ['name', 'variables', 'constraints', 'transitions'])
Action = namedtuple('Action', ['name', 'arguments', 'transitions'])


def process_command_line():
    parser = ArgumentParser(description="Example illustrating acquisition of instance data from PDDL")
    parser.add_argument("--instance", dest='instance', default='4-0')
    parser.add_argument("--verbose", dest='verbose', action='store_true')
    opt = parser.parse_args()
    return opt


def check_constraints(C, s, subst):
    return all([s[substitute_expression(c, subst)] for c in C])


def ground_action_schemas(lang, schemas):

    actions = []
    s = tarski.model.create(lang)
    s.evaluator = evaluate

    for sch in schemas:
        sch_x = [entry[0] for entry in sch.variables]
        sch_D = [entry[1] for entry in sch.variables]

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

    return actions


def main(opt: Namespace):

    lang = tarski.language("blocksworld", theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    object_type = lang.get('object')

    blocks = [lang.constant(obj, object_type) for obj in ['A', 'B', 'C', 'D']]
    table = lang.constant('table', object_type)
    nothing = lang.constant('nothing', object_type)

    on = lang.function('on', object_type, object_type)
    below = lang.function('below', object_type, object_type)
    holding = lang.function('holding', object_type)

    # We define SAS action schemas in a very straightforward way
    target = lang.variable('x', object_type)
    pickup = Schema(name='pickup',
                    variables=[(target, blocks)],
                    constraints=[],
                    transitions=[
                        (holding(), nothing, target),
                        (on(target), nothing, nothing),
                        (below(target), table, nothing)
                    ])

    putdown = Schema(name='putdown',
                     variables=[(target, blocks)],
                     constraints=[],
                     transitions=[
                         (holding(), target, nothing),
                         (below(target), nothing, table)
                     ])

    target2 = lang.variable('y', object_type)
    stack = Schema(name='stack',
                   variables=[(target, blocks), (target2, blocks)],
                   constraints=[target != target2],
                   transitions=[
                       (holding(), target, nothing),
                       (on(target2), nothing, target),
                       (below(target), nothing, target2)
                   ])

    unstack = Schema(name='unstack',
                     variables=[(target, blocks), (target2, blocks)],
                     constraints=[target != target2],
                     transitions=[
                         (holding(), nothing, target),
                         (on(target2), target, nothing),
                         (below(target), target2, nothing)
                     ])

    actions = ground_action_schemas(lang, [pickup, putdown, stack, unstack])

    A, B, C, D = blocks

    initial = [
        (on(C), nothing),
        (on(A), nothing),
        (on(B), nothing),
        (on(D), nothing),
        (below(C), table),
        (below(A), table),
        (below(B), table),
        (below(D), table),
        (holding(), nothing)
    ]

    # we could also have the goal
    goal = [
        (on(D), C),
        (on(C), B),
        (on(B), A)
    ]

    print("Ground actions generated:", len(actions))

    X = SymbolIndex()
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

    print("State variables:", len(X))

    D = SymbolIndex()
    D.add(symref(nothing))
    D.add(symref(table))
    for b in blocks:
        D.add(symref(b))

    for k, a in enumerate(actions):
        for x, v, w in a.transitions:
            #print(k, x, v, w)
            #print(k, type(x), type(v), type(w))
            print(k, X.get_index(symref(x)), D.get_index(symref(v)), D.get_index(symref(w)))

    for x, v in initial:
        print(X.get_index(symref(x)), D.get_index(symref(v)))

    for x, v in goal:
        print(X.get_index(symref(x)), D.get_index(symref(v)))


if __name__ == '__main__':
    opt = process_command_line()
    main(opt)