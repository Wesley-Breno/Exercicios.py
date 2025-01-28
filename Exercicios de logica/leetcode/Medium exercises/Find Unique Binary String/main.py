from itertools import combinations_with_replacement


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        for per in combinations_with_replacement(["0", "1"], len(nums[0])):
            binary = ''.join(per)
            if binary not in nums:
                return binary
