from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ordered = sorted(dict(Counter(nums)).items(), key=lambda item: item[1], reverse=True)
        return list(dict(ordered).keys())[:k]