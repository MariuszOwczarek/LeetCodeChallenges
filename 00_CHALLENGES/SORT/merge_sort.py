"""
MERGE SORT

Sort a list using the Merge Sort algorithm.

Merge Sort is a recursive divide-and-conquer algorithm that works by splitting
the input list into two halves, recursively sorting each half, and then merging
the two sorted halves into a single sorted list.

This algorithm guarantees O(n log n) time complexity for all cases and is
well-suited for large datasets. It is stable and produces a new sorted list
rather than modifying the input in place (depending on implementation).

Steps of the algorithm:
    1. If the list has zero or one element, it is already sorted.
    2. Split the list into two halves.
    3. Recursively apply merge sort to each half.
    4. Merge the two sorted halves by repeatedly selecting the smaller element
       from the front of each sublist.
    5. Return the merged, sorted list.

Args:
    lst (list): The list of comparable values to be sorted.

Returns:
    list: A new list containing the sorted elements.

Example:
    >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
"""


class MergeSort:
    @staticmethod
    def sort(lst: list[int]) -> list[int]:

        if len(lst) <= 1:
            return lst

        mid: int = len(lst) // 2
        left = lst[0:mid]
        right = lst[mid:]

        sorted_left: list[int] = MergeSort.sort(left)
        sorted_right: list[int] = MergeSort.sort(right)

        merged: list[int] = []
        i: int = 0
        j: int = 0
        while i < len(sorted_left) and j < len(sorted_right):
            if sorted_left[i] <= sorted_right[j]:
                merged.append(sorted_left[i])
                i += 1
            else:
                merged.append(sorted_right[j])
                j += 1
        merged.extend(sorted_left[i:])
        merged.extend(sorted_right[j:])
        return merged


lst = [9, 3, 4, -1, 5, 8, 7, 6, 1, 2, 10, 0, -11]
merge_sort = MergeSort.sort(lst)
print(merge_sort)
