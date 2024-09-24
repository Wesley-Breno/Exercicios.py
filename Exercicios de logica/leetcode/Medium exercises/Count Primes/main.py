class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primo = [True] * n
        primo[0] = primo[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primo[i]:
                for j in range(i * i, n, i):
                    primo[j] = False

        return sum(primo)