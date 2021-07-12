from pathlib import Path

HERE = Path(__file__).resolve().parent


def resolve_path(filename):
    """ """
    return HERE / filename
