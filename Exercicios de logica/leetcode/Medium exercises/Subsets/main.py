from itertools import combinations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        combs = []
        for i in range(0, len(nums) + 1):
            for comb in combinations(nums, i):
                combs.append(list(comb))
        return combs
