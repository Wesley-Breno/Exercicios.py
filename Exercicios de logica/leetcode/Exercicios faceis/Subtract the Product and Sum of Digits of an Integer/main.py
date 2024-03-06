class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multiplications = 1
        soma = 0

        for digit in str(n):
            multiplications *= int(digit)
            soma += int(digit)

        return multiplications - soma
