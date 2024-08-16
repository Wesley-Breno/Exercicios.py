from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        result = [0] * n
        prefix_sum = 0
        for i in range(n):
            num = nums[i]
            result[i] = (num * i - prefix_sum) + ((total_sum - prefix_sum - num) - num * (n - i - 1))
            prefix_sum += num
        return result
