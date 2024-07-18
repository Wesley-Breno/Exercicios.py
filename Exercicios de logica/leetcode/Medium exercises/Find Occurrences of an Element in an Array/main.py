class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        indexes = []
        for i, n in enumerate(nums):
            if n == x:
                indexes.append(i)

        response = []
        for query in queries:
            if query <= len(indexes):
                response.append(indexes[query - 1])
                continue
            response.append(-1)

        return response