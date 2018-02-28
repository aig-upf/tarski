
from ..fstrips import Problem
from .. import fol

from ._fstrips.reader import FStripsParser


class FstripsReader(object):

    def __init__(self, domain, instance):
        self.domain = domain
        self.instance = instance
        self.problem = Problem()
        self.problem.language = fol.language()

    def read(self):
        parser = FStripsParser(self.problem)

        print("Parsing domain description...")
        _, domain_parse_tree = parser.parse(self.domain)
        print("Processing domain AST...")
        parser.visit(domain_parse_tree)

        print("Parsing problem description...")
        _, instance_parse_tree = parser.parse(self.instance)
        print("Processing instance AST...")
        parser.visit(instance_parse_tree)

        return self.problem


class FstripsWriter(object):

    def __init__(self, filename):
        self.filename = filename

    def write(self, element):
        raise RuntimeError("Unimplemented")


