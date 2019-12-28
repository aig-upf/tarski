import io
import logging
import operator
import itertools
import os
import time
from collections import defaultdict
from functools import reduce
from pathlib import Path

from .util import stdout_redirector
from ..utils import resources
from ..utils.serialization import serialize_atom
from ..evaluators.simple import evaluate
from ..syntax import lor, neg, Atom, BuiltinPredicateSymbol, CompoundFormula, Connective, Variable, Tautology, builtins
from ..syntax.ops import flatten
from ..grounding.ops import approximate_symbol_fluency
from ..grounding.common import StateVariableLite
from ..fstrips import fstrips
from ..fstrips.representation import collect_literals_from_conjunction

from tarski.modules import import_sdd
sdd = import_sdd()


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
        # logging.info(f'{action.ident()}:\t{" * ".join(map(str, cardinalities))} = {ngroundings} potential groundings')
        if ngroundings == 0:
            empty.append(action.name)
        else:
            actions.append(action)
            data['action'] += [action.ident()]
            data['arity'] += [len(action.parameters)]
            data['groundings'] += [ngroundings]

    logging.info(f"{len(actions)} actions to ground; actions discarded: {empty}")
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


def create_grounding_constraints(selects, statics, init, atoms, reachable_vars=None):
    """ Create the core grounding constraints, taking into account static predicate information.
    For each predicate p(X_1, ..., X_n) in the precondition of the action, a constraint is created with form:

        select(X_1, c_1) and ... and select(X_n, c_n)  --> p(c_1, ..., c_n)

    where the c_i's are the values that the variables X_i can take.

     - selects: select atoms
     - statics: set of static predicate symbols
     - init: initial state model
     - precs: set of action precondition atoms
     - reachable_vars: (optional) set of reachable vars to constrain the possible groundings
    """
    fluents = set()
    count = defaultdict(int)
    constraints = []
    nullary_atoms, unary_atoms = [], defaultdict(list)
    for atom in atoms:
        lang = atom.predicate.language  # The language of the original problem
        ar = atom.predicate.arity

        for x in atom.subterms:
            count[x.symbol] += 1

        if ar == 0:
            nullary_atoms.append(atom)

        argument_selects = [selects[sub.symbol] for sub in atom.subterms]
        for selectlist in itertools.product(*argument_selects):
            # Note that this will have one iteration with selectlist=() for nullary atoms
            values = [lang.get_constant(s.subterms[-1].symbol) for s in selectlist]
            head = atom.predicate(*values)
            body = [neg(h) for h in selectlist]

            if ar == 1:
                assert len(selectlist) == 1
                affected_select = selectlist[0]
                unary_atoms[affected_select].append(head)

            # We disinguish the following cases:
            # (1) The atom p is a fluent: post a constraint -sel(x1, z1) or ... or -sel(xn, zn) or p(x1, ..., xn)
            # (2) The atom p is static, and holds in the initial state: no need to post anything
            # (3) The atom p is static, but doesn't hold in init: then post -sel(x1, z1) or ... or -sel(xn, zn)
            # Note that (2) and (3) are just specializations of (1)

            if atom.predicate in statics:
                if init[head]:  # Case (2): p is static and holds in init
                    continue
                else:  # Case (3): p is static and doesn't hold in init
                    assert body
                    constraints += body if len(body) == 1 else [lor(*body)]
            else:  # Case (1): p is a fluent
                svar = StateVariableLite.from_atom(head)
                if reachable_vars is None or svar in reachable_vars:
                    fluents.add(head)
                    constraints.append(lor(*body, head) if body else head)
                else:
                    # If we have a constraint of the style
                    # select(X_1, c_1) and ... and select(X_n, c_n)  --> p(c_1, ..., c_n)
                    # and atom p(c_1, ..., c_n) has been proven unreachable, then we simply add the (negated) antecedent
                    # of the implication

                    # TODO This assert is probably incorrect, if body is empty, then we should simply conclude
                    #      that the schema can yield no applicable ground action
                    assert body
                    constraints += body if len(body) == 1 else [lor(*body)]

    return constraints, count, fluents, nullary_atoms, unary_atoms


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
    """ Create the atoms of the form select(X, x) for each action parameter X and possible value x in its domain.
     Each such atom is paired with constraints of the form
         select(X, x1) or ... or select(X, xn); for all values x1, ..., xn
         not select(X, x_i) or not select(X, x_j); for all pairs of values x_i, x_j
     """
    select_constraints = []

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
        assert len(sel) > 0
        if len(sel) == 1:
            # If parameter X has one single possible value V, then selected(X, V) must be true
            select_constraints.append(sel[0])
            continue

        select_constraints.append(lor(*sel, flat=True))
        select_constraints.extend(lor(neg(v1), neg(v2)) for v1, v2 in itertools.combinations(sel, 2))

    return selects, sum(len(s) for s in selects.values()), select_constraints


def preprocess_parameter_domains(action, statics, domains, init, reachable_vars):
    """ Simplify the precondition formula and prune the potential domains of action parameters based on statics,
    reachability information (if available), and some basic CSP techniques. """
    flattened = flatten(action.precondition)
    constraints = collect_literals_from_conjunction(flattened)
    if constraints is None:
        # Check that we have have a plain conjunction of atoms (constraints); if not, abort
        raise UnsupportedFormalism(f'Cannot process complex precondition of action "{action.ident()}":'
                                   f'\n\t{action.precondition}"')
    constraints = list(constraints)  # Just to make sure iteration is always in the same order
    using_reachability_info = reachable_vars is not None

    # Index the values that can go on each position of each precondition atom according to the initial state
    # Note that this is equivalent to creating a DB index for each column in each table (=atom)
    lang = action.language
    extensions = init.list_all_extensions()
    indexed_values = {}
    for k in extensions.keys():
        symbol = lang.get(k[0])
        indexed_values[k[0]] = [set() for _ in range(symbol.uniform_arity())]
    for signature, ext in extensions.items():
        sname = signature[0]
        for tup in ext:
            for pos, value in enumerate(tup):
                indexed_values[sname][pos].add(value.name)

    # If an overapproximation of reachable (fluent) atoms was provided, add those values to the column indexes.
    # In this case, the column indexes represent an overapproximation of all possible values that can ever be reached.
    # Otherwise, they only represent that for the static atoms
    if using_reachability_info:
        for v in reachable_vars:
            sname = v.symbol.name
            for pos, value in enumerate(v.binding):
                indexed_values[sname][pos].add(value.name)

    # Create yet another index with the role that each parameter plays in each (non-builtin) atom of the precondition,
    # so e.g. parameter_roles[x] = (p, i) means that action parameter x appears in the i-th position of precondition
    # atom p
    parameter_roles = defaultdict(list)
    eq_atoms, standard_constraints = set(), list()
    for i, (atom, polarity) in enumerate(constraints, start=0):
        predicate = atom.predicate

        if predicate.symbol in builtins.get_equality_predicates():
            # If the atom is an (in-)equality atom, record it as such
            eq_atoms.add(atom if polarity else builtins.negate_builtin_atom(atom))
        else:
            assert polarity is True
            standard_constraints.append(atom)
            for j, st in enumerate(atom.subterms, start=0):
                assert isinstance(st, Variable)
                # TODO This could be improved to deal also with static atoms p(c), where c is a constant, not a variable
                parameter_roles[st.symbol].append((atom, j))  # param st.symbol appears in constraint atom, position j

    # Prune away any domain value that is not arc-consistent, i.e. such that there is some precondition atom for which
    # that value cannot be extended into a full assignment that fulfills the constraint
    for parameter in action.parameters:
        nbefore = len(domains[parameter.symbol])  # Just for debugging purposes
        for atom, position in parameter_roles[parameter.symbol]:
            if atom.predicate not in statics and not using_reachability_info:
                # If we are not using reachability info, we cannot prune any domain value for fluents
                continue
            assert atom.subterms[position].symbol == parameter.symbol
            values = indexed_values[atom.predicate.name][position]
            domains[parameter.symbol].intersection_update(values)

        # print(f'{nbefore - len(domains[parameter.symbol])} objects pruned from domain of parameter '
        #       f'"{parameter}" for being arc-inconsistent')

    # Separate and return those atoms that are not builtin and that, if static, have arity > 1
    # (arity 1 statics have also played their role in shaping the allowed domains, so no need to consider them further)
    removable_subformulas = set(c for c in standard_constraints if c.predicate.arity == 1 and c.predicate in statics)
    active = [c for c in standard_constraints if c not in removable_subformulas]
    if len(active) == 0:
        active = [Tautology]

    return domains, active, eq_atoms


def reshapen_vtree(alpha, manager):
    # Some experiments customizing the shape of the vtree
    vtree = manager.vtree()

    # ref alpha (so it is not gc'd)
    alpha.ref()

    # garbage collect (no dead nodes when performing vtree operations)
    print(f"Collecting garbage in SDD with {manager.dead_count()} dead nodes")
    manager.garbage_collect()
    print(f"dead sdd nodes = {manager.dead_count()}")

    print("left rotating ... ")
    succeeded = vtree.right().rotate_left(manager, 0)
    print("succeeded!" if succeeded == 1 else "did not succeed!")

    print(f"Collecting garbage in SDD with {manager.dead_count()} dead nodes")
    manager.garbage_collect()
    print(f"dead sdd nodes = {manager.dead_count()}")

    print("left rotating ... ")
    succeeded = manager.vtree().right().rotate_left(manager, 0)
    print("succeeded!" if succeeded == 1 else "did not succeed!")

    print(f"Collecting garbage in SDD with {manager.dead_count()} dead nodes")
    manager.garbage_collect()
    print(f"dead sdd nodes = {manager.dead_count()}")

    print("left rotating ... ")
    succeeded = manager.vtree().right().rotate_left(manager, 0)
    print("succeeded!" if succeeded == 1 else "did not succeed!")

    # deref alpha, since ref's are no longer needed
    alpha.deref()

    # the root changed after rotation, so get the manager's vtree again
    # this time using root_location
    # manager_vtree = manager.vtree()


def compile_action_schema(problem, statics, action, data, max_size,
                          conjoin_with_init=False, var_ordering=None, reachable_vars=None,
                          sdd_incr_minimization_time=None):
    print(f'Processing action "{action.ident()}"')
    with resources.timing(f"\tGenerating theory"):
        data['instance'] += [problem.name]

        # Set up a metalanguage for the encoding of the SDD applicability theory
        metalang, parameters, domains = setup_metalanguage(action)

        domains, precondition_nonbuiltin_atoms, eq_atoms =\
            preprocess_parameter_domains(action, statics, domains, problem.init, reachable_vars)

        if any(len(dom) == 0 for dom in domains.values()):
            # Some action parameter has empty associated domain, hence no ground action will result from this
            logging.info(f'Action "{action.ident()}" has parameter with empty domain, hence can be pruned')
            report_theory(data, [], [], [], [], 0,
                          sdd_sizes=0, sdd_size=0, as0=0, t0=None)
            manager, false = setup_false_sdd_manager()  # This will return a "False" precondition
            return manager, false, {}, []

        selects, nvars, select_constraints = generate_select_atoms(action, metalang, parameters, domains)

        eq_constraints = create_equality_constraints(eq_atoms, selects)

        grounding_constraints, count, fluents, nullary_atoms, unary_atoms = create_grounding_constraints(
            selects, statics, problem.init, precondition_nonbuiltin_atoms, reachable_vars=reachable_vars)

        nvars += len(fluents)

        symbols = compute_symbol_ids(count, selects, fluents)

    if var_ordering == "arity":  # Compute a good variable ordering
        sdd_vars_from_nullaries = set(symbols[a] for a in nullary_atoms)
        sdd_vars_from_unaries = []
        for var, select_atoms in unary_atoms.items():
            sdd_vars_from_unaries += [symbols[var]] + [symbols[a] for a in select_atoms]

        remaining = [i for i in range(1, nvars + 1) if
                     i not in sdd_vars_from_nullaries and i not in set(sdd_vars_from_unaries)]

        var_order = list(sdd_vars_from_nullaries) + sdd_vars_from_unaries + remaining
        manager = setup_sdd_manager(nvars, var_order=var_order)
    else:
        if var_ordering is not None and var_ordering != "default":
            raise RuntimeError(f'Variable ordering type "{var_ordering} not recognised')
        manager = setup_sdd_manager(nvars)

    allconstraints = list(itertools.chain(select_constraints, eq_constraints, grounding_constraints))
    # allconstraints = list(itertools.chain(atoms, select_constraints, eq_constraints, nonatoms))
    # allconstraints = list(itertools.chain(eq_constraints, grounding_constraints, select_constraints))
    # alltranslated = [translate_to_pysdd(c, symbols, manager) for c in allconstraints]

    if not allconstraints:
        # No constraints at all must mean an action schema with no parameters and and empty precondition
        logging.info(f'Action "{action.ident()}" has an empty SDD theory')
        report_theory(data, select_constraints, eq_constraints, fluents, grounding_constraints, nvars,
                      sdd_sizes=0, sdd_size=0, as0=1, t0=None)
        manager, true = setup_true_sdd_manager()  # This will return a "False" precondition
        return manager, true, {}, []

    sdd_sizes = []
    failed = False

    t0 = time.time()

    with resources.timing(f"\tBuilding SDD for {manager.var_count()} variables and {len(allconstraints)} constraints"):
        precondition_sdd = translate_to_pysdd(allconstraints[0], symbols, manager)

        for c in allconstraints[1:]:
            precondition_sdd = precondition_sdd & translate_to_pysdd(c, symbols, manager)
            size = precondition_sdd.size()
            if sdd_incr_minimization_time is not None and sdd_incr_minimization_time > 0:
                minimize_sdd(manager, precondition_sdd, int(sdd_incr_minimization_time))
            size = (size, precondition_sdd.size())
            sdd_sizes.append(size)

            if size[-1] > max_size:
                failed = True
                break

    # reshapen_vtree(precondition_sdd, manager)

    # sdd_clauses = sdd_ground + sdd_eq + sdd_dom
    # plot_sdd_size(the_task.domain_name, the_task.name, act, sdd_sizes, sdd_clauses, sdd_eq, sdd_ground, sdd_dom)

    if conjoin_with_init and not failed:
        s0_literals = [p if problem.init[p] else neg(p) for p in fluents]
        # print(f'\tRelevant literals on the initial state: {s0_literals}')
        pysdd_s0 = [translate_to_pysdd(l, symbols, manager) for l in s0_literals]
        assert pysdd_s0

        # Condition the precondition formula to the initial state
        # see https://pysdd.readthedocs.io/en/latest/examples/conditioning.htm
        app = reduce(manager.conjoin, pysdd_s0, precondition_sdd)
        # wmc = app.wmc(log_mode=False)
        # wmc.propagate()
        as0 = app.model_count()

        act_str = action.ident()
        print(f'\tModel count for action {act_str} on initial state: {as0}')
        if as0 > 20:
            print(f'\tAction {act_str} has too many models ({as0}) on the initial state to list them all here')
        else:
            try:
                for i, model in enumerate(app.models(), start=1):
                    binding = compute_binding(model, selects, symbols)
                    print(f'\tModel #{i} maps to applicable ground action {compute_ground_action_name(act_str, binding)}')
            except ValueError:
                print(f'\tNo more models found for action {act_str}')

            # Now let's do the same but with out models implementation instead of the conjoin+enumerate approach
            s0_literal_ids = {varid(node.literal): truth_value(node.literal) for node in pysdd_s0}
            for i, model in enumerate(models(precondition_sdd, s0_literal_ids), start=1):
                binding = compute_binding(model, selects, symbols)
                print(f'\t[Fixed] Model #{i} maps to applicable ground action {compute_ground_action_name(act_str, binding)}')

    else:
        as0 = None

    size = sdd_sizes[-1] if sdd_sizes else 0
    report_theory(data, select_constraints, eq_constraints, fluents, grounding_constraints, nvars,
                  sdd_sizes=sdd_sizes, sdd_size=size, as0=as0, t0=t0)

    return manager, precondition_sdd, symbols, allconstraints


def compute_binding(model, selects, symbols):
    binding = dict()
    for parameter, selectatoms in selects.items():
        chosen = [selatom for selatom in selectatoms if model[symbols[selatom]] == 1]
        assert len(chosen) == 1
        assert parameter not in binding
        binding[parameter] = chosen[0].subterms[1].symbol
    return binding


def compute_ground_action_name(action, binding):
    # An inefficient and dirty hack to get the name of the ground action :-)
    groundaction_string = action
    for x, v in binding.items():
        groundaction_string = groundaction_string.replace(x, v)
    return groundaction_string


def report_theory(data, select_constraints, eq_constraints, fluents, grounding_constraints, nvars,
                  sdd_sizes, sdd_size, as0, t0):
    data['selects'] += [nvars]
    data['atoms'] += [len(fluents)]
    data['DOM'] += [len(select_constraints)]
    data['EQ'] += [len(eq_constraints)]
    data['GROUND'] += [len(grounding_constraints)]
    data['nclauses'] += [len(select_constraints) + len(eq_constraints) + len(grounding_constraints)]
    data['nvars'] += [nvars]
    data['sdd_sizes'] += [sdd_sizes]
    data['sdd_size'] += [sdd_size]
    data['A(s0)'] += [as0]
    data['runtime'] += [None] if t0 is None else  [time.time() - t0]


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
            return reduce(manager.conjoin, sub, manager.true())
        elif phi.connective == Connective.Or:
            return reduce(manager.disjoin, sub, manager.false())
    elif isinstance(phi, Atom):
        return manager.literal(syms[phi])
    raise RuntimeError(f"Could not translate {phi}")


def validate_var_order(nvars, var_order):
    assert len(var_order) == nvars
    assert all(x in set(var_order) for x in range(1, nvars + 1))


def setup_sdd_manager(nvars, var_order=None):
    """ Set up the SDD manager with some sensible defaults"""
    # set up vtree and manager
    var_order = var_order or list(range(1, nvars + 1))  # lexicographic
    validate_var_order(nvars, var_order)
    # var_order = list(range(nvars,0,-1)) # state atoms first
    vtree_type = "right"  # OBDD-style
    # vtree_type = "balanced"
    # vtree_type = "left"
    # vtree_type = "random"

    vtree = sdd.Vtree(nvars, var_order, vtree_type)
    return sdd.SddManager(var_count=nvars, auto_gc_and_minimize=0, vtree=vtree)


def setup_false_sdd_manager():
    manager = setup_sdd_manager(1)  # The library doesn't allow for the creation of a manager with 0 vars
    precondition = manager.false()
    return manager, precondition


def setup_true_sdd_manager():
    manager = setup_sdd_manager(1)  # The library doesn't allow for the creation of a manager with 0 vars
    precondition = manager.true()
    return manager, precondition


def process_problem(problem, max_size=20000000,
                    serialization_directory=None, conjoin_with_init=False,
                    graphs_directory=None, sdd_minimization_time=None,
                    var_ordering=None, reachable_vars=None,
                    sdd_incr_minimization_time=None):
    # Make sure the initial state has some associated evaluator:
    problem.init.evaluator = problem.init.evaluator or evaluate

    data = defaultdict(list)
    actions = scout_actions(problem, data)
    _, statics = approximate_symbol_fluency(problem)

    for action in actions:
        manager, node, symbols, theory = compile_action_schema(
            problem, statics, action, data, max_size, conjoin_with_init=conjoin_with_init,
            var_ordering=var_ordering, reachable_vars=reachable_vars, sdd_incr_minimization_time=sdd_incr_minimization_time)

        print(f"\tSDD has {node.size()} nodes")
        if sdd_minimization_time is not None and sdd_minimization_time > 0:
            minimize_sdd(manager, node, sdd_minimization_time)

        if graphs_directory is not None:
            print_sdd(action, graphs_directory, manager, node, symbols, theory)

        if serialization_directory is not None:
            store_schema_data(action, manager, node, symbols, serialization_directory)

    return data


def print_sdd(action, directory, manager, node, symbols, theory):
    import subprocess
    import string
    if not Path(directory).is_dir():
        raise Exception(f"Directory '{directory}' does not exist")

    var_mapping_filename = f"{directory}/{action.name}-theory.txt"
    sdd_stats_filename = f"{directory}/{action.name}-sdd-stats.txt"
    sdd_dot_filename = f"{directory}/sdd-{action.name}.dot"
    sdd_png_filename = f"{directory}/sdd-{action.name}.png"
    vtree_dot_filename = f"{directory}/vtree-{action.name}.dot"
    vtree_png_filename = f"{directory}/vtree-{action.name}.png"

    def varname(i):
        # Variables are 1-indexed
        return f'x{i}' if i-1 >= len(string.ascii_uppercase) else string.ascii_uppercase[i-1]

    print(f'\tPrinting SDD graphic information to \n\t"{sdd_png_filename}", \n\t"{vtree_png_filename}", '
          f'\n\t{var_mapping_filename},\n\t{sdd_stats_filename}')
    with open(var_mapping_filename, "w") as f:
        varidxs = sorted(symbols.values())
        inv = {v: k for k, v in symbols.items()}
        print('\n'.join(f"{varname(i)}: {inv[i]}" for i in varidxs), file=f)
        print(f'\nLogical theory for action theory {action.ident()}:', file=f)
        print(f'Action precondition: {action.precondition}', file=f)
        print('\n'.join(f"{c}" for c in theory), file=f)

    with open(sdd_dot_filename, "w") as f:
        print(node.dot(), file=f)
    with open(vtree_dot_filename, "w") as f:
        print(manager.vtree().dot(), file=f)
    with open(sdd_png_filename, "w") as f:
        subprocess.call(f"dot -Tpng {sdd_dot_filename}".split(), stdout=f)
    with open(vtree_png_filename, "w") as f:
        subprocess.call(f"dot -Tpng {vtree_dot_filename}".split(), stdout=f)
    with open(sdd_stats_filename, "w") as f:
        buf = io.BytesIO()
        with stdout_redirector(buf):
            manager.print_stdout()
        print(buf.getvalue().decode('utf-8'), file=f)


def minimize_sdd(manager, node, sdd_minimization_time, verbose=False):
    node.ref()
    manager.set_vtree_search_time_limit(sdd_minimization_time)
    manager.set_vtree_search_convergence_threshold(0.1)
    if verbose:
        with resources.timing(f"\tMinimizing SDD ({node.size()} nodes) for up to {sdd_minimization_time} sec."):
            manager.minimize_limited()
        print(f"\tAfter first minimization pass, SDD has {node.size()} nodes")
    else:
        manager.minimize_limited()

    node.deref()
    return node


def store_schema_data(action, manager, node, symbols, path):
    """ Serialize under the given path (expected to be a directory) relevant data on the SDD corresponding to the given
     action schema, including the full SDD plus some bookkeeping data such as the correspondence between the atoms
     *relevant* to the schema and the SDD variable IDs. """
    if not Path(path).is_dir():
        raise Exception(f"Directory '{path}' does not exist")

    # sanitized = action.name.replace('-', '_')
    sanitized = action.name.lower()
    manager.save(os.path.join(path, f'{sanitized}.manager.sdd').encode(), node)
    manager.vtree().save(os.path.join(path, f'{sanitized}.vtree.sdd').encode())

    paramidxs = defaultdict(dict)
    with open(os.path.join(path, f'{sanitized}.atoms.data'), 'w') as f:
        for atom, atomid in symbols.items():
            if atom.predicate.symbol == '_select_':  # e.g. _select_(?x, b1)
                # Here we just collect the info related to the select atoms, we'll serialize it later
                variable, value = atom.subterms
                param = action.parameters.index(variable.symbol)
                assert value.symbol not in paramidxs[param]
                paramidxs[param][value.symbol] = atomid
            else:
                # Note that this will only store info about atoms that are relevant to the action schema.
                print(f'{serialize_atom(atom)}:{atomid}', file=f)

    with open(os.path.join(path, f'{sanitized}.bindings.data'), 'w') as f:
        for i, _ in enumerate(action.parameters):
            param_bindings = paramidxs[i]
            line = ','.join(f'{o}:{atomid}' for o, atomid in param_bindings.items())
            print(line, file=f)


def join_models(model1, model2):
    """ Concatenate two SDD models. Assumes that both dictionaries do not share keys.
    """
    model = model1.copy()
    model.update(model2)
    return model


def truth_value(literal):
    assert literal != 0
    return False if literal < 0 else True


def varid(literal):
    assert literal != 0
    return abs(literal)


def node_is_false(node, fixed):
    if not node.is_literal():  # A decision node, we cannot determine its truth value
        return False
    vid = varid(node.literal)

    return vid in fixed and fixed[vid] != truth_value(node.literal)


def models(node, fixed, vtree=None):
    """
    Enumerate of models of the given SDD, restricted to the values given in `fixed`, which  maps variable ids
    to truth values (True, False) for those variables whose truth value we want to be fixed in the returned models.

    Mostly copy-pasted from the model enumeration routine from the original pysdd library in
        https://github.com/wannesm/PySDD/blob/5a301a961a87cef07e13b2bfc1bef01abd46e879/pysdd/sdd.pyx#L247,
    but modified to accept a mapping of fixed values.
    """

    if node.is_false():
        raise ValueError("False has no models")
    if vtree is None:
        if node.is_true():
            vtree = node.manager.vtree()
        else:
            vtree = node.vtree()
    if vtree.is_leaf():
        var = vtree.var()
        if node.is_true():
            if var in fixed:
                yield {var: int(fixed[var])}
            else:
                yield {var: 0}
                yield {var: 1}
        elif node.is_literal():
            assert var not in fixed or fixed[var] == truth_value(node.literal)  # Just in case
            sign = 0 if node.literal < 0 else 1
            yield {var: sign}
    else:
        if node.is_true():  # sdd is true
            for left in models(node, fixed, vtree.left()):
                for right in models(node, fixed, vtree.right()):
                    yield join_models(left, right)
        elif node.vtree() == vtree:
            for prime, sub in node.elements():
                if sub.is_false():
                    continue

                if node_is_false(sub, fixed) or node_is_false(prime, fixed):
                    continue

                for left in models(prime, fixed, vtree.left()):
                    for right in models(sub, fixed, vtree.right()):
                        yield join_models(left, right)
        else:  # fill in gap in vtree
            true_sdd = node.manager.true()
            if sdd.Vtree.is_sub(node.vtree(), vtree.left()):
                for left in models(node, fixed, vtree.left()):
                    for right in models(true_sdd, fixed, vtree.right()):
                        yield join_models(left, right)
            else:
                for left in models(true_sdd, fixed, vtree.left()):
                    for right in models(node, fixed, vtree.right()):
                        yield join_models(left, right)
