"""
"""
from ..model import Model


def parse_atom(lang, string):
    """ Parse a string representation of an atom such as "on(b1, b2)" from the given language
    and return a Tarski atom object. """
    parts = string.rstrip(')').replace('(', ',').split(',')
    pred = lang.get(parts[0])
    args = [lang.get(o) for o in parts[1:]]
    return pred(*args)


def parse_model(lang, atoms):
    """ Parse a list of strings representing atoms from the given language. """
    model = Model(lang)

    for atom in atoms:
        model.add(parse_atom(lang, atom))

    return model
