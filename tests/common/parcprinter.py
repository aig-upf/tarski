"""
    Generate parcprinter language elements
"""
import tarski as tsk
import tarski.model
from tarski.theories import Theory
from tarski import fstrips as fs
from tarski.syntax import top, land
from tarski.evaluators.simple import evaluate


def create_small_language():
    upp = tsk.fstrips.language("upp", theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    upp.sheet_t = upp.sort('sheet_t')
    upp.resource_t = upp.sort('resource_t')
    upp.location_t = upp.sort('location_t')
    upp.size_t = upp.sort('size_t')

    upp.letter = upp.constant('Letter', upp.size_t)
    upp.finisher2_rsrc = upp.constant('Finisher2-RSRC', upp.resource_t)
    upp.some_finisher_tray = upp.constant('Some_Finisher_Tray', upp.location_t)
    upp.some_feeder_tray = upp.constant('Some_Feeder_Tray', upp.location_t)
    upp.finisher2_entry_finisher1_exit = upp.constant('Finisher2_Entry-Finisher1_Exit', upp.location_t)
    upp.finisher2_tray = upp.constant('Finisher2_Tray', upp.location_t)

    upp.Available = upp.predicate('Available', upp.resource_t)
    upp.Prevsheet = upp.predicate('Prevsheet', upp.sheet_t, upp.sheet_t)
    upp.Location = upp.predicate('Location', upp.sheet_t, upp.location_t)
    upp.Sheetsize = upp.predicate('Sheetsize', upp.sheet_t, upp.size_t)
    upp.Stackedin = upp.predicate('Stackedin', upp.sheet_t, upp.location_t)
    upp.Uninitialized = upp.predicate('Uninitialized')

    upp.total_cost = upp.function('total-cost', upp.Real)

    return upp


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
    upp = create_small_language()
    dummy_sheet = upp.constant('dummy-sheet', upp.sheet_t)
    sheet1 = upp.constant('sheet1', upp.sheet_t)

    M = tsk.model.create(upp)
    M.evaluator = evaluate
    M.add(upp.Uninitialized)
    M.add(upp.Location, dummy_sheet, upp.some_finisher_tray)
    M.add(upp.Prevsheet, sheet1, dummy_sheet)
    M.add(upp.Sheetsize, sheet1, upp.letter)
    M.add(upp.Location, sheet1, upp.some_feeder_tray)
    M.set(upp.total_cost(), 0)

    sheet = upp.variable('sheet', upp.sheet_t)
    prevsheet = upp.variable('prevsheet', upp.sheet_t)

    precondition = land(upp.Available(upp.finisher2_rsrc),
                        upp.Prevsheet(sheet, prevsheet),
                        upp.Location(prevsheet, upp.some_finisher_tray),
                        upp.Sheetsize(sheet, upp.letter),
                        upp.Location(sheet, upp.finisher2_entry_finisher1_exit))

    effects = [fs.DelEffect(upp.Available(upp.finisher2_rsrc)),
               fs.DelEffect(upp.Location(sheet, upp.finisher2_entry_finisher1_exit)),
               fs.AddEffect(upp.Location(sheet, upp.some_finisher_tray)),
               fs.AddEffect(upp.Stackedin(sheet, upp.finisher2_tray)),
               fs.AddEffect(upp.Available(upp.finisher2_rsrc)),
               fs.IncreaseEffect(upp.total_cost(), 8000)
               ]

    problem = fs.Problem()
    problem.name = "fun"
    problem.language = upp
    problem.init = M
    problem.goal = top
    problem.action('Finisher2-Stack-Letter', [sheet, prevsheet], precondition, effects)
    problem.metric = fs.OptimizationMetric(upp.total_cost(), fs.OptimizationType.MINIMIZE)
    return problem
