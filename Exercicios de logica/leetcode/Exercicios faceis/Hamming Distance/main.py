class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutives = 0
        new_consecutives = 0

        for i, n in enumerate(nums):
            if n == 1:
                new_consecutives += 1
            if n != 1 or i + 1 == len(nums):
                if new_consecutives >= consecutives:
                    consecutives = new_consecutives
                new_consecutives = 0

        return consecutives