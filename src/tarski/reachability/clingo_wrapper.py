import logging
import os
import shutil
import tempfile
from collections import defaultdict

from ..errors import CommandNotFoundError, ExternalCommandError, OutOfMemoryError, OutOfTimeError
from ..utils import command as cmd


def run_clingo(lp):
    gringo = shutil.which("gringo")
    if gringo is None:
        raise CommandNotFoundError("gringo")

    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        _ = [print(str(r), file=f) for r in lp.rules]
        _ = [print(str(r), file=f) for r in lp.directives]
        theory_filename = f.name

    logging.debug('Using gringo binary found in "{}"'.format(gringo))
    errlog = ''
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as stderr:
            # Option "-t" enforces an easier-to-parse textual output. Warnings could also be supressed with
            # option "-Wno-atom-undefined"
            retcode = cmd.execute([gringo, "-t", theory_filename], stdout=f, stderr=stderr)
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


def parse_model(filename, symbol_mapping):
    tr = symbol_mapping
    model = defaultdict(set)
    with open(filename, "r") as f:
        for line in f:
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
