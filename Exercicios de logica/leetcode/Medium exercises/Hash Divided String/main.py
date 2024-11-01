from string import ascii_lowercase


class Solution:
    def get_substring(self, s, k):
        cont = 0
        new_s = []
        damn = []

        while True:
            try:
                if cont != k:
                    damn.append(s[cont])
                    cont += 1
                else:
                    new_s.append(''.join(damn))
                    damn = []
                    s = s[cont:]
                    cont = 0
            except IndexError:
                break

        return new_s

    def stringHash(self, s: str, k: int) -> str:
        s = self.get_substring(s, k)
        result = ""

        for comb in s:
            comb_sum = 0
            for letter in comb:
                comb_sum += ascii_lowercase.index(letter)
            result += ascii_lowercase[comb_sum % 26]

        return result
