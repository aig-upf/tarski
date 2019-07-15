import logging
import operator
import itertools
from collections import OrderedDict
from functools import reduce

try:
    from pysdd.sdd import Vtree, SddManager
except ImportError as err:
    raise RuntimeError(f"Could not import pysdd - sdd module not available")


from tarski.errors import DuplicatePredicateDefinition, DuplicateConstantDefinition
from tarski.evaluators.simple import evaluate
from tarski.syntax import symref, lor, neg, Atom, BuiltinPredicateSymbol, CompoundFormula, Connective


class MaxSizeError(Exception):
    pass


def scout_actions(task, data_df):
    actions, empty = [], []
    for _, action in task.actions.items():
        cardinalities = [len(list(x.sort.domain())) for x in action.parameters]
        count = reduce(operator.mul, cardinalities, 1)
        logging.debug('{}:\t{} = {} potential groundings'.format(action.ident(),
                                                                 " * ".join(map(str, cardinalities)), count))
        if count == 0:
            empty.append(action.name)
            continue

        actions.append(action)
        data_df['action'] += [action.ident()]
        data_df['arity'] += [len(action.parameters)]
        data_df['groundings'] += [count]

    logging.debug(f"{len(actions)} actions to ground; actions discarded: {empty}")
    return actions


def find_static_predicates(task):  # TODO Use Tarski native static predicate detection
    prec_atoms = set()
    for _, act in task.actions.items():
        extract_regular_atoms(act.precondition, prec_atoms)

    eff_atoms = set()
    for _, act in task.actions.items():
        # MRJ: needs to take into account conditional effects and non-STRIPS ones
        for eff in act.effects:
            eff_atoms.add(eff.atom.predicate.symbol)

    static_predicates = set()
    for p in prec_atoms:
        if p.expr.predicate.symbol in eff_atoms:
            continue
        static_predicates.add(p.expr.predicate.symbol)
    print(f"Static predicates: {static_predicates}")
    return static_predicates


def is_static(a: Atom, st_table):  # TODO Use Tarski native static predicate detection
    return a.predicate.symbol in st_table


def extract_regular_atoms(phi, atoms):
    if isinstance(phi, Atom):
        if phi.predicate.symbol != BuiltinPredicateSymbol.EQ:  # TODO Use Tarski native static predicate detection
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


def create_equality_constraints(equalities, selects, eq_constraints):
    for s, p in equalities.items():
        # print(s.expr.subterms)
        lhs, rhs = s.expr.subterms
        sel_lhs = selects[symref(lhs)]
        sel_rhs = selects[symref(rhs)]
        for l, r in itertools.product(*[sel_lhs, sel_rhs]):
            if l.subterms[-1].symbol == r.subterms[-1].symbol:
                if not p:
                    eq_constraints += [lor(neg(l), neg(r))]
                if p:
                    eq_constraints += [lor(neg(l), r), lor(neg(r), l)]
                    # Let us have a strong abort here to inspect preconditions of this type (i.e.: a precondition X=Y
                    # on two different action parameters X and Y), if they every arise, as that would be quite
                    # surprising to me. If they indeed occur in practice, it might be better to deal with them by pre-
                    # compiling them away?
                    raise RuntimeError('Weird precondition atom "X=Y". Might be worth inspecting it.')


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
            if len(body) == 1:
                body = body[0]

            if not is_static(p.expr, statics):
                if symref(head) not in state_atoms:
                    state_atoms.add(symref(head))
                if arity == 0:  # 0-arity predicate
                    constraints += [head]
                    continue
                try:
                    body = lor(*body)
                except TypeError:
                    pass
                constraints += [lor(body, head)]
                continue

            # static predicate handling
            if init[head]:
                continue  # no grounding constraint is generated

            # only selects
            try:
                constraints += [lor(*body)]
            except TypeError:
                constraints += [body]


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


def process_problem(the_task):
    # setup model evaluator
    the_task.init.evaluator = evaluate

    data_df = {'instance': [],
               'action': [],
               'arity': [],
               'groundings': [],
               'selects': [],
               'atoms': [],
               'DOM': [],
               'EQ': [],
               'GROUND': [],
               'nclauses': [],
               'nvars': [],
               'sdd_size': [],
               'sdd_sizes': [],
               'A(s0)': [],
               'runtime': []
               }
    actions = scout_actions(the_task, data_df)
    static_predicates = find_static_predicates(the_task)

    for act in actions:
        data_df['instance'] += [the_task.name]
        nvars = 0
        selects, reified, n = create_select_atoms(act)
        nvars += n
        data_df['selects'] += [nvars]
        dom_constraints = []
        create_domain_constraints(act, selects, dom_constraints)
        equalities = extract_equalities(act.precondition)
        eq_constraints = []
        create_equality_constraints(equalities, selects, eq_constraints)
        state_atoms = set()
        grounding_constraints = []
        prec_atoms = set()
        extract_regular_atoms(act.precondition, prec_atoms)
        # Create the constraints of the form
        #     select(X1, x1) and ... and select (Xn, xn) --> p(x1, ..., xn)
        # for each atom p in the precondition conjunction.
        count = OrderedDict({x: 0 for x in selects})
        # create_grounding_constraints(count, S_a, prec_atoms, grounding_constraints, state_atoms)
        create_grounding_constraints_with_statics(count, selects, static_predicates, the_task.init, prec_atoms,
                                                  grounding_constraints, state_atoms)
        nvars += len(state_atoms)

        data_df['atoms'] += [len(state_atoms)]
        data_df['DOM'] += [len(dom_constraints)]
        data_df['EQ'] += [len(eq_constraints)]
        data_df['GROUND'] += [len(grounding_constraints)]
        data_df['nclauses'] += [len(dom_constraints) + len(eq_constraints) + len(grounding_constraints)]
        data_df['nvars'] += [nvars]

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

        # set up vtree and manager
        var_order = list(range(1, nvars + 1))  # lexicographic
        # var_order = list(range(nvars,0,-1)) # state atoms first
        vtree_type = "right"  # OBDD-style

        vtree = Vtree(nvars, var_order, vtree_type)
        manager = SddManager(var_count=nvars, auto_gc_and_minimize=1, vtree=vtree)

        sdd_ground = [translate(c, symbols, manager) for c in grounding_constraints]
        sdd_eq = [translate(c, symbols, manager) for c in eq_constraints]
        sdd_dom = [translate(c, symbols, manager) for c in dom_constraints]
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
            pass
        # tf = time.time()
        # data_df['runtime'] += [tf - t0]

        # sdd_clauses = sdd_ground + sdd_eq + sdd_dom
        # plot_sdd_size(the_task.domain_name, the_task.name, act, sdd_sizes, sdd_clauses, sdd_eq, sdd_ground, sdd_dom)

        data_df['sdd_sizes'] += [sdd_sizes]
        data_df['sdd_size'] += [sdd_sizes[-1]]

        if not failed:
            s = []
            for p in state_atoms:
                if the_task.init[p.expr]:
                    s += [p.expr]
                else:
                    s += [neg(p.expr)]
            # MRJ: code below is good but if state has more than 255 literals we
            # exceed the maximal recursion depth allowed by the interpreter
            # s = land(*s)
            # sdd_s = translate(s, symbols, manager)
            s = [translate(l, symbols, manager) for l in s]
            sdd_s = s[0]
            for l in s[1:]:
                sdd_s = sdd_s & l
            app = sdd_pre & sdd_s
            wmc = app.wmc(log_mode=False)
            wmc.propagate()
            data_df['A(s0)'] += [app.model_count()]
        else:
            data_df['A(s0)'] += [None]
    return data_df


def translate(phi, syms, manager):
    if isinstance(phi, CompoundFormula):
        sub = [translate(psi, syms, manager) for psi in phi.subformulas]
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
