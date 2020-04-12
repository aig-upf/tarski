import os
from enum import Enum
from pathlib import Path

from ..fstrips.manipulation import Simplify
from ..errors import TarskiError
from ..fstrips.representation import is_conjunction_of_literals, has_state_variable_shape
from ..grounding.common import StateVariableLite
from ..syntax import QuantifiedFormula, Quantifier, Contradiction, CompoundFormula, Atom, CompoundTerm, \
    is_neg, symref, Constant, Variable, Tautology, top
from ..syntax.ops import collect_unique_nodes, flatten
from ..syntax.transform import to_prenex_negation_normal_form


class CSPSchemaCompilationError(TarskiError):
    def __init__(self, msg=None):
        msg = msg or 'Unspecified error when attempting to compile action schema into CSP'
        super().__init__(msg)


class CSPVarType(Enum):
    """"  """
    Bool = "bool"
    Int = "int"

    def __str__(self):
        return self.value.lower()


def get_type_prefix(t):
    return {CSPVarType.Bool: "b", CSPVarType.Int: "z"}[t]


class CSPInformation:
    def __init__(self):
        self.name_to_vardata = dict()
        self.vardata = list()
        self.constraints = []

    def add_constraint(self, c):
        self.constraints.append(c)


class TableConstraint:
    def __init__(self, expr, variables, reification, negative):
        assert isinstance(expr, (CompoundTerm, Atom))
        self.expr = expr
        self.symbol = expr.symbol.name
        self.variables = variables
        self.reification = reification
        self.negative = negative

    def is_negated(self):
        return is_neg(self.expr)

    def __str__(self):
        return f'Table(<{",".join(self.variables)}> in ext({self.symbol}), ' \
               f'negative={self.negative}, reif={self.reification})'
    __repr__ = __str__


class StateVariableConstraint:
    def __init__(self, expr, value):
        self.expr = expr
        self.value = value
        self.reification = None

    def __str__(self):
        return f'StateVar({self.expr}={self.value}, reif={self.reification})'

    __repr__ = __str__


class RelationalConstraint:
    def __init__(self, lhs, rhs, rel):
        self.lhs = lhs
        self.rhs = rhs
        self.rel = rel
        self.reification = None

    def __str__(self):
        return f'RelationalConstraint({self.lhs} {self.rel} {self.rhs}, reif={self.reification})'

    __repr__ = __str__


class CSPCompiler:
    def __init__(self, problem, state_variables, sort_bounds, object_ids):
        self.problem = problem
        self.lang = problem.language
        self.state_variables = state_variables
        self.sort_bounds = sort_bounds
        self.object_ids = object_ids

    def process_problem(self, serialization_directory=None):
        simplifier = Simplify(self.problem, self.problem.init)
        inapplicable = set()

        for action in self.problem.actions.values():
            csp = self.compile_schema_csp(action, simplifier)
            if csp is None:
                inapplicable.add(action.name)
                continue

            if serialization_directory is not None:
                self.serialize_schema_csp(action, csp, serialization_directory)
        return inapplicable

    def compile_schema_csp(self, action, simplifier):
        print(f'Processing action "{action}"')

        # Do some transformation and validation of the action precondition
        precondition = to_prenex_negation_normal_form(self.lang, flatten(action.precondition))
        foralls = collect_unique_nodes(precondition,
                                       lambda f: isinstance(f, QuantifiedFormula) and f.quantifier == Quantifier.Forall)
        if foralls:
            raise CSPSchemaCompilationError(f"Cannot process universal quantification in action {action}")

        if not is_conjunction_of_literals(precondition):
            raise CSPSchemaCompilationError(
                f"Compilation not yet finished for actions with non-conjunctive preconditions such as {action}")

        precondition = simplifier.simplify_expression(precondition)
        if precondition is False:
            return None
        if precondition is True:
            precondition = top

        csp = CSPInformation()
        csp.parameter_index = [self.variable(p, csp, "param") for p in action.parameters]
        self.compile_expression(precondition, csp)
        return csp

    def compile_expression(self, node, csp, reify=False, negate=False):

        if isinstance(node, Variable):
            return self.variable(node, csp, "var")

        elif isinstance(node, Constant):
            return self.variable(node, csp, "const")

        elif isinstance(node, Tautology):
            pass  # No need to do anything

        elif isinstance(node, Contradiction):
            assert 0

        elif isinstance(node, (CompoundTerm, Atom)):
            if has_state_variable_shape(node) and StateVariableLite.from_atom(node) in self.state_variables:
                assert isinstance(node, Atom)  # CompoundTerm case yet to be implemented
                csp.add_constraint(StateVariableConstraint(node, value=not negate))
                return None

            if node.symbol.builtin:
                lhs, rhs = (self.compile_expression(s, csp) for s in node.subterms)
                rel = node.symbol.name.complement() if negate else node.symbol.name
                csp.add_constraint(RelationalConstraint(lhs, rhs, str(rel)))
                return None

            _ = [self.compile_expression(s, csp) for s in node.subterms]
            variables = [self.compile_expression(s, csp) for s in node.subterms]
            # reif = self.variable(node, csp, is_reification_var=True) if reify else None
            csp.add_constraint(TableConstraint(node, variables=variables, reification=None, negative=negate))
            return None

        elif is_neg(node):
            assert isinstance(node.subformulas[0], Atom)  # Because formula must be in NNF
            assert not negate
            self.compile_expression(node.subformulas[0], csp, reify=reify, negate=True)

        elif isinstance(node, CompoundFormula):  # won't be a negation, since we checked that case above
            if reify:
                assert 0, "To implement"
            _ = [self.compile_expression(s, csp, reify=reify) for s in node.subformulas]

        elif isinstance(node, QuantifiedFormula):
            assert node.quantifier == Quantifier.Exists
            _ = [self.variable(node, csp, "existential") for v in node.variables]

        else:
            raise CSPSchemaCompilationError(f'Unexpected expression "{node}" of type "{type(node)}"')

    def variable(self, expression, csp, type_, is_reification_var=False):
        """ """
        cspvartype = CSPVarType.Bool if is_reification_var else CSPVarType.Int
        name = f"{expression}"
        if isinstance(expression, (Variable, CompoundTerm)):
            lb, ub = self.sort_bounds[expression.sort]
            # Note that Gecode bounds are inclusive, i.e. lb <= x <= ub, whereas in Tarski the upper-bound is exclusive,
            # so we have to fix that here:
            bounds = (lb, ub-1)
        elif isinstance(expression, Constant):
            val = self.object_ids[symref(expression)]
            bounds = (val, val)
        else:
            assert 0, "to implement"

        vdata = (name, type_, cspvartype, bounds)
        stored = csp.name_to_vardata.get(name)
        if stored is None:
            csp.vardata.append(vdata)
            csp.name_to_vardata[name] = csp.vardata[-1]

        return name

    def serialize_schema_csp(self, action, csp, path):
        """ Serialize under the given directory path the relevant data for the CSP corresponding to the given
         action schema."""
        if not Path(path).is_dir():
            raise Exception(f"Directory '{path}' does not exist")

        # sanitized = action.name.replace('-', '_')
        # sanitized = action.name.lower()
        sanitized = action.name

        with open(os.path.join(path, f'{sanitized}.csp'), 'w') as f:
            print(f'variables', file=f)
            print(len(csp.vardata), file=f)
            for name, type_, cspvartype, range_ in csp.vardata:
                print(f'{name} {type_} {cspvartype} {range_[0]} {range_[1]}', file=f)
            print(f'end-variables', file=f)

            print(f'parameter-index', file=f)
            print(len(csp.parameter_index), file=f)
            for name in csp.parameter_index:
                print(f'{name}', file=f)
            print(f'end-parameter-index', file=f)

            print(f'constraints', file=f)
            print(len(csp.constraints), file=f)
            for c in csp.constraints:
                if isinstance(c, TableConstraint):
                    print(f'table-constraint', file=f)
                    print(f'{c.symbol} negative={c.negative} ' + " ".join(c.variables), file=f)
                elif isinstance(c, StateVariableConstraint):
                    sv_id = self.state_variables.get_index(StateVariableLite.from_atom(c.expr))
                    print(f'statevar=const', file=f)
                    print(f'{sv_id} {c.value}', file=f)
                elif isinstance(c, RelationalConstraint):
                    print(f'relational', file=f)
                    print(f'{c.lhs} {c.rel} {c.rhs}', file=f)
                else:
                    raise RuntimeError(f'Constraint printer for constraints like "{c}" not yet implemented')
            print(f'end-constraints', file=f)
