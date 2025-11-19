"""
RADIX SORT

Sort a list of non-negative integers in ascending order using the
Radix Sort algorithm.

Radix Sort is a non-comparison-based sorting algorithm that processes integers
digit by digit, from the least significant digit (LSD) to the most significant
digit (MSD). It uses a stable sorting algorithm (like Counting Sort) as a
subroutine to sort the numbers at each digit level.

Radix Sort has O(n * k) time complexity, where n is the number of elements and
k is the number of digits in the maximum number. It is most efficient when
the number of digits is small relative to the number of elements.

Steps of the algorithm:
    1. Find the maximum value in the input list to determine the
       number of digits.
    2. Initialize the digit position to the least significant
       digit (ones place).
    3. While the current digit position is less than or equal to
       the number of digits:
        a. Use a stable sorting algorithm (e.g., Counting Sort) to
           sort the list
           based on the current digit.
        b. Move to the next more significant digit (tens, hundreds, etc.).
    4. Repeat until the most significant digit has been processed.
    5. Return the sorted list.

Radix Sort is stable because it preserves the relative order of numbers with
the same digit value at each stage.

Args:
    lst (list[int]): A list of non-negative integers to sort.

Returns:
    list[int]: A new list containing the sorted integers.

Example:
    >>> lst = [170, 45, 75, 90, 802, 24, 2, 66]
    >>> radix_sort(lst)
    [2, 24, 45, 66, 75, 90, 170, 802]
"""


class RadixSort:
    @staticmethod
    def sort(lst: list[int]) -> list[int]:
        max_val: int = max(lst)
        digit_place: int = 1

        while max_val // digit_place > 0:
            count_arr: list[int] = [0] * 10
            for number in lst:
                current_digit: int = (number // digit_place) % 10
                count_arr[current_digit] += 1

            for i in range(1, len(count_arr)):
                count_arr[i] += count_arr[i - 1]

            output: list[int] = [0] * len(lst)
            for i in range(len(lst)-1, -1, -1):
                current_digit: int = (lst[i] // digit_place) % 10
                output[count_arr[current_digit] - 1] = lst[i]
                count_arr[current_digit] -= 1
            lst = output[:]
            digit_place *= 10
        return lst


lst = [9, 13, 104, 1245, 585, 9765234, 16, 95672, 258234, 1000, 0]
radix_sort = RadixSort.sort(lst)
print(radix_sort)
