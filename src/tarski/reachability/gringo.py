#!/usr/bin/env python3
import sys

try:
    from clingo.application import Application, clingo_main  # type: ignore
except ModuleNotFoundError:
    print("Clingo not installed")
    sys.exit(-1)


class WrapperClingo(Application):
    """
    A wrapper to emulate the default clingo app behavior
    """
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


# run the clingo application in the default gringo mode
clingo_main(WrapperClingo("gringo"), ["--mode", "gringo"] + sys.argv[1:])
