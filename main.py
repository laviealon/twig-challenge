"""
============== Twig Coding Challenge ==============
This module implements the <group_array_elements> function
specified in the attached PDF spec (twig_coding_challenge.pdf).
See the README file for more information on specifics.

All files in this directory and all subdirectories are:
Copyright (c) 2022 Alon Lavie
===================================================
"""

from typing import List, Any
from queue import SimpleQueue


def group_array_elements(array: List[int], n: int) -> List[List[int]]:
    """ Return the contents of <array> divided into <n> equally sized
    arrays. Where the size of the original array cannot be divided equally
    by <n>, the final part should have a length equal to the remainder.

    Preconditions:
        - len(array) >= 0
        - n > 0

    >>> group_array_elements([1, 2, 3, 4, 5], 3)
    [[1, 2], [3, 4], [5]]
    >>> group_array_elements([1, 2, 3, 4, 5, 6, 7, 8], 5)
    [[1, 2], [3, 4], [5, 6], [7], [8]]
    >>> group_array_elements([1, 2, 3], 7)
    [[1], [2], [3], [], [], [], []]
    >>> group_array_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3)
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
    >>> group_array_elements([], 4)
    [[], [], [], []]
    """
    q = create_queue_copy(array)
    lsts = [[] for _ in range(n)]
    distribute_elements(q, lsts)
    return rearrange(array, lsts)


def create_queue_copy(array: List[Any]) -> SimpleQueue[Any]:
    """ Create and return a queue copy of <arrau>. To be used as
    a helper function for <group_array_elements>. To be used as a helper function
     for <group_array_elements>.
    """
    q = SimpleQueue()
    array_copy = array.copy()
    for i in range(len(array_copy)):
        q.put(array_copy[i])
    return q


def distribute_elements(q: SimpleQueue[Any], empty_lsts: List[List]) -> None:
    """ Iterate along lists inside <lsts> and pop one item from <q> into
    the current list. Loop back to the beginning of lsts when necessary. Continue
    until q is empty. To be used as a helper function for <group_array_elements>.

    Preconditions:
        - <lsts> contains only empty lists
        - <lsts> is nonempty
    """
    n, i = len(empty_lsts), 0
    while not q.empty():
        empty_lsts[i].append(q.get())
        i = (i + 1) % n


def rearrange(array: List[Any], lsts: List[List[Any]]) -> List[List[Any]]:
    """ Rearrange the lists in <lsts> according to how they should
    have been distributed based on <array>. To be used as
    a helper function for <group_array_elements>.
    """
    lst1 = []
    i = 0
    for lst in lsts:
        lst2 = []
        for j in range(len(lst)):
            lst2.append(array[i])
            i += 1
        lst1.append(lst2)
    return lst1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
