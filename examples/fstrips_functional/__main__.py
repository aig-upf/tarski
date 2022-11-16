"""
    Functional STRIPS features showcase
"""

from argparse import ArgumentParser, Namespace

from tarski.errors import UndefinedSort, UndefinedPredicate
from tarski.fstrips import AddEffect, FunctionalEffect
from tarski.fstrips.errors import InvalidEffectError
from tarski.io.fstrips import ParsingError, FstripsReader
from tarski.syntax import Atom, CompoundFormula, Tautology
from tarski.syntax.util import get_symbols
from tarski.theories import Theory


def parse_options():

    parser = ArgumentParser(description="Example illustrating acquisition of expressive FSTRIPS Models")
    parser.add_argument("--domain", dest='domain_file', type=str, default=None)
    parser.add_argument("--instance", dest='problem_file', type=str, default=None)
    parser.add_argument("--verbose", dest='verbose', action='store_true')
    opt = parser.parse_args()
    return opt


def reader(theories=None, strict_with_requirements=True, case_insensitive=False):
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True, theories=theories,
                         strict_with_requirements=strict_with_requirements,
                         case_insensitive=case_insensitive)


def main(opt: Namespace):
    # We create a `FstripsReader` object to parse the input PDDL
    parser = reader()

    instance_ast = None
    # We locate the input pddl files for the domain and the instance data
    instance_ast = parser.read_problem(opt.domain_file, opt.problem_file)

    if not instance_ast:
        raise SystemExit("Parsing failed! Check expected PDDL paths ")


if __name__ == '__main__':
    main(parse_options())