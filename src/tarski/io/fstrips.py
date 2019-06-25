import logging
from collections import defaultdict

from .common import load_tpl
from ..model import ExtensionalFunctionDefinition
from ..syntax import Tautology, Contradiction, Atom, CompoundTerm, CompoundFormula, QuantifiedFormula, \
    Term, Variable, Constant, Formula
from ..syntax.sorts import parent, Interval, ancestors

from ._fstrips.common import tarski_to_pddl_type, get_requirements_string
from ..fstrips import create_fstrips_problem, language, FunctionalEffect, AddEffect, DelEffect, IncreaseEffect,\
    UniversalEffect

from ._fstrips.reader import FStripsParser

# Leave the next import so that it can be imported from the outside without warnings of importing a private module
# pylint: disable=unused-import
from ._fstrips.reader import ParsingError


class FstripsReader:

    def __init__(self, raise_on_error=False, theories=None):
        self.problem = create_fstrips_problem(language=language(theories=theories))
        self.parser = FStripsParser(self.problem, raise_on_error)

    def read_problem(self, domain, instance):
        self.parse_domain(domain)
        self.parse_instance(instance)
        return self.problem

    def parse_file(self, filename, start_rule):
        logging.info('Parsing filename "{}" from grammar rule "{}"'.format(filename, start_rule))
        domain_parse_tree, _ = self.parser.parse_file(filename, start_rule)
        self.parser.visit(domain_parse_tree)

    def parse_domain(self, filename):
        self.parse_file(filename, 'domain')

    def parse_instance(self, filename):
        self.parse_file(filename, 'problem')

    def parse_string(self, string, start_rule):
        logging.info('Parsing custom string from grammar rule "{}"'.format(start_rule))
        parse_tree, _ = self.parser.parse_string(string, start_rule)
        logging.info("Processing AST")
        return self.parser.visit(parse_tree)


_TAB = " " * 4

action_tpl = """
    (:action {name}
     :parameters ({parameters})
     :precondition {precondition}
     :effect {effect}
    )
"""

derived_tpl = """
    (:derived ({name} {parameters})
              {formula}
    )
"""


def print_objects(constants):
    """ Print a PDDL object declaration with the given objects.
    Objects are sorted by name and grouped by type, and types sorted by name as well """
    constants_by_sort = defaultdict(list)
    for c in constants:
        constants_by_sort[c.sort.name].append(c.symbol)

    elements = []
    for sort in sorted(constants_by_sort.keys()):
        sobjects = " ".join(sorted(constants_by_sort[sort]))
        elements.append("{} - {}".format(sobjects, sort))

    return linebreaks(elements, indentation=2, indent_first=False)


def linebreaks(elements, indentation, indent_first):
    def indent_while_iterating():
        for i, element in enumerate(elements, 0):
            idt = 0 if i == 0 and not indent_first else indentation
            yield indent(element, idt)

    return "\n".join(indent_while_iterating())


def print_init(problem):
    elements = []
    # e.g. (= (value c0) 0)
    for signature, definition in problem.init.function_extensions.items():
        if not isinstance(definition, ExtensionalFunctionDefinition):
            continue  # Ignore intensionally defined symbols
        fname = signature[0]
        for point, value in definition.data.items():
            elements.append("(= ({} {}) {})".format(fname, print_term_ref_list(point), value))

    # e.g. (clear b1)
    for signature, definition in problem.init.predicate_extensions.items():
        assert isinstance(definition, set)
        predname = signature[0]
        for point in definition:
            elements.append("({} {})".format(predname, print_term_ref_list(point)))

    return linebreaks(elements, indentation=2, indent_first=False)


def print_goal(problem):
    return print_formula(problem.goal, 1)


def print_domain_bounds(problem):
    lang = problem.language
    bounds = []
    for sort in lang.sorts:
        if not sort.builtin and isinstance(sort, Interval):
            assert lang.has_sort('Integer')
            if lang.Integer in ancestors(sort):
                bounds.append("({} - int[{}..{}])".format(sort.name, sort.lower_bound, sort.upper_bound))
            elif lang.Real in ancestors(sort):
                pass  # TODO

    if not bounds:  # No bounded type was found
        return ""

    inner = "\n".join(indent(b, 2) for b in bounds)
    return "(:bounds\n{})".format(inner)


def print_problem_constraints(problem):
    # pylint: disable=unused-argument
    return ""  # TODO


def print_metric(metric):
    return '(:metric {type} {exp})'.format(type=metric.opt_type.value,
                                           exp=print_term(metric.opt_expression))


def print_problem_metric(problem):
    return print_metric(problem.plan_metric) if problem.plan_metric else ''


class FstripsWriter:

    def __init__(self, problem):
        self.problem = problem
        self.lang = problem.language

    def write(self, domain_filename, instance_filename, domain_constants=None):
        domain_constants = domain_constants or []
        self.write_domain(domain_filename, domain_constants)
        self.write_instance(instance_filename, domain_constants)

    def print_domain(self, constant_objects=None):
        tpl = load_tpl("fstrips_domain.tpl")
        content = tpl.format(
            header_info="",
            domain_name=self.problem.domain_name,
            requirements=" ".join(get_requirements_string(self.problem)),
            types=self.get_types(),
            functions=self.get_functions(),
            predicates=self.get_predicates(),
            actions=self.get_actions(),
            derived=self.get_derived_predicates(),
            constants=print_objects(constant_objects if constant_objects else set()),
        )
        return content

    def write_domain(self, filename, constant_objects):
        with open(filename, 'w') as file:
            file.write(self.print_domain(constant_objects))

    def print_instance(self, constant_objects=None):
        tpl = load_tpl("fstrips_instance.tpl")

        # Only objects which are not declared in the domain file need to be printed in the instance file
        constant_objs_set = set(constant_objects) if constant_objects else set()
        instance_objects = [c for c in self.problem.language.constants() if c not in constant_objs_set]

        content = tpl.format(
            header_info="",
            domain_name=self.problem.domain_name,
            problem_name=self.problem.name,

            objects=print_objects(instance_objects),
            init=print_init(self.problem),
            goal=print_goal(self.problem),
            constraints=print_problem_constraints(self.problem),
            domain_bounds=print_domain_bounds(self.problem),
            metric=print_problem_metric(self.problem),
        )
        return content

    def write_instance(self, filename, constant_objects):
        with open(filename, 'w') as file:
            file.write(self.print_instance(constant_objects))

    def get_types(self):
        res = []
        for t in self.lang.sorts:
            if t.builtin or t == self.lang.Object:
                continue  # Don't declare builtin elements
            tname = tarski_to_pddl_type(t)
            p = parent(t)
            if p:
                res.append("{} - {}".format(tname, tarski_to_pddl_type(p)))
            else:
                res.append(tname)
        return ("\n" + _TAB * 2).join(res)

    def get_functions(self):
        res = []
        for fun in self.lang.functions:
            if fun.builtin:
                continue  # Don't declare builtin elements
            domain_str = build_signature_string(fun.domain)
            codomain_str = tarski_to_pddl_type(fun.codomain)
            res.append("({} {}) - {}".format(fun.symbol, domain_str, codomain_str))
        return ("\n" + _TAB * 2).join(res)

    def get_predicates(self):
        res = []
        for fun in self.lang.predicates:
            if fun.builtin:
                continue  # Don't declare builtin elements
            domain_str = build_signature_string(fun.sort)
            res.append("({} {})".format(fun.symbol, domain_str))
        return ("\n" + _TAB * 2).join(res)

    def get_actions(self):
        return "\n".join(self.get_action(a) for a in self.problem.actions.values())

    @staticmethod
    def get_action(a):
        base_indentation = 1
        return action_tpl.format(
            name=a.name,
            parameters=print_variable_list(a.parameters),
            precondition=print_formula(a.precondition, base_indentation),
            effect=print_effects(a.effects, base_indentation)
        )

    def get_derived_predicates(self):
        return "\n".join(self.get_derived(d) for d in self.problem.derived_predicates.values())

    @staticmethod
    def get_derived(d):
        return derived_tpl.format(
            name=d.predicate.symbol,
            parameters=print_variable_list(d.parameters),
            formula=print_formula(d.formula))


def build_signature_string(domain):
    if not domain:
        return ""

    return " ".join("?x{} - {}".format(i, tarski_to_pddl_type(t)) for i, t in enumerate(domain, 1))


def print_variable_list(parameters):
    return " ".join("?{} - {}".format(p.symbol, p.sort.name) for p in parameters)


def print_formula(formula, indentation=0):
    # pylint: disable=unused-argument
    assert isinstance(formula, Formula)
    if isinstance(formula, Tautology):
        return "(and )"
    elif isinstance(formula, Contradiction):
        return "(= 0 1)"  # PDDL HACK =)
    elif isinstance(formula, Atom):
        return print_atom(formula)
    elif isinstance(formula, CompoundFormula):
        return "({} {})".format(formula.connective, print_formula_list(formula.subformulas))

    elif isinstance(formula, QuantifiedFormula):
        vars_ = print_variable_list(formula.variables)
        # e.g. (exists (?x - object) (and (= ?x 2)))
        return '({} ({}) {})'.format(formula.quantifier, vars_, print_formula(formula.formula))
    raise RuntimeError("Unexpected element type: {}".format(formula))


def print_effects(effects, indentation=0):
    if not effects:
        return "(and )"
    return "(and\n{})".format("\n".join(print_effect(e, indentation + 1) for e in effects))


def print_unconditional_effect(eff, indentation=0):
    functional = isinstance(eff, FunctionalEffect)
    increase = isinstance(eff, IncreaseEffect)

    if increase:
        return indent("(increase {} {})".format(print_term(eff.lhs), print_term(eff.rhs)), indentation)
    elif functional:
        return indent("(assign {} {})".format(print_term(eff.lhs), print_term(eff.rhs)), indentation)
    elif isinstance(eff, AddEffect):
        return indent("{}".format(print_atom(eff.atom)), indentation)
    elif isinstance(eff, DelEffect):
        return indent("(not {})".format(print_atom(eff.atom)), indentation)
    elif isinstance(eff, UniversalEffect):
        effect_str = (print_effect(eff.effects[0]) if len(eff.effects) == 1 else print_effects(eff.effects))
        return indent("(forall ({}) {})".format(print_variable_list(eff.variables), effect_str),
                      indentation)

    raise RuntimeError("Unexpected element type: {}".format(eff))


def print_effect(eff, indentation=0):
    conditional = not isinstance(eff.condition, Tautology)

    if conditional:
        return indent(
            "(when {} {})".format(print_formula(eff.condition), print_unconditional_effect(eff)),
            indentation)
    else:
        return print_unconditional_effect(eff, indentation)


def print_term(term):
    assert isinstance(term, Term)
    if isinstance(term, Variable):
        return "?{}".format(term.symbol)
    elif isinstance(term, CompoundTerm):
        return "({} {})".format(term.symbol.symbol, print_term_list(term.subterms))
    elif isinstance(term, Constant):
        return "{}".format(term.symbol)
    raise RuntimeError("Unexpected element type: {}".format(term))


def print_atom(atom):
    assert isinstance(atom, Atom)
    return "({} {})".format(atom.predicate.symbol, print_term_list(atom.subterms))


def print_term_list(terms):
    return " ".join(print_term(t) for t in terms)


def print_term_ref_list(termrefs):
    return " ".join(print_term(t.expr) for t in termrefs)


def print_formula_list(formulas):
    return " ".join(print_formula(f) for f in formulas)


def indent(text, indentation):
    return (indentation * _TAB) + text
