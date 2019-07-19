
from tarski.fstrips import fstrips
from tarski.theories import Theory


def generate_spider_language():
    """ The FOL of the IPC18 Spider benchmark  """
    lang = fstrips.language("Spider", theories=[Theory.EQUALITY, Theory.ARITHMETIC])

    lang.sort("cardposition", "object")
    lang.sort("card_or_tableau", "cardposition")
    lang.sort("card", "card_or_tableau")
    lang.sort("tableau", "card_or_tableau")
    lang.sort("deal", "cardposition")

    lang.constant("discard", "cardposition")  # Domain constant

    lang.predicate("on", "card", "cardposition")
    lang.predicate("clear", "cardposition")
    lang.predicate("in-play", "card")
    lang.predicate("current-deal", "deal")

    # Note that the following predicates are defined in uppercase in the IPC PDDL, but we lowercase
    # for consistency with what the parser does
    lang.predicate("can-continue-group", "card", "cardposition")
    lang.predicate("can-be-placed-on", "card", "card")
    lang.predicate("is-ace", "card")
    lang.predicate("is-king", "card")
    lang.predicate("next-deal", "deal", "deal")
    lang.predicate("to-deal", "card", "tableau", "deal", "cardposition")

    lang.predicate("currently-dealing")
    lang.predicate("currently-collecting-deck")
    lang.predicate("collect-card", "cardposition")
    lang.predicate("part-of-tableau", "cardposition", "tableau")
    lang.predicate("movable", "card")
    lang.predicate("currently-updating-unmovable")
    lang.predicate("make-unmovable", "card")
    lang.predicate("currently-updating-movable")
    lang.predicate("make-movable", "cardposition")
    lang.predicate("currently-updating-part-of-tableau")
    lang.predicate("make-part-of-tableau", "card", "tableau")

    lang.function("total-cost", lang.Real)

    lang.constant("card-d0-s0-v0", "card")  # The constants from the smallest instance p01.pddl
    lang.constant("card-d0-s0-v1", "card")
    lang.constant("card-d0-s0-v2", "card")
    lang.constant("card-d0-s1-v0", "card")
    lang.constant("card-d0-s1-v1", "card")
    lang.constant("card-d0-s1-v2", "card")
    lang.constant("card-d0-s2-v0", "card")
    lang.constant("card-d0-s2-v1", "card")
    lang.constant("card-d0-s2-v2", "card")
    lang.constant("card-d0-s3-v0", "card")
    lang.constant("card-d0-s3-v1", "card")
    lang.constant("card-d0-s3-v2", "card")
    lang.constant("pile-0", "tableau")
    lang.constant("pile-1", "tableau")
    lang.constant("pile-2", "tableau")
    lang.constant("deal-0", "deal")
    lang.constant("deal-1", "deal")
    lang.constant("deal-2", "deal")

    return lang
