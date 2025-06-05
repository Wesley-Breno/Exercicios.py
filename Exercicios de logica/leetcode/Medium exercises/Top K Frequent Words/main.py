from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        ordered = sorted(dict(Counter(words)).items(), key=lambda item: item[1], reverse=True)
        response = dict(ordered)

        max_num = max(response.values())
        combs = []
        comb = []

        while max_num != 0:
            for word in response.keys():
                if response[word] == max_num:
                    comb.append(word)
            for e in sorted(comb):
                combs.append(e)
            comb = []
            max_num -= 1

        return combs[:k]
