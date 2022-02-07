import logging
import os
import sys
import shutil
import tempfile
from pathlib import Path
from collections import defaultdict

from ..errors import CommandNotFoundError, ExternalCommandError, OutOfMemoryError, OutOfTimeError, ArgumentError
from ..utils import command as cmd
from importlib.util import find_spec


def get_gringo_command():
    """Assemble the command to run gringo

    :return: A list depicting the command with arguments
    :rtype: list of String / None(if command could not be assembled)
    """
    command = None
    if find_spec("clingo"):
        command = [sys.executable, os.path.join(Path(__file__).parent.absolute(), "gringo.py")]
        logging.debug("Using the clingo pypi bindings to emulate gringo binary")
    else: 
        gringo = shutil.which("gringo")
        command = [gringo] if gringo else None
        logging.debug('Using gringo binary found in "{}"'.format(gringo))

    return command

def run_clingo(lp):
    gringo_command = get_gringo_command()
    if gringo_command is None:
        raise CommandNotFoundError("gringo")
          
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        _ = [print(str(r), file=f) for r in lp.rules]
        _ = [print(str(r), file=f) for r in lp.directives]
        theory_filename = f.name

    errlog = ''
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as stderr:
            # Option "-t" enforces an easier-to-parse textual output. Warnings could also be supressed with
            # option "-Wno-atom-undefined"
            retcode = cmd.execute(gringo_command+["--text", theory_filename], stdout=f, stderr=stderr)
            model_filename = f.name
            
            if retcode == 0:
                return model_filename, theory_filename

    if os.path.isfile(stderr.name):
        with open(stderr.name, 'r') as file:
            errlog = file.read()

    if 'std::bad_alloc' in errlog:
        raise OutOfMemoryError(f"Gringo ran out of memory. Full error log: {errlog}")
    if retcode == -24:  # i.e. SIGXCPU
        raise OutOfTimeError(f"Gringo ran out of time. Full error log: {errlog}")

    raise ExternalCommandError(f"Unknown Gringo error. Gringo exited with code {retcode}. Full error log: {errlog}")

def parse_model(*, filename=None, content=None, symbol_mapping):
    if filename and not content:
        with open(filename, "r") as f:
            return _parse_model(f, symbol_mapping)
    elif content and not filename:
        return _parse_model(content.splitlines(), symbol_mapping)
    else:
        raise ArgumentError(f"Cannot have both filename and content as arguments.")

def _parse_model(lines, symbol_mapping):
    tr = symbol_mapping
    model = defaultdict(set)
    for line in lines:
        data = line.rstrip(' \n.').rstrip(')')
        components = data.split('(')
        if len(components) == 1:
            symbol = tr.back(components[0])
            model[symbol].add(())
        elif len(components) == 2:
            symbol, arguments = components
            model[tr.back(symbol)].add(tuple(tr.back(s) for s in arguments.split(',')))
        else:
            # No nested terms expected, so there should be at most 2 components
            raise RuntimeError('Unexpected line "{}" in Clingo solution file'.format(line))
    
    return model
