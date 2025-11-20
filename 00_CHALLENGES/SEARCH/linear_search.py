"""
LINEAR SEARCH
"""


class LinearSearch:
    """
    Implements a simple linear (sequential) search algorithm.

    Attributes:
        lst (list[int]): The list of integers to search through.
        target (int): The value to search for.

    Methods:
        search() -> int:
            Searches for the target in the list.
            Returns the index of the target if found, otherwise -1.

    Example:
        >>> lst = [1, 2, 3, 4, 5]
        >>> target = 3
        >>> linear_search = LinearSearch(lst, target)
        >>> linear_search.search()
        2
    """

    def __init__(self, lst: list[int], target: int) -> None:
        """
        Initializes the LinearSearch object with a list and a target value.

        Args:
            lst (list[int]): List of integers to search.
            target (int): Value to search for in the list.
        """

        self.lst = lst
        self.target = target

    def search(self):
        """
        Performs a linear search for the target value in the list.

        Returns:
            int: The index of the target if found; otherwise -1.

        Example:
            >>> lst = [10, 20, 30, 40]
            >>> target = 30
            >>> linear_search = LinearSearch(lst, target)
            >>> linear_search.search()
            2
        """

        for i in range(len(self.lst)):
            if self.lst[i] == self.target:
                return i
        return -1


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 11
linear_search = LinearSearch(lst, target)
index = linear_search.search()
print("Found at index:", index if index != -1 else "Not found")
