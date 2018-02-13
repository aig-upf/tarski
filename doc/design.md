
# Design Notes

## First-Order Logic

One of the aims of the package is to follow as closely as possible the textbook definition of 
the standard first-order logic constructs. 
In particular, we aim at keeping a clear _distinction between syntax and semantics_.
Here we should follow a separation-of-concerns approach and take advantage of the clean an elegant
design mathematical definitions. Our implementation should have a syntax layer and a semantic layer:

* _Syntax_ is concerned with the correct formation of the language constructs: terms, formulas, sentences, 
from the (lower-level) elements of the first-order vocabulary: connectives, quantifiers, variables, function and predicate symbols.

* _Semantics_ is concerned with the meaning assigned to these constructs: models (interpretations), their universes, 
the denotations of terms under any given model, the satisfiability of formulas by any given model.
 
It is thus clear that the syntax module / layer of our implementation should have no knowledge about anything
pertaining to the semantic level.
