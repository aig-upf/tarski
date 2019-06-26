
from ...syntax import Interval
from ... import theories
from ...theories import Theory


def pddl_to_tarski_type(typename):
    """ Translate a few PDDL types into their corresponding Tarski names
        (e.g. the FSTRIPS type "int" corresponds to the Tarski type "Integer").
    """
    translations = {"int": "Integer"}
    return translations.get(typename, typename)


def tarski_to_pddl_type(typename):
    """ Translate a few Tarski types into their corresponding FSTRIPS names
    """
    translations = {"Integer": "int", "Natural": "int", "Real": "number"}
    return translations.get(typename.name, typename.name)


def parse_number(number, lang):
    # Because of the grammar, we know that number will be either an int or a float
    try:
        value = int(number)
        return lang.constant(lang.Integer.cast(value), lang.Integer)
    except ValueError:
        value = float(number)
        return lang.constant(lang.Real.cast(value), lang.Real)


def process_requirements(requirements, lang):
    if ':action-costs' in requirements:
        theories.load_theory(lang, Theory.ARITHMETIC)
        create_number_type(lang)
    elif ':numeric-fluents' in requirements:
        theories.load_theory(lang, Theory.ARITHMETIC)


def get_requirements_string(problem):
    """ Get a list with all PDDL requirement strings based on the given problem """
    # TODO To be completed
    requirements = []
    for t in problem.language.theories:
        # The Arithmetic theory incorporates arithmetic functions (which are PDDL numeric operators)
        if t == Theory.ARITHMETIC:
            requirements.append(":numeric-fluents")

    # Functional STRIPS with action costs, keeping in line with IPC convention
    if problem.metric is not None and problem.language.has_function('total-cost'):
        requirements.append(":action-costs")

    return requirements


def create_number_type(lang):
    """ Creates a sort corresponding to the PDDL "number" """
    # For the moment being, we assume that PDDL "number"s are unbound integers
    parent = lang.get_sort("Integer")
    lower = parent.lower_bound
    upper = parent.upper_bound
    lang.interval("number", parent, lower, upper)


def create_sort(lang, typename, basename):
    """ Create a Tarski sort from a PDDL type, performing a few checks and translations to ensure consistency """
    if typename == 'object':
        return
    
    typename = pddl_to_tarski_type(typename)
    basename = pddl_to_tarski_type(basename)

    if basename in ("Natural", "Integer", "Real"):
        # The new type will necesarily be an interval subset of it parent
        parent = lang.get_sort(basename)
        assert isinstance(parent, Interval)
        # TODO This is a small hack: since we don't yet know the lower and upper bound (because they are declared in
        # the instance file, not domain file), we put the widest possible range allowed by the parent. If we do not
        # do that, then the processing of the instance file might raise some error, because when the initial state is
        # parsed, we check that each assignment is within bounds - but that again might happen before knowing the real
        # bounds. A better solution would be to parse the instance file one first pass looking only for the bounds.
        lower = parent.lower_bound
        upper = parent.upper_bound
        lang.interval(typename, parent, lower, upper)
    else:
        lang.sort(typename, lang.get_sort(basename))
