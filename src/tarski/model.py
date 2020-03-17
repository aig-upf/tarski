from . import errors as err
from .syntax import Function, Constant, CompoundTerm, symref
from .syntax.predicate import Predicate


def _check_assignment(fun, point, value=None):
    assert isinstance(point, tuple)

    elements = point + (value,) if value is not None else point
    processed = []

    typ = fun.sort

    if len(typ) != len(elements):
        raise err.ArityMismatch(fun, elements)

    language = fun.language
    for element, expected_type in zip(elements, typ):

        if not isinstance(element, Constant):
            # Assume a literal value has been passed instead of its corresponding constant
            element = Constant(expected_type.cast(element), expected_type)
            # raise err.IncorrectExtensionDefinition(fun, point, value)

        if element.language != language:
            raise err.LanguageMismatch(element, element.language, language)

        if not language.is_subtype(element.sort, expected_type):
            raise err.SortMismatch(element, element.sort, expected_type)

        processed.append(element)

    if value is None:
        return tuple(processed)

    assert len(processed) > 0
    return tuple(processed[:-1]), processed[-1]


class Model:
    """ A First Order Language Model """

    def __init__(self, language, evaluator=None):
        self.evaluator = evaluator
        self.language = language
        self.function_extensions = dict()
        self.predicate_extensions = dict()

    def setx(self, term: CompoundTerm, value: Constant):
        """ Set the value of the interpretation on the given term to be equal to `value`. """
        if not isinstance(term.symbol, Function):
            raise err.SemanticError("Model.set() can only set the value of function symbols")
        if term.symbol.builtin:
            raise err.SemanticError(f"Model.set() attempted to redefine builtin symbol '{term.symbol}'")
        for st in term.subterms:
            if not isinstance(st, Constant):
                raise err.SemanticError(f"Model.set(): subterms of '{term}' need to be constants")
        point, value = _check_assignment(term.symbol, tuple(term.subterms), value)
        definition = self.function_extensions.setdefault(term.symbol.signature, ExtensionalFunctionDefinition())
        if not isinstance(definition, ExtensionalFunctionDefinition):
            raise err.SemanticError("Cannot define extension of intensional definition")

        definition.set(point, value)

    def set(self, fun, *args):
        """ Set the value of fun(args[:-1]) to be args[-1] for the current interpretation """
        # TODO: Deprecate in favor of Model.setx()
        self.setx(fun(*args[:-1]), args[-1])

    def add(self, predicate, *args):
        """ """
        from .syntax import Atom
        if isinstance(predicate, Atom):
            args = predicate.subterms
            predicate = predicate.predicate

        if not isinstance(predicate, Predicate):
            raise err.SemanticError("Model.add() can only set the value of predicate symbols")
        if predicate.builtin:
            raise err.SemanticError(f"Model.add() attempted to redefine builtin symbol '{predicate}'")
        point = _check_assignment(predicate, args)
        definition = self.predicate_extensions.setdefault(predicate.signature, set())
        definition.add(wrap_tuple(point))

    def remove(self, predicate: Predicate, *args):
        self.predicate_extensions[predicate.signature].remove(wrap_tuple(args))

    def value(self, fun: Function, point):
        """ Return the value of the given function on the given point in the current model """
        definition = self.function_extensions[fun.signature]
        return definition.get(point)

    def holds(self, predicate: Predicate, point):
        """ Return true iff the given predicate is true on the given point in the current model """
        return predicate.signature in self.predicate_extensions and \
            wrap_tuple(point) in self.predicate_extensions[predicate.signature]

    def list_all_extensions(self):
        """ Return a mapping between predicate and function signatures and a list of all their respective extensions.
        This list *unwraps* the TermReference's used internally in this class back into plain Tarski terms, so that
        you can rely on the returned extensions being made up of Constants, Variables, etc., not TermReferences
        """
        from .syntax.util import get_symbols
        exts = {k: [unwrap_tuple(tup) for tup in ext] for k, ext in self.predicate_extensions.items()}
        exts.update((k, [unwrap_tuple(point) + (value, ) for point, value in ext.data.items()])
                    for k, ext in self.function_extensions.items())

        # Add the empty extensions for those symbols in the language that have no true atom
        for symbol in get_symbols(self.language, type_="predicate", include_builtin=False):
            if symbol.signature not in exts:
                exts[symbol.signature] = set()
        for symbol in get_symbols(self.language, type_="function", include_builtin=False):
            if symbol.signature not in exts:
                exts[symbol.signature] = ExtensionalFunctionDefinition()

        return exts

    def as_atoms(self):
        """ Return a representation of the model as a list of atoms that are true. For functional symbols f, return
        tuples of the form (f(o1, ..., on), value)
         """
        atoms = []
        for k, ext in self.predicate_extensions.items():
            pred = self.language.get_predicate(k[0])
            # create one atom per tuple in the predicate's extension:
            atoms += [pred(*unwrap_tuple(tup)) for tup in ext]

        for k, ext in self.function_extensions.items():
            fun = self.language.get_function(k[0])
            for point, value in ext.data.items():
                atoms.append((fun(*unwrap_tuple(point)), value))

        return atoms

    def get_extension(self, symbol):
        """ Return the extension of the given (predicate or function) symbol in the
         current model. """
        if isinstance(symbol, Predicate):
            return self.predicate_extensions.get(symbol.signature, set())

        # else we must have a function
        return self.function_extensions.get(symbol.signature, ExtensionalFunctionDefinition())

    def __getitem__(self, arg):
        if self.evaluator is None:
            raise ModelWithoutEvaluatorError(arg)

        try:
            expr, sigma = arg
            return self.evaluator(expr, self, sigma)
        except (ValueError, TypeError):
            # MRJ: This for expressions that have the __getitem__ operator overloaded
            return self.evaluator(arg, self)

    def __str__(self):
        npreds = len(self.predicate_extensions)
        nfuns = len(self.function_extensions)
        return f'Model(num_predicates="{npreds}", num_functions="{nfuns}")'
    __repr__ = __str__


def create(lang, evaluator=None):
    """ Create a Tarski model with given evaluator. """
    return Model(lang, evaluator)


class ExtensionalFunctionDefinition:
    def __init__(self):
        self.data = dict()

    def set(self, point, value):
        assert isinstance(point, tuple)
        assert isinstance(value, Constant)
        self.data[wrap_tuple(point)] = value

    def get(self, point):
        return self.data[wrap_tuple(point)]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data.items()

# class IntensionalFunctionDefinition:
#     pass


def wrap_tuple(tup):
    """ Create a tuple of Term references from a tuple of terms """
    return tuple(symref(a) for a in tup)


def unwrap_tuple(tup):
    """ Create a tuple of Tarski terms from a tuple of Term references"""
    return tuple(ref.expr for ref in tup)


class ModelWithoutEvaluatorError(err.SemanticError):
    def __init__(self, exp):
        super().__init__(f'Attempted to evaluate expression "{exp}" on a model with no attached evaluator. '
                         f'Please set some evaluator into the model before attempting such evaluations')
