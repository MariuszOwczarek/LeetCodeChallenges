"""
BUBBLE SORT

    Sort a list of integers in ascending order using the Bubble Sort algorithm.

    Bubble Sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. This process continues
    until a full pass is completed without performing any swaps, indicating
    that the list is sorted.

    This implementation sorts the list in place and returns the same list
    for convenience.

    Args:
        lst (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The sorted list (same object as the input).

    Example:
        >>> BubbleSort.sort([3, 1, 2])
        [1, 2, 3]

"""


class BubbleSort:
    @staticmethod
    def sort(lst: list[int]) -> list[int]:
        swapped: bool = True
        while swapped:
            swapped = False
            for i in range(1, len(lst)):
                if lst[i - 1] > lst[i]:
                    lst[i - 1], lst[i] = lst[i], lst[i-1]
                    swapped = True
        return lst


# Examples / tests
examples = [
    [],
    [4],
    [4, 2, 2, 8, 3, 3, 1],
    [0, 1, 2, 3],
    [9, 3, 4, 5, 5, 7, 6, 9, 2, 10, 0],
]
for lst in examples:
    print(f"{lst} -> {BubbleSort.sort(lst)}")
