"""
    Generate FSTRIPS Counters languages and problems
"""
from ..fstrips import create_fstrips_problem, language
from ..syntax import land
from ..theories import Theory


BASE_DOMAIN_NAME = "counters-fn"


def generate_fstrips_counters_language(ncounters=3, upper_bound=None):
    """ The (typed) FSTRIPS Counters encoding. """
    upper_bound = ncounters * 2 if upper_bound is None else upper_bound

    lang = language(BASE_DOMAIN_NAME, theories=[Theory.EQUALITY, Theory.ARITHMETIC])
    lang.sort('counter')
    lang.interval('val', lang.Integer, lower_bound=0, upper_bound=upper_bound)

    lang.function('value', 'counter', 'val')
    lang.function('max_int', 'val')

    _ = [lang.constant(f'c{k}', 'counter') for k in range(1, ncounters+1)]
    return lang


def generate_fstrips_counters_problem(ncounters=3, upper_bound=None):
    """ Generate a (typed) FSTRIPS Counters problem with the given number of counters. """
    upper_bound = ncounters * 2 if upper_bound is None else upper_bound
    lang = generate_fstrips_counters_language(ncounters=ncounters, upper_bound=upper_bound)

    problem = create_fstrips_problem(lang, domain_name=BASE_DOMAIN_NAME, problem_name='test-instance')
    counters = sorted(lang.ns.counter.domain(), key=lambda x: x.symbol)

    value = lang.get_function('value')
    max_int = lang.get_function('max_int')

    inequalities = [value(c1) < value(c2) for c1, c2 in zip(counters, counters[1:])]
    problem.goal = land(*inequalities, flat=True)

    c = lang.variable('c', 'counter')

    problem.action(
        "increment", [c],
        precondition=value(c) < max_int(),
        effects=[value(c) << value(c) + 1]
    )

    problem.action(
        "decrement", [c],
        precondition=value(c) > 0,
        effects=[value(c) << value(c) - 1]
    )

    problem.init.set(max_int, upper_bound)
    for c in counters:
        problem.init.set(value, c, 0)

    return problem


def get_counters_elements(ncounters=3):
    """ This is just a simple helper method to generate and return all relevant elements of the problem, for easier
     access. """
    problem = generate_fstrips_counters_problem(ncounters=ncounters)
    lang = problem.language

    counters = sorted(lang.ns.counter.domain(), key=lambda x: x.symbol)
    return [problem, lang, lang.ns.value, lang.ns.max_int] + counters
