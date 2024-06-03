class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        positives, negatives = 0, 0
        for n in nums:
            if n > 0:
                positives += 1
                continue
            if n < 0:
                negatives += 1
        return max(positives, negatives)