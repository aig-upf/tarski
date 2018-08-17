import logging
import os
from collections import defaultdict

from tarski import Term, Variable, Constant, Formula
from tarski.fstrips.fstrips import SingleEffect
from tarski.model import ExtensionalFunctionDefinition
from tarski.syntax import Tautology, Contradiction, Atom, CompoundTerm, CompoundFormula, QuantifiedFormula
from tarski.syntax.sorts import parent, Interval, ancestors

from ._fstrips.common import tarsky_to_pddl_type, get_requirements_string
from ..fstrips import create_fstrips_problem, language, FunctionalEffect, AddEffect, DelEffect

from ._fstrips.reader import FStripsParser

_CURRENT_DIR_ = os.path.dirname(os.path.realpath(__file__))


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


_TAB = " "*4

action_tpl = """
    (:action {name}
     :parameters ({parameters})
     :precondition {precondition}
     :effect {effect}
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
            elements.append("(= ({} {}) {})".format(fname, print_term_list(point), value))

    # e.g. (clear b1)
    for signature, definition in problem.init.predicate_extensions.items():
        assert isinstance(definition, set)
        predname = signature[0]
        for point in definition:
            elements.append("({} {})".format(predname, print_term_list(point)))

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


def print_problem_metric(problem):
    # pylint: disable=unused-argument
    return ""  # TODO


class FstripsWriter:

    def __init__(self, problem):
        self.problem = problem
        self.lang = problem.language

    def write(self, domain_filename, instance_filename, domain_constants=None):
        domain_constants = domain_constants or []
        self.write_domain(domain_filename, domain_constants)
        self.write_instance(instance_filename, domain_constants)

    def load_tpl(self, name):
        with open(os.path.join(_CURRENT_DIR_, "templates", name), 'r') as file:
            return file.read()

    def write_domain(self, filename, constant_objects):
        tpl = self.load_tpl("fstrips_domain.tpl")
        content = tpl.format(
            header_info="",
            domain_name=self.problem.domain_name,
            requirements=" ".join(get_requirements_string(self.problem)),
            types=self.get_types(),
            functions=self.get_functions(),
            predicates=self.get_predicates(),
            actions=self.get_actions(),
            constants=print_objects(constant_objects),
        )
        with open(filename, 'w') as file:
            file.write(content)

    def write_instance(self, filename, constant_objects):
        tpl = self.load_tpl("fstrips_instance.tpl")

        # Only objects which are not declared in the domain file need to be printed in the instance file
        instance_objects = [c for c in self.problem.language.constants() if c not in set(constant_objects)]

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
        with open(filename, 'w') as file:
            file.write(content)

    def get_types(self):
        res = []
        for t in self.lang.sorts:
            if t.builtin or t == self.lang.Object:
                continue  # Don't declare builtin elements
            tname = tarsky_to_pddl_type(t)
            p = parent(t)
            if p:
                res.append("{} - {}".format(tname, tarsky_to_pddl_type(p)))
            else:
                res.append(tname)
        return ("\n" + _TAB*2).join(res)

    def get_functions(self):
        res = []
        for fun in self.lang.functions:
            if fun.builtin:
                continue  # Don't declare builtin elements
            domain_str = build_signature_string(fun.domain)
            codomain_str = tarsky_to_pddl_type(fun.codomain)
            res.append("({} {}) - {}".format(fun.symbol, domain_str, codomain_str))
        return ("\n" + _TAB*2).join(res)

    def get_predicates(self):
        res = []
        for fun in self.lang.predicates:
            if fun.builtin:
                continue  # Don't declare builtin elements
            domain_str = build_signature_string(fun.sort)
            res.append("({} {})".format(fun.symbol, domain_str))
        return ("\n" + _TAB*2).join(res)

    def get_actions(self):
        return "\n".join(self.get_action(a) for a in self.problem.actions.values())

    def get_action(self, a):
        base_indentation = 1
        return action_tpl.format(
            name=a.name,
            parameters=print_variable_list(a.parameters),
            precondition=print_formula(a.precondition, base_indentation),
            effect=print_effects(a.effects, base_indentation)
        )


def build_signature_string(domain):
    if not domain:
        return ""

    return " ".join("?x{} - {}".format(i, tarsky_to_pddl_type(t)) for i, t in enumerate(domain, 1))


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
    return "(and\n{})".format("\n".join(print_effect(e, indentation+1) for e in effects))


def print_effect(eff, indentation=0):
    assert isinstance(eff, SingleEffect)  # Universal, etc. effects yet to be implemented
    conditional = not isinstance(eff.condition, Tautology)  # We have a conditional effect
    functional = isinstance(eff, FunctionalEffect)

    if conditional:
        raise RuntimeError("Unimplemented")

    if functional:
        return indent("(assign {} {})".format(print_term(eff.lhs), print_term(eff.rhs)), indentation)
    elif isinstance(eff, AddEffect):
        return indent("{}".format(print_atom(eff.atom)), indentation)
    elif isinstance(eff, DelEffect):
        return indent("(not {})".format(print_atom(eff.atom)), indentation)
    raise RuntimeError("Unexpected element type: {}".format(eff))


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


def print_formula_list(formulas):
    return " ".join(print_formula(f) for f in formulas)


def indent(text, indentation):
    return (indentation*_TAB) + text
