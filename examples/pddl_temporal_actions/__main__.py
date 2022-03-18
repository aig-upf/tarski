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

from tarski.io.pddl import Features
from tarski.io.pddl.parser import PDDLparser, UnsupportedFeature
from tarski.syntax.visitors import CollectEqualityAtoms

def process_command_line():
    parser = ArgumentParser(description="Example illustrating acquisition of instance data from PDDL")
    parser.add_argument("--domain", dest='domain_file', type=str, default='data/pddl/temporal/elevators/p01-domain.pddl')
    parser.add_argument("--problem", dest='problem_file', type=str, default='data/pddl/temporal/elevators/p01.pddl')
    parser.add_argument("--verbose", dest='verbose', action='store_true')
    opt = parser.parse_args()
    return opt


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

        assert parser.domain_name == 'foo'
        assert parser.problem_name == 'instance_001'
        assert Features.DURATIVE_ACTIONS in parser.required_features
        assert Features.TYPING in parser.required_features

        instance = parser.instance
        assert instance is not None

        print("Functions", len(instance.functions))
        print("Predicates", len(instance.predicates))
        print("Types", len(instance.types))
        print("Constants", len(instance.constants))
        print("Actions: instantaneous: {} durative: {}".format(len(instance.actions), len(instance.durative)))
        print("Derived predicates:", len(instance.derived))
        print("Initial State literals", len(instance.init))

        eq_atoms_visitor = CollectEqualityAtoms()
        eq_atoms_visitor.visit(instance.goal)
        goal_atoms = eq_atoms_visitor.atoms
        print("Goal literals", len(goal_atoms))


if __name__ == '__main__':
    main(process_command_line())