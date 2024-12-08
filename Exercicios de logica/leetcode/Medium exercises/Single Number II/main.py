from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        co = dict(Counter(nums))
        for key, value in co.items():
            if value == 1:
                return key