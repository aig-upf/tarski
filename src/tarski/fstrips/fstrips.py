
from enum import Enum
from typing import Union, List, Optional, Callable, Any

from ..syntax import CompoundTerm, Term, Constant, symref, top
from .. import theories as ths
from .errors import InvalidEffectError


class BaseEffect:
    """ A base class for all FSTRIPS effects, which might have an (optional) condition. """
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        raise NotImplementedError()


class SingleEffect(BaseEffect):
    def __str__(self):
        return "({} -> {})".format(self.condition, self.tostring())

    __repr__ = __str__

    def tostring(self):
        raise NotImplementedError("To be subclassed")


class AddEffect(SingleEffect):
    """ A standard add-effect, possibly with a condition. """
    def __init__(self, atom, condition=top):
        super().__init__(condition)
        self.atom = atom

    def tostring(self):
        return "ADD({})".format(self.atom)


class DelEffect(SingleEffect):
    """ A standard delete-effect, possibly with a condition. """
    def __init__(self, atom, condition=top):
        super().__init__(condition)
        self.atom = atom

    def tostring(self):
        return "DEL({})".format(self.atom)


class LiteralEffect(SingleEffect):
    def __init__(self, lit, condition=top):
        super().__init__(condition)
        self.lit = lit

    def tostring(self):
        return "LIT({})".format(self.lit)


class FunctionalEffect(SingleEffect):
    """ A functional effect of the form f(t) := g(u), possibly with a condition. """
    def __init__(self, lhs, rhs, condition=top):
        super().__init__(condition)
        self.lhs = lhs
        self.rhs = rhs
        self.check_well_formed()

    def check_well_formed(self):
        if not isinstance(self.lhs, CompoundTerm):
            raise InvalidEffectError(self, f"Error declaring FunctionalEffect {self}: left hand side"
                                           f" expression '{self.lhs}' needs to be a functional term")

        if not isinstance(self.rhs, Term):
            raise InvalidEffectError(self, f"Error declaring FunctionalEffect {self}: right hand side"
                                           f" expression '{self.rhs}' needs to be a functional term")

    def tostring(self):
        return f"{self.lhs} := {self.rhs}"


class UniversalEffect(BaseEffect):
    """ A forall-effect that represents a number of effects that results from all possible
    substitutions to the forall-effect variables. """

    def __init__(self, variables, effects, condition=top):
        super().__init__(condition)
        self.variables = variables
        self.effects = effects

    def __str__(self):
        effects_str = ', '.join(map(str, self.effects))
        return f"({self.condition} -> forall ({self.variables}) : ({effects_str}))"

    __repr__ = __str__


class IncreaseEffect(FunctionalEffect):
    def __init__(self, lhs, rhs, condition=top):
        super().__init__(lhs, rhs, condition)

        # MRJ: normalise rhs so it is easier to handle later on
        if type(self.rhs) == int:
            self.rhs = Constant(self.rhs, self.lhs.language.Integer)
        elif type(self.rhs) == float:
            self.rhs = Constant(self.rhs, self.lhs.language.Real)

    def check_well_formed(self):
        if not isinstance(self.lhs, CompoundTerm):
            raise InvalidEffectError(self, f'Ill-formed increase effect "{self.tostring()}". '
                                           f'Left hand side needs to be a functional term.')

        if not isinstance(self.rhs, (int, float, Term)):
            raise InvalidEffectError(self, f'Ill-formed increase effect "{self.tostring()}". '
                                           f'Right hand side needs to be a constant or functional term.')


class OptimizationType(Enum):
    MINIMIZE = "minimize"
    MAXIMIZE = "maximize"

    def __str__(self):
        return self.value.lower()

    @staticmethod
    def from_string(string):
        assert string in ("minimize", "maximize")
        return OptimizationType.MINIMIZE if string == "minimize" else OptimizationType.MAXIMIZE


class ProceduralEffect(SingleEffect):

    def __init__(self, input_: List[CompoundTerm], output: List[CompoundTerm]):
        super().__init__(top)
        self.input = input_
        self.output = output

    def tostring(self):
        return "in: {}, out: {}".format(','.join([str(x) for x in self.input]),
                                        ','.join([str(x) for x in self.output]))


class ChoiceEffect(SingleEffect):

    def __init__(self, obj_type: OptimizationType, obj, variables: List[CompoundTerm], constraints=top):
        super().__init__(constraints)
        # MRJ: verify the effect is well formed
        self.obj = obj
        self.obj_type = obj_type
        self.variables = variables
        self.check_well_formed()

    def check_well_formed(self):
        if not isinstance(self.obj, CompoundTerm):
            msg = "Error declaring Choice Effect: {}\n Invalid objective expression: \
            expression to optimize needs to be a functional term!".format(self.tostring())
            raise InvalidEffectError(self, msg)

    def tostring(self):
        return "{} {}, vars: {} subject to: {}".format(self.obj_type,
                                                       self.obj, ','.join([str(x) for x in self.variables]),
                                                       self.condition)


class VectorisedEffect(SingleEffect):
    """ Action effects that modify the denotation of a vector (tuple) of terms """

    def __init__(self, lhs, rhs, condition=top):
        super().__init__(condition)
        self.lhs = lhs
        self.rhs = rhs
        self.check_well_formed()

    def tostring(self):
        return "VectorisedEffect({} := {})".format(self.lhs, self.rhs)

    def check_well_formed(self):
        if not hasattr(self.lhs, 'shape'):
            msg = "Error declaring VectorisedEffect, lhs needs needs to be\
                vector or matrix like"
            raise InvalidEffectError(self, msg)
        if self.lhs.shape[0] > 1:
            msg = "Error declaring VectorisedEffect, lhs needs needs to be\
                a vector in column order"
            raise InvalidEffectError(self, msg)
        if not hasattr(self.rhs, 'shape'):
            msg = "Error declaring VectorisedEffect, rhs needs needs to be\
                vector or matrix like"
            raise InvalidEffectError(self, msg)
        if self.lhs.shape == self.rhs.shape:
            msg = "Error declaring VectorisedEffect, lhs and rhs need to have\
                same dimensions"
            raise InvalidEffectError(self, msg)


class LinearEffect(SingleEffect):
    """
        Action effects that modify the denotation of a vector of (terms)  with
        the restriction of interactions between the expressions on the right hand
        side to be of the form:

            Ax + b
    """

    def __init__(self, y, a, x, b, condition=top):
        super().__init__(condition)
        self.y = y
        self.A = a
        self.x = x
        self.b = b
        self.check_well_formed()

    def tostring(self):
        return "LinearEffect({} := {} * {} + {})".format(self.y, self.A, self.x, self.b)

    def check_well_formed(self):
        if not hasattr(self.y, 'shape'):
            msg = "Error declaring VectorisedEffect, y needs needs to be\
                vector or matrix like"
            raise InvalidEffectError(self, msg)
        if self.y.shape[0] > 1:
            msg = "Error declaring VectorisedEffect, y needs needs to be\
                a vector in column order"
            raise InvalidEffectError(self, msg)
        if not hasattr(self.x, 'shape'):
            msg = "Error declaring VectorisedEffect, x needs needs to be\
                vector or matrix like"
            raise InvalidEffectError(self, msg)
        if self.y.shape != self.x.shape:
            msg = "Error declaring VectorisedEffect, y and x need to have\
                same dimensions: shape(y)={}, shape(x)={}".format(self.y.shape, self.x.shape)
            raise InvalidEffectError(self, msg)

        if not hasattr(self.A, 'shape'):
            msg = "Error declaring VectorisedEffect, coefficients matrix A needs to be\
                vector or matrix like"
            raise InvalidEffectError(self, msg)
        if self.y.shape[0] != self.A.shape[1]:
            msg = "Error declaring VectorisedEffect, y and x need to have\
                same dimensions"
            raise InvalidEffectError(self, msg)

        if not hasattr(self.b, 'shape'):
            msg = "Error declaring VectorisedEffect, coefficient vector b needs needs to be\
                vector or matrix like"
            raise InvalidEffectError(self, msg)
        if self.x.shape != self.b.shape:
            msg = "Error declaring VectorisedEffect, x and b need to have\
                same dimensions"
            raise InvalidEffectError(self, msg)


class BlackBoxEffect(SingleEffect):
    """
        Black box functional effect
    """

    def __init__(self, lhs, f, condition=top):
        super().__init__(condition)
        self.lhs = lhs
        self.function = f
        self.check_well_formed()

    def tostring(self):
        return "{} := {}".format(self.lhs, 'some function')

    def check_well_formed(self):
        """
            This method verifies
        """
        if not hasattr(self.lhs, 'shape'):
            msg = "Error declaring BlackBoxEffect, lhs needs needs to be\
                vector or matrix like"
            raise InvalidEffectError(self, msg)
        if self.lhs.shape[1] > 1:
            msg = "Error declaring BlackBoxEffect, lhs needs needs to be\
                a vector in column order"
            raise InvalidEffectError(self, msg)

        self.function.bind_to_language(self.lhs[0, 0].language)
        for k, y in enumerate(self.lhs[:, 0]):
            ys = symref(y)
            ok = symref(self.function.out_x[k].symbol)
            if ys != ok:
                msg = "Error declaring BlackBoxEffect, lhs {}-th symbol {} is not\
                matched by corresponding function output, {}".format(k, str(y), str(ok))
                raise InvalidEffectError(self, msg)


class OptimizationMetric:
    def __init__(self, opt_expression, opt_type):
        self.opt_expression = opt_expression
        self.opt_type = opt_type


def language(name="Unnamed FOL Language", theories: Optional[List[Union[str, ths.Theory]]] = None):
    """ Create an FSTRIPS-oriented First-Order Language.
        This is a standard FOL with a few convenient add-ons.
    """
    # By default, when defining a FSTRIPS problem we use FOL with equality
    theories = ['equality'] if theories is None else theories
    lang = ths.language(name, theories)
    lang.register_operator_handler("<<", Term, Term, FunctionalEffect)
    lang.register_operator_handler(">>", Term, Term, lambda lhs, rhs: FunctionalEffect(rhs, lhs))  # Inverted
    return lang


def visit_effect(effect, callback: Callable[[Any], None]):
    """ Visit all nodes in the AST of the given effect, down to formulas and terms. """
    callback(effect)
    callback(effect.condition)  # All our effects have a condition

    if isinstance(effect, (AddEffect, DelEffect)):
        callback(effect.atom)
    elif isinstance(effect, LiteralEffect):
        callback(effect.lit)
    elif isinstance(effect, FunctionalEffect):
        callback(effect.lhs)
        callback(effect.rhs)
    elif isinstance(effect, UniversalEffect):
        _ = [callback(x) for x in effect.variables]
        _ = [visit_effect(x, callback) for x in effect.effects]
    elif isinstance(effect, ProceduralEffect):
        _ = [callback(x) for x in effect.input]
        _ = [callback(x) for x in effect.output]
    else:
        raise RuntimeError(f'Unexpected type "{type(effect)}" for expression "{effect}"')
