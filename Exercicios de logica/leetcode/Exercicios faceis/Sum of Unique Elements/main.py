from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum([key for key, value in Counter(nums).items() if value == 1])
