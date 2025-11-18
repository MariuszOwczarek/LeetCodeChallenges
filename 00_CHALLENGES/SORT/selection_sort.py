"""
SELECTION SORT

Sort a list of values in ascending order using the Selection Sort algorithm.

Selection Sort works by repeatedly selecting the smallest element from the
unsorted portion of the list and swapping it with the first unsorted element.
As the algorithm progresses, the sorted portion grows from the left while the
unsorted portion shrinks.

This algorithm performs well for small datasets and for educational purposes,
but it is generally inefficient for large input sizes due to its O(n²) time
complexity. It is, however, easy to understand and implement and does not
require additional memory.

Args:
    lst (list): The list of comparable values to be sorted.

Returns:
    list: The sorted list (same object as the input).

Example:
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
"""


class SelectionSort:
    @staticmethod
    def sort(lst):
        for i in range(len(lst)):
            min_index = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst


lst = [9, 3, 4, -1, 5, 8, 7, 6, 1, 2, 0]
selection_sort = SelectionSort.sort(lst)
print(selection_sort)
