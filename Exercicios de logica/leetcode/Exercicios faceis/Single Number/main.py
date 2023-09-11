from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        conted_numbers = dict(Counter(nums))
        for key, value in conted_numbers.items():
            if value == 1:
                return key
