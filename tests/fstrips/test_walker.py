from tarski.benchmarks.blocksworld import generate_fstrips_blocksworld_problem


# def test_fstrips_problem_walker():
#     problem = generate_fstrips_blocksworld_problem(
#         nblocks=2,
#         init=[('b1', 'b2'), ('b2', 'table')],
#         goal=[('b2', 'table'), ('b1', 'table')]
#     )
#     lang = problem.language
#     b1, b2, clear, loc, table = lang.get('b1', 'b2', 'clear', 'loc', 'table')
#
#     walker = NestedExpressionWalker(problem)
#
#     node = walker.visit_expression((loc(b1) == table))
#     assert str(node) == '=(loc(b1),table)' and not walker.nested_symbols  # Nothing is changed
#
#     node = walker.visit_expression(land(clear(b1) & clear(loc(b1)) & clear(loc(b2)), flat=True))
#     assert str(node) == '((clear(b1) and =(_clear_fun(loc(b1)),True)) and =(_clear_fun(loc(b2)),True))'
