from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total_distinct = len(set(nums))
        count = 0
        freq = Counter()
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) == total_distinct:
                count += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count
