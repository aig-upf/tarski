
import logging
import operator
import itertools
from collections import defaultdict
from functools import reduce

try:
    from pysdd.sdd import Vtree, SddManager
except ImportError as err:
    raise RuntimeError("Could not import pysdd - sdd module not available") from None


from ..errors import DuplicatePredicateDefinition, DuplicateConstantDefinition
from ..evaluators.simple import evaluate
from ..syntax import symref, lor, neg, Atom, BuiltinPredicateSymbol, CompoundFormula, Connective, Variable
from ..syntax.ops import flatten, collect_unique_nodes
from ..grounding import ProblemGrounding
from ..fstrips import fstrips


class MaxSizeError(Exception):
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


def is_static(a: Atom, statics):
    return a.predicate in statics


def compute_statics(problem):
    index = ProblemGrounding(problem)
    index.process_symbols(problem)
    fluents, statics = index.compute_fluent_and_statics()
    return statics


def create_equality_constraints(equalities, selects):
    """ Return a list of equality constraints of the form """
    eq_constraints = []
    for s, p in equalities.items():
        lhs, rhs = s.expr.subterms
        # TODO The code below needs to be adapted to cases as atoms "X != c", where X is a parameter and c a constant
        if any(not isinstance(v, Variable) for v in (lhs, rhs)):
            raise NotImplementedError()
        sel_lhs = selects[lhs.symbol]
        sel_rhs = selects[rhs.symbol]
        for l, r in itertools.product(sel_lhs, sel_rhs):
            if l.subterms[-1].symbol == r.subterms[-1].symbol:
                if p:
                    eq_constraints += [lor(neg(l), r), lor(neg(r), l)]
                    # Let us have a strong abort here to inspect preconditions of this type (i.e.: a precondition X=Y
                    # on two different action parameters X and Y), if they every arise, as that would be quite
                    # surprising to me. If they indeed occur in practice, it might be better to deal with them by pre-
                    # compiling them away?
                    raise RuntimeError('Weird precondition atom "X=Y". Might be worth inspecting it.')
                eq_constraints.append(lor(neg(l), neg(r)))
    return eq_constraints


def create_grounding_constraints(selects, statics, init, atoms, state_atoms):
    """ Create the core grounding constraints, taking into account static predicate information.
     For each predicate p(X_1, ..., X_n) in the precondition of the action, a constraint is created with form:

        select(X_1, z_1) and ... and select(X_n, z_n)  --> p(X_1, ..., X_n)


         - count: table keeping track of how often a variable appears on a clause
         - selects: select atoms
         - statics: set of static predicate symbols
         - init: initial state model
         - precs: set of action precondition atoms
         - state_atoms: set of (state) atoms relevant to the action
    """
    count = defaultdict(int)
    constraints = []
    for atom in atoms:
        lang = atom.predicate.language  # The language of the original problem
        for x in atom.subterms:
            count[x.symbol] += 1
        SX = [selects[sub.symbol] for sub in atom.subterms]
        for selectlist in itertools.product(*SX):
            # We want to post: -sel(x1, z1) or ... or -sel(xn, zn) or p(x1, ..., xn)
            values = [lang.get_constant(s.subterms[-1].symbol) for s in selectlist]
            head = atom.predicate(*values)
            body = [neg(h) for h in selectlist]
            arity = len(body)
            # if len(body) == 1:
            #     body = body[0]

            if not is_static(atom, statics):
                if symref(head) not in state_atoms:
                    state_atoms.add(symref(head))
                constraints.append(lor(*body, head) if arity > 0 else head)
                continue

            if init[head]:  # If the atom is static and holds in the initial state, no grounding constraint is necessary
                continue

            assert body
            if len(body) == 1:
                constraints += body
            else:
                constraints += [lor(*body)]
    return constraints, count


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

        domain_constraints.append(lor(*sel, flat=True))
        domain_constraints.extend(lor(neg(v1), neg(v2)) for v1, v2 in itertools.combinations(sel, 2))

    return selects, sum(len(s) for s in selects.values()), domain_constraints


def create_domain_constraints(action, selects):
    """ Create for each action parameter X constraints of the form
        [OR_{x in dom(X)} sel(X, x)] AND [AND_{x, y in dom(X)} (-sel(X, x) OR -sel(X, y))]
    """
    dom_constraints = []
    for parameter in action.parameters:
        Sx = selects[symref(parameter)]
        if len(Sx) == 1:  # note the possibility of singletons
            dom_constraints += [Sx[0]]
            continue
        dom_constraints += [lor(*Sx)]
        for v1, v2 in itertools.combinations(Sx, 2):
            dom_constraints += [lor(neg(v1), neg(v2))]
    return dom_constraints


def extract_equalities(phi):
    """ Extract a table with action parameter equalities of the form X=Y, X!=Y"""
    return collect_unique_nodes(phi, lambda x: isinstance(x, Atom) and x.predicate.symbol in
                                               (BuiltinPredicateSymbol.EQ, BuiltinPredicateSymbol.NE))


def prune_parameter_domains(precondition, statics, domains, init):
    """ """
    flattened = flatten(precondition)
    if flattened.connective != Connective.And or not all(isinstance(sub, Atom) for sub in flattened.subformulas):
        return precondition  # If we don't have a plain conjunction of atoms, we don't do any pruning

    # At the moment we only enforce node consistency for (static, of course) unary constraints
    # TODO Might be worth achieving arc-consistency taking all constraints into account

    removable_subformulas = set()
    for atom in flattened.subformulas:
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
            if init[predicate(lang.get_constant(obj))] is False:
                unsatisfied.add(obj)
        # print(f"Objects {unsatisfied} can be pruned for node-inconsistency reasons from the extension of {predicate}")
        domains[parameter].difference_update(unsatisfied)  # Remove the values from the domains
        removable_subformulas.add(atom)  # Mark the static atom to be removed from the precondition

    flattened.subformulas = tuple(sub for sub in flattened.subformulas if sub not in removable_subformulas)

    return domains, flattened


def process_schema(problem, statics, action, data, max_size):
    # print(f"Processing action schema:\n{action}")
    data['instance'] += [problem.name]

    # Set up a metalanguage for the encoding of the SDD applicability theory
    metalang, parameters, domains = setup_metalanguage(action)

    domains, precondition = prune_parameter_domains(action.precondition, statics, domains, problem.init)

    selects_, nvars_, dom_constraints_ = generate_select_atoms(action, metalang, parameters, domains)
    data['selects'] += [nvars_]
    # dom_constraints = create_domain_constraints(action, selects) # TODO Remove
    equalities = extract_equalities(precondition)
    prec_atoms = collect_unique_nodes(precondition, lambda x: isinstance(x, Atom) and not x.predicate.builtin)

    eq_constraints = create_equality_constraints(equalities, selects_)
    state_atoms = set()
    # Create the constraints of the form
    #     select(X1, x1) and ... and select (Xn, xn) --> p(x1, ..., xn)
    # for each atom p in the precondition conjunction.

    grounding_constraints, count = create_grounding_constraints(
        selects_, statics, problem.init, prec_atoms, state_atoms)
    nvars_ += len(state_atoms)

    data['atoms'] += [len(state_atoms)]
    data['DOM'] += [len(dom_constraints_)]
    data['EQ'] += [len(eq_constraints)]
    data['GROUND'] += [len(grounding_constraints)]
    data['nclauses'] += [len(dom_constraints_) + len(eq_constraints) + len(grounding_constraints)]
    data['nvars'] += [nvars_]

    symbols = compute_symbol_ids(count, selects_, state_atoms)

    manager = setup_sdd_manager(nvars_)

    sdd_ground = [translate_to_pysdd(c, symbols, manager) for c in grounding_constraints]
    sdd_eq = [translate_to_pysdd(c, symbols, manager) for c in eq_constraints]
    sdd_dom = [translate_to_pysdd(c, symbols, manager) for c in dom_constraints_]
    sdd_pre = sdd_dom[0]
    sdd_sizes = []

    failed = False
    # t0 = time.time()
    try:

        for i in range(1, len(sdd_dom)):
            sdd_pre = sdd_pre & sdd_dom[i]
            sdd_sizes += [sdd_pre.size()]
            if sdd_sizes[-1] > max_size:
                raise MaxSizeError()

        for i in range(len(sdd_eq)):
            sdd_pre = sdd_pre & sdd_eq[i]
            sdd_sizes += [sdd_pre.size()]
            if sdd_sizes[-1] > max_size:
                raise MaxSizeError()

        for i in range(len(sdd_ground)):
            sdd_pre = sdd_pre & sdd_ground[i]
            sdd_sizes += [sdd_pre.size()]
            if sdd_sizes[-1] > max_size:
                raise MaxSizeError()

    except MaxSizeError:
        failed = True
    # tf = time.time()
    # data_df['runtime'] += [tf - t0]

    # sdd_clauses = sdd_ground + sdd_eq + sdd_dom
    # plot_sdd_size(the_task.domain_name, the_task.name, act, sdd_sizes, sdd_clauses, sdd_eq, sdd_ground, sdd_dom)

    data['sdd_sizes'] += [sdd_sizes]
    data['sdd_size'] += [sdd_sizes[-1]]

    if not failed:
        s = []
        for p in state_atoms:
            if problem.init[p.expr]:
                s += [p.expr]
            else:
                s += [neg(p.expr)]
        # MRJ: code below is good but if state has more than 255 literals we
        # exceed the maximal recursion depth allowed by the interpreter
        # s = land(*s)
        # sdd_s = translate(s, symbols, manager)
        s = [translate_to_pysdd(l, symbols, manager) for l in s]
        sdd_s = s[0]
        for l in s[1:]:
            sdd_s = sdd_s & l
        app = sdd_pre & sdd_s
        wmc = app.wmc(log_mode=False)
        wmc.propagate()
        data['A(s0)'] += [app.model_count()]
    else:
        data['A(s0)'] += [None]


def compute_symbol_ids(count, selects_, state_atoms):
    symbols = {}
    sdd_var_id = 1
    inv_symbols = {}
    scored_x = [(v, x) for x, v in count.items()]
    scored_x.sort(key=lambda x: x[0], reverse=True)
    for _, x in scored_x:
        for s in selects_[x]:
            symbols[symref(s)] = sdd_var_id
            inv_symbols[sdd_var_id] = s
            sdd_var_id += 1
    for p in state_atoms:
        symbols[p] = sdd_var_id
        inv_symbols[sdd_var_id] = p
        sdd_var_id += 1
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
        sdd_lit = manager.literal(syms[symref(phi)])
        return sdd_lit
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
    statics = compute_statics(problem)

    for action in actions:
        process_schema(problem, statics, action, data, max_size)
    return data
