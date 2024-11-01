class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        soma = 0
        piles.sort(reverse=True)
        try:
            for n in range(1, len(piles), 2):
                soma += piles[n]
                piles.pop()
        except IndexError:
            return soma
        return soma

