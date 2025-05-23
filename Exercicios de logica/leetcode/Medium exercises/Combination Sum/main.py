class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(remaining, start, path):
            if remaining == 0:
                results.append(path[:])
                return
            elif remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(remaining - candidates[i], i, path)
                path.pop()

        backtrack(target, 0, [])
        return results
