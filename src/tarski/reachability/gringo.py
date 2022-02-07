#!/usr/bin/env python3
import sys
from clingo.application import Application, clingo_main

"""
A wrapper to emulate the default clingo app behavior
"""
class WrapperClingo(Application):
    def __init__(self, name):
        self.program_name = name

    def main(self, ctl, files):
        """
        The default implementation from clingo documentation
        Note- main(...) must be implemented
        """
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground([("base", [])])
        ctl.solve()

"""
run the clingo application in the default gringo mode
"""
clingo_main(WrapperClingo("gringo"), ["--mode", "gringo"]+sys.argv[1:])