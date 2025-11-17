"""
You are given a sorted unique intereg array "nums". A range [a,b] is the set
of all integers from a to b (inclusive). Return the smallest sorted list of
ranges that cover all the numbers in the array exactly. That is each element
of "nums" is covered by exactly one of the ranges but there is no integer
"x" such that "x" is in one of the ranges but not in "nums".
"""


class SummaryRanges:
    @staticmethod
    def result(nums: list[int]) -> list[str]:
        if not nums:
            return []

        start_value = nums[0]
        end_value = nums[0]
        result = []

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                end_value = nums[i+1]
            else:
                if start_value == end_value:
                    result.append(f'{start_value}')
                else:
                    result.append(f'{start_value}->{end_value}')

                start_value = nums[i+1]
                end_value = nums[i+1]

        if start_value == end_value:
            result.append(f'{start_value}')
        else:
            result.append(f'{start_value}->{end_value}')
        return result


lst = [0, 1, 3, 5, 7, 8, 10, 11]
summary_ranges = SummaryRanges.result(lst)
print(summary_ranges)
