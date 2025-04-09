class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        if max(nums) <= 0:
            return 1

        nums = set(n for n in nums if n >= 1)

        for n in range(1, max(nums) + 2):
            try:
                nums.remove(n)
                continue
            except KeyError:
                return n
