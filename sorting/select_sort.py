"""
Select sort implementation.
Reference: MIT 6.0001 lecture 12: Searching and Sorting
https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-12-searching-and-sorting/
"""

import logging
from copy import deepcopy
from typing import List

logger = logging.getLogger(__name__)


def select_sort(L: List[int]):
    """Perform sorting by selection of given list

    Arguments:
        L -- given list to be sorted

    Returns:
        Sorted list
    """
    L = deepcopy(L)
    counter = 0
    length = len(L)
    for j in range(length):
        for i in range(j, length):
            counter += 1
            if L[j] > L[i]:
                L[j], L[i] = L[i], L[j]
    logger.debug("Select it: %s", counter)
    return L
