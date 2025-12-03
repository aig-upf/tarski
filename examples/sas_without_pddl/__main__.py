# ----------------------------------------------------------------------------------------------------------------------
# examples/sas_without_pddl/__main__.py
#
# In this example we construct a sas instance programmatically and write it in a JSON document which can then be
# transformed or loaded by a backend planner.
#
# Extensive inline comments explain the code as we go.
# ----------------------------------------------------------------------------------------------------------------------

import json
from argparse import ArgumentParser, Namespace
from collections import namedtuple
from itertools import product
from tarski.evaluators.simple import evaluate

import tarski
import tarski.model

from tarski.syntax import symref
from tarski.theories import Theory
from tarski.syntax.transform.substitutions import substitute_expression, create_substitution

from tarski.sas import Action, Schema

from tarski.util import SymbolIndex


def process_command_line():
    parser = ArgumentParser(description="Example illustrating acquisition of instance data from PDDL")
    parser.add_argument("--instance", dest='instance', default='4-0')
    parser.add_argument("--verbose", dest='verbose', action='store_true')
    opt = parser.parse_args()
    return opt


def check_constraints(C, s, subst):
    """
    Returns true if s \models C[x/subst(x)], that is, the result of replacing every variable symbol x by
    subst(x) in C is satisfiable under s.
    :param C: A constraint (predicate)
    :param s: A semantic structure (model) object
    :param subst: A mapping of variable symbols in C to constants
    :return:
    """
    return all([s[substitute_expression(c, subst)] for c in C])


def ground_action_schemas(lang, schemas):
    """
    Straightforward grounding by enumeration
    :param lang: domain theory
    :param schemas: action schemas to be enumerated
    :return:
    """

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



def dump(lang, actions, initial, goal, objects, fp):
    """
    Serializes instance elements (domain theory, actions, initial state and goal condition) into a JSON
    formatted stream.

    :param lang: Domain theory
    :param actions: List of ground actions
    :param init: Initial state, a list of equality literals, given as pairs of terms
    (symbol of the form $x(\bar{a})$) and values v (constant symbols)
    :param goal: Goal state, a list of equality literals, given as pairs of term (as above) and values v (as above)
    :param fp:
    :return:
    """

    # `SymbolIndex` is a container class that allows to define a set of objects, where each element is indexed
    X = SymbolIndex()

    # We identify the set of terms by inspecting 1) action transition constraints, 2) the definition of the
    # initial state, and 3) the structure of the (conjunctive) goal3 formula.
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
            trans_data += [
                {"a": k,
                 "x": X.get_index(symref(x)),
                 "v": D.get_index(symref(v)),
                 "w": D.get_index(symref(w))}
            ]

    # We provide the definitions of initial and goal states as lists of pairs of indices into the
    # set of variables and values in the domain D.
    init_data = [[X.get_index(symref(x)), D.get_index(symref(v))] for x, v in initial]

    goal_data = [[X.get_index(symref(x)), D.get_index(symref(v))] for x, v in goal]

    # Now we put all the instance data together and build the JSON document
    doc = {
        "metadata": {
            "domain": "blocksworld",
            "instance": "probBLOCKS-4-0"
        },
        "types": types_data,
        "vars": vars_data,
        "actions": action_names,
        "trans": trans_data,
        "init": init_data,
        "goal": goal_data
    }

    json.dump(doc, fp, indent=4)


def main(opt: Namespace):

    # We start by creating an instance of the `FirstOrderLanguage` class, that represents
    # the domain theory for blocksworld.
    lang = tarski.language("blocksworld", theories=[Theory.EQUALITY])

    # Built-in sorts (`Object`, `Integer`, `Real`) can be accessed via the corresponding
    # attribute of the domain theory instance
    object_type = lang.Object

    # We define the `domain` objects, objects that are relevant to every instance of blocksworld
    # planning problems. Note that we model as objects the table/surface, where blocks can stand
    # on, and 'nothing' becomes an object too.
    table = lang.constant('table', object_type)
    nothing = lang.constant('nothing', object_type)

    # We define `instance` objects (blocks), that is the objects which are associated with a strict
    # subset of the set of possible blocksworld instances.
    blocks = [lang.constant(obj, object_type) for obj in ['A', 'B', 'C', 'D']]

    # We factorise the state space of blocksworld with three functions that relate objects
    # on(x) -> y, what object y is on top of x
    on = lang.function('on', object_type, object_type)
    # below(x) -> y, what object y is below x
    below = lang.function('below', object_type, object_type)
    # holding() -> x, what object x is being held by the manipulator
    holding = lang.function('holding', object_type)

    # We define SAS action schemas in a very straightforward way. We define a first order variable
    # symbol, `target`, to represent the target object of the action `pickup`
    target = lang.variable('x', object_type)

    # The schema for `pickup` is parametrized by target, which can take as a value any element of the
    # set `blocks`. The transitions associated with this action refer to three variables, and for
    # every s, pickup(target), s' it must hold that"
    # 1) s \models holding() = nothing, s' \models holding() = target
    # 2) s \models on(target) = nothing, s' \models on(target) = nothing
    # 3) s \models below(target) = table, s' \models below(target) = nothing
    pickup = Schema(name='pickup',
                    variables=[(target, blocks)],
                    constraints=[],
                    transitions=[
                        (holding(), nothing, target),
                        (on(target), nothing, nothing),
                        (below(target), table, nothing)
                    ])

    # The schema for `putdown` is also parametrized by target, which can take any value from the
    # set `blocks`. Transitions associated with `putdown` refer to three variables, so that for
    # every s, putdown(target), s' it must hold that:
    # 1) s \models holding() = target, s' \models holding() = nothing
    # 2) s \models on(target) = nothing, s' \models on(target) = nothing
    # 3) s \models below(target) = nothing, s' \models below(target) = table
    putdown = Schema(name='putdown',
                     variables=[(target, blocks)],
                     constraints=[],
                     transitions=[
                         (holding(), target, nothing),
                         (on(target), nothing, nothing),
                         (below(target), nothing, table)
                     ])

    # The schema for `stack` is parametrized by `target` and `target2` FO-variables, both taking
    # values from the set 'blocks'. The schema constraints require that `target` and `target2` are
    # different. The transitions associated with `stack` are such that:
    # 1) s \models holding() = target, s' \models holding() = nothing
    # 2) s \models on(target2) = nothing, s' \models on(target2) = target
    # 3) s \models below(target) = nothing, s' \models below(target) = target2
    target2 = lang.variable('y', object_type)
    stack = Schema(name='stack',
                   variables=[(target, blocks), (target2, blocks)],
                   constraints=[target != target2],
                   transitions=[
                       (holding(), target, nothing),
                       (on(target2), nothing, target),
                       (below(target), nothing, target2)
                   ])

    # The schema for `unstack` is parametrized by `target` and `target2` FO-variables too, that can take
    # values from the set 'blocks'. As with `stack`, the schema constraints require that `target` and `target2` are
    # different. The transitions associated with `unstack` are such that:
    # 1) s \models holding() = nothing, s' \models holding() = target
    # 2) s \models on(target2) = target, s' \models on(target2) = nothing
    # 3) s \models below(target) = target2, s' \models below(target) = nothing
    unstack = Schema(name='unstack',
                     variables=[(target, blocks), (target2, blocks)],
                     constraints=[target != target2],
                     transitions=[
                         (holding(), nothing, target),
                         (on(target2), target, nothing),
                         (below(target), target2, nothing)
                     ])

    # Once the schemas are defined, we ground them
    actions = ground_action_schemas(lang, [pickup, putdown, stack, unstack])

    # We unpack the elements of blocks for convenience
    A, B, C, D = blocks

    # We define the initial state
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

    # and the goal
    goal = [
        (on(C), D),
        (on(B), C),
        (on(A), B)
    ]

    print("Ground actions generated:", len(actions))

    # we group together all the instance objects
    objects = blocks + [table] + [nothing]

    # and we store the result in a JSON document
    with open("probBLOCKS-4-0.json", "w") as output:
        dump(lang, actions, initial, goal, objects, output)


if __name__ == '__main__':
    opt = process_command_line()
    main(opt)
