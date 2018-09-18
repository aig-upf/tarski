"""
    RDDL model acquisition module
"""
import tarski
from tarski.syntax import *
from tarski.theories import Theory
import pyrddl


class Reader(object):
    """
        Reader creates a FOL and several language components
        that specify a RDDL task
    """
    def __init__(self, filename):
        self.language = None
        self.rddl_model = self._load_rddl_model(filename)        

    def _load_rddl_model(self, filename):
        with open(filename, 'r') as input_file:
            rddl = input_file.read()
        parser = pyrddl.Parser()
        parser.build()
        # parse RDDL
        return parser.parse(rddl)

class Writer(object):
    """
        Writer compiles the specification of a planning task
        into RDDL
    """
    def __init__(self, task):
        pass
