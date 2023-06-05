(define (domain recharging-robots)
(:requirements :typing :adl)
(:types
    location - object
    robot - object
    battery-level - object
    config - object
)

(:predicates
    (at ?r - robot ?l - location)
    (stopped ?r - robot)
    (battery-predecessor ?f1 - battery-level ?f2 - battery-level)
    (battery ?r - robot ?f - battery-level)
    (connected ?l1 - location ?l2 - location)
    (guarded ?l - location)
    (guard-config ?c - config ?l - location)
    (config-fullfilled ?c - config)
)

(:functions
    (total-cost) - number
)

(:action move
    :parameters (?r - robot ?from - location ?to - location
                 ?fpre - battery-level ?fpost - battery-level)
    :precondition
        (and
            (not (stopped ?r))
            (at ?r ?from)
            (battery ?r ?fpre)
            (battery-predecessor ?fpost ?fpre)
            (or (connected ?from ?to) (connected ?to ?from))
        )
    :effect
        (and
            (not (at ?r ?from))
            (at ?r ?to)
            (not (battery ?r ?fpre))
            (battery ?r ?fpost)
            (increase (total-cost) 1)
        )
)

(:action recharge
    :parameters (?rfrom - robot ?rto - robot ?loc - location
                 ?fpre-from - battery-level ?fpost-from - battery-level
                 ?fpre-to - battery-level ?fpost-to - battery-level)
    :precondition
        (and
            (not (= ?rfrom ?rto))
            (at ?rfrom ?loc)
            (at ?rto ?loc)
            (battery ?rfrom ?fpre-from)
            (battery ?rto ?fpre-to)
            (battery-predecessor ?fpost-from ?fpre-from)
            (battery-predecessor ?fpre-to ?fpost-to)
        )
    :effect
        (and
            (not (battery ?rfrom ?fpre-from))
            (battery ?rfrom ?fpost-from)
            (not (battery ?rto ?fpre-to))
            (battery ?rto ?fpost-to)
            (increase (total-cost) 1)
        )
)

(:action stop-and-guard
    :parameters (?r - robot ?l - location)
    :precondition
        (and
            (not (stopped ?r))
            (at ?r ?l)
        )
    :effect
        (and
            (stopped ?r)
            (guarded ?l)
            (forall (?l2 - location)
                (when (or (connected ?l ?l2) (connected ?l2 ?l))
                      (guarded ?l2)
                )
            )
        )
)

(:action verify-guard-config
    :parameters (?c - config)
    :precondition
        (and
            (forall (?l - location)
                (imply (guard-config ?c ?l) (guarded ?l))
            )
        )
    :effect
        (and
            (forall (?r - robot) (not (stopped ?r)))
            (forall (?l - location) (not (guarded ?l)))
            (config-fullfilled ?c)
        )
)

)
