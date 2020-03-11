
# import copy

#  TODO - Work in Progress
# def compile_types_into_unary_predicates(problem):
#     """ Take an FSTRIPS problem and return an equivalent problem where language types have been compiled into (static)
#     unary predicates. In spanner, e.g., "man", "spanner", "location", etc. will be new unary predicates, whereas
#     man(bob), spanner(spanner1), spanner(spanner2), etc. will be new atoms in the initial state of the problem """
#     result = copy.deepcopy(problem)
#     lang = result.language
#     for s in lang.sorts:
#         if s.builtin:
#             continue
#         lang.remove_sort(s)
#         lang.predicate(s.name, lang.Object)  # each type is maped into a unary untyped predicate with same name
#     for c in lang.constants():
#         # each constant of a certain type other than the root Object type gets mapped into an additional static atom
#         # in the initial state of the problem
#         x = 2


