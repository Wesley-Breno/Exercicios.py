from collections import Counter


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []
        for key, value in Counter(nums).items():
            if value >= 2:
                duplicates.append(key)

        return duplicates
