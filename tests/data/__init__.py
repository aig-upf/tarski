from pathlib import Path

HERE = Path(__file__).resolve().parent


def resolve_path(filename):
    """ Return the given filename interpreted as relative to the data directory in the test distribution. """
    return (HERE / filename).absolute()
