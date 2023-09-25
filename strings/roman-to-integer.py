class Solution:
    def romanToInt(self, s: str) -> int:
        roman_list = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum = 0

        for i in range(len(s)-1):
            if roman_list[s[i]] >= roman_list[s[i + 1]]:
                sum += roman_list[s[i]]
            else:
                sum -= roman_list[s[i]]

        return sum + roman_list[s[-1]]

    romanToInt(0, s="MCMXCIV")


class Solution_2:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000}

        s = s.replace('IV', 'IIII') \
            .replace('IX', 'VIIII') \
            .replace('XL', 'XXXX') \
            .replace('XC', 'LXXXX') \
            .replace('CD', 'CCCC') \
            .replace('CM', 'DCCCC')

        return sum(map(roman_to_integer.get, s))
