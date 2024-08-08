from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = [num for num in range(1, n + 1)]

        results = []
        for comb in combinations(nums, k):
            results.append(list(comb))

        return results
