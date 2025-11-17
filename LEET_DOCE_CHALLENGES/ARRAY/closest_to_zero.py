"""
Given an integer array nums of size n, return number with the value
closest to 0 in nums. If there are multiple answers return the number
with the largest value.
"""


class ClosestToZero:

    @staticmethod
    def Result(arr: list[int]) -> int:
        if not arr:
            return -1

        closest = arr[0]

        for elem in arr:
            if (abs(elem) < abs(closest) or
                    (abs(elem) == abs(closest) and elem > closest)):
                closest = elem
        return closest


arr = [-2, 3, 5, 6, 7, 1]
closest_number = ClosestToZero.Result(arr)
print(closest_number)
