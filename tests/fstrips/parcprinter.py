"""
    Generate Parcprinter language elements
"""
import tarski as tsk
import tarski.model

from tests.common import parcprinter
from tarski import fstrips as fs
from tarski.syntax import *
# from tarski.symbols import *

from tarski.evaluators.simple import evaluate

""" Fragment of ParcPrinter relevant for testing

(:types
    sheet_t resource_t location_t
)

(:constants
    Finisher2-RSRC - resource_t
    Some_Finisher_Tray Finisher2_Entry-Finisher1_Exit Finisher2_Tray - location_t
)

(:predicates


)

(:action Finisher2-Stack-Letter
 :parameters ( ?sheet - sheet_t ?prevsheet - sheet_t)
 :precondition (and
		(Available Finisher2-RSRC)
		(Prevsheet ?sheet ?prevsheet)
		(Location ?prevsheet Some_Finisher_Tray)
		(Sheetsize ?sheet Letter)
		(Location ?sheet Finisher2_Entry-Finisher1_Exit))
 :effect (and
		(not (Available Finisher2-RSRC))
		(Location ?sheet Some_Finisher_Tray)
		(Stackedin ?sheet Finisher2_Tray)
		(not (Location ?sheet Finisher2_Entry-Finisher1_Exit))
		(Available Finisher2-RSRC)
		(increase (total-cost) 8000))
)

)
"""


def create_small_task():
    upp = parcprinter.create_small_language()
    dummy_sheet = upp.constant('dummy-sheet', upp.sheet_t)
    sheet1 = upp.constant('sheet1', upp.sheet_t)

    M = tsk.model.create(upp)
    M.evaluator = evaluate
    M.add(upp.Uninitialized)
    M.add(upp.Location, dummy_sheet, upp.some_finisher_tray)
    M.add(upp.Prevsheet, sheet1, dummy_sheet)
    M.add(upp.Sheetsize, sheet1, upp.letter)
    M.add(upp.Location, sheet1, upp.some_feeder_tray)

    sheet = upp.variable('sheet', upp.sheet_t)
    prevsheet = upp.variable('prevsheet', upp.sheet_t)

    precondition = land(upp.Available(upp.finisher2_rsrc),
                        upp.Prevsheet(sheet, prevsheet),
                        upp.Location(prevsheet, upp.some_finisher_tray),
                        upp.Sheetsize(sheet, upp.letter),
                        upp.Location(sheet, upp.finisher2_entry_finisher1_exit))
    # MRJ: note that the positive effects should be under an extra X op, as per the
    # "deletes before adds" semantics,
    effects = [fs.DelEffect(upp.Available(upp.finisher2_rsrc)),
               fs.DelEffect(upp.Location(sheet, upp.finisher2_entry_finisher1_exit)),
               fs.AddEffect(upp.Location(sheet, upp.some_finisher_tray)),
               fs.AddEffect(upp.Stackedin(sheet, upp.finisher2_tray)),
               fs.AddEffect(upp.Available(upp.finisher2_rsrc))
               ]

    P = fs.Problem()
    P.name = "fun"
    P.language = upp
    P.init = M
    P.goal = top
    P.action('Finisher2-Stack-Letter', [sheet, prevsheet], precondition, effects)
    return P
