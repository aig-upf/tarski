
import tarski.model
from tarski import fstrips as fs
from tarski.syntax import land, neg


def create_simple_untyped_language():
    lang = fs.language("simple")
    lang.predicate("p", lang.Object)
    lang.predicate("q", lang.Object)
    lang.constant("a", lang.Object)
    return lang


def create_simple_problem():
    lang = create_simple_untyped_language()
    problem = fs.create_fstrips_problem(lang, problem_name="simple", domain_name="simple")
    p, q, a = lang.get("p", "q", "a")

    init = tarski.model.create(lang)
    problem.init = init
    init.add(p, a)  # p(a)
    init.add(q, a)  # q(a)

    problem.goal = neg(p(a))

    x = lang.variable("x", lang.Object)
    problem.action("negate", [x],
                   precondition=p(a),
                   effects=[fs.DelEffect(p(a))])
    return problem
