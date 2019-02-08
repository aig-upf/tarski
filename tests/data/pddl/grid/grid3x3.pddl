(define (problem grid6x6)
  (:domain grid)
  (:objects
	p1x1 p1x2 p1x3
	p2x1 p2x2 p2x3
	p3x1 p3x2 p3x3 - position
  )
  (:init
	(at p3x3)

	(leftof p1x1 p1x2)
	(leftof p1x2 p1x3)
	(leftof p2x1 p2x2)
	(leftof p2x2 p2x3)
	(leftof p3x1 p3x2)
	(leftof p3x2 p3x3)

	(above p1x1 p2x1)
	(above p2x1 p3x1)
	(above p1x2 p2x2)
	(above p2x2 p3x2)
	(above p1x3 p2x3)
	(above p2x3 p3x3)
  )
  (:goal (and
	(at p1x1)
  ))
)
