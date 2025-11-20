"""
BINARY SEARCH RECURSIVE

Recursive Binary Search Implementation

This module implements a recursive binary search algorithm for a sorted list.
It efficiently finds the index of a target value by dividing the search
interval in half at each step.
"""


class BinarySearchRecursive:
    """
    Implements a recursive binary search algorithm on a sorted list.

    Attributes:
        lst (list[int]): The sorted list of integers to search through.
        target (int): The value to search for in the list.

    Methods:
        search(low: int, high: int) -> int:
            Recursively searches for the target in the list.
            Returns the index of the target if found; otherwise returns -1.

    Example:
        >>> lst = [1, 2, 3, 4, 5]
        >>> target = 3
        >>> searcher = BinarySearchRecursive(lst, target)
        >>> searcher.search(0, len(lst) - 1)
        2
    """

    def __init__(self, lst: list[int], target: int) -> None:
        """
        Initializes the BinarySearchRecursive object with a sorted list
        and target value.

        Args:
            lst (list[int]): Sorted list of integers to search.
            target (int): Value to find in the list.
        """
        self.lst = lst
        self.target = target

    def search(self, low: int, high: int) -> int:
        """
        Performs a recursive binary search for the target value within the
        interval [low, high].

        Args:
            low (int): Lower index of the current search interval.
            high (int): Upper index of the current search interval.

        Returns:
            int: The index of the target in the list if found; otherwise -1.

        Example:
            >>> lst = [10, 20, 30, 40, 50]
            >>> target = 30
            >>> searcher = BinarySearchRecursive(lst, target)
            >>> searcher.search(0, len(lst) - 1)
            2
        """

        if low > high:
            return -1

        mid = (low + high) // 2

        if self.lst[mid] == self.target:
            return mid

        if self.lst[mid] > self.target:
            high = mid - 1

        if self.lst[mid] < self.target:
            low = mid + 1

        return self.search(low, high)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 6
binary_search_recursive = BinarySearchRecursive(lst, target)
index = binary_search_recursive.search(0, len(lst) - 1)
print("Found at index:", index if index != -1 else "Not found")
