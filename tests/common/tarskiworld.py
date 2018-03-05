"""
    Generate blocksworld language elements
"""
import tarski as tsk
import tarski.model

from tarski import fstrips as fs
from tarski.syntax import *
from tarski.syntax.temporal import ltl

def create_small_world():
    lang = tsk.language()

    lang.Cube = lang.predicate('Cube', lang.Object)
    lang.Tet = lang.predicate('Tet', lang.Object)
    lang.LeftOf = lang.predicate('LeftOf', lang.Object, lang.Object)
    lang.Dodec = lang.predicate('Dodec', lang.Object)
    lang.BackOf = lang.predicate('BackOf', lang.Object, lang.Object)

    return lang
