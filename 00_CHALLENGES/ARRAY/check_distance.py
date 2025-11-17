"""
1437.
Given an binary array nums and an integer k, return true if all 1's
are at least k places away from each other, otherwise return false.
"""


class CheckDistance:
    @staticmethod
    def result(nums: list[int], k: int):
        zeros = k
        for i in nums:
            if i == 1:
                if zeros < k:
                    return False
                zeros = 0
            else:
                zeros += 1
        return True


nums = [1, 0, 0, 1, 0, 0, 1]
k = 2
check_distance = CheckDistance.result(nums, k)
print(check_distance)
