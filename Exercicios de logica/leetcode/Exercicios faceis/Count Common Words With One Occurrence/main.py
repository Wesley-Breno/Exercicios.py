from collections import Counter


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        words1, words2 = dict(Counter(words1)), dict(Counter(words2))

        cont = 0
        for key, value in words1.items():
            if key in words2.keys() and words2[key] == 1 and value == 1:
                cont += 1
        return cont
