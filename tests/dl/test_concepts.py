"""
 Tests for the Description Logic module
"""
import pytest

import tarski.benchmarks.blocksworld
from tarski.dl import SyntacticFactory, PrimitiveRole, PrimitiveConcept, NominalConcept, StarRole, InverseRole, \
    ArityDLMismatch
from ..common import blocksworld


def test_basic_concept_creation():
    language, factory = get_bw_language()

    on_r = PrimitiveRole(language.get_predicate("on"))
    on_r2 = PrimitiveRole(language.get_predicate("on"))
    assert on_r == on_r2
    assert str(on_r) == "on"

    holding_c = PrimitiveConcept(language.get_predicate("holding"))
    ontable_c = PrimitiveConcept(language.get_predicate("ontable"))

    with pytest.raises(ArityDLMismatch):
        _ = PrimitiveRole(language.get_predicate("ontable"))
    with pytest.raises(ArityDLMismatch):
        _ = PrimitiveRole(language.get_predicate("handempty"))
    with pytest.raises(ArityDLMismatch):
        _ = PrimitiveConcept(language.get_predicate("on"))

    on_star = StarRole(PrimitiveRole(language.get_predicate("on")))
    _ = factory.create_forall_concept(on_star, PrimitiveConcept(language.get_predicate("clear")))

    _ = factory.create_exists_concept(on_r, factory.top)
    _ = factory.create_not_concept(ontable_c)

    ##
    not_holding = factory.create_not_concept(holding_c)
    blocks = language.get_constant("b1")
    a = NominalConcept(blocks.symbol, blocks.sort)
    not_a = factory.create_not_concept(a)

    # Forall(Star(on),Not({a}))
    above = StarRole(on_r)
    below = StarRole(InverseRole(on_r))
    not_above_a = factory.create_forall_concept(above, not_a)
    not_below_a = factory.create_forall_concept(below, not_a)

    c1 = factory.create_and_concept(not_holding, not_a)
    c2 = factory.create_and_concept(not_above_a, not_below_a)
    _ = factory.create_and_concept(c1, c2)


def get_bw_language():
    language = tarski.benchmarks.blocksworld.generate_strips_bw_language()
    # model = Model(lang)
    factory = SyntacticFactory(language)
    return language, factory
