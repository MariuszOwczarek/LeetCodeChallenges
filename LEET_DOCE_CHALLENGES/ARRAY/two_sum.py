"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class TwoSum:
    @staticmethod
    def result(nums: list[int], target: int) -> list[int] | None:
        results = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in results:
                return [results[complement], i]
            else:
                results[num] = i
        return None


nums = [3, 2, 4]
target = 6
two_sum = TwoSum.result(nums, target)
print(two_sum)
