class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, n in enumerate(sorted(nums)) if n == target]
