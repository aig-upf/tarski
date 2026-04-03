import logging
import os
import shutil
import sys
import tempfile
from collections import defaultdict
from importlib.util import find_spec
from pathlib import Path

from ..errors import ArgumentError, CommandNotFoundError, ExternalCommandError, OutOfMemoryError, OutOfTimeError
from ..utils import command as cmd


def get_gringo_command() -> list[str]:
    """Assemble the command to run gringo. First try to find a pip-installed gringo, then fall back to a system-wide
    gringo installation. Raise exception if no gringo is found.

    :return: A list with the command and arguments to invoke gringo.
    """
    if find_spec("clingo"):
        logging.debug("Using the clingo pypi bindings to emulate gringo binary")
        return [sys.executable, os.path.join(Path(__file__).parent.absolute(), "gringo.py")]

    gringo = shutil.which("gringo")
    if gringo is None:
        raise CommandNotFoundError("gringo")

    logging.debug(f'Using gringo binary found in "{gringo}"')
    return [gringo]


def run_clingo(lp):
    gringo_command = get_gringo_command()

    with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as f:
        _ = [print(str(r), file=f) for r in lp.rules]
        _ = [print(str(r), file=f) for r in lp.directives]
        theory_filename = f.name

    errlog = ""
    with (
        tempfile.NamedTemporaryFile(mode="w+t", delete=False) as f,
        tempfile.NamedTemporaryFile(mode="w+t", delete=False) as stderr,
    ):
        # Option "-t" enforces an easier-to-parse textual output. Warnings could also be supressed with
        # option "-Wno-atom-undefined"
        retcode = cmd.execute(gringo_command + ["--text", theory_filename], stdout=f, stderr=stderr)
        model_filename = f.name

        if retcode == 0:
            return model_filename, theory_filename

    if os.path.isfile(stderr.name):
        with open(stderr.name, encoding="utf8") as file:
            errlog = file.read()

    if "std::bad_alloc" in errlog:
        raise OutOfMemoryError(f"Gringo ran out of memory. Full error log: {errlog}")
    if retcode == -24:  # i.e. SIGXCPU
        raise OutOfTimeError(f"Gringo ran out of time. Full error log: {errlog}")

    raise ExternalCommandError(f"Unknown Gringo error. Gringo exited with code {retcode}. Full error log: {errlog}")


def parse_model(*, filename=None, content=None, symbol_mapping):
    if filename and not content:
        with open(filename, encoding="utf8") as f:
            return _parse_model(f, symbol_mapping)
    elif content and not filename:
        return _parse_model(content.splitlines(), symbol_mapping)
    else:
        raise ArgumentError("Cannot have both filename and content as arguments.")


def _parse_model(lines, symbol_mapping):
    tr = symbol_mapping
    model = defaultdict(set)
    for line in lines:
        data = line.rstrip(" \n.").rstrip(")")
        components = data.split("(")
        if len(components) == 1:
            symbol = tr.back(components[0])
            model[symbol].add(())
        elif len(components) == 2:
            symbol, arguments = components
            model[tr.back(symbol)].add(tuple(tr.back(s) for s in arguments.split(",")))
        else:
            # No nested terms expected, so there should be at most 2 components
            raise RuntimeError(f'Unexpected line "{line}" in Clingo solution file')

    return model
