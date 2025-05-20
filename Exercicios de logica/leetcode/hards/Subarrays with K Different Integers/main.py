from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMostK(k):
            count = defaultdict(int)
            left = 0
            res = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1

                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1

                res += right - left + 1
            return res

        return atMostK(k) - atMostK(k - 1)
