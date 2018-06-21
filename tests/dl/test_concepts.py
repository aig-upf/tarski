"""
 Tests for the Description Logic module
"""
import pytest
from tarski.dl import SyntacticFactory, BasicRole, BasicConcept, SingletonConcept, StarRole, InverseRole, \
    ArityDLMismatch
from ..common import blocksworld


def test_basic_concept_creation():
    language, syntaxis = get_bw_language()

    on_r = BasicRole(language.get_predicate("on"))
    on_r2 = BasicRole(language.get_predicate("on"))
    assert on_r == on_r2
    assert str(on_r) == "on"

    holding_c = BasicConcept(language.get_predicate("holding"))
    ontable_c = BasicConcept(language.get_predicate("ontable"))

    with pytest.raises(ArityDLMismatch):
        _ = BasicRole(language.get_predicate("ontable"))
    with pytest.raises(ArityDLMismatch):
        _ = BasicRole(language.get_predicate("handempty"))
    with pytest.raises(ArityDLMismatch):
        _ = BasicConcept(language.get_predicate("on"))

    on_star = StarRole(BasicRole(language.get_predicate("on")))
    _ = syntaxis.create_forall_concept(on_star, BasicConcept(language.get_predicate("clear")))

    _ = syntaxis.create_exists_concept(on_r, syntaxis.top)
    _ = syntaxis.create_not_concept(ontable_c)

    ##
    not_holding = syntaxis.create_not_concept(holding_c)
    blocks = language.get_constant("b1")
    a = SingletonConcept(blocks.symbol, blocks.sort)
    not_a = syntaxis.create_not_concept(a)

    # Forall(Star(on),Not({a}))
    above = StarRole(on_r)
    below = StarRole(InverseRole(on_r))
    not_above_a = syntaxis.create_forall_concept(above, not_a)
    not_below_a = syntaxis.create_forall_concept(below, not_a)

    c1 = syntaxis.create_and_concept(not_holding, not_a)
    c2 = syntaxis.create_and_concept(not_above_a, not_below_a)
    _ = syntaxis.create_and_concept(c1, c2)


def get_bw_language():
    language = blocksworld.generate_small_strips_bw_language()
    # model = Model(lang)
    syntaxis = SyntacticFactory(language)
    return language, syntaxis
