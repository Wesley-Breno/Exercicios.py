from collections import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        count = dict(Counter(nums)).values()
        count_pairs = sum([1 for value in count if value % 2 == 0])
        if count_pairs == len(count):
            return True
        return False
    