"""
INSERTION SORT

    Sort a list of integers in ascending order using the
    Insertion Sort algorithm.

    Insertion Sort builds the final sorted list one element at a time.
    It iterates through the list, removing one element per iteration,
    and inserts it into the correct position among the previously
    sorted elements.

    This algorithm is efficient for small or nearly-sorted datasets
    and performs well in situations where simplicity is preferred
    over raw speed.

    The function sorts the list in place and returns the same list
    for convenience.

    Args:
        lst (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The sorted list (same object as the input).

    Example:
        >>> insertion_sort([5, 2, 4, 6, 1, 3])
        [1, 2, 3, 4, 5, 6]

"""


class InsretionSort:
    @staticmethod
    def sort(lst: list[int]) -> list[int]:
        for i in range(1, len(lst)):
            for j in range(i, 0, -1):
                if lst[j - 1] > lst[j]:
                    lst[j - 1], lst[j] = lst[j], lst[j-1]
                else:
                    break
        return lst


lst = [9, 3, 4, -1, 5, 8, 7, 6, 1, 2, 0]
insertion_sort = InsretionSort.sort(lst)
print(insertion_sort)
