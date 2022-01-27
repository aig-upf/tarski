;; https://github.com/dosydon/axiom_benchmarks/blob/master/mincut/domain.pddl

(define (domain min-cut)
    (:requirements :strips :typing :negative-preconditions :derived-predicates)

    (:types node edge block)

    (:predicates
    ;; static
    (adjacent ?e - edge ?f - edge)
    (edge-from ?e - edge ?n - node)
    (edge-to ?e - edge ?n - node)
    (source-node ?n - node)
    ;; derived:
    (blocked ?e - edge)
    (reachable-node ?n - node)
    (reachable-edge ?e - edge)
    (isolated ?n - node)
    )

    (:functions
    ;; primary state variables:
    (at ?b - block) - edge
    )

    (:derived (blocked ?e - edge)
        (exists (?b - block) (= (at ?b) ?e)))

    (:derived (reachable-node ?n - node) (source-node ?n))
    (:derived (reachable-node ?n - node)
        (exists (?e - edge) (and (edge-to ?e ?n)
                     (not (blocked ?e))
                     (reachable-edge ?e))))
    (:derived (reachable-edge ?e - edge)
        (exists (?n - node) (and (edge-from ?e ?n)
                     (reachable-node ?n))))
    (:derived (isolated ?n - node) (not (reachable-node ?n)))

    (:action move
    :parameters (?b - block ?from - edge ?to - edge)
    :precondition (and (adjacent ?from ?to)
              (= (at ?b) ?from))
    :effect (assign (at ?b) ?to)
    )

)