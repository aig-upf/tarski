"""
    Generate parcprinter language elements
"""
import tarski as tsk
import tarski.model

from tarski import fstrips as fs
from tarski.syntax import *
from tarski.syntax.temporal import ltl
from tarski.theories import Theory


def create_small_language():
    upp = tsk.fstrips.language("upp", theories=[Theory.EQUALITY])

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

    return upp
