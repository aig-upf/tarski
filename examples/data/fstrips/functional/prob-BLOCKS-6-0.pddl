(define
    (problem pddl)
    (:domain blocks)
    (:objects e a b c f d - block)
    (:init
        (= (above D) nothing) (= (above F) nothing) (= (above C) A) (= (above A) D) (= (above B) E) (= (above E) F)
        (on_table B) (on_table C)
    )
    (:goal
      (and
        (= (above E A)) (= (above A) B) (= (above B) C) (= (above F) E) (= (above D) F)
      )
    )
)
