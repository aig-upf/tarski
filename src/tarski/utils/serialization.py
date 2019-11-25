

def serialize_atom(atom):
    """ Return a comma-separated serialization of a given atom, e.g. from atom "on(a,b)", it will return "on,a,b". """
    if not atom.subterms:
        return atom.predicate.symbol
    return f'{atom.predicate.symbol},{",".join(st.symbol for st in atom.subterms)}'
