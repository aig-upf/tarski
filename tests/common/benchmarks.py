

def get_lenient_benchmarks():
    """ Return a list of IPC domains that require non-strict PDDL parsing because of missing requirement flags or
    similar minor bugs, which would result in a parsing error. """
    return [
        'floortile-opt11-strips',  # Uses action costs without declaring them in the requirements section
        'ged-opt14-strips',  # "DEFINE" used in caps. The PDDL grammar doesn't mention it is case-insensitive
    ]
