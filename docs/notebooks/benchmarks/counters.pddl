
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; counters domain, functional strips version
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain counters-fn)
    (:requirements :adl :numeric-fluents)
    (:types
        counter - object
        val     - number
    )

    (:functions
        (value ?c - counter) - val  ;; The value shown in counter ?c
        (max_int) - val ;; The maximum integer we consider - a static value
    )

    ;; Increment the value in the given counter by one
    (:action increment
         :parameters (?c - counter)
         :precondition (and (< (value ?c) (max_int)))
         :effect (and (assign (value ?c) (+ (value ?c) 1)))
    )

    ;; Decrement the value in the given counter by one
    (:action decrement
         :parameters (?c - counter)
         :precondition (and (> (value ?c) 0))
         :effect (and (assign (value ?c) (- (value ?c) 1)))
    )
)
