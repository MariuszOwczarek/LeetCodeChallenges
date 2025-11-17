"""
Given two strings "S" and "T" return TRUE if "S" is subsequence of "T"
 or FALSE otherwise. A subsequence of a string is a new string that is formed
 from the original string by deleting some (can be none) pf the characters
without disturbing the relative positions of the remaining characters.
"""


class IsSubsequence:
    @staticmethod
    def result(s: str, t: str) -> bool:

        pointer_s = 0
        pointer_t = 0

        for pointer_t in range(len(t)):
            if pointer_s < len(s) and s[pointer_s] == t[pointer_t]:
                pointer_s += 1

        if pointer_s == len(s):
            return True
        return False


s = 'xy'
t = 'axbyc'
isSubsequence = IsSubsequence.result(s, t)
print(isSubsequence)
