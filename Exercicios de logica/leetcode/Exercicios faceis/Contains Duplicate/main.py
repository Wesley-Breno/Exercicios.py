from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        max_repetion = max(list(dict(Counter(nums)).values()))
        if max_repetion > 1:
            return True
        return False
