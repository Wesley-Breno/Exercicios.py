class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        try:
            return max([n for n in nums if n > 0 and -n in nums])
        except ValueError:
            return -1
