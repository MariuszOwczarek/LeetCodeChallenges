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
        sorted: bool = True
        while sorted:
            sorted = False
            for i in range(1, len(lst)):
                if lst[i - 1] > lst[i]:
                    lst[i - 1], lst[i] = lst[i], lst[i-1]
                    sorted = True
        return lst


lst = [9, 3, 4, -1, 5, 8, 7, 6, 1, 2, 0]
bubble_sort = BubbleSort.sort(lst)
print(bubble_sort)
