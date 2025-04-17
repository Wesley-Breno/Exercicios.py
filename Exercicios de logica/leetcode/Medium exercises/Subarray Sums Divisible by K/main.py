class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        prefix = 0
        count = 0
        mod_count = defaultdict(int)
        mod_count[0] = 1
        for num in nums:
            prefix += num
            mod = prefix % k
            mod = (mod + k) % k
            count += mod_count[mod]
            mod_count[mod] += 1
        return count