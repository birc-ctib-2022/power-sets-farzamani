"""Module for computing power sets."""

from typing import Any


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.
    """
    subsets = []
    powerset_size = 2**len(x)
    set_size = len(x)

    for counter in range(powerset_size):
        subset = []
        for k in range(set_size):
            # Going through binary counter            
            if counter & 1<<k:
                subset.append(x[k])
            subsets.append(subset)        

    return subsets
