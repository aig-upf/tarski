import tempfile

from tarski.analysis.csp_schema import process_problem, CSPInformation, compile_expression
from tarski.benchmarks.blocksworld import generate_strips_blocksworld_problem
from tarski.grounding import NaiveGroundingStrategy


def test_bw_csp():
    problem = generate_strips_blocksworld_problem()
    lang = problem.language
    clear, on, ontable, handempty, holding = lang.get('clear', 'on', 'ontable', 'handempty', 'holding')
    b1, b2 = lang.get('b1', 'b2')
    x = lang.variable('x', 'object')
    y = lang.variable('y', 'object')

    grounding = NaiveGroundingStrategy(problem, ignore_symbols={'total-cost'})
    state_variables = grounding.ground_state_variables()

    csp = CSPInformation()
    compile_expression(on(b1, b2) & clear(x), csp, state_variables)
    assert len(csp.constraints) == 2 and \
        str(csp.constraints[0]) == 'StateVar(on(b1,b2)=True, reif=None)' and \
        str(csp.constraints[1]) == 'Table(<z[x]>, ext(clear), reif=None)'

    csp = CSPInformation()
    compile_expression(handempty() & ~handempty(), csp, state_variables)
    assert len(csp.constraints) == 2 and \
        str(csp.constraints[0]) == 'StateVar(handempty()=True, reif=None)' and \
        str(csp.constraints[1]) == 'StateVar(handempty()=False, reif=None)'

    with tempfile.TemporaryDirectory() as dirpath:
        _ = process_problem(problem, state_variables=state_variables, serialization_directory=dirpath)
