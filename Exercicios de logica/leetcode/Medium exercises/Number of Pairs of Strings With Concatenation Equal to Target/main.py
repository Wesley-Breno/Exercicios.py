class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        sum = 0
        for i, n in enumerate(nums):
            for ii, nn in enumerate(nums):
                if n + nn == target and i != ii:
                    sum += 1
        return sum
