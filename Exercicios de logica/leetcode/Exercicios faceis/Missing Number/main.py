class Solution:
    def missingNumber(self, nums) -> int:
        nums = sorted(nums)
        for i, n in enumerate(range(len(nums) + 1)):

            try:
                if i != nums[i]:
                    return i
            except IndexError:
                return i
