(define (domain grid)

	(:requirements :conditional-effects :typing)

	(:types
	    locatable - object
		door key - locatable
		position
	)

	(:predicates
		(at ?pos - position)
		(above ?pos1 ?pos2 - position)
		(leftof ?pos1 ?pos2 - position)
		(blocked ?pos - position)

		(hand-free)
		(holding ?key - key)

		(at-pos ?obj - locatable ?pos - position)
		(opened-by ?door - door ?key - key)
	)

	(:action up
		:parameters ()
		:precondition (and) 
		:effect (and
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos2)
						(above ?pos1 ?pos2)
						(not (blocked ?pos1))
					)
					(and
						(not (at ?pos2))
						(at ?pos1)
					)
				)
			)
		)
	)

	(:action down
		:parameters ()
		:precondition (and) 
		:effect (and
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos1)
						(above ?pos1 ?pos2)
						(not (blocked ?pos2))
					)
					(and
						(not (at ?pos1))
						(at ?pos2)
					)
				)
			)
		)
	)

	(:action left
		:parameters ()
		:precondition (and) 
		:effect (and
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos2)
						(leftof ?pos1 ?pos2)
						(not (blocked ?pos1))
					)
					(and
						(not (at ?pos2))
						(at ?pos1)
					)
				)
			)
		)
	)

	(:action right
		:parameters ()
		:precondition (and) 
		:effect (and
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos1)
						(leftof ?pos1 ?pos2)
						(not (blocked ?pos2))
					)
					(and
						(not (at ?pos1))
						(at ?pos2)
					)
				)
			)
		)
	)

	(:action pickup
		:parameters (?key - key)
		:precondition (hand-free)
		:effect (and
			(forall (?pos - position)
				(when
					(and
						(at ?pos)
						(at-pos ?key ?pos)
					)
					(and
						(not (at-pos ?key ?pos))
						(not (hand-free))
						(holding ?key)
					)
				)
			)
		)
	)

	(:action unlock
		:parameters (?door - door ?key - key)
		:precondition (and
			(holding ?key)
			(opened-by ?door ?key)
		)
		:effect (and
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos2)
						(at-pos ?door ?pos1)
						(above ?pos1 ?pos2)
					)
					(and
						(not (blocked ?pos1))
						(not (holding ?key))
						(hand-free)
					)
				)
			)
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos1)
						(at-pos ?door ?pos2)
						(above ?pos1 ?pos2)
					)
					(and
						(not (blocked ?pos2))
						(not (holding ?key))
						(hand-free)
					)
				)
			)
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos2)
						(at-pos ?door ?pos1)
						(leftof ?pos1 ?pos2)
					)
					(and
						(not (blocked ?pos1))
						(not (holding ?key))
						(hand-free)
					)
				)
			)
			(forall (?pos1 ?pos2 - position)
				(when
					(and
						(at ?pos1)
						(at-pos ?door ?pos2)
						(leftof ?pos1 ?pos2)
					)
					(and
						(not (blocked ?pos2))
						(not (holding ?key))
						(hand-free)
					)
				)
			)
		)
	)
)
