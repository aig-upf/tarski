# tarski: An AI Planning Modeling Framework
#
# Author: Miquel Ramirez (miquel.ramirez@pm.me) 2018-2022
#
#----------------------------------------------------------------------------------------------------------------------
# io/pddl/__init__.py
#
# PDDL common definitions and data structures
#----------------------------------------------------------------------------------------------------------------------

from enum import Enum


class Features(Enum):
    """PDDL 3.1 features"""
    STRIPS = 0,
    TYPING = 1,
    NEGATIVE_PRECONDITIONS = 2,
    DISJUNCTIVE_PRECONDITIONS = 3,
    EQUALITY = 4,
    EXISTENTIAL_PRECONDITIONS = 5,
    UNIVERSAL_PRECONDITIONS = 6,
    CONDITIONAL_EFFECTS = 7,
    NUMERIC_FLUENTS = 8,
    DURATIVE_ACTIONS = 9,
    DURATION_INEQUALITIES = 10,
    CONTINUOUS_EFFECTS = 11,
    DERIVED_PREDICATES = 12,
    TIMED_INITIAL_LITERALS = 13,
    PREFERENCES = 14,
    CONSTRAINTS = 15,
    ACTION_COSTS = 16,
    OBJECT_FLUENTS = 17


supported_features = {
    Features.STRIPS,
    Features.TYPING,
    Features.NEGATIVE_PRECONDITIONS,
    Features.EQUALITY,
    Features.DURATIVE_ACTIONS,
    Features.OBJECT_FLUENTS,
    Features.DERIVED_PREDICATES,
    Features.NUMERIC_FLUENTS
}
