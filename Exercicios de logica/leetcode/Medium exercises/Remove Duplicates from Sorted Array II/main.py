class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for n in nums:
            while nums.count(n) >= 3:
                nums.remove(n)
        return len(nums)