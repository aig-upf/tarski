#
# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez <miquel.ramirez@pm.me>
# ----------------------------------------------------------------------------------------------------------------------
# examples/pddl_derived_predicates/__main__.py
#
# Example documenting the use of Tarski to acquire a planning instance from a PDDL description that contains derived
# predicates. Extensive inline comments are provided to explain what are the steps involved and what design decisions
# need to be made by Tarski's users.
# ----------------------------------------------------------------------------------------------------------------------

import os
from argparse import ArgumentParser, Namespace

from tarski.io.pddl.parser import PDDLparser, UnsupportedFeature
from tarski.syntax.visitors import CollectEqualityAtoms

def process_command_line():
    parser = ArgumentParser(description="Example illustrating acquisition of instance data from PDDL")
    parser.add_argument("--domain", dest='domain_file', type=str, default='data/pddl/derived_predicates/min_cut/domain.pddl')
    parser.add_argument("--problem", dest='problem_file', type=str, default='data/pddl/derived_predicates/min_cut/p00.pddl')
    parser.add_argument("--verbose", dest='verbose', action='store_true')
    opt = parser.parse_args()
    return opt


def main(opt: Namespace):

    # By default the example processes the instance due to Ivankovid and Haslum in the directory
    # `examples/data/pddl/derived_predicates/min_cut`. Feel free to experiment with other PDDL specifications
    # specifying the domain and problem files via the command line.
    print("Domain file:", opt.domain_file)
    print("Problem file:", opt.problem_file)

    # The very first step is to obtain a `PDDLParser` instance. Turn the argument to `True` if you want to
    # see a trace of the work done by the parser
    parser = PDDLparser(debug=False)

    # Setting up the parser is a two-step process, as it is required to invoke the `build()` method to
    # set internal data structures and other parameters (such a log file to store error messages etc.).
    parser.build(logfile="pddl_derived_predicates.parse.log")

    # Now we acquire the text of the pddl domain file and parse it
    with open(opt.domain_file) as instream:
        parser.parse(instream.read())

    # and the problem file
    with open(opt.problem_file) as instream:
        parser.parse(instream.read())

    # We note that domain and problem sections of a PDDL specification can be combined into one
    # single file/stream, or directly from a memory buffer, as it best suits. Whatever the modality,
    # the domain file needs to be parsed first always.

    # once parsed correctly, we can then access the structural elements of the instance (e.g. types,
    # predicates, etc.)
    instance_data = parser.instance

    # constants are grouped per type
    total_constants = 0
    print("Objects (constant symbols) found in the instance:")
    for typename, constant_list in instance_data.domains.items():
        print("Type:", typename, "# constants:", len(constant_list))
        total_constants += len(constant_list)
    print("Total constants (objects) in instance:", total_constants)

    print("instance data:")
    print("# types:", len(instance_data.types))
    print("# constants:", total_constants)
    print("# predicates:", len(instance_data.predicates))
    print("# functions:", len(instance_data.functions))
    print("# instantaneous actions:", len(instance_data.actions))
    print("# durative actions:", len(instance_data.durative))
    print("# derived predicates:", len(instance_data.derived))

    # In this example, we use the instance data to "fill in" an instance of the class `Problem` of
    # the `fstrips` module, which can then be grounded with the provided grounding algorithms (see
    # modules `tarski.grounding.lp_grounding` and `tarski.grounding.naive_grounding`.

    # TBC




if __name__ == '__main__':
    opt = process_command_line()
    main(opt)