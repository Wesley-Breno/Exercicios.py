import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        factors = [2, 3, 5]
        for _ in range(n):
            ugly = heapq.heappop(heap)
            for factor in factors:
                next_ugly = ugly * factor
                if next_ugly not in seen:
                    seen.add(next_ugly)
                    heapq.heappush(heap, next_ugly)
        return ugly
