import copy
from typing import Set, Union, Tuple, Optional

from ..errors import TarskiError
from .problem import Problem
from . import fstrips as fs
from ..syntax import Formula, CompoundTerm, Atom, CompoundFormula, QuantifiedFormula, is_and, is_neg, exists, symref,\
    VariableBinding, Constant, Tautology, land
from ..syntax.ops import collect_unique_nodes, flatten, free_variables, all_variables
from ..syntax.sorts import compute_signature_bindings
from ..syntax.util import get_symbols
from ..fstrips import AddEffect, DelEffect, LiteralEffect, FunctionalEffect, UniversalEffect, BaseEffect, SingleEffect
from .action import Action


class RepresentationError(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'Unexpected representation errir'
        super().__init__(msg)


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
    return is_conjunction_of_positive_atoms(action.precondition) and is_strips_effect_set(action.effects)


def is_strips_problem(problem: Problem):
    """
    A propositional planning task is a STRIPS planning task if all of its operators are STRIPS operators
    its goal is a conjunction of state variables.
    """
    return is_conjunction_of_positive_atoms(problem.goal) \
        and all(is_strips_operator(a) for a in problem.actions.values())


def transform_to_strips(what: Union[Problem, Action]):
    """ """
    if isinstance(what, Problem):
        return transform_problem_to_strips(what)
    elif isinstance(what, Action):
        return transform_operator_to_strips(what)
    raise RuntimeError(f'Unable to transform to positive normal form object {what}')


def is_atomic_effect(eff: BaseEffect):
    """ An effect is atomic if it is a single, unconditional effect. """
    return isinstance(eff, SingleEffect) and isinstance(eff.condition, Tautology)


def is_propositional_effect(eff: BaseEffect):
    """ An effect is propositional if it is either an add or a delete effect. """
    return isinstance(eff, (AddEffect, DelEffect))


def is_strips_effect_set(effects):
    """ Return whether the all effects in the given list of effects are propositional, atomic,
    and there is no two contradictory effect, e.g. in the form of an add-effect and a delete-effect
    over the same variable. """
    try:
        conflicts = compute_effect_set_conflicts(effects)
    except RepresentationError:
        return False  # Some effect was not STRIPS

    return len(conflicts) == 0  # If there was some conflict, the effect is not STRIPS


def compute_effect_set_conflicts(effects):
    """ """
    polarities = dict()
    conflicts = set()
    for eff in effects:
        if not is_atomic_effect(eff) or not is_propositional_effect(eff):
            raise RepresentationError(f"Don't know how to compute conflicts for effect {eff}")
        pol = isinstance(eff, AddEffect)  # i.e. polarity will be true if add effect, false otherwise
        prev = polarities.get(eff.atom, None)
        if prev is not None and prev != pol:
            conflicts.add(eff.atom)
        polarities[eff.atom] = pol
    return conflicts


def transform_problem_to_strips(problem: Problem):
    """ """
    raise NotImplementedError()


def transform_operator_to_strips(action: Action):
    """ """
    raise NotImplementedError()


def is_literal(phi: Formula):
    """ Return true iff the given formula is a literal """
    return isinstance(phi, Atom) or (is_neg(phi) and isinstance(phi.subformulas[0], Atom))


def is_ground(element):
    return len(all_variables(element)) == 0


def is_delete_free(problem: Problem):
    for _, a in problem.actions.items():
        for eff in a.effects:
            if contains_delete_subeffects(eff):
                return False
    return True


def contains_delete_subeffects(effect: BaseEffect):
    if isinstance(effect, DelEffect):
        return True
    elif isinstance(effect, AddEffect):
        return False
    elif isinstance(effect, UniversalEffect):
        return any(contains_delete_subeffects(e) for e in effect.effects)
    raise RuntimeError(f'Unexpected type for effect {effect}')


def compute_delete_free_relaxation(problem: Problem):
    problem = copy.deepcopy(problem)
    for _, a in problem.actions.items():
        a.effects = remove_delete_effects(a.effects)
    return problem


def remove_delete_effects(effects):
    deletefree = []
    for effect in effects:
        if isinstance(effect, DelEffect):
            pass
        elif isinstance(effect, AddEffect):
            deletefree.append(effect)
        elif isinstance(effect, UniversalEffect):
            effect.effects = remove_delete_effects(effect.effects)  # i.e. remove delete-free effects recursively
            deletefree.append(effect)
        else:
            raise RuntimeError(f'Unexpected type for effect {effect}')
    return deletefree


def is_conjunction_of_literals(phi: Formula):
    """
    Return whether the given formula is a conjunction of literals, i.e. of atoms or negations of atoms.
    """
    f = flatten(phi)
    return isinstance(f, Atom) or \
        (isinstance(f, CompoundFormula) and all(is_literal(sub) for sub in f.subformulas))


def is_conjunction_of_positive_atoms(phi: Formula):
    """
    Return whether the given formula is a conjunction of literals, i.e. of atoms or negations of atoms.
    """
    f = flatten(phi)
    return isinstance(f, Atom) or \
        (isinstance(f, CompoundFormula) and all(isinstance(sub, Atom) for sub in f.subformulas))


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


def classify_atom_occurrences_in_formula(phi: Formula):
    """ Classify atoms in the given formula according to whether they occur as positive or negative literals
    """
    pos, neg, fun = set(), set(), set()
    for atom, truthval in collect_literals_from_conjunction(phi):
        if atom.predicate.builtin:
            fun.update(symref(t) for t in collect_unique_nodes(atom, lambda x: isinstance(x, CompoundTerm)))

        elif truthval:
            pos.add(symref(atom))
        else:
            neg.add(symref(atom))
    return pos, neg, fun


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
    """ Add to `output` the names of all function symbols in the given expression. """
    terms = collect_unique_nodes(expression, lambda x: isinstance(x, CompoundTerm))
    output.update(f.symbol.name for f in terms)


def identify_cost_related_functions(problem: Problem):
    """ Return a list of those function symbols that are *only* used in effects that relate to the special
    "total-cost" function. """
    functions = list(get_symbols(problem.language, type_='function', include_builtin=False))
    related_to_non_cost_effects = set()

    collect_all_function_names(problem.goal, related_to_non_cost_effects)

    for action in problem.actions.values():
        collect_all_function_names(action.precondition, related_to_non_cost_effects)
        for effect in action.effects:
            mark_cost_unrelated_functions_in_effect(effect, related_to_non_cost_effects)

    return set(f.name for f in functions if f.name not in related_to_non_cost_effects)


def mark_cost_unrelated_functions_in_effect(effect, functions):
    collect_all_function_names(effect.condition, functions)

    if isinstance(effect, (AddEffect, DelEffect)):
        collect_all_function_names(effect.atom, functions)
    elif isinstance(effect, LiteralEffect):
        collect_all_function_names(effect.lit, functions)
    elif isinstance(effect, FunctionalEffect):
        collect_all_function_names(effect.lhs, functions)
        collect_all_function_names(effect.rhs, functions)
    elif isinstance(effect, UniversalEffect):
        _ = [mark_cost_unrelated_functions_in_effect(x, functions) for x in effect.effects]


def is_unit_cost_problem(problem):
    return all(is_unit_cost_action(a) for a in problem.actions.values())


def is_constant_cost_problem(problem):
    return all(is_constant_cost_action(a) for a in problem.actions.values())


def is_unit_cost_action(action):
    if not action.cost:
        return True

    addend = action.cost.addend
    return isinstance(addend, Constant) and addend.symbol == 1


def is_zero_cost_action(action):
    if not action.cost:
        return True

    addend = action.cost.addend
    return isinstance(addend, Constant) and addend.symbol == 0


def is_constant_cost_action(action):
    if not action.cost:
        return True

    addend = action.cost.addend
    return isinstance(addend, Constant)


def compile_negated_preconditions_away(problem: Problem, inplace=False):
    """ Compile away negated literals in the problem actions and goal.
    See docs from `compile_away_formula_negated_literals` for details. """
    problem = copy.deepcopy(problem) if not inplace else problem

    # First compile the action preconditions away
    negpreds = dict()
    newactions = []
    for aname, action in problem.actions.items():
        newactions.append((aname, compile_action_negated_preconditions_away(action, negpreds, inplace=True)))

    # Now compile goal away
    problem.goal = compile_away_formula_negated_literals(problem.goal, negpreds, inplace=True)

    # Now that we know which predicates have been artificially duplicated,
    # we can add the appropriate effects to update the denotation of those predicates
    for aname, action in newactions:
        problem.actions[aname] = update_action_effects_with_negated_counterparts(action, negpreds)

    # Finally, if any negated precondition was created, then insert the appropriate atoms
    # in the initial state
    model = problem.init
    for pred, negpred in negpreds.items():
        for point in compute_complementary_atoms(model, pred):
            model.add(negpred, *point)

    return problem


def update_action_effects_with_negated_counterparts(action: Action, negpreds):
    """ """
    neweffects = []
    for eff in action.effects:
        if not is_propositional_effect(eff):
            raise RepresentationError(f"Don't know how to update negated counterpart atoms for effect {eff}")

        atom = eff.atom
        negpred = negpreds.get(atom.predicate)
        if negpred is not None:
            # Insert the converse type of effect with the converse predicate
            if isinstance(eff, DelEffect):
                neweffects.append(AddEffect(negpred(*atom.subterms), eff.condition))
            else:
                assert isinstance(eff, AddEffect)
                neweffects.append(DelEffect(negpred(*atom.subterms), eff.condition))

    action.effects += neweffects
    return action


def compile_action_negated_preconditions_away(action: Action, negpreds, inplace=False):
    """ Compile away negated literals in the action precondition and effect conditions.
    See docs from `compile_away_formula_negated_literals` for details. """
    action = copy.deepcopy(action) if not inplace else action
    action.precondition = compile_away_formula_negated_literals(action.precondition, negpreds, inplace=True)
    for eff in action.effects:
        if not isinstance(eff, SingleEffect):
            raise RepresentationError(f"Cannot compile away negated conditions for effect '{eff}'")

        if not isinstance(eff.condition, Tautology):
            eff.condition = compile_away_formula_negated_literals(eff.condition, negpreds, inplace=True)

    return action


def compile_away_formula_negated_literals(phi, negpreds, inplace=False):
    """ Compile away all negated literals in the given formula, which is assumed to be
    a conjunction of literals, by replacing them by new atoms that use a fresh predicate
    "not_p" for every literal not p(x). """
    phi = copy.deepcopy(phi) if not inplace else phi
    f = flatten(phi)
    if isinstance(f, Atom):
        return f

    if is_neg(f):
        return _compile_possibly_negated_literal(f, negpreds)

    if not isinstance(f, CompoundFormula):
        raise RepresentationError(f"Cannot compile away negated conditions of formula '{phi}'")

    compiled_subformulas = []
    for sub in f.subformulas:
        if not is_literal(sub):
            raise RepresentationError(f"Cannot compile away negated conditions of formula '{phi}'")

        compiled_subformulas.append(_compile_possibly_negated_literal(sub, negpreds))

    return land(*compiled_subformulas, flat=True)


def _compile_possibly_negated_literal(sub, negpreds):
    """ A helper that processes a given literal; if the literal is of the form not p(x),
    it generates a replacement positive atom _not_p(x), and registers the new predicate
    _not_p within the problem language. """
    if not is_neg(sub):
        return sub

    atom = sub.subformulas[0]  # This is well-defined because we assume is_literal(sub)
    pred = atom.predicate
    if pred.builtin:
        return sub  # We don't want to compile away negated builtin predicates
    negpred = negpreds.get(pred, None)
    if negpred is None:
        lang = pred.language
        negpreds[pred] = negpred = lang.predicate(f"_not_{pred.name}", *pred.sort)

    return negpred(*atom.subterms)


def compute_complementary_atoms(model, predicate):
    """ Generate all bindings for the given predicate which are not true in the given model. """
    extension = model.get_extension(predicate)
    for binding in compute_signature_bindings(predicate.sort):
        refd = tuple(symref(x) for x in binding)
        if refd not in extension:
            yield binding


def has_state_variable_shape(expression):
    """ Return whether the given atom or compound term can be considered a state variable for planning purposes, i.e.
    all their subterms are constants. Whether the expression is actually used as a state variable or not will also
    depend on whether the head is static or fluent, or on other types analyses, but we don't deal with that here."""
    if not isinstance(expression, (CompoundTerm, Atom)):
        return False
    return all(isinstance(s, Constant) for s in expression.subterms)
