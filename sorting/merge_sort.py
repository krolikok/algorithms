"""
Merge sort implementation.
Reference: MIT 6.0001 lecture 12: Searching and Sorting
https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-12-searching-and-sorting/
"""

import logging
from copy import deepcopy
from typing import List

logger = logging.getLogger(__name__)


def _merge(first: List[int], second: List[int]):
    sorted_list = []
    while True:
        logger.debug(
            "first: %s, second: %s, sorted_list %s", first, second, sorted_list
        )
        if len(second) == 0:
            sorted_list.extend(first)
            return sorted_list
        elif len(first) == 0:
            sorted_list.extend(second)
            return sorted_list
        elif first[0] >= second[0]:
            sorted_list.append(second.pop(0))
        else:
            sorted_list.append(first.pop(0))


def merge_sort(L: List[int]):
    """Perform sorting by merging of given list

    Arguments:
        L -- given list to be sorted

    Returns:
        Sorted list
    """
    L = deepcopy(L)
    logger.debug(L)
    length = len(L)
    if length <= 1:
        return L
    middle = length // 2
    first_half = merge_sort(L[:middle])
    second_half = merge_sort(L[middle:])
    return _merge(first_half, second_half)