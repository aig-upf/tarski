from ...errors import TarskiError
from ...fstrips import FunctionalEffect
from ...fstrips.action import AdditiveActionCost, generate_zero_action_cost
from ...fstrips.representation import is_typed_problem
from ...syntax import Interval, CompoundTerm, Tautology, BuiltinFunctionSymbol
from ... import theories
from ...theories import Theory


def pddl_to_tarski_type(typename):
    """ Translate a few PDDL types into their corresponding Tarski names
        (e.g. the FSTRIPS type "int" corresponds to the Tarski type "Integer").
    """
    translations = {"int": "Integer", "real": "Real", "number": "Real"}
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
    if ':action-costs' in requirements and not lang.has_sort('Integer'):
        theories.load_theory(lang, Theory.ARITHMETIC)
        create_number_type(lang)
    elif ':numeric-fluents' in requirements and not lang.has_sort('Integer'):
        theories.load_theory(lang, Theory.ARITHMETIC)


def get_requirements_string(problem):
    """ Get a list with all PDDL requirement strings based on the given problem """
    # TODO To be completed
    requirements = []
    if is_typed_problem(problem):
        requirements.append(":typing")

    # TODO Add ":negative-preconditions" requirement when representation.is_positive_normal_form_problem is implemented

    for t in problem.language.theories:
        # The Arithmetic theory incorporates arithmetic functions (which are PDDL numeric operators)
        if t == Theory.ARITHMETIC:
            requirements.append(":numeric-fluents")
        elif t == Theory.EQUALITY:
            requirements.append(":equality")

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


def process_cost_effects(effects):
    """ Filter a list of given effects into those that are cost-related and
    those that are not. """
    simple, cost_related = [], []
    for eff in effects:
        e = process_cost_effect(eff)
        if e is None:
            simple.append(eff)
        else:
            cost_related.append(process_cost_effect(eff))
    return simple, cost_related


def process_cost_effect(eff):
    """ Check if the given effect is a cost effect. If it is, return the additive cost; if it is not, return None. """
    if isinstance(eff, FunctionalEffect) and isinstance(eff.lhs, CompoundTerm) and eff.lhs.symbol.name == "total-cost":
        if not isinstance(eff.condition, Tautology):
            raise TarskiError(f'Don\'t know how to process conditional cost effects such as {eff}')
        if not isinstance(eff.rhs, CompoundTerm) or eff.rhs.symbol.name != BuiltinFunctionSymbol.ADD:
            raise TarskiError(f'Don\'t know how to process non-additive cost effects such as {eff}')
        addend = eff.rhs.subterms[1]
        return AdditiveActionCost(addend)

    return None


def uniformize_costs(problem):
    some_cost_defined = any(action.cost for action in problem.actions.values())
    if not some_cost_defined:  # No need to do anything
        return

    # If at least one action has a defined cost, then for those that have no cost, assume that they are zero cost,
    # and make sure that the zero-cost is properly defined.
    for action in problem.actions.values():
        if not action.cost:
            action.cost = generate_zero_action_cost(action.language)


class LowerCasingStreamWrapper(object):
    """ A simple wrapper around a stream to lowercase all characters.
     @see https://github.com/antlr/antlr4/blob/master/doc/case-insensitive-lexing.md
    """
    def __init__(self, stream):
        self._stream = stream

    def __getattr__(self, name):
        return self._stream.__getattribute__(name)

    def LA(self, offset):
        c = self._stream.LA(offset)
        if c <= 0:
            return c
        return ord(chr(c).lower())
