#!/usr/bin/env python3
import sys

from tarski import fstrips

sys.path.append('../src')
from src import tarski as tsk

if __name__ == "__main__":

    # First we create the necessary elements of the FOL language
    fol = fstrips.language()  # i.e. create a (first-order) "language" object, which will act as facade to all things FOL

    block = fol.sort('block')
    place = fol.sort('place')

    loc = fol.function('loc', 'place')
    clear = fol.predicate('clear', 'place')

    b1 = fol.const('b1', block)
    b2 = fol.const('b2', block)
    b3 = fol.const('b3', block)
    table = fol.const('table', place)


    # Now we create the different elements of the planning problem, which mostly build
    # on the first-order language we have created above

    # The goal
    goal = (loc(b1) == b2) & (loc(b2) == table)

    # The initial state
    # ??? TODO How to cleanly specify the denotation of all symbols? To be though about.
    # Do we want to model FOL interpretations as objects? (in the object-oriented sense)
    # One possibility: extensions. For functions, use a Python map; for predicates, a set.
    loc_denotation = fol.function_denotation({b1: table, b2: table})
    clear_denotation = fol.predicate_denotation({...})

    # Another possibility which would allow a more incremental building of the denotation:
    # Recall: a FSTRIPS state is nothing other than a full first-order interpretation
    init = tsk.interpretation(fol)  # The interpretation will likely need to be bound to the particular FOL
    init.define(loc, b1, table)  # We could perhaps also accept passing "loc" as a string
    init.define(loc, b2, table)
    init.define(clear, table)  # The table is always clear
    init.define(clear, b1)
    init.define(clear, b2)


    # The actions
    move = tsk.action(fol,
                      name="move",
                      parameters=[fol.variable("c", block), fol.variable("to", place)],
                      precondition=(clear(to) & ...),
                      effects=[
                          ...
                      ]
                      )

    # An interesting thing would be to provide helpers to ease up the task of writing this models by hand. Example:
    move = tsk.action(header="move(b: block, to: place)",  # i.e. the action name, parameters, and their types
                                                           # can be easily and unambiguously deduced from this "header"

                      )





    # Finally set up all the pieces together
    problem = tsk.problem(domain="blocksworld", # or use setters, etc., but I like this style
                          instance="two_blocks_on_table",
                          init=init,
                          goal=goal,
                          actions=[move]
                          )
