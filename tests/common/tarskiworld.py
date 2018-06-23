"""
    Generate Tarski-world language elements =)
"""
import tarski as tsk
from tarski.theories import Theory


def create_small_world():
    lang = tsk.language("TarskiWorld", theories=[Theory.EQUALITY])

    lang.Cube = lang.predicate('Cube', lang.Object)
    lang.Tet = lang.predicate('Tet', lang.Object)
    lang.LeftOf = lang.predicate('LeftOf', lang.Object, lang.Object)
    lang.Dodec = lang.predicate('Dodec', lang.Object)
    lang.BackOf = lang.predicate('BackOf', lang.Object, lang.Object)

    return lang
