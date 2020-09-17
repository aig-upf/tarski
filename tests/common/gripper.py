
import tarski.model
from tarski import fstrips as fs
from tarski.syntax import land


def create_sample_language():
    # The standard, untyped version of gripper
    lang = fs.language("gripper")
    object_t = lang.get_sort('object')

    [lang.predicate(p, object_t) for p in ["room", "ball", "gripper", "at-robby", "free"]]
    [lang.predicate(p, object_t, object_t) for p in ["at", "carry"]]

    [lang.constant(name, object_t) for name in ['rooma', 'roomb', 'ball4', 'ball3', 'ball2', 'ball1', 'left', 'right']]
    return lang


def create_sample_problem():
    lang = create_sample_language()
    init = tarski.model.create(lang)

    room, ball, at_robby, free, at, gripper, carry = lang.get(
        "room", "ball", "at-robby", "free", "at", "gripper", "carry")
    rooma, roomb, ball4, ball3, ball2, ball1, left, right = lang.get(
        'rooma', 'roomb', 'ball4', 'ball3', 'ball2', 'ball1', 'left', 'right')

    init.add(room, rooma)
    init.add(room, roomb)
    init.add(ball, ball1)
    init.add(ball, ball2)
    init.add(ball, ball3)
    init.add(ball, ball4)
    init.add(gripper, left)
    init.add(gripper, right)

    init.add(at_robby, rooma)
    init.add(free, left)
    init.add(free, right)
    init.add(at, ball1, rooma)
    init.add(at, ball2, rooma)
    init.add(at, ball3, rooma)
    init.add(at, ball4, rooma)

    problem = fs.create_fstrips_problem(lang, problem_name="sample", domain_name="gripper-strips")
    problem.init = init
    problem.goal = land(at(ball1, roomb), at(ball2, roomb), at(ball3, roomb), at(ball4, roomb))

    from_, to, o, r, g = [lang.variable(x, lang.Object) for x in ["from", "to", "o", "r", "g"]]

    problem.action("move", [from_, to],
                   precondition=land(from_ != to, room(from_), room(to), at_robby(from_), flat=True),
                   effects=[fs.AddEffect(at_robby(to)), fs.DelEffect(at_robby(from_))])

    problem.action("pick", [o, r, g],
                   precondition=land(ball(o), room(r), gripper(g), at(o, r), at_robby(r), free(g), flat=True),
                   effects=[fs.AddEffect(carry(o, g)), fs.DelEffect(at(o, r)), fs.DelEffect(free(g))])

    problem.action("drop", [o, r, g],
                   precondition=land(ball(o), room(r), gripper(g), carry(o, g), at_robby(r), flat=True),
                   effects=[fs.DelEffect(carry(o, g)), fs.AddEffect(at(o, r)), fs.AddEffect(free(g))])

    return problem
