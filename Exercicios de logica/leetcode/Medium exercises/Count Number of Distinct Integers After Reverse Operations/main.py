class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        return len(set(nums + [int(str(n)[::-1]) for n in nums]))
