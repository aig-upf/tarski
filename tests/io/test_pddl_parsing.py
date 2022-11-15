# Unit tests for PDDL lexer, parser and instance structure
#
# Contact: Miquel Ramirez (miquel.ramirez@pm.me)
import tempfile

import pytest

import tarski.io.pddl.errors
from tarski.io.pddl.lexer import PDDLlex
from tarski.io.pddl import Features
from tarski.io.pddl.parser import PDDLparser, UnsupportedFeature
from tarski.syntax.visitors import CollectEqualityAtoms


@pytest.mark.pddl
def test_pddl_lexer_airport_002_domain():

    pddl_data = None
    with open('tests/data/pddl/temporal/ipc18/airport-temporal-strips/2/domain.pddl') as instream:
        pddl_data = instream.read()

    lexer = PDDLlex()
    lexer.build()

    lexer.input(pddl_data)

    count = 0
    for tok in lexer():
        count += 1

    assert count == 5930


@pytest.mark.pddl
def test_pddl_lexer_cushing_domain():

    pddl_data = None
    with open('tests/data/pddl/temporal/ipc18/cushing/domain.pddl') as instream:
        pddl_data = instream.read()

    lexer = PDDLlex()
    lexer.build()

    lexer.input(pddl_data)

    count = 0
    for tok in lexer():
        count += 1

    assert count == 253


@pytest.mark.pddl
def test_basic_constructs():
    pddl_data = """(define 
        (domain FOO)
        (:requirements :durative-actions :derived-predicates :typing)
        (:types 
                paz naz - caz
                bar baz
        )
        (:constants
            a0 a1 a2 a3 a4 a5 - bar
            d0 d1 d2 d3 d4 d5 - baz
            b1 b2 b3 b4 b5 b6 - paz
            c1 c2 c3 c4 c5 c6 - naz
        )
        (:predicates 
            (p ?x - bar ?y - baz)
            (q ?x - bar ?y - baz)
            (r ?x - bar)
            (s ?x - bar)
            (t1 ?y - bar)
            (t2 ?y - bar)
            (t3 ?y - bar)
            (t4 ?y - bar)
        )

        (:functions
            (h ?x - bar) - baz
            (g ?x - baz)
        )

        (:action dummy1
            :parameters (?x - bar)
            :precondition   (and
                                    (not (r ?x)) 
                            )
            :effect     (and
                            (r ?x)
                        )
        )

        (:durative-action dummy
            :parameters (?x - bar ?y - baz)
            :duration   (= ?duration 10)
            :condition  (and
                            (at start (q ?x ?y))
                            (over all (r ?x)) 
                        )
            :effect     (and
                            (at start (q ?x ?y))
                            (at end (not (q ?x ?y)))
                        )
        )

        (:derived
            (s ?x - bar)
            (and    (t1 ?x)
                    (t2 ?x)
                    (t3 ?x)
                    (t4 ?x)
            )
        )
    )

    (define (problem INSTANCE_001)
        (:domain FOO)
        (:objects
            z0 z1 z2 z3 - bar
        )
        (:init
            (p z2 d2)
            (p z3 d3)
        )
        (:goal
            (and    (p z0 d0)
                    (p z1 d1))
        )
        (:metric
            minimize
                (total-time)
        )
    )
    """
    parser = PDDLparser(debug=True)

    with tempfile.NamedTemporaryFile() as f:
        parser.build(logfile=f.name)

        parser.parse(pddl_data)

        assert parser.domain_name == 'foo'
        assert parser.problem_name == 'instance_001'
        assert Features.DURATIVE_ACTIONS in parser.required_features
        assert Features.TYPING in parser.required_features

        instance = parser.instance
        assert instance is not None

        print("Functions", len(instance.functions))
        print("Predicates", len(instance.predicates))
        print("Types", len(instance.types))
        print("Constants", len(instance.domains))
        print("Actions: instantaneous: {} durative: {}".format(len(instance.actions), len(instance.durative)))
        print("Derived predicates:", len(instance.derived))
        print("Initial State literals", len(instance.init))

        eq_atoms_visitor = CollectEqualityAtoms()
        eq_atoms_visitor.visit(instance.goal)
        goal_atoms = eq_atoms_visitor.atoms
        print("Goal literals", len(goal_atoms))

        assert len(instance.types) == 6
        assert 'object' in instance.types
        assert len(instance.domains) == 4
        assert len(instance.functions) == 2
        assert len(instance.predicates) == 8
        assert len(instance.types) == 6
        assert len(instance.actions) == 1
        assert len(instance.durative) == 1
        assert len(instance.derived) == 1
        assert len(instance.init) == 2
        assert len(goal_atoms) == 2


@pytest.mark.pddl
def test_temporal_numeric():

    pddl_data = ""

    with open('tests/data/pddl/temporal/ipc08/elevators/p01-domain.pddl') as instream:
        pddl_data = instream.read()

    with open('tests/data/pddl/temporal/ipc08/elevators/p01.pddl') as instream:
        pddl_data += instream.read()

    parser = PDDLparser(debug=True)

    with tempfile.NamedTemporaryFile() as f:
        parser.build(logfile=f.name)

        parser.parse(pddl_data)

        #assert parser.domain_name == 'foo'
        #assert parser.problem_name == 'instance_001'
        #assert Features.DURATIVE_ACTIONS in parser.required_features
        #assert Features.TYPING in parser.required_features

        instance = parser.instance
        assert instance is not None

        print("Functions", len(instance.functions))
        print("Predicates", len(instance.predicates))
        print("Types", len(instance.types))
        print("Constants", len(instance.domains))
        print("Actions: instantaneous: {} durative: {}".format(len(instance.actions), len(instance.durative)))
        print("Derived predicates:", len(instance.derived))
        print("Initial State literals", len(instance.init))

        eq_atoms_visitor = CollectEqualityAtoms()
        eq_atoms_visitor.visit(instance.goal)
        goal_atoms = eq_atoms_visitor.atoms
        print("Goal literals", len(goal_atoms))

        #assert len(instance.types) == 6
        #assert 'object' in instance.types
        #assert len(instance.constants) == 4
        #assert len(instance.functions) == 2
        #assert len(instance.predicates) == 8
        #assert len(instance.types) == 6
        #assert len(instance.actions) == 1
        #assert len(instance.durative) == 1
        #assert len(instance.derived) == 1
        #assert len(instance.init) == 2
        #assert len(goal_atoms) == 2


@pytest.mark.pddl
def test_preconditions_with_existential_effects():

    pddl_data = """\
(define (domain logistics)
(:requirements :strips :typing :existential-preconditions) 
(:types  city location thing - object
         package vehicle - thing
         truck airplane - vehicle  
         airport - location)
(:predicates  (in-city ?l - location ?c - city)
              (at ?obj - thing ?l - location)
              (in ?p - package ?veh - vehicle))
(:action drive
         :parameters    (?t - truck ?to - location)
         :precondition  (and 
                             (exists (?c - city ?from - location)
                                (and (at ?t ?from) (in-city ?from ?c) (in-city ?to ?c))
                              ))
         :effect        (and (not (at ?t ?from))
                             (at ?t ?to)))
)
"""
    parser = PDDLparser(debug=True)

    with tempfile.NamedTemporaryFile() as f:
        parser.build(logfile=f.name)

        with pytest.raises(tarski.io.pddl.errors.UnsupportedFeature):
            parser.parse(pddl_data)

        assert parser.domain_name == 'logistics'
        assert Features.TYPING in parser.required_features
        assert Features.EXISTENTIAL_PRECONDITIONS in parser.required_features


