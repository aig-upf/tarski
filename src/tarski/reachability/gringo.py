#!/usr/bin/env python3
import sys
from typing import Sequence

from clingo import Control
from clingo.application import Application, clingo_main  # type: ignore


class WrapperClingo(Application):
    """
    A wrapper to emulate the default clingo app behavior
    """
    def __init__(self, name):
        self.program_name = name

    def main(self, control: Control, files: Sequence[str]) -> None:
        """
        The default implementation from clingo documentation
        Note- main(...) must be implemented
        """
        for f in files:
            control.load(f)
        if not files:
            control.load("-")
        control.ground([("base", [])])
        control.solve()


# run the clingo application in the default gringo mode
clingo_main(WrapperClingo("gringo"), ["--mode", "gringo"] + sys.argv[1:])
