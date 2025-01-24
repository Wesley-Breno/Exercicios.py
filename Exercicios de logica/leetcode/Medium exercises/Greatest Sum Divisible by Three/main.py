class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp = [0, 0, 0]
        for a in nums:
            for i in dp[:]:
                dp[(i + a) % 3] = max(dp[(i + a) % 3], i + a)
        return dp[0]