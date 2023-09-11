from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        copy_prices = prices[:]

        while True:
            try:
                maior = max(copy_prices)
                menor = min(copy_prices)
            except ValueError:
                break

            if prices.index(maior) > prices.index(menor):
                result = prices.index(maior)
                break

            copy_prices.pop(copy_prices.index(maior))

        return result
