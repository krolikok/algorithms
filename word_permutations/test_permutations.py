from .permutations import get_permutations


def test_permutations():
    test_case = "abc"
    permutations = get_permutations(test_case)
    expected_result = ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert set(permutations) == set(expected_result)
