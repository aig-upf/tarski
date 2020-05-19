"""
    Generate FSTRIPS+sets encodings of the Storytellers domain from

        Gregory, P., Long, D., Fox, M., & Beck, J. C. (2012).
        Planning modulo theories: Extending the planning paradigm.
        In Twenty-Second International Conference on Automated Planning and Scheduling.
"""
import math
import random

from ..fstrips import create_fstrips_problem, language
from ..syntax import sorts, top, forall, land, exists
from ..theories.sets import set_union, set_cardinality, set_in, set_emptyset, set_literal

BASE_DOMAIN_NAME = "storytellers"


# (define (domain storytellers)
# (:types storyteller audiences stories)
# (:modules integer set)
# (:functions
#   (known ?t - storyteller) - set of stories
#   (heard ?a - audience) - set of stories
#   (story-set) - set of stories)

def generate_language(nstorytellers, naudiences, nstories):
    lang = language(BASE_DOMAIN_NAME, theories=["sets", "equality"])

    lang.sort('storyteller')
    lang.sort('audience')
    lang.sort('story')

    _ = [lang.constant(f'teller{k}', 'storyteller') for k in range(1, nstorytellers + 1)]
    _ = [lang.constant(f'aud{k}', 'audience') for k in range(1, naudiences + 1)]
    _ = [lang.constant(f'st{k}', 'story') for k in range(1, nstories + 1)]

    set_of_stories = sorts.Set(lang, lang.Object)
    lang.function('known', 'storyteller', set_of_stories)
    lang.function('heard', 'audience', set_of_stories)
    # lang.function('story_set', set_of_stories)  # Not sure this one is needed

    return lang


# (:action entertain
# :parameters (?t - storyteller ?a - audience)
# :precondition (true)
# :effect ((heard ?a) := (union (heard ?a) (known ?t)))))

def generate_problem(nstorytellers, naudiences, nstories, goal_type="saturation"):
    assert nstorytellers > 0 and naudiences > 0 and nstories > 0
    lang = generate_language(nstorytellers, naudiences, nstories)

    problem = create_fstrips_problem(lang, domain_name=BASE_DOMAIN_NAME,
                                     problem_name=f'instance-{nstorytellers}-{naudiences}-{nstories}')

    set_of_stories = sorts.Set(lang, lang.Object)
    known, heard = lang.get('known', 'heard')
    audiences = sorted(lang.ns.audience.domain(), key=lambda x: x.symbol)
    stories = sorted(lang.ns.story.domain(), key=lambda x: x.symbol)
    tellers = sorted(lang.ns.storyteller.domain(), key=lambda x: x.symbol)

    st = lang.variable('s', 'story')
    teller = lang.variable('teller', 'storyteller')
    a = lang.variable('a', 'audience')

    problem.action(
        "entertain", [teller, a],
        precondition=top,
        effects=[heard(a) << set_union(heard(a), known(teller))]
    )

    # We consider two different goals with the same basic problems: saturation and equality. Both of these goals
    # require the audiences to hear at least half of the stories, but the saturation problems require all of the
    # stories to have been heard by at least one of the audiences, while the equality problems require that the
    # audiences all hear the same stories.
    # We use problems with two audiences and five storytellers and vary the number of stories
    at_least_half = forall(a, set_cardinality(heard(a)) >= math.floor(nstories / 2))
    if goal_type == "saturation":
        extra = forall(st, exists(a, set_in(st, heard(a))))
    else:
        a0 = audiences[0]
        extra = land(*(heard(a0) == heard(a) for a in audiences[1:]), flat=True)
    problem.goal = land(at_least_half, extra)

    # All audiences start having heard nothing
    for a in audiences:
        problem.init.setx(heard(a), set_emptyset(set_of_stories))

    for teller in tellers:
        chosen = random.sample(stories, math.floor(nstories / 4))
        problem.init.setx(known(teller), set_literal(set_of_stories, *chosen))

    return problem
