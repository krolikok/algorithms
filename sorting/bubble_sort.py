"""
Bubble sort implementation.
Reference: MIT 6.0001 lecture 12: Searching and Sorting
https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-12-searching-and-sorting/
"""

import logging
from copy import deepcopy
from typing import List

logger = logging.getLogger(__name__)


def bubble_sort(L: List[int]):
    """Perform sorting by bubble sorting of given list

    Arguments:
        L -- given list to be sorted

    Returns:
        Sorted list
    """
    L = deepcopy(L)
    counter = 0
    aux = 1
    changed = True
    length = len(L)
    while changed:
        changed = False
        # the algorithm guarantee to move the largest element after each \
        # iteration to the end, so we dont need to iterate the whole list on each iteration
        # after each iteration (changed) number of  iterations given by (j) is smaller
        for j in range(length - aux):
            counter += 1
            if L[j] > L[j + 1]:
                changed = True

                L[j], L[j + 1] = L[j + 1], L[j]
        # logger.debug("%s: %s", aux, L)
        aux += 1
    logger.debug("Bubble it: %s", counter)
    return L
