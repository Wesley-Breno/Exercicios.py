class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        try:
            return [sorted(nums).index(target), len(nums) - sorted(nums, reverse=True).index(target) - 1]
        except ValueError:
            return [-1, -1]
