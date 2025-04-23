class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        def is_decreasing(array):
            last = array[0]
            for e in array[1:]:
                if not e >= last:
                    return False
                last = e
            return True

        from itertools import combinations

        sets2 = []
        for e in range(2, len(nums)+1):
            for comb in combinations(nums, e):
                lista_comb = list(comb)
                if is_decreasing(comb) and lista_comb not in sets2:
                    sets2.append(lista_comb)

        return sets2