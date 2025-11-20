"""
BINARY SEARCH ITERATIVE
"""


class BinarySearchIterative:
    """
    Implements an iterative binary search algorithm on a sorted list.

    Binary search efficiently finds the position of a target value
    in a sorted list by repeatedly dividing the search interval in half.

    Attributes:
        lst (list[int]): The sorted list of integers to search through.
        target (int): The value to search for in the list.

    Methods:
        search() -> int:
            Performs iterative binary search and returns the index of
            the target if found; otherwise returns -1.

    Example:
        >>> lst = [1, 2, 3, 4, 5]
        >>> target = 3
        >>> searcher = BinarySearchIterative(lst, target)
        >>> searcher.search()
        2
    """

    def __init__(self, lst: list[int], target: int) -> None:
        """
        Initializes the BinarySearchIterative object with a sorted list
        and target value.

        Args:
            lst (list[int]): Sorted list of integers to search.
            target (int): Value to find in the list.
        """

        self.lst = lst
        self.target = target
        self.low: int = 0
        self.high: int = len(self.lst) - 1

    def search(self):
        """
        Performs an iterative binary search for the target value.

        Returns:
            int: The index of the target in the list if found; otherwise -1.

        Example:
            >>> lst = [10, 20, 30, 40, 50]
            >>> target = 30
            >>> searcher = BinarySearchIterative(lst, target)
            >>> searcher.search()
            2
        """

        while self.low <= self.high:
            mid = (self.low + self.high) // 2
            if self.lst[mid] == self.target:
                return mid

            if self.lst[mid] > self.target:
                self.high = mid - 1

            if self.lst[mid] < self.target:
                self.low = mid + 1
        return -1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 8
binary_search = BinarySearchIterative(lst, target)
target = binary_search.search()
print("Found at index:", target if target != -1 else "Not found")
