class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(key=None, reverse=True)
        soma = 0
        for i in range(k):
            if happiness[i] - i <= 0:
                return soma
            soma += happiness[i] - i
        return soma