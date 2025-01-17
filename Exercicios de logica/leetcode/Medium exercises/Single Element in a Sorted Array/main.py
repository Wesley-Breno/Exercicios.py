from collections import Counter


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        return list(dict(sorted(Counter(nums).items(), key=lambda x: x[1])).keys())[0]
