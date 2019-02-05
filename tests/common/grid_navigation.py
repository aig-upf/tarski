"""
    Generate language to describe navigation on a grid
"""
import tarski as tsk
from tarski.theories import Theory


def generate_single_agent_language():
    lang = tsk.fstrips.language(theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    # Functions
    _ = lang.function('x', lang.Real)
    _ = lang.function('y', lang.Real)

    return lang
