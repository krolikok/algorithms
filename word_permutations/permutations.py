import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def get_permutations(sequence: str) -> List[str]:
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    seq_length = len(sequence)

    assert seq_length > 0

    if seq_length == 1:
        logger.debug("Basecase sequence %s", sequence)
        return [sequence]
    first = sequence[0]
    rest = sequence[1:]

    permutations = get_permutations(rest)
    res = []
    for perm in permutations:
        for i in range(len(perm) + 1):
            new = perm[:i] + first + perm[i:]
            res.append(new)
    logger.debug(
        "Recursive case res: %s, first: %s, rest: %s, permutations: %s",
        res,
        first,
        rest,
        permutations,
    )
    return res


if __name__ == "__main__":
    example_input = "abc"
    print("Input:", example_input)
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    permutations = get_permutations(example_input)
    print("Actual Output:", permutations)
    print(f"Input size: n={len(example_input)}, output size: {len(permutations)}")
    pass
