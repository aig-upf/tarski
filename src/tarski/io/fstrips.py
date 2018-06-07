import logging

from ..fstrips import Problem

from ._fstrips.reader import FStripsParser


class FstripsReader(object):

    def __init__(self, raise_on_error=False, theories=None):
        self.problem = Problem()
        self.parser = FStripsParser(self.problem, raise_on_error, theories)

    def read_problem(self, domain, instance):
        self.parse_domain(domain)
        self.parse_instance(instance)
        return self.problem

    def parse_file(self, filename, start_rule):
        logging.info('Parsing filename "{}" from grammar rule "{}"'.format(filename, start_rule))
        domain_parse_tree, _ = self.parser.parse_file(filename, start_rule)
        logging.info("Processing AST")
        self.parser.visit(domain_parse_tree)

    def parse_domain(self, filename):
        self.parse_file(filename, 'domain')

    def parse_instance(self, filename):
        self.parse_file(filename, 'problem')

    def parse_string(self, string, start_rule):
        logging.info('Parsing custom string from grammar rule "{}"'.format(start_rule))
        parse_tree, _ = self.parser.parse_string(string, start_rule)
        logging.info("Processing AST")
        return self.parser.visit(parse_tree)


class FstripsWriter(object):

    def __init__(self, filename):
        self.filename = filename

    def write(self, element):
        raise RuntimeError("Unimplemented")


