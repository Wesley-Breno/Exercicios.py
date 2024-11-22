class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        p = [n for n in range(1, m + 1)]
        result = []
        for e in queries:
            index = p.index(e)
            result.append(index)
            p.pop(index)
            p.insert(0, e)
        return result
