class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        count = 0
        odd_count = 0
        for num in nums:
            if num % 2:
                odd_count += 1
            count += prefix_count[odd_count - k]
            prefix_count[odd_count] += 1
        return count
