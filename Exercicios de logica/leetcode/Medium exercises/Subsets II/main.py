from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        combs = []
        nums.sort()
        for i in range(0, len(nums) + 1):
            for comb in combinations(nums, i):
                if str(list(comb)) not in str(combs) or str(list(comb)) == "[]":
                    combs.append(list(comb))
        return combs
