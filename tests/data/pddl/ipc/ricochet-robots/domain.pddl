(define (domain ricochet-robots)
(:requirements :typing :adl)

(:types
    robot - object
    cell - object
    direction - object
)

(:predicates
    ;; ?cnext is right next to ?c in the direction of ?dir
    (next ?c - cell ?cnext - cell ?dir - direction)
    ;; moving from ?c in the direction ?dir is blocked
    (blocked ?c - cell ?dir - direction)
    ;; Robot ?r is located in the cell ?c
    (at ?r - robot ?c - cell)
    ;; No robot is located in the cell ?c
    (free ?c - cell)
    ;; No robot is moving anywhere
    (nothing-is-moving)
    ;; Robot ?r is moving in the direction ?dir
    (is-moving ?r - robot ?dir - direction)
)

(:functions
    (total-cost) - number

    ;; The costs of actions are configurable.
    ;; If we want to count only the number of movements of robots instead of
    ;; counting all steps from a cell to cell (as it would be in the real
    ;; game), then we need to set
    ;;      (= (go-cost) 1)
    ;;      (= (step-cost) 0)
    ;;      (= (stop-cost) 0)
    (go-cost) - number
    (step-cost) - number
    (stop-cost) - number
)

;; Starts movement of the robot ?r in the direction ?dir
(:action go
    :parameters (?r - robot ?dir - direction)
    :precondition
        (and
            (nothing-is-moving)

            ;; If we want to make sure that the robot can actually make a step
            ;; in the specified direction, then we need to add the following
            ;; (and the corresponding parameters ?cfrom and ?cto):
            ;;
            ;; (at ?r ?cfrom)
            ;; (next ?cfrom ?cto ?dir)
            ;; (free ?cto)
            ;; (not (blocked ?cfrom ?dir))
        )
    :effect
        (and
            (not (nothing-is-moving))
            (is-moving ?r ?dir)
            (increase (total-cost) (go-cost))
        )
)

;; Make one step from the cell ?cfrom to the cell ?cto with the robot ?r
;; Robot is allowed to make the step only if it is the (only) one currently
;; moving, and it is moving in the direction ?dir
(:action step
    :parameters (?r - robot ?cfrom - cell ?cto - cell ?dir - direction)
    :precondition
        (and
            (is-moving ?r ?dir)
            (at ?r ?cfrom)
            (next ?cfrom ?cto ?dir)
            (free ?cto)
            (not (blocked ?cfrom ?dir))
        )
    :effect
        (and
            (not (at ?r ?cfrom))
            (free ?cfrom)
            (not (free ?cto))
            (at ?r ?cto)
            (increase (total-cost) (step-cost))
        )
)

;; Stopping of the robot is split between
;; (i) stop-at-barrier which stops the robot if it cannot move further due to
;;     a barrier expressed with (blocked ...) predicate
;; (ii) stop-at-robot which stops the robot if the next step is blocked by
;;      another robot
(:action stop-at-barrier
    :parameters (?r - robot ?cat - cell ?dir - direction)
    :precondition
        (and
            (is-moving ?r ?dir)
            (at ?r ?cat)
            (blocked ?cat ?dir)
        )
    :effect
        (and
            (not (is-moving ?r ?dir))
            (nothing-is-moving)
            (increase (total-cost) (stop-cost))
        )
)

(:action stop-at-robot
    :parameters (?r - robot ?cat - cell ?cnext - cell ?dir - direction)
    :precondition
        (and
            (is-moving ?r ?dir)
            (at ?r ?cat)
            (next ?cat ?cnext ?dir)
            (not (free ?cnext))
        )
    :effect
        (and
            (not (is-moving ?r ?dir))
            (nothing-is-moving)
            (increase (total-cost) (stop-cost))
        )
)

;; (:action stop
;;     :parameters (?r - robot ?cat - cell ?dir - direction)
;;     :precondition
;;         (and
;;             (is-moving ?r ?dir)
;;             (at ?r ?cat)
;;             (or
;;                 (blocked ?cat ?dir)
;;                 (forall (?cnext - cell)
;;                     (imply (next ?cat ?cnext ?dir) (not (free ?cnext)))
;;                 )
;;             )
;;         )
;;     :effect
;;         (and
;;             (not (is-moving ?r ?dir))
;;             (nothing-is-moving)
;;             (increase (total-cost) (stop-cost))
;;         )
;; )
)
