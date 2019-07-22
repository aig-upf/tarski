
import logging
import operator
import itertools
import time
from collections import defaultdict
from functools import reduce

try:
    from pysdd.sdd import Vtree, SddManager
except ImportError as err:
    raise RuntimeError("Could not import pysdd - sdd module not available") from None


from ..evaluators.simple import evaluate
from ..syntax import lor, neg, Atom, BuiltinPredicateSymbol, CompoundFormula, Connective, Variable, Tautology, builtins
from ..syntax.ops import flatten, collect_unique_nodes
from ..grounding.ops import classify_symbols
from ..fstrips import fstrips
from ..fstrips.representation import is_literal, collect_literals_from_conjunction


class UnsupportedFormalism(RuntimeError):
    """ The maximum size of the SDD data structure has been surpassed """
    pass


def scout_actions(task, data):
    """ Check & report which actions have (potentially) some groundings, and which not """
    # TODO: This will probably fail on parameter-less actions??
    actions, empty = [], []
    for action in task.actions.values():
        cardinalities = [len(list(x.sort.domain())) for x in action.parameters]
        ngroundings = reduce(operator.mul, cardinalities, 1)
        logging.debug(f'{action.ident()}:\t{" * ".join(map(str, cardinalities))} = {ngroundings} potential groundings')
        if ngroundings == 0:
            empty.append(action.name)
        else:
            actions.append(action)
            data['action'] += [action.ident()]
            data['arity'] += [len(action.parameters)]
            data['groundings'] += [ngroundings]

    logging.debug(f"{len(actions)} actions to ground; actions discarded: {empty}")
    return actions


def create_equality_constraints(equalities, selects):
    """ Create for each atom X != Y a set of equality constraints
            AND_{v in D} not select(X, v) or not select(Y, v)
    """
    eq_constraints = []
    for eq in equalities:
        if eq.predicate.symbol != BuiltinPredicateSymbol.NE:
            # eq_constraints += [lor(neg(l), r), lor(neg(r), l)]
            # Let us have a strong abort here to inspect preconditions of this type (i.e.: a precondition X=Y
            # on two different action parameters X and Y), if they every arise, as that would be quite
            # surprising to me. If they indeed occur in practice, it might be better to deal with them by pre-
            # compiling them away?
            raise UnsupportedFormalism(f'Unexpected precondition atom of the form "X=Y": {eq}. '
                                       f'Might be worth inspecting it.')

        lhs, rhs = eq.subterms
        if any(not isinstance(v, Variable) for v in (lhs, rhs)):
            # TODO Extend this to cases as atoms "X != c", where X is a parameter and c a constant
            raise NotImplementedError()
        for l, r in itertools.product(selects[lhs.symbol], selects[rhs.symbol]):
            # TODO This quadratic search could be improved if necessary by indexing the select atoms
            if l.subterms[-1].symbol == r.subterms[-1].symbol:
                eq_constraints.append(lor(neg(l), neg(r)))
    return eq_constraints


def create_grounding_constraints(selects, statics, init, atoms):
    """ Create the core grounding constraints, taking into account static predicate information.
     For each predicate p(X_1, ..., X_n) in the precondition of the action, a constraint is created with form:

        select(X_1, z_1) and ... and select(X_n, z_n)  --> p(X_1, ..., X_n)


     - selects: select atoms
     - statics: set of static predicate symbols
     - init: initial state model
     - precs: set of action precondition atoms
    """
    fluents = set()
    count = defaultdict(int)
    constraints = []
    for atom in atoms:
        lang = atom.predicate.language  # The language of the original problem
        for x in atom.subterms:
            count[x.symbol] += 1
        SX = [selects[sub.symbol] for sub in atom.subterms]
        for selectlist in itertools.product(*SX):
            values = [lang.get_constant(s.subterms[-1].symbol) for s in selectlist]
            head = atom.predicate(*values)
            body = [neg(h) for h in selectlist]

            # We disinguish the following cases:
            # (1) The atom p is a fluent: post a constraint -sel(x1, z1) or ... or -sel(xn, zn) or p(x1, ..., xn)
            # (2) The atom p is static, and holds in the initial state: no need to post anything
            # (3) The atom p is static, but doesn't hold in init: then post -sel(x1, z1) or ... or -sel(xn, zn)
            # Note that (2) and (3) are just specializations of (1)

            if atom.predicate in statics:  # p is static
                if init[head]:
                    continue  # No need to post anything
                else:
                    assert body
                    if len(body) == 1:
                        constraints += body
                    else:
                        constraints.append(lor(*body))
            else:  # p is a fluent
                fluents.add(head)
                constraints.append(lor(*body, head) if body else head)

    return constraints, count, fluents


def setup_metalanguage(action):
    """ """
    lang = action.language  # The original language
    metalang = fstrips.language(action.name, theories=[])

    # The metalanguage has a constant x for each action parameter x in the action schema
    parameters = {p.symbol: metalang.constant(p.symbol, metalang.Object) for p in action.parameters}
    domains = {p.symbol: set(c.symbol for c in p.sort.domain()) for p in action.parameters}

    # The metalanguage has a predicate select_t for each type t of some action parameter
    sorts = {p.sort for p in action.parameters}  # a set with all distinct types relevant to the parameters
    for sort in sorts:
        _ = metalang.Object if sort.name == 'object' else metalang.sort(sort.name)  # Declares the sort if necessary
        # for o in sort.domain():
        #     metalang.constant(o.symbol, t)

    # Declare all objects in the metalanguage, but ignore the types
    for o in lang.constants():
        metalang.constant(o.symbol, metalang.Object)

    return metalang, parameters, domains


def generate_select_atoms(action, metalang, parameters, domains):
    """ Create the atoms of the form select(X, x) for each action parameter X and possible value x in its domain """
    domain_constraints = []

    # Declare a type-agnostic "select(x, v)" predicate
    selectpred = metalang.predicate('_select_', metalang.Object, metalang.Object)
    # for param in action.parameters:
    #     t = param.sort.name
    #     select_predicates[param.symbol] = metalang.predicate(f'select_{t}', metalang.get_sort(t))

    def selatom(parameter, value):
        return selectpred(parameters[parameter.symbol], metalang.get_constant(value))

    selects = dict()
    for p in action.parameters:
        sel = selects[p.symbol] = [selatom(p, value) for value in domains[p.symbol]]

        if len(sel) == 1:
            # If parameter X has one single possible value V, then selected(X, V) must be true
            domain_constraints.append(sel[0])
            continue

        assert len(sel) >= 2
        domain_constraints.append(lor(*sel, flat=True))
        domain_constraints.extend(lor(neg(v1), neg(v2)) for v1, v2 in itertools.combinations(sel, 2))

    return selects, sum(len(s) for s in selects.values()), domain_constraints


def extract_equalities(prec_constraints):
    """ Extract a table with action parameter equalities of the form X=Y, X!=Y"""
    eqs = set()
    for atom, polarity in prec_constraints:
        if atom.predicate.symbol in builtins.get_equality_predicates():
            eqs.add(atom if polarity else builtins.negate_builtin_atom(atom))
    return eqs


def preprocess_parameter_domains(action, statics, domains, init):
    """ Simplify the precondition formula and prune the potential domains of action parameters based on statics
    and basic CSP techniques"""
    flattened = flatten(action.precondition)
    constraints = collect_literals_from_conjunction(flattened)
    if constraints is None:
        # Check that we have have a plain conjunction of atoms (constraints); if not, abort
        raise UnsupportedFormalism(f'Cannot process complex precondition of action "{action.ident()}":'
                                   f'\n\t{action.precondition}"')

    # At the moment we only enforce node consistency for (static, of course) unary constraints
    # TODO Might be worth achieving arc-consistency taking all constraints into account
    removable_subformulas = set()
    for atom, polarity in constraints:
        predicate = atom.predicate
        if predicate.arity != 1:
            continue
        if predicate not in statics:
            if not predicate.builtin:
                continue

        term = atom.subterms[0]
        if not isinstance(term, Variable):
            continue  # TODO This could be improved to resolve static atoms p(c), where c is a constant, not a variable

        lang = predicate.language
        parameter = term.symbol
        unsatisfied = set()
        for obj in domains[parameter]:
            if init[predicate(lang.get_constant(obj))] is not polarity:
                unsatisfied.add(obj)
        # print(f"Objects {unsatisfied} can be pruned for node-inconsistency reasons from the extension of {predicate}")
        domains[parameter].difference_update(unsatisfied)  # Remove the values from the domains
        removable_subformulas.add(atom)  # Mark the static atom to be removed from the precondition

    active = tuple(sub if polarity else neg(sub) for sub, polarity in constraints if sub not in removable_subformulas)
    if len(active) == 0:
        optimized = Tautology
    elif len(active) == 1:
        optimized = active[0]
    else:
        optimized = flattened  # If we get here, flattened must be a conjunction
        optimized.subformulas = active
    return domains, optimized, constraints


def process_schema(problem, statics, action, data, max_size):
    # print(f"Processing action schema:\n{action}")
    data['instance'] += [problem.name]

    # Set up a metalanguage for the encoding of the SDD applicability theory
    metalang, parameters, domains = setup_metalanguage(action)

    domains, precondition, prec_constraints = preprocess_parameter_domains(action, statics, domains, problem.init)

    selects_, nvars_, dom_constraints_ = generate_select_atoms(action, metalang, parameters, domains)
    data['selects'] += [nvars_]
    equalities = extract_equalities(prec_constraints)
    prec_atoms = collect_unique_nodes(precondition, lambda x: isinstance(x, Atom) and not x.predicate.builtin)
    eq_constraints = create_equality_constraints(equalities, selects_)

    grounding_constraints, count, fluents = create_grounding_constraints(selects_, statics, problem.init, prec_atoms)
    nvars_ += len(fluents)

    data['atoms'] += [len(fluents)]
    data['DOM'] += [len(dom_constraints_)]
    data['EQ'] += [len(eq_constraints)]
    data['GROUND'] += [len(grounding_constraints)]
    data['nclauses'] += [len(dom_constraints_) + len(eq_constraints) + len(grounding_constraints)]
    data['nvars'] += [nvars_]

    symbols = compute_symbol_ids(count, selects_, fluents)

    manager = setup_sdd_manager(nvars_)

    alltranslated = [translate_to_pysdd(c, symbols, manager)
                     for c in itertools.chain(dom_constraints_, eq_constraints, grounding_constraints)]

    if not alltranslated:
        # No constraints at all must mean an action schema with no parameters and and empty precondition
        data['sdd_sizes'] += [0]
        data['sdd_size'] += [0]
        data['A(s0)'] += [1]
        return

    sdd_sizes = []
    failed = False

    t0 = time.time()

    sdd_pre = alltranslated[0]
    for c in alltranslated[1:]:
        sdd_pre = sdd_pre & c
        sdd_sizes += [sdd_pre.size()]
        if sdd_sizes[-1] > max_size:
            failed = True
            break
    tf = time.time()
    data['runtime'] += [tf - t0]
    data['sdd_sizes'] += [sdd_sizes]
    data['sdd_size'] += [sdd_sizes[-1]]
    # sdd_clauses = sdd_ground + sdd_eq + sdd_dom
    # plot_sdd_size(the_task.domain_name, the_task.name, act, sdd_sizes, sdd_clauses, sdd_eq, sdd_ground, sdd_dom)

    if failed:
        data['A(s0)'] += [None]
        return

    s0_literals = [p if problem.init[p] else neg(p) for p in fluents]
    pysdd_s0 = [translate_to_pysdd(l, symbols, manager) for l in s0_literals]
    assert pysdd_s0
    app = sdd_pre
    for lit in pysdd_s0:
        app = manager.conjoin(app, lit)
    wmc = app.wmc(log_mode=False)
    wmc.propagate()
    data['A(s0)'] += [app.model_count()]


def compute_symbol_ids(count, selects_, fluents):
    """ Assign IDs to all the symbols that will be involved in the SDD """
    symbols = {}
    # Iterate from most- to least-used variables
    scores = {x: 0 for x in selects_.keys()}
    scores.update(count)
    scored = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for x, _ in scored:
        for s in selects_[x]:
            sdd_var_id = len(symbols) + 1  # Start IDs with 1
            symbols[s] = sdd_var_id

    for p in fluents:
        sdd_var_id = len(symbols) + 1
        symbols[p] = sdd_var_id

    return symbols


def translate_to_pysdd(phi, syms, manager):
    if isinstance(phi, CompoundFormula):
        sub = [translate_to_pysdd(psi, syms, manager) for psi in phi.subformulas]
        if phi.connective == Connective.Not:
            return -sub[0]
        elif phi.connective == Connective.And:
            return sub[0] & sub[1]
        elif phi.connective == Connective.Or:
            return sub[0] | sub[1]
    elif isinstance(phi, Atom):
        return manager.literal(syms[phi])
    raise RuntimeError(f"Could not translate {phi}")


def setup_sdd_manager(nvars):
    """ Set up the SDD manager with some sensible defaults"""
    # set up vtree and manager
    var_order = list(range(1, nvars + 1))  # lexicographic
    # var_order = list(range(nvars,0,-1)) # state atoms first
    vtree_type = "right"  # OBDD-style

    vtree = Vtree(nvars, var_order, vtree_type)
    return SddManager(var_count=nvars, auto_gc_and_minimize=1, vtree=vtree)


def process_problem(problem, max_size=20000000):
    # Make sure the initial state has some associated evaluator:
    problem.init.evaluator = problem.init.evaluator or evaluate

    data = defaultdict(list)
    actions = scout_actions(problem, data)
    _, statics = classify_symbols(problem)

    for action in actions:
        process_schema(problem, statics, action, data, max_size)
    return data
