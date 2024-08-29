from itertools import permutations


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        permu = set()
        for permutation in permutations(nums):
            permu.add(permutation)
        return [list(per) for per in permu]
