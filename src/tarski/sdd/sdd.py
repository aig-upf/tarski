import logging
import operator
import itertools
from collections import OrderedDict, defaultdict
from functools import reduce

from tarski.grounding import ProblemGrounding

try:
    from pysdd.sdd import Vtree, SddManager
except ImportError as err:
    raise RuntimeError(f"Could not import pysdd - sdd module not available")


from tarski.errors import DuplicatePredicateDefinition, DuplicateConstantDefinition
from tarski.evaluators.simple import evaluate
from tarski.syntax import symref, lor, neg, Atom, BuiltinPredicateSymbol, CompoundFormula, Connective


class MaxSizeError(Exception):
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


def extract_regular_atoms(phi, atoms):
    if isinstance(phi, Atom):
        if phi.predicate.symbol != BuiltinPredicateSymbol.EQ:
            atoms.add(symref(phi))
    elif isinstance(phi, CompoundFormula):
        if phi.connective == Connective.Not:
            extract_regular_atoms(phi.subformulas[0], atoms)
        elif phi.connective == Connective.And:
            for gamma in phi.subformulas:
                extract_regular_atoms(gamma, atoms)
        elif phi.connective == Connective.Or:
            for gamma in phi.subformulas:
                extract_regular_atoms(gamma, atoms)
    else:
        raise RuntimeError('Unsupported formula: {}'.format(str(phi)))


def create_equality_constraints(equalities, selects):
    """ Return a list of equality constraints of the form """
    eq_constraints = []
    for s, p in equalities.items():
        lhs, rhs = s.expr.subterms
        sel_lhs = selects[symref(lhs)]
        sel_rhs = selects[symref(rhs)]
        for l, r in itertools.product(*[sel_lhs, sel_rhs]):
            if l.subterms[-1].symbol == r.subterms[-1].symbol:
                if p:
                    eq_constraints += [lor(neg(l), r), lor(neg(r), l)]
                    # Let us have a strong abort here to inspect preconditions of this type (i.e.: a precondition X=Y
                    # on two different action parameters X and Y), if they every arise, as that would be quite
                    # surprising to me. If they indeed occur in practice, it might be better to deal with them by pre-
                    # compiling them away?
                    raise RuntimeError('Weird precondition atom "X=Y". Might be worth inspecting it.')
            eq_constraints += [lor(neg(l), neg(r))]
    return eq_constraints


def create_grounding_constraints_with_statics(count, selects, statics, init, precs, constraints, state_atoms):
    """
        Creates programmatically the grounding constraints taking into account
        static predicate information

         - count: table keeping track of how often a variable appears on a clause
         - selects: select atoms
         - statics: set of static predicate symbols
         - init: initial state model
         - precs: set of action precondition atoms
         - constraints: set of generated grounding constraints
         - state_atoms: set of (state) atoms relevant to the action
    """
    for p in precs:
        # print(p.expr.predicate.symbol, p.expr.subterms)
        for x in p.expr.subterms:
            count[symref(x)] += 1
        SX = [selects[symref(x)] for x in p.expr.subterms]
        for selectlist in itertools.product(*SX):
            body = [s for s in selectlist]  # neg(s) for s in selectlist]
            values = [s.subterms[-1] for s in selectlist]

            head = p.expr.predicate(*values)
            body = [neg(h) for h in body]
            arity = len(body)
            # if len(body) == 1:
            #     body = body[0]

            if not is_static(p.expr, statics):
                if symref(head) not in state_atoms:
                    state_atoms.add(symref(head))
                constraints.append(lor(*body, head) if arity > 0 else head)
                continue

            if init[head]:  # If the atom is static and holds in the initial state, no grounding constraint is necessary
                continue

            assert body
            if len(body) == 1:
                constraints += [body]
            else:
                constraints += [lor(*body)]


def create_select_atoms(action):
    """ Create the atoms of the form select(X, x) for each action parameter X and possible value x in its domain """
    selects, reified = {}, {}
    nvars = 0
    lang = action.language
    for param in action.parameters:
        try:
            x_obj = lang.constant(param.symbol, lang.Object)
        except DuplicateConstantDefinition:
            x_obj = lang.get(param.symbol)
        Dx = list(param.sort.domain())

        name = 'select_{}_{}'.format(param.symbol, param.sort.name)
        try:
            select = lang.predicate(name, lang.Object, param.sort)
        except DuplicatePredicateDefinition:
            select = lang.get(name)

        reified[symref(param)] = x_obj
        # Note that for the type object we need to make sure we don't consider the "reified" variable
        select_x = [select(x_obj, v) for v in Dx if v.symbol != x_obj.symbol and '?' not in v.symbol]
        nvars += len(select_x)
        selects[symref(param)] = select_x
    return selects, reified, nvars


def create_domain_constraints(action, selects, dom):
    """ Create for each action parameter X constraints of the form
        [OR_{x in dom(X)} sel(X, x)] AND [AND_{x, y in dom(X)} (-sel(X, x) OR -sel(X, y))]
    """
    for x in action.parameters:
        Sx = selects[symref(x)]
        if len(Sx) == 1:  # note the possibility of singletons
            dom += [Sx[0]]
            continue
        dom += [lor(*Sx)]
        for v1, v2 in itertools.combinations(Sx, 2):
            dom += [lor(neg(v1), neg(v2))]


def extract_equalities(phi):
    """ Extract a table with action parameter equalities of the form X=Y, X!=Y"""
    table = {}
    _extract_equalities_rec(phi, table)
    return table


def _extract_equalities_rec(phi, table):
    """ Extract a table with action parameter equalities of the form X=Y, X!=Y"""
    if isinstance(phi, Atom):
        if phi.predicate.symbol == BuiltinPredicateSymbol.EQ:
            return phi
    elif isinstance(phi, CompoundFormula):
        if phi.connective == Connective.Not:
            a = _extract_equalities_rec(phi.subformulas[0], table)
            if a is not None:
                table[symref(a)] = False
        elif phi.connective == Connective.And:
            for gamma in phi.subformulas:
                a = _extract_equalities_rec(gamma, table)
                if a is not None:
                    table[symref(a)] = True
        else:
            raise RuntimeError('Unsupported formula: {}'.format(str(phi)))


def process_schema(problem, statics, action, data):
    print(f"Processing action schema:\n{action}")
    data['instance'] += [problem.name]
    nvars = 0
    selects, reified, n = create_select_atoms(action)
    nvars += n
    data['selects'] += [nvars]
    dom_constraints = []
    create_domain_constraints(action, selects, dom_constraints)
    equalities = extract_equalities(action.precondition)
    eq_constraints = create_equality_constraints(equalities, selects)
    state_atoms = set()
    grounding_constraints = []
    prec_atoms = set()
    extract_regular_atoms(action.precondition, prec_atoms)
    # Create the constraints of the form
    #     select(X1, x1) and ... and select (Xn, xn) --> p(x1, ..., xn)
    # for each atom p in the precondition conjunction.
    count = OrderedDict({x: 0 for x in selects})
    # create_grounding_constraints(count, S_a, prec_atoms, grounding_constraints, state_atoms)
    create_grounding_constraints_with_statics(count, selects, statics, problem.init, prec_atoms,
                                              grounding_constraints, state_atoms)
    nvars += len(state_atoms)

    data['atoms'] += [len(state_atoms)]
    data['DOM'] += [len(dom_constraints)]
    data['EQ'] += [len(eq_constraints)]
    data['GROUND'] += [len(grounding_constraints)]
    data['nclauses'] += [len(dom_constraints) + len(eq_constraints) + len(grounding_constraints)]
    data['nvars'] += [nvars]

    symbols = {}
    sdd_var_id = 1
    inv_symbols = {}

    scored_x = [(v, x) for x, v in count.items()]
    scored_x.sort(key=lambda x: x[0], reverse=True)
    # print(scored_x)
    for _, x in scored_x:
        # print(S_a[x])
        for s in selects[x]:
            symbols[symref(s)] = sdd_var_id
            inv_symbols[sdd_var_id] = s
            sdd_var_id += 1
    for p in state_atoms:
        symbols[p] = sdd_var_id
        inv_symbols[sdd_var_id] = p
        sdd_var_id += 1

    manager = setup_sdd_manager(nvars)

    sdd_ground = [translate_to_pysdd(c, symbols, manager) for c in grounding_constraints]
    sdd_eq = [translate_to_pysdd(c, symbols, manager) for c in eq_constraints]
    sdd_dom = [translate_to_pysdd(c, symbols, manager) for c in dom_constraints]
    sdd_pre = sdd_dom[0]
    sdd_sizes = []

    max_size = 20000000
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


def process_problem(problem):
    # Make sure the initial state has some associated evaluator:
    problem.init.evaluator = problem.init.evaluator or evaluate

    data = defaultdict(list)
    actions = scout_actions(problem, data)
    statics = compute_statics(problem)

    for action in actions:
        process_schema(problem, statics, action, data)
    return data
