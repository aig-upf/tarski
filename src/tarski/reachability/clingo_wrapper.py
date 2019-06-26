import logging
import shutil
import tempfile
from collections import defaultdict

from ..errors import CommandNotFoundError, ExternalCommandError
from ..utils import command as cmd


def run_clingo(lp):
    gringo = shutil.which("gringo")
    if gringo is None:
        raise CommandNotFoundError("gringo")

    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        _ = [print(str(r), file=f) for r in lp.rules]
        filename = f.name

    logging.debug('Using gringo binary found in "{}"'.format(gringo))
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as f:
        # Option "-t" enforces an easier-to-parse textual output. Warnings could also be supressed with
        # option "-Wno-atom-undefined"
        retcode = cmd.execute([gringo, "-t", filename], stdout=f)
        model_filename = f.name
        if retcode != 0:
            raise ExternalCommandError("Gringo exited with code {}".format(retcode))

    return model_filename


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
