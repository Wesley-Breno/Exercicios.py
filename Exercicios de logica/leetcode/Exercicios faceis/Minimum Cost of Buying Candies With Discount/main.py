class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost = sorted(cost, reverse=True)
        tot = 0
        while True:
            try:
                tot += cost[0] + cost[1]
                cost = cost[3:]
            except IndexError:
                return tot + sum(cost) if len(cost) > 0 else tot