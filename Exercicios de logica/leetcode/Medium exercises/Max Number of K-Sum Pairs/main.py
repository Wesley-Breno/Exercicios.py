from collections import Counter


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        num_count = Counter(nums)
        operations = 0
        for num in num_count:
            complement = k - num
            if complement in num_count:
                if complement == num:
                    operations += num_count[num] // 2
                else:
                    operations += min(num_count[num], num_count[complement])
                num_count[num] = 0
                num_count[complement] = 0
        return operations
