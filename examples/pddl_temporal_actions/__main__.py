# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# tarski/examples/pddl_temporal_actions/__main__.py
#
# Example illustrating parsing and basic processing of PDDL 2.1 features for modeling temporal planning problems
# ----------------------------------------------------------------------------------------------------------------------

import tempfile
from argparse import ArgumentParser, Namespace

from tarski.io.pddl import Features
from tarski.io.pddl.parser import PDDLparser
from tarski.syntax.visitors import CollectEqualityAtoms


def process_command_line():
    parser = ArgumentParser(description="Example illustrating acquisition of instance data from PDDL")
    parser.add_argument(
        "--domain", dest="domain_file", type=str, default="data/pddl/temporal/elevators/p01-domain.pddl"
    )
    parser.add_argument("--problem", dest="problem_file", type=str, default="data/pddl/temporal/elevators/p01.pddl")
    parser.add_argument("--verbose", dest="verbose", action="store_true")
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

        assert parser.domain_name == "elevators-time-numeric"
        assert parser.problem_name == "elevators-time-p8_4_1"
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
                print(f"\t{pddl_type.name} [Built-in Type]")
                continue
            print(f"\t{pddl_type.name} Domain:")
            print("\t\t{}".format(", ".join([str(obj) for obj in pddl_type.domain()])))

        # The attribute `Instance.functions` is a List[str] object with the names of every
        # function defined in the PDDL domain. `total-time` does not appear here because it is
        # not an actual function (as in being a symbol we can obtain an interpretation from a state).
        print("Functions", len(instance.functions))

        for f in instance.functions:
            func = instance.L.get(f)
            print("\t{}: ({}) -> {}".format(func, ", ".join([str(s) for s in func.domain]), func.codomain))

        # Similarly, `Instance.predicates` is a List[str] object with the names of every predicate
        # defined in the PDDL domain. Predicates are modelled as functions mapping to the Booleans {0, 1}.
        print("Predicates", len(instance.predicates))

        for p in instance.predicates:
            pred = instance.L.get(p)
            print("\t{} \in ({})".format(pred, " x ".join([str(s) for s in pred.domain])))

        # The constants (terms) defined in the domain and problem definitions can be also accessed directly
        # with the interface below
        print("Domains", len(instance.domains))

        # Instance.domains is a Dictionary[Sort, List[Constant]] object
        for t, D in instance.domains.items():
            obj = instance.L.get(t)
            dom = [str(obj) for obj in D]
            print("\t{}: {}".format(str(obj), ", ".join(dom)))

        # The durative actions in the domain are stored in the `Instance.durative` attribute
        print(f"Actions: durative: {len(instance.durative)}")

        # For each action
        for act in instance.durative:
            # we have its name
            print(f"\tname: {act.name}")
            # its parameters as a List[Variable] object
            print(f"\tparameters: {act.parameters}")
            # and its duration
            print(f"\tduration: {act.duration}")
            # the preconditions and effects of the `start` event
            print("\tstart:")
            # preconditions are given as lists of equality literals
            print("\t\tprecondition:", ", ".join([str(p.expr) for p in act.at_start.pre]))
            print("\t\teffects:")
            for eff in act.at_start.post:
                print(f"\t\t\t{eff.lhs} := {eff.rhs}")

            print("\t\toverall:", ", ".join([str(o.expr) for o in act.overall]))

            print("\tend:")
            # preconditions are given as lists of equality literals
            print("\t\tprecondition:", ", ".join([str(p.expr) for p in act.at_end.pre]))
            print("\t\teffects:")
            for eff in act.at_end.post:
                print(f"\t\t\t{eff.lhs} := {eff.rhs}")

        print("Initial State literals", len(instance.init))
        # The initial state is given as a set of tuple of CompoundTerm and a value that can be Boolean or
        # `number`
        for l in instance.init:
            print(f"\t{l}")

        eq_atoms_visitor = CollectEqualityAtoms()
        eq_atoms_visitor.visit(instance.goal)
        goal_atoms = eq_atoms_visitor.atoms
        print("Goal literals", len(goal_atoms))

        for l in goal_atoms:
            print(f"\t{l}")


if __name__ == "__main__":
    main(process_command_line())
