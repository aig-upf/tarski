from tarski.errors import UndefinedSort, UndefinedPredicate
from tarski.fstrips import AddEffect, FunctionalEffect
from tarski.fstrips.errors import InvalidEffectError
from tarski.io.fstrips import ParsingError, FstripsReader
from tarski.syntax import Atom, CompoundFormula, Tautology
from tarski.syntax.util import get_symbols
from tarski.theories import Theory


def reader(theories=None, strict_with_requirements=True, case_insensitive=False):
    """ Return a reader configured to raise exceptions on syntax errors """
    return FstripsReader(raise_on_error=True, theories=theories,
                         strict_with_requirements=strict_with_requirements,
                         case_insensitive=case_insensitive)


def main():
    # We create a `FstripsReader` object to parse the input PDDL
    parser = reader()

    instance_ast = None
    # We locate the input pddl files for the domain and the instance data
    domain_path = 'data/fstrips/exists_precs/logistics-domain-exists.pddl'
    instance_path = 'data/fstrips/exists_precs/logistics-problem.pddl'
    instance_ast = parser.read_problem(domain_path, instance_path)

    if not instance_ast:
        raise SystemExit("Parsing failed! Check expected PDDL paths ")


if __name__ == '__main__':
    main()