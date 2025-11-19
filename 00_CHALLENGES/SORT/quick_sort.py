"""
QUICK SORT

Sort a list of integers in ascending order using the Quick Sort algorithm.

Quick Sort is a recursive divide-and-conquer sorting algorithm:

1. Select a pivot element from the list.
2. Partition the remaining elements into two sublists:
   - Elements less than or equal to the pivot.
   - Elements greater than the pivot.
3. Recursively apply Quick Sort to both sublists.
4. Combine the sorted sublists with the pivot to produce the final sorted list.

Quick Sort has an average-case time complexity of O(n log n) and a worst-case
of O(n^2) (which occurs when the pivot selection is poor). It is generally
efficient for large datasets and can be implemented in-place or with extra
lists.

Args:
    lst (list[int]): The list of integers to be sorted.

Returns:
    list[int]: A new list containing the sorted integers.

Example:
    >>> lst = [9, 3, 4, -1, 5, 8, 7, 6, 1, 2, 0]
    >>> quick_sort(lst)
    [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


class QuickSort:
    @staticmethod
    def sort(lst: list[int]) -> list[int]:
        if len(lst) <= 1:
            return lst

        pivot: int = lst[-1]
        left: list[int] = [i for i in lst[:-1] if i <= pivot]
        right: list[int] = [i for i in lst[:-1] if i > pivot]

        left_sorted: list[int] = QuickSort.sort(left)
        right_sorted: list[int] = QuickSort.sort(right)

        sorted_list: list[int] = left_sorted + [pivot] + right_sorted
        return sorted_list


lst = [9, 3, 4, -1, 5, 8, 7, -11, 6, 1, 2, 10, 0, -13, -12, -11]
quick_sort = QuickSort.sort(lst)
print(quick_sort)
