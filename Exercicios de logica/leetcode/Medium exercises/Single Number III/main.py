from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        found = []
        for key, value in dict(sorted(Counter(nums).items(), key=lambda x: x[1])).items():
            if value == 1:
                found.append(key)
                if len(found) >= 2:
                    break
        return found