"""
COUNTING SORT

Sort a list of non-negative integers in ascending order using the
Counting Sort algorithm.

Counting Sort is a non-comparison-based sorting algorithm that works
by counting the number of occurrences of each unique value in the input
list and then calculating the positions of each value in the sorted output.

This algorithm is efficient when the range of input values is not much larger
than the number of elements in the list. It has O(n + k) time complexity,
where n is the number of elements and k is the maximum value in the input.
It uses extra space proportional to the maximum value.

Counting Sort is stable (preserves the relative order of equal elements).

Steps of the algorithm:
    1. Find the maximum value in the input list.
    2. Initialize a count array of size (max_value + 1) with all zeros.
    3. Iterate through the input list and increment the count of each element.
    4. Modify the count array to hold the cumulative count (optional if
       producing output directly).
    5. Build the sorted output list using the count array.
    6. Return the sorted list.

Args:
    lst (list[int]): A list of non-negative integers to sort.

Returns:
    list[int]: A new list containing the sorted integers.

Example:
    >>> lst = [4, 2, 2, 8, 3, 3, 1]
    >>> counting_sort(lst)
    [1, 2, 2, 3, 3, 4, 8]
"""

# This version of Counting Sort works for non-negative integers only #
# This way of sorting inefficient with big numbers #


class CountingSort:
    @staticmethod
    def sort(lst: list[int]) -> list[int]:
        max_val = max(lst)
        count_arr = [0] * (max_val + 1)

        for i in range(len(lst)):
            count_arr[lst[i]] += 1

        new_lst = []
        for i in range(len(count_arr)):
            new_lst.extend([i] * count_arr[i])
        return new_lst


lst = [9, 3, 4, 5, 5, 7, 6, 9, 2, 10, 0]
counting_sort = CountingSort.sort(lst)
print(counting_sort)
