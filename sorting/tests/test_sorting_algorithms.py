import pytest
from ..bubble_sort import bubble_sort
from ..merge_sort import merge_sort
from ..select_sort import select_sort

# from sorting.select_sort import select_sort

TEST_CASES = [
    [3, 1],
    [1, 7, 9, 0],
    [3, 2, 1, 4, 23, 5, 6, 89, 1, 3, 57, 9, 0, 7],
    [],
    [10],
    [1, -3],
]

pytestmark = pytest.mark.parametrize("tested", TEST_CASES, ids=lambda x: str(x))


def test_bubble_sort(tested):
    assert bubble_sort(tested) == sorted(tested)


def test_select_sort(tested):
    assert select_sort(tested) == sorted(tested)


def test_merge_sort(tested):
    assert merge_sort(tested) == sorted(tested)
