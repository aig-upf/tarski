(define (domain blocks)

    (:requirements :strips :equality :typing :negative-preconditions)

    (:types
        block - object
    )

    (:constants
        nothing - object
    )

    (:predicates
        (on_table ?b1 - block)
    )

    (:functions
        (above ?b1 - block) - object
    )

    (:action move
        :parameters (?b_m ?b_from ?b_to - block)
        :precondition
        (and
            (= (above ?b_m) nothing)
            (= (above ?b_from) ?b_m)
            (= (above ?b_to) nothing)
            (not (= ?b_m ?b_to))
            (not (= ?b_m ?b_from))
        )
        :effect
        (and
            (assign (above ?b_from) nothing)
            (assign (above ?b_to) ?b_m)
        )
    )

    (:action moveToTable
        :parameters (?b_m ?b_from - block)
        :precondition
        (and
            (= (above ?b_m) nothing)
            (= (above ?b_from) ?b_m)
            (not (on_table ?b_m))
            (not (= ?b_m ?b_from))
        )
        :effect
        (and
            (assign (above ?b_from) ?b_m)
            (on_table ?b_m)
        )
    )

    (:action moveFromTable
        :parameters (?b_m ?b_to - block)
        :precondition (and
            (= (above ?b_m) nothing)
            (= (above ?b_to) nothing)
            (on_table ?b_m)
            (not (= ?b_m ?b_to))
        )
        :effect (and
            (not (on_table ?b_m))
            (assign (above ?b_to) ?b_m)
        )
    )

)