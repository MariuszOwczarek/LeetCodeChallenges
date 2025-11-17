"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without duplicate characters.
"""


class LongestSubstr:
    @staticmethod
    def result(s: str) -> int:
        left = 0
        right = 0
        letters = set()
        max_length = 0

        while right < len(s):
            if s[right] not in letters:
                letters.add(s[right])
                right += 1
                max_length = max(max_length, right-left)
            else:
                letters.remove(s[left])
                left += 1
        return max_length


s = 'bbbbb'
longest_substring = LongestSubstr.result(s)
print(longest_substring)
