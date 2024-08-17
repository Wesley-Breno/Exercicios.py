class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        try:
            return [i for i in range(1, n + 1) if n % i == 0][k-1]
        except IndexError:
            return -1