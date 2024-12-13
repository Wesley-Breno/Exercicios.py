class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums = sorted([int(n) for n in nums], reverse=True)
        return str(nums[k-1])
