# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez (miquel.ramirez@pm.me)
# ----------------------------------------------------------------------------------------------------------------------
# io/pddl/errors.py
#
# PDDL parser
# ----------------------------------------------------------------------------------------------------------------------

class SemanticError(Exception):

    def __init__(self, line, msg):
        super().__init__(msg)
        self.line = line
        self.msg = msg

    def __str__(self):
        return "Semantic Error: Line {}: {}".format(self.line, self.msg)


class ParseError(Exception):

    def __init__(self, line, msg):
        super().__init__(msg)
        self.line = line
        self.msg = msg

    def __str__(self):
        return "Parse Error: Line {}: {}".format(self.line, self.msg)


class UnsupportedFeature(Exception):

    def __init__(self, line, msg):
        super().__init__(msg)
        self.line = line
        self.msg = msg

    def __str__(self):
        return "Unsupported PDDL feature: Line {}: {}".format(self.line, self.msg)
