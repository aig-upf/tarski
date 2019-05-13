import shutil

from tarski.grounding.lp import ground_actions

from tests.common.gripper import create_sample_problem

if shutil.which("gringo") is None:
    import pytest
    pytest.skip('Install the Clingo ASP solver and put the "gringo" binary on your PATH in order to test ASP-based '
                "reachability analysis", allow_module_level=True)


def test_ground_actions_for_small_gripper():
    prob = create_sample_problem()
    groundings = ground_actions(prob)
    assert len(groundings['pick']) == len(groundings['drop']) == 16  # 4 balls, two rooms, two grippers
    assert len(groundings['move']) == 2  # 2 rooms
