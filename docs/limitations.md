
# Known Limitations

At the moment, Tarski is able to parse problems specified in PDDL, Functional STRIPS and RDDL, 
but (1) parsing of derived predicates is not supported yet, and (2)
the PDDL `either` keyword for defining compound types is not supported, and it is unlikely it will ever be.
Additionally, and for compatibility reasons with old standard benchmarks, the parser represents all predicate,
function (including constants) and PDDL types (i.e. FOL sorts) _in lowercase_.  