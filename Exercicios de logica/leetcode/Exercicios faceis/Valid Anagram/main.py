from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = dict(Counter(s))
        counter_t = dict(Counter(t))

        for letter, count in counter_s.items():
            if letter not in counter_t or counter_t[letter] != count:
                return False

        return True
