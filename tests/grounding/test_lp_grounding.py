import shutil

from tarski.grounding import LPGroundingStrategy, NaiveGroundingStrategy

from tests.common.gripper import create_sample_problem

if shutil.which("gringo") is None:
    import pytest
    pytest.skip('Install the Clingo ASP solver and put the "gringo" binary on your PATH in order to test ASP-based '
                "reachability analysis", allow_module_level=True)


def test_ground_actions_for_small_gripper():
    problem = create_sample_problem()
    grounding = LPGroundingStrategy(problem)
    actions = grounding.ground_actions()
    assert len(actions['pick']) == len(actions['drop']) == 16  # 4 balls, two rooms, two grippers
    assert len(actions['move']) == 2  # 2 rooms

    as_list2 = lambda symbols: sorted(map(str, symbols))
    lpvariables = grounding.ground_state_variables()
    assert len(lpvariables) == 20

    grounding = NaiveGroundingStrategy(problem)
    naive_variables = grounding.ground_state_variables()
    # The naive grounding strategy will result in many unreachable state variables such as 'carry(left,left)'
    assert len(set(as_list2(naive_variables)) - set(as_list2(lpvariables))) == 124

