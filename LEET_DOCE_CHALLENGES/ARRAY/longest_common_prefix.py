"""
Write a function to find the longest common prefix string
amongst an array of strings. If there is no common prefix
return an ampty string "" .
"""


class LongestCommonPrefix:
    @staticmethod
    def result(strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        min_length = min([len(i) for i in strs])
        prefix = ""

        for i in range(min_length):
            for word in strs:
                if word[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix


lst = ["batallion", "battle", "battery"]
longest_common_prefix = LongestCommonPrefix.result(lst)
print(longest_common_prefix)
