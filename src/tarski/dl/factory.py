
import logging

from .. import FirstOrderLanguage
from ..syntax import builtins
from . import Concept, Role, UniversalConcept, PrimitiveConcept, NotConcept, ExistsConcept, ForallConcept, \
    EqualConcept, PrimitiveRole, RestrictRole, AndConcept, EmptyConcept, CompositionRole, NominalConcept, NullaryAtom, \
    GoalNullaryAtom, GoalConcept, GoalRole, OrConcept


def filter_subnodes(elem, t):
    """ Return a list with all subnodes of a certain concept or role which conform to the given Python type """
    return list(filter(lambda x: type(x) == t, elem.flatten()))


def compute_dl_vocabulary(lang):
    """ Return the DL vocabulary for the given language.
    This is the list of all predicates of arity 0, 1 and 2, all types, and all functions of arity 0 and 1
    """
    v = [(p.symbol, p) for p in lang.predicates if not builtins.is_builtin_predicate(p) and 0 <= p.arity <= 2] +\
        [(f.symbol, f) for f in lang.functions if not builtins.is_builtin_function(f) and f.arity in (0, 1)] + \
        [(s.name, s) for s in lang.sorts if not s.builtin]
    return dict(v)


class SyntacticFactory:
    def __init__(self, language: FirstOrderLanguage):
        self.language = language
        self.universe_sort = language.get_sort('object')
        self.top = UniversalConcept(self.universe_sort.name)
        self.bot = EmptyConcept(self.universe_sort.name)

    def generate_primitives_from_language(self, nominals, types, goal_predicates):
        """ Generate primitive concepts from the language taking into account only the given nominals """

        concepts, roles, primitive_atoms = [], [], []
        for predfun in list(self.language.predicates) + list(self.language.functions):
            if builtins.is_builtin_predicate(predfun) or builtins.is_builtin_function(predfun):
                # Skip "=" and other built-in symbols
                # TODO We might want to revise this and allow for certain builtins
                continue

            if predfun.uniform_arity() == 0:
                primitive_atoms.append(NullaryAtom(predfun))
                if predfun.symbol in goal_predicates:
                    primitive_atoms.append(GoalNullaryAtom(predfun))

            elif predfun.uniform_arity() == 1:
                concepts.append(PrimitiveConcept(predfun))
                if predfun.symbol in goal_predicates:
                    concepts.append(GoalConcept(predfun))

            elif predfun.uniform_arity() == 2:
                roles.append(PrimitiveRole(predfun))
                if predfun.symbol in goal_predicates:
                    roles.append(GoalRole(predfun))

            else:
                logging.warning('Predicate/Function "{}" with normalized arity > 2 ignored'.format(predfun))

        for c in nominals:
            concepts.append(NominalConcept(c.symbol, c.sort))

        for t in types:
            concepts.append(PrimitiveConcept(t))

        logging.info('Primitive (nullary) atoms : {}'.format(", ".join(map(str, primitive_atoms))))
        logging.info('Primitive (unary) concepts: {}'.format(", ".join(map(str, concepts))))
        logging.info('Primitive (binary) roles  : {}'.format(", ".join(map(str, roles))))

        return concepts, roles, primitive_atoms

    def create_exists_concept(self, role: Role, concept: Concept):
        # exists(R.C) = { x | exists y R(x,y) and C(y) }

        result = ExistsConcept(role, concept)
        _, s2 = role.sort

        if concept == self.bot:
            logging.debug('Concept "{}" is statically empty'.format(result))
            return None

        # TODO ADD: If C is a sort-concept of the same sort than s2, then the concept will be equiv to exist(R.True)
        if not self.language.are_vertically_related(s2, concept.sort):
            logging.debug('Concept "{}" pruned for type-inconsistency reasons'.format(result))
            return None

        if isinstance(role, RestrictRole) and concept == self.top:
            return None  # Is syntactically equivalent to a simpler exists concept

        return result

    def create_not_concept(self, concept: Concept):
        if isinstance(concept, NotConcept):
            return None

        result = NotConcept(concept, self.universe_sort)
        return result

    def create_forall_concept(self, role: Role, concept: Concept):
        # forall(R.C) = { x | forall y R(x,y) implies C(y) }

        result = ForallConcept(role, concept)
        _, s2 = role.sort

        if isinstance(concept, UniversalConcept):
            # logging.debug('Concept "{}" equivalent to simpler concept'.format(result))
            return None

        if not self.language.are_vertically_related(s2, concept.sort):
            logging.debug('Concept "{}" pruned for type-inconsistency reasons'.format(result))
            return None

        return result

    def create_and_concept(self, c1: Concept, c2: Concept):
        # C1 AND C2 = { x | C1(x) AND C2(x) }

        sort = self.language.most_restricted_type(c1.sort, c2.sort)

        if c1 == c2:
            return None  # No sense in C and C

        if c1 in (self.top, self.bot) or c2 in (self.top, self.bot):
            logging.debug('AND of {} and {} pruned, no sense in AND\'ing with top or bot'.format(c1, c2))
            return None

        if sort is None:
            # i.e. c1 and c2 are disjoint types
            logging.debug('AND of {} and {} pruned for type-inconsistency reasons'.format(c1, c2))
            return None

        return AndConcept(c1, c2, sort)

    def create_or_concept(self, c1: Concept, c2: Concept):
        sort = self.language.most_restricted_type(c1.sort, c2.sort)

        if c1 == c2:
            return None  # No sense in C OR C

        if c1 in (self.top, self.bot) or c2 in (self.top, self.bot):
            logging.debug('OR of {} and {} pruned, no sense in OR\'ing with top or bot'.format(c1, c2))
            return None

        return OrConcept(c1, c2, sort)

    def create_equal_concept(self, r1: Role, r2: Role):
        assert isinstance(r1, Role) and isinstance(r2, Role)
        # The sort of the resulting concept will be the most restricted sort between the left sorts of the two roles
        sort = self.language.most_restricted_type(r1.sort[0], r2.sort[0])

        if sort is None:
            logging.debug('Concept "EqualConcept({},{})" pruned for type-inconsistency reasons'.format(r1, r2))
            return None
        return EqualConcept(r1, r2, sort)

    def create_restrict_role(self, r: Role, c: Concept):

        result = RestrictRole(r, c)
        if not self.language.are_vertically_related(r.sort[1], c.sort):
            logging.debug('Role "{}" pruned for type-inconsistency reasons'.format(result))
            return None

        if isinstance(c, UniversalConcept) or c == self.bot:
            logging.debug('Role "{}" pruned; no sense in restricting to top / bot concepts'.format(result))
            return None

        if isinstance(r, RestrictRole):
            logging.debug('Role "{}" pruned; no direct nesting of restrictions'.format(result))
            return None

        return result

    def create_composition_role(self, r1: Role, r2: Role):

        # Compose only on primitives or their inversions
        # if (not isinstance(r1, (PrimitiveRole, InverseRole)) or
        #    not isinstance(r2, (PrimitiveRole, InverseRole))):
        #     return None

        result = CompositionRole(r1, r2)

        if not self.language.are_vertically_related(r1.sort[1], r2.sort[0]):
            logging.debug('Role "{}" pruned for type-inconsistency reasons'.format(result))
            return None

        num_comp = len(filter_subnodes(result, CompositionRole))
        if num_comp > 2:
            logging.debug('Role "{}" pruned: number of compositions ({}) exceeds threshold'.format(result, num_comp))
            return None

        return result
