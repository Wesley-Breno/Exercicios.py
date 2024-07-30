from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        sorte = dict(sorted(dict(Counter(s)).items(), key=lambda item: item[1], reverse=True))
        response = ''
        for key, value in sorte.items():
            response += key * value
        return response
