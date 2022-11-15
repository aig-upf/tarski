(define (problem bw_both_generative_policies_0)

(:domain logistics)

(:objects
	c0 c1 - city
     a0 a1 - airport
     plane - airplane
     p0 - package
)

(:init
	(in-city a0 c0)
	(in-city a1 c1)
	(at plane a0)
	(at p0 a1)
)

(:goal (and
	(at p0 a0)
))
)