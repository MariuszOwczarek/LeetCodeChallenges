"""
There are seven Roman numeral symbols, each associated with a specific integer:
I is 1, V is 5, X is 10, L is 50, C is 100, D is 500, and M is 1000.
In most cases, you add the values of these symbols from left to right.
For example, the numeral "VIII" is read as 5 + 1 + 1 + 1 = 8.

However, Roman numerals also allow for a subtractive notation.
This occurs when a smaller numeral appears before a larger one,
indicating that the smaller value should be subtracted from the larger.
For instance, "IV" is 4, because 1 comes before 5, and "IX" is 9,
because 1 comes before 10. This rule applies specifically to six cases:
"IV" (4), "IX" (9), "XL" (40), "XC" (90), "CD" (400), and "CM" (900).
"""


class RomanToInteger:
    @staticmethod
    def result(Value: str) -> int:
        n = len(Value)
        total = 0
        roman_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        for i in range(n):
            if i < n-1 and roman_numbers[Value[i]] < roman_numbers[Value[i+1]]:
                total -= roman_numbers[Value[i]]
            else:
                total += roman_numbers[Value[i]]
        return total


value = 'MCMXXVI'
roman_to_integer = RomanToInteger.result(value)
print(roman_to_integer)
