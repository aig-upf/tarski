import os
from collections import defaultdict
from enum import Enum
from pathlib import Path

from tarski import Constant, Variable
from tarski.errors import TarskiError
from tarski.fstrips.representation import is_conjunction_of_literals, has_state_variable_shape
from tarski.grounding.common import StateVariableLite
from tarski.syntax import QuantifiedFormula, Quantifier, Contradiction, Tautology, CompoundFormula, Atom, CompoundTerm, \
    Connective, is_neg
from tarski.syntax.ops import collect_unique_nodes, flatten
from tarski.syntax.transform import to_prenex_negation_normal_form


class CSPSchemaCompilationError(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'Unspecified error when attempting to compile action schema into CSP'
        super().__init__(msg)


class CSPVarType(Enum):
    """"  """
    Bool, Int = range(2)


def get_type_prefix(t):
    return {CSPVarType.Bool: "b", CSPVarType.Int: "z"}[t]


class CSPInformation:
    def __init__(self):
        self.name_to_var = dict()
        self.name_to_domain = dict()
        self.constraints = []

    def variable(self, expression, type_=None):
        """ """
        name = f"{get_type_prefix(type_)}[{expression}]"
        v = self.name_to_var.get(name)
        if v is None:
            v = self.name_to_var[name] = name
            self.name_to_domain[name] = None  # TODO
        else:
            pass  # TODO CHeck we're not attempting to redefine the domain of the variable, raise if that's the case
        return v

    def add_constraint(self, c):
        self.constraints.append(c)


class TableConstraint:
    def __init__(self, expr, variables, reification):
        assert isinstance(expr, (CompoundTerm, Atom))
        self.expr = expr
        self.variables = variables
        self.reification = reification

    def is_negated(self):
        return is_neg(self.expr)

    def __str__(self):
        return f'Table(<{",".join(self.variables)}>, ext({self.expr.symbol.name}), reif={self.reification})'
    __repr__ = __str__


class StateVariableConstraint:
    def __init__(self, expr, value):
        self.expr = expr
        self.value = value
        self.reification = None

    def __str__(self):
        return f'StateVar({self.expr}={self.value}, reif={self.reification})'

    __repr__ = __str__


def process_problem(problem, state_variables, serialization_directory=None):

    for action in problem.actions.values():
        csp = compile_schema_csp(problem, action, state_variables)

        if serialization_directory is not None:
            serialize_schema_csp(action, csp, serialization_directory)


def compile_schema_csp(problem, action, state_variables):
    print(f'Processing action "{action}"')

    # Do some transformation and validation of the action precondition
    precondition = to_prenex_negation_normal_form(problem.language, flatten(action.precondition))
    foralls = collect_unique_nodes(precondition,
                                   lambda f: isinstance(f, QuantifiedFormula) and f.quantifier == Quantifier.Forall)
    if foralls:
        raise CSPSchemaCompilationError(f"Cannot process universal quantification in action {action}")

    if not is_conjunction_of_literals(precondition):
        raise CSPSchemaCompilationError(
            f"Compilation not yet finished for actions with non-conjunctive preconditions such as {action}")

    csp = CSPInformation()
    compile_expression(precondition, csp, state_variables)
    return csp


def compile_expression(node, csp, state_variables, reify=False, negate=False):
    variables, constraints = set(), set()

    if isinstance(node, Variable):
        csp.variable(node, CSPVarType.Int)  # TODO: Specify the domain

    elif isinstance(node, Constant):
        pass

    elif isinstance(node, (Variable, Constant, Contradiction, Tautology)):
        pass

    elif isinstance(node, (CompoundTerm, Atom)):
        if has_state_variable_shape(node) and StateVariableLite.from_atom(node) in state_variables:
            assert isinstance(node, Atom)  # CompoundTerm case yet to be implemented
            value = not negate
            csp.add_constraint(StateVariableConstraint(node, value))

        else:
            _ = [compile_expression(s, csp, state_variables) for s in node.subterms]
            variables = [csp.variable(s, CSPVarType.Int) for s in node.subterms]
            reif = csp.variable(node, CSPVarType.Bool) if reify else None
            csp.add_constraint(TableConstraint(node, variables=variables, reification=reif))

    elif is_neg(node):
        assert isinstance(node.subformulas[0], Atom)  # Because formula must be in NNF
        assert not negate
        compile_expression(node.subformulas[0], csp, state_variables, reify=reify, negate=True)

    elif isinstance(node, CompoundFormula):  # won't be a negation, since we checked that case above
        if reify:
            assert 0, "To implement"
        _ = [compile_expression(s, csp, state_variables, reify=reify) for s in node.subformulas]

    elif isinstance(node, QuantifiedFormula):
        assert node.quantifier == Quantifier.Exists
        subv, subc = compile_expression(node.formula, csp, state_variables)
        subv.update(node.variables)
        return subv, subc

    else:
        raise CSPSchemaCompilationError(f'Unexpected expression "{node}" of type "{type(node)}"')

    return variables, constraints


def serialize_schema_csp(action, csp, path):
    """ Serialize under the given directory path the relevant data for the CSP corresponding to the given
     action schema."""
    if not Path(path).is_dir():
        raise Exception(f"Directory '{path}' does not exist")

    # sanitized = action.name.replace('-', '_')
    sanitized = action.name.lower()

    with open(os.path.join(path, f'{sanitized}.csp'), 'w') as f:
        print(f'variables', file=f)
        for c in csp.constraints:
            print(f'{c}', file=f)
        print(f'endvariables', file=f)

        print(f'constraints', file=f)
        for v in csp.name_to_var.keys():
            print(f'TODO', file=f)
        print(f'endconstraints', file=f)
