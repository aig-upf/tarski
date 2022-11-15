;; Adapted from: https://github.com/josej30/Planner-Sat-Constraints
;; We use existential preconditions (exists) to remove as many parameters from the actions as possible

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
         :parameters    (?t - truck ?from ?to - location)
         :precondition  (and 
                             (exists (?c - city)
                                (and (at ?t ?from) (in-city ?from ?c) (in-city ?to ?c))
                              )
                         )
         :effect        (and (not (at ?t ?from))
                             (at ?t ?to)))

(:action fly
         :parameters    (?a - airplane ?from ?to - airport)
         :precondition  (at ?a ?from)
         :effect        (and (not (at ?a ?from))
                             (at ?a ?to)))

(:action load
         :parameters    (?v - vehicle ?p - package ?l - location)
         :precondition  (and (at ?v ?l)
                             (at ?p ?l))
         :effect        (and (not (at ?p ?l))
                             (in ?p ?v)))

(:action unload
         :parameters    (?v - vehicle ?p - package ?l - location)
         :precondition  (and (at ?v ?l)
                             (in ?p ?v))
         :effect        (and (not (in ?p ?v))
                             (at ?p ?l)))

)