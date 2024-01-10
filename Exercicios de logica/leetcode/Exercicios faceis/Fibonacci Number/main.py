class Solution:
    def fib(self, n: int) -> int:
        n1 = 1
        n2 = n1
        n3 = n2

        if n == 0:
            return 0

        else:
            for c in range(n - 1):
                n3 = n1 + n2
                n1 = n2
                n2 = n3

        return n1