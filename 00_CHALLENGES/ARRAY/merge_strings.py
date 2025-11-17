"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order starting with word1.
If a string is longer than the other append additional letters
onto the end of merged string. Return the merged string.
"""


class MergeStrings:
    @staticmethod
    def result(word1: str, word2: str) -> str:
        final_word = []
        min_len = min(len(word1), len(word2))

        for i in range(0, min_len):
            final_word.append(word1[i])
            final_word.append(word2[i])

        letters_left = word1 if len(word1) > len(word2) else word2
        final_word.extend(letters_left[min_len:])
        return ''.join(final_word)


word1 = 'abcxyzdd'
word2 = 'defccc'

merge_strings = MergeStrings.result(word1, word2)
print(merge_strings)
