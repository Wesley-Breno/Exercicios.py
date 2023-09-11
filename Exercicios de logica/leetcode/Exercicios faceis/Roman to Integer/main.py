import re


class Solution:
    LIST_ROMAN_NUMBERS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    SUBTRACTION_INSTANCES = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    VALUES_ROMAN_NUMBERS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def isromanstring(self, string: str):
        verified_numbers = list()
        for number in string:
            if number in self.LIST_ROMAN_NUMBERS:
                verified_numbers.append(number)

        return len(verified_numbers) == len(string)

    def romanToInt(self, s: str) -> int:
        if 1 <= len(s) <= 15 and self.isromanstring(s):
            roman_number_converted = 0

            subtractions = re.findall(r'IV|IX|XL|XC|CD|CM', s)
            for sub in subtractions:
                for key, value in self.SUBTRACTION_INSTANCES.items():
                    if key == sub:
                        roman_number_converted += value
                        s = s.replace(sub, '')

            for roman_number in s:
                for key, value in self.VALUES_ROMAN_NUMBERS.items():
                    if key == roman_number:
                        roman_number_converted += value
                        s = s.replace(roman_number, '')

            if 1 <= roman_number_converted <= 3999:
                return roman_number_converted
