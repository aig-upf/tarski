import copy
from typing import Set, Union, Tuple, Optional

from .problem import Problem
from . import fstrips as fs
from ..syntax import Formula, CompoundTerm, Atom, CompoundFormula, QuantifiedFormula, is_and, is_neg, exists, symref,\
    VariableBinding
from ..syntax.ops import collect_unique_nodes, flatten, free_variables
from ..syntax.util import get_symbols
from ..fstrips import AddEffect, DelEffect, LiteralEffect, FunctionalEffect, UniversalEffect
from .action import Action


def is_typed_problem(problem: Problem):
    """ A planning problem is typed if it has some sort other than 'object'. """
    return sum(1 for s in problem.language.sorts if not s.builtin) > 1


def is_positive_normal_form_problem(problem: Problem):
    """
    A propositional planning task is positive if all its operators and its goal are positive.
    """
    raise NotImplementedError()


def is_positive_operator(action: Action):
    """
    An operator o is positive if pre(o) and all effect conditions in eff(o) are positive.
    """
    raise NotImplementedError()


def is_positive_formula(phi: Formula):
    """
    A logical formula is positive if no negation symbols appear in it.
    """
    raise NotImplementedError()


def transform_to_positive_normal_form(what: Union[Problem, Action]):
    """ """
    if isinstance(what, Problem):
        return transform_problem_to_positive_normal_form(what)
    elif isinstance(what, Action):
        return transform_operator_to_positive_normal_form(what)
    raise RuntimeError(f'Unable to transform to positive normal form object {what}')


def transform_problem_to_positive_normal_form(problem: Problem):
    """ """
    raise NotImplementedError()


def transform_operator_to_positive_normal_form(action: Action):
    """ """
    raise NotImplementedError()


def is_strips_operator(action: Action):
    """
    An operator o is a STRIPS operator if
    (1) pre(o) is a conjunction of state variables, and
    (2) eff(o) is a conflict-free conjunction of atomic effects.
    """
    raise NotImplementedError()


def is_strips_problem(problem: Problem):
    """
    A propositional planning task is a STRIPS planning task if all of its operators are STRIPS operators
    its goal is a conjunction of state variables.
    """
    raise NotImplementedError()


def transform_to_strips(what: Union[Problem, Action]):
    """ """
    if isinstance(what, Problem):
        return transform_problem_to_strips(what)
    elif isinstance(what, Action):
        return transform_operator_to_strips(what)
    raise RuntimeError(f'Unable to transform to positive normal form object {what}')


def transform_problem_to_strips(problem: Problem):
    """ """
    raise NotImplementedError()


def transform_operator_to_strips(action: Action):
    """ """
    raise NotImplementedError()


def is_literal(phi: Formula):
    """ Return true iff the given formula is a literal """
    return isinstance(phi, Atom) or (is_neg(phi) and is_literal(phi.subformulas[0]))


def is_conjunction_of_literals(phi: Formula):
    """
    Return whether the given formula is a conjunction of literals, i.e. of atoms or negations of atoms.
    """
    f = flatten(phi)
    return isinstance(f, Atom) or \
        (isinstance(f, CompoundFormula) and all(is_literal(sub) for sub in f.subformulas))


def collect_literals_from_conjunction(phi: Formula) -> Optional[Set[Tuple[Atom, bool]]]:
    """ Return a list of all literals in phi, if is_conjunction_of_literals(phi), or None otherwise.
    The returned list consists of one tuple (a, p) for each literal in the conjunction phi, where a is the literal atom
    and p its polarity (i.e. True if positive, False if negative)
    """
    literals = set()  # type: Set[Tuple[Atom, bool]]
    if _collect_literals_from_conjunction(phi, literals):
        return literals
    return None


def _collect_literals_from_conjunction(f, literals: Set[Tuple[Atom, bool]]):
    if isinstance(f, Atom):
        literals.add((f, True))
    elif is_neg(f) and isinstance(f.subformulas[0], Atom):
        literals.add((f.subformulas[0], False))
    elif is_and(f):
        for sub in f.subformulas:
            if not _collect_literals_from_conjunction(sub, literals):
                return False
    else:
        return False
    return True


def is_function_free(phi: Formula):
    """
    Return whether the given formula is function-free, that is, has no function symbols other than constant symbols.
    """
    return len(collect_unique_nodes(phi, lambda x: isinstance(x, CompoundTerm))) == 0


def is_quantifier_free(phi: Formula):
    """ Return whether the given formula is quantifier-free. """
    return len(collect_unique_nodes(phi, lambda x: isinstance(x, QuantifiedFormula))) == 0


def collect_effect_free_parameters(action: Action):
    """ Return the "effect-free" parameters of the given action schema.
    These are the set of action parameters (logical variables) that do not appear on any effect of the action.
    """
    free = set()
    for eff in action.effects:
        _collect_effect_free_variables(eff, free)
    parameters = {symref(x) for x in action.parameters}
    return parameters.difference(free)


def project_away_effect_free_variables(action: Action, inplace=False):
    """ Return an action schema which is equivalent to the given `action` except that all "effect-free" parameters have
    been compiled away into existential variables in the precondition. The value of `inplace` determines whether
    the modification will be done in-place to the given action, or a new action will be created.

    As an example, an action

    action a(x, y, z)
        PRE: p(x, y) and q(y, z)
        EFF: not p(x, y)

    would become:

    action a(x, y)
        PRE: Exists z [p(x, y) and q(y, z)]
        EFF: not p(x, y)

    """
    free = collect_effect_free_parameters(action)
    bound = [x for x in action.parameters if symref(x) not in free]
    projected = action if inplace else copy.deepcopy(action)
    projected.parameters = VariableBinding(bound)
    projected.precondition = exists(*(x.expr for x in free), action.precondition)
    return projected


def project_away_effect_free_variables_from_problem(problem: Problem, inplace=False):
    """ Return a new problem equivalent to the given one but where all action schemas have had their "effect-free"
     parameters compiled away into existential variables in the precondition. The value of `inplace` determines whether
    the modification will be done in-place to the given problem, or a new problem will be created.
    """
    # If not modifying inplace, we copy the full problem (including its actions) and then modify that one inplace
    projected = problem if inplace else copy.deepcopy(problem)
    _ = [project_away_effect_free_variables(action, inplace=True) for action in projected.actions.values()]
    return projected


def collect_effect_free_variables(eff: fs.BaseEffect):
    """ Return the set of all variables that appear free in the given effect. """
    free = set()
    _collect_effect_free_variables(eff, free)
    return free


def _collect_effect_free_variables(eff: fs.BaseEffect, free: Set):
    """
    """
    if isinstance(eff, (fs.AddEffect, fs.DelEffect)):
        free.update(symref(x) for x in free_variables(eff.atom))

    elif isinstance(eff, fs.LiteralEffect):
        free.update(symref(x) for x in free_variables(eff.lit))

    elif isinstance(eff, fs.FunctionalEffect):
        free.update(symref(x) for x in free_variables(eff.lhs))
        free.update(symref(x) for x in free_variables(eff.rhs))

    elif isinstance(eff, fs.UniversalEffect):
        bound = {symref(x) for x in eff.variables}
        free_in_sub = set()
        for sub in eff.effects:
            _collect_effect_free_variables(sub, free_in_sub)
        free.update(free_in_sub - bound)

    else:
        raise RuntimeError(f'Effect "{eff}" of type "{type(eff)}" cannot be processed')


def collect_all_function_names(expression, output):
    terms = collect_unique_nodes(expression, lambda x: isinstance(x, CompoundTerm))
    output.update(f.symbol.name for f in terms)


def identify_cost_related_functions(problem: Problem):
    """ Return a list of those function symbols that are *only* used in effects that relate to the special
    "total-cost" function. """
    functions = list(get_symbols(problem.language, type_='function', include_builtin=False))
    cost_unrelated = set()

    collect_all_function_names(problem.goal, cost_unrelated)

    for action in problem.actions.values():
        collect_all_function_names(action.precondition, cost_unrelated)
        for effect in action.effects:
            mark_cost_unrelated_functions_in_effect(effect, cost_unrelated)

    return set(f.name for f in functions if f.name not in cost_unrelated)


def mark_cost_unrelated_functions_in_effect(effect, functions):
    collect_all_function_names(effect.condition, functions)

    if isinstance(effect, (AddEffect, DelEffect)):
        collect_all_function_names(effect.atom, functions)
    elif isinstance(effect, LiteralEffect):
        collect_all_function_names(effect.lit, functions)
    elif isinstance(effect, FunctionalEffect):
        if isinstance(effect.lhs, CompoundTerm) and effect.lhs.symbol.name == "total-cost":
            pass
        else:
            collect_all_function_names(effect.lhs, functions)
            collect_all_function_names(effect.rhs, functions)
    elif isinstance(effect, UniversalEffect):
        _ = [mark_cost_unrelated_functions_in_effect(x, functions) for x in effect.effects]





