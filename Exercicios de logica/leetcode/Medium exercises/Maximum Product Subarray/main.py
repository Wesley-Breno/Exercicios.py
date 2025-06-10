class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod = nums[0]
        max_ending_here = nums[0]
        min_ending_here = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here

            max_ending_here = max(num, max_ending_here * num)
            min_ending_here = min(num, min_ending_here * num)

            max_prod = max(max_prod, max_ending_here)

        return max_prod
