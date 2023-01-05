# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# tarski/examples/pddl_temporal_actions/__main__.py
#
# Example illustrating parsing and basic processing of PDDL 2.1 features for modeling temporal planning problems
# ----------------------------------------------------------------------------------------------------------------------

import os
import tempfile
from argparse import ArgumentParser, Namespace

from tarski.errors import UndefinedTerm
from tarski.grounding import LPGroundingStrategy
from tarski.io.pddl import Features
from tarski.io.pddl.instance import InstanceModel, AssignmentEffectData, DurativeActionData, EventData
from tarski.io.pddl.parser import PDDLparser, UnsupportedFeature
from tarski.syntax.visitors import CollectEqualityAtoms
from tarski.syntax.transform.substitutions import create_substitution, substitute_expression


def process_command_line():
    parser = ArgumentParser(description="Example illustrating acquisition of instance data from PDDL")
    parser.add_argument("--domain", dest='domain_file', type=str, default='data/pddl/temporal/elevators/p01-domain.pddl')
    parser.add_argument("--problem", dest='problem_file', type=str, default='data/pddl/temporal/elevators/p01.pddl')
    parser.add_argument("--verbose", dest='verbose', action='store_true')
    opt = parser.parse_args()
    return opt


def calculate_groundings(instance: InstanceModel):
    """
    Grounds the given PDDL 2.1 instance
    :param instance:
    :return:
    """
    fs_counterpart = instance.compile_to_functional_strips()

    grounding = LPGroundingStrategy(fs_counterpart, relax_numeric_atoms=True)
    action_groundings = grounding.ground_actions()

    # We store in a dictionary the groundings
    temporal_action_groundings = {}
    for temp_action in instance.durative:

        for schema, assignments in action_groundings.items():
            if temp_action.name in schema:
                try:
                    if len(assignments) > len(temporal_action_groundings[temp_action.name]):
                        temporal_action_groundings[temp_action.name] = assignments
                except KeyError:
                    temporal_action_groundings[temp_action.name] = assignments

    return temporal_action_groundings


def ground_durative_actions(instance: InstanceModel, groundings):
    """
    Returns list of (ground) durative actions
    :param instance:
    :param groundings:
    :return:
    """
    actions = []

    for temp_action in instance.durative:
        assignments = groundings[temp_action.name]
        for point in assignments:
            # MRJ: note that the assignments are just constant names!
            point = [instance.L.get(elem) for elem in point]
            subst = create_substitution(temp_action.parameters, point)

            at_start_pre = [substitute_expression(atom.expr, subst) for atom in temp_action.at_start.pre]
            at_start_post = []
            for eff in temp_action.at_start.post:
                g_eff_lhs = substitute_expression(eff.lhs, subst)
                if isinstance(eff.rhs, (int, float)):
                    g_eff_rhs = eff.rhs
                else:
                    g_eff_rhs = substitute_expression(eff.rhs, subst)
                at_start_post += [AssignmentEffectData(g_eff_lhs, g_eff_rhs)]

            at_end_pre = [substitute_expression(atom.expr, subst) for atom in temp_action.at_end.pre]
            at_end_post = []
            for eff in temp_action.at_end.post:
                g_eff_lhs = substitute_expression(eff.lhs, subst)
                if isinstance(eff.rhs, (int, float)):
                    g_eff_rhs = eff.rhs
                else:
                    g_eff_rhs = substitute_expression(eff.rhs, subst)
                at_end_post += [AssignmentEffectData(g_eff_lhs, g_eff_rhs)]

            overall = [substitute_expression(atom.expr, subst) for atom in temp_action.overall]
            duration = substitute_expression(temp_action.duration, subst)

            actions += [DurativeActionData(name=temp_action.name,
                                           parameters=point,
                                           at_start=EventData(pre=at_start_pre, post=at_start_post),
                                           at_end=EventData(pre=at_end_pre, post=at_end_post),
                                           overall=overall,
                                           duration=duration)]
    return actions


def main(opt: Namespace):
    parser = PDDLparser(debug=True)

    with tempfile.NamedTemporaryFile() as f:
        parser.build(logfile=f.name)

        pddl_data = ""
        with open(opt.domain_file) as instream:
            pddl_data += instream.read()
        with open(opt.problem_file) as instream:
            pddl_data += instream.read()

        parser.parse(pddl_data)

        assert parser.instance.domain_name == 'elevators-time-numeric'
        assert parser.instance.instance_name == 'elevators-time-p8_4_1'
        assert Features.DURATIVE_ACTIONS in parser.required_features
        assert Features.TYPING in parser.required_features

        instance = parser.instance
        assert instance is not None

        # Now we inspect the PDDL types defined in the domain, and for each of these
        # what objects were defined in the domain as "constants", or in the problem file as "objects"
        print("PDDL Types", len(instance.types))

        for t in instance.types:
            pddl_type = instance.L.get(t)
            if pddl_type.builtin:
                print("\t{} [Built-in Type]".format(pddl_type.name))
                continue
            print("\t{} Domain:".format(pddl_type.name))
            print("\t\t{}".format(', '.join([str(obj) for obj in pddl_type.domain()])))

        # The attribute `Instance.functions` is a List[str] object with the names of every
        # function defined in the PDDL domain. `total-time` does not appear here because it is
        # not an actual function (as in being a symbol we can obtain an interpretation from a state).
        print("Functions", len(instance.functions))

        for f in instance.functions:
            func = instance.L.get(f)
            print('\t{}: ({}) -> {}'.format(func, ', '.join([str(s) for s in func.domain]), func.codomain))

        # Similarly, `Instance.predicates` is a List[str] object with the names of every predicate
        # defined in the PDDL domain. Predicates are modelled as functions mapping to the Booleans {0, 1}.
        print("Predicates", len(instance.predicates))

        for p in instance.predicates:
            pred = instance.L.get(p)
            print('\t{} \in ({})'.format(pred, ' x '.join([str(s) for s in pred.domain])))

        # The constants (terms) defined in the domain and problem definitions can be also accessed directly
        # with the interface below
        print("Domains", len(instance.domains))

        # Instance.domains is a Dictionary[Sort, List[Constant]] object
        for t, D in instance.domains.items():
            obj = instance.L.get(t)
            dom = [str(obj) for obj in D]
            print('\t{}: {}'.format(str(obj), ', '.join(dom)))

        # The durative actions in the domain are stored in the `Instance.durative` attribute
        print("Actions: durative: {}".format(len(instance.durative)))

        # For each action
        for act in instance.durative:
            # we have its name
            print("\tname: {}".format(act.name))
            # its parameters as a List[Variable] object
            print("\tparameters: {}".format(act.parameters))
            # and its duration
            print("\tduration: {}".format(act.duration))
            # the preconditions and effects of the `start` event
            print("\tstart:")
            # preconditions are given as lists of equality literals
            print("\t\tprecondition:", ', '.join([str(p.expr) for p in act.at_start.pre]))
            print("\t\teffects:")
            for eff in act.at_start.post:
                print("\t\t\t{} := {}".format(eff.lhs, eff.rhs))

            print("\t\toverall:", ', '.join([str(o.expr) for o in act.overall]))

            print("\tend:")
            # preconditions are given as lists of equality literals
            print("\t\tprecondition:", ', '.join([str(p.expr) for p in act.at_end.pre]))
            print("\t\teffects:")
            for eff in act.at_end.post:
                print("\t\t\t{} := {}".format(eff.lhs, eff.rhs))

        # The initial state is given as a set of tuple of CompoundTerm and a value that can be Boolean or
        # `number`
        print("Some facts about the initial state:")
        for l in instance.init.as_atoms():
            print('\t{}'.format(l))

        eq_atoms_visitor = CollectEqualityAtoms()
        eq_atoms_visitor.visit(instance.goal)
        goal_atoms = eq_atoms_visitor.atoms
        print("Goal literals", len(goal_atoms))

        for l in goal_atoms:
            print('\t{}'.format(l))

        print("Grounding")
        temporal_action_groundings = calculate_groundings(instance)
        ground_action_count = 0
        for schema, assignments in temporal_action_groundings.items():
            print('\t', schema, len(assignments))
            #for a in assignments:
            #    print('\t\t', a)
            ground_action_count += len(assignments)
        print("Ground actions", ground_action_count)

        grounded_actions = ground_durative_actions(instance, temporal_action_groundings)

        print("Static evaluation of duration expressions")
        valid_grounded_actions = []
        invalid_grounded_actions = 0
        for act in grounded_actions:
            try:
                valid_grounded_actions += [DurativeActionData(name=act.name,
                                                              parameters=act.parameters,
                                                              at_start=act.at_start,
                                                              at_end=act.at_end,
                                                              overall=act.overall,
                                                              duration=instance.init[act.duration])]
            except UndefinedTerm:
                invalid_grounded_actions += 1

        for act in valid_grounded_actions:
            print("{}({})".format(act.name, ','.join([str(x) for x in act.parameters])))
            print("\tAt Start")
            print("\t\tPre")
            print("\t\t\t{}".format(act.at_start.pre))
            print("\t\tPost")
            for eff in act.at_start.post:
                print("\t\t\t{}' = {}".format(eff.lhs, eff.rhs))
            print("\tAt End")
            print("\t\tPre")
            print("\t\t\t{}".format(act.at_end.pre))
            print("\t\tPost")
            for eff in act.at_end.post:
                print("\t\t\t{}' = {}".format(eff.lhs, eff.rhs))
            print("\tOverall")
            print("\t\t{}".format(act.overall))
            print("\tDuration")
            print("\t\t{}".format(act.duration))

        print("Valid grounded actions", len(valid_grounded_actions))
        print("Invalid grounded actions", invalid_grounded_actions)

if __name__ == '__main__':
    main(process_command_line())